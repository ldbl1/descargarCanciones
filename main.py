import youtube_dl
import csv
from easygui import *
import os
clear = lambda: os.system('cls')
import colorama
from colorama import Fore
from colorama import Style

def get_folder():
    print("")
    input(Fore.GREEN + Style.BRIGHT + "Ahora se le solicitará un directorio donde descargar las canciones. Pulse cualquier botón para continuar" + Style.RESET_ALL)
    folder = diropenbox('test', 'Seleccione la carpeta para descargar las canciones', 'C:\\')
    return folder

def download(folder,url):
    video_url = url
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    titulo = parseFileName(video_info['title'])
    filename = folder + "\\" +f"{titulo}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    try:
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
            print(Fore.GREEN + Style.BRIGHT + "Descarga completada en ruta: {}".format(filename) + Style.RESET_ALL)
    except:
        raise Exception(Fore.RED + Style.BRIGHT + "Error 001" + Style.RESET_ALL)

def read_csv(folder):
    clear()
    printProgramName()
    input(Fore.GREEN + Style.BRIGHT + "Seleccione ahora el csv con los enlaces a YouTube. Pulse cualquier tecla para continuar" + Style.RESET_ALL)
    csv_file = getCSV()
    print(Fore.BLUE + Style.BRIGHT + "El fichero seleccionado es -> "+ csv_file + Style.RESET_ALL)
    input(Fore.GREEN + Style.BRIGHT + "Pulse cualquier tecla para continuar" + Style.RESET_ALL)
    clear()
    printProgramName()
    print(Fore.BLUE + Style.BRIGHT + "Comenzando descarga. Espere hasta que se haya finalizado..." + Style.RESET_ALL)
    canciones_erroneas = 0
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                try:
                    print(Fore.GREEN + Style.BRIGHT + f"Intentando descargar cancion en {row[0]}" + Style.RESET_ALL)
                    download(folder,row[0])
                    line_count += 1
                except:
                    print(Fore.RED + Style.BRIGHT + f"Error al descargar el enlace: {row[0]}" + Style.RESET_ALL)
                    canciones_erroneas += 1
        clear()
        printProgramName()
        print(Fore.GREEN + Style.BRIGHT + "Programa finalizado" + Style.RESET_ALL)
        print(Fore.BLUE + Style.BRIGHT + f'Se han descargado {line_count-1} canciones en la carpeta {folder}' + Style.RESET_ALL)
        print(Fore.RED + style.BRIGHT + f'Pero hubo {canciones_erroneas} que no se pudieron descargar' + Style.RESET_ALL)
        input("Pulse cualquier tecla para finalizar el programa")
        
    
def parseFileName(titulo):
    titulo = titulo.replace('\\','-')
    titulo = titulo.replace('/','-')
    titulo = titulo.replace(':','-')
    titulo = titulo.replace('*','-')
    titulo = titulo.replace('¿','-')
    titulo = titulo.replace('"','-')
    titulo = titulo.replace('<','-')
    titulo = titulo.replace('>','-')
    titulo = titulo.replace('|','-')
    return titulo

def getCSV():
    file = fileopenbox( default="./data/*.csv")
    return file

def run():
    clear()
    printProgramName()
    print(Fore.YELLOW + Style.BRIGHT + "Bienvenido al descargador de canciones" + Style.RESET_ALL)
    folder = get_folder()
    print(Fore.BLUE + Style.BRIGHT + "Carpeta seleccionada -> " + folder + Style.RESET_ALL)
    input(Fore.GREEN + Style.BRIGHT + "Pulse cualquier tecla para continuar" + Style.RESET_ALL)
    read_csv(folder)

def printProgramName():
    print(Fore.LIGHTCYAN_EX + """
                ________   _                         _          ___   ___ ___  ___            
               /  ____  \ | |                       | |        |__ \ / _ \__ \|__ \           
              /  / ___|  \| |     ___  _ __ ___   __| | ___       ) | | | | ) |  ) |          
             |  | |       | |    / _ \| '__/ _ \ / _` |/ _ \     / /| | | |/ /  / /           
             |  | |___    | |___| (_) | | | (_) | (_| | (_) |   / /_| |_| / /_ / /_           
              \  \____|  /|______\___/|_|  \___/ \__,_|\___/   |____|\___/____|____|          
  _____        \________/                       _____                 _                       
 |  __ \                                       / ____|               (_)                      
 | |  | | ___  ___  ___ __ _ _ __ __ _  __ _  | |     __ _ _ __   ___ _  ___  _ __   ___  ___ 
 | |  | |/ _ \/ __|/ __/ _` | '__/ _` |/ _` | | |    / _` | '_ \ / __| |/ _ \| '_ \ / _ \/ __|
 | |__| |  __/\__ \ (_| (_| | | | (_| | (_| | | |___| (_| | | | | (__| | (_) | | | |  __/\__ \\
 |_____/ \___||___/\___\__,_|_|  \__, |\__,_|  \_____\__,_|_| |_|\___|_|\___/|_| |_|\___||___/
                                  __/ |    _____  _______      __                             
                                 |___/    / ____|/ ____\ \    / /                             
                         ___ ___  _ __   | |    | (___  \ \  / /                              
                        / __/ _ \| '_ \  | |     \___ \  \ \/ /                               
                       | (_| (_) | | | | | |____ ____) |  \  /                                
                        \___\___/|_| |_|  \_____|_____/    \/                                 



    """ + Style.RESET_ALL)

if __name__=='__main__':
    colorama.init()
    printProgramName()
    print(Fore.GREEN + Style.BRIGHT + "Pulse cualquier tecla para comenzar el programa" + Style.RESET_ALL)
    input("Pulse Ctrl - C para cerrar el programa en cualquier momento")
    run()