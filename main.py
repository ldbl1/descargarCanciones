import youtube_dl
import csv
from easygui import *
import os
clear = lambda: os.system('cls')


def get_folder():
    print("")
    input("Ahora se le solicitará un directorio donde descargar las canciones. Pulse cualquier botón para continuar")
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
            print("Descarga completada... {}".format(filename))
    except:
        raise Exception("Error 001")

def read_csv(folder):
    clear()
    printProgramName()
    input("Seleccione ahora el csv con los enlaces a YouTube. Pulse cualquier tecla para continuar")
    csv_file = getCSV()
    print("El fichero seleccionado es -> "+ csv_file)
    input("Pulse cualquier tecla para continuar")
    clear()
    printProgramName()
    print("Comenzando descarga. Espere hasta que se haya finalizado...")
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                try:
                    print(f"Intentando descargar cancion en {row[0]}")
                    download(folder,row[0])
                    line_count += 1
                except:
                    print(f"Error al descargar el enlace: {row[0]}")
        clear()
        printProgramName()
        print("Programa finalizado")
        print(f'Se han descargado {line_count} canciones en la carpeta {folder}')
        
    
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
    print("Bienvenido al descargador de canciones")
    folder = get_folder()
    print("Carpeta seleccionada -> " + folder)
    input(" Pulse cualquier tecla para continuar")
    read_csv(folder)

def printProgramName():
    print("""
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



    """)

if __name__=='__main__':
    printProgramName()
    print("Pulse cualquier tecla para comenzar el programa")
    input("Pulse CTRL + C para finalizarlo en cualquier momento")
    run()