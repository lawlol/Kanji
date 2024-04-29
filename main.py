import os
import shutil
import tempfile
from typing import Dict, List

red = "\033[31m"

redirects: Dict[str, List[str]] = {
    "GIFs": ["gif"],
    "Pictures": ["jpg", "png", "jpeg", "bmp", "svg", "tiff", "webp", "ico"],
    "Videos": ["mp4", "wmv", "avi", "flv", "mkv", "mov", "3gp", "m4v", "mpeg"],
    "Music": ["mp3", "wav", "flac", "aac", "ogg", "wma", "alac"],
    "Archives": ["zip", "rar", "7z", "tar", "gz", "bz2", "iso"],
    "PDFs": ["pdf", "epub", "mobi", "azw"],
    "Documents": ["docx", "txt", "odt", "pptx", "xls", "xlsx", "csv", "rtf"],
    "Executables": ["exe", "bat", "sh", "msi"],
    "Code": ["py", "js", "java", "c", "cpp", "html", "css", "php", "rb", "pl", "go"],
    "Scripts": ["vbs", "ps1", "cmd"],
    "Fonts": ["ttf", "otf", "woff"],
    "Databases": ["sql", "db", "mdb", "sqlite"]
}

def clean_logs():
    logs = [os.path.expanduser(r"~\AppData\Local\Temp"),
            os.path.expanduser(r"C:\Windows\Logs"),
            os.path.expanduser(r"C:\Windows\Temp")]
    for log in logs:
        if os.path.exists(log):
            for item in os.listdir(log):
                if item.endswith(".log"):
                    items = os.path.join(log, item)
                    os.remove(items)

def clean_temp():
    temps = [tempfile.gettempdir(), os.environ.get("TEMP"), os.environ.get("TMP")]
    for temp in temps:
        if temp:
            for item in os.listdir(temp):
                items = os.path.join(temp, item)
                if os.path.isdir(items):
                    shutil.rmtree(items, ignore_errors=True)
                else:
                    os.remove(items)

def optimize():
    clean_logs()
    clean_temp()

directory = os.getcwd()

def organize(directory: str, redirects: Dict[str, List[str]]):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir():
                continue

            extension = entry.name.split('.')[-1].lower()

            for folder, extensions in redirects.items():
                if extension in extensions:
                    end_path = os.path.join(directory, folder)
                    os.makedirs(end_path, exist_ok=True)
                    shutil.move(entry.path, os.path.join(end_path, entry.name))
                    break

def Kanji():
    kanji = f"""
{red}

                                          ,,,xxxx\

   ``''==xx#################xxxxx===---xxx##########\

                  `''################################\

                     ####           ####P'   
  --                ####            ####
                  ####              ####
                ####`'=..           ####      ,#####
            ,####      ###,,        ####,,==#####""'
         ,###`'==        '####\     ####
      ,,##`     ""###      ####     ####
                   ####   ####      ####
                     #######        ####
                      ####          ####
                    ####            ####
                  ####              ####            #
              ,####'                ####           ##
          ,####'                    #################
      ,x##                            ##############

            welcome to kanji file organizer

  -----------------------------------------------------
          1 = file organizer | 2 = optimize pc

"""
    print(kanji)

if __name__ == "__main__":
    Kanji()
    x = input(f"{red}[root@kanji ~]# ")

    if x == "1":
        organize(directory, redirects)
        print(f"{red}done!")

    elif x == "2":
        optimize()
        print(f"\n{red}done!")

    else:
        print(f"{red}invalid choice!")
