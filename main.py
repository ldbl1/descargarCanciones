import youtube_dl
import csv

def get_folder():
    folder = input("Introduzca la carpeta en la que se deben guardar los mp3:")
    return folder



def download(folder,url):
    video_url = url
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = folder + "\\" +f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

def read_csv(folder):
    csv_file = input("Introduzca la ruta del csv con extensión: ")
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                download(folder,row[0])
                line_count += 1
        print(f'Processed {line_count} lines.')


def run():
    folder = get_folder()
    read_csv(folder)


if __name__=='__main__':
    run()