import os
import shutil
import platform
import tempfile
import subprocess

red = "\033[31m"

class Redirects:
  def __init__(self):
      self.redirects = {
          'gif': 'GIFs',
          'png': 'Pictures',
          'jpg': 'Pictures',
          'jpeg': 'Pictures',
          'bmp': 'Pictures',
          'svg': 'Pictures',
          'tiff': 'Pictures',
          'webp': 'Pictures',
          'ico': 'Pictures',
          'mp4': 'Videos',
          'wmv': 'Videos',
          'avi': 'Videos',
          'flv': 'Videos',
          'mkv': 'Videos',
          'mov': 'Videos',
          '3gp': 'Videos',
          'm4v': 'Videos',
          'mpeg': 'Videos',
          'mp3': 'Music',
          'wav': 'Music',
          'flac': 'Music',
          'aac': 'Music',
          'ogg': 'Music',
          'wma': 'Music',
          'alac': 'Music',
          'zip': 'Archives',
          'rar': 'Archives',
          '7z': 'Archives',
          'tar': 'Archives',
          'gz': 'Archives',
          'bz2': 'Archives',
          'iso': 'Archives',
          'pdf': 'PDFs',
          'epub': 'PDFs',
          'mobi': 'PDFs',
          'azw': 'PDFs',
          'docx': 'Documents',
          'txt': 'Documents',
          'odt': 'Documents',
          'pptx': 'Documents',
          'xls': 'Documents',
          'xlsx': 'Documents',
          'csv': 'Documents',
          'rtf': 'Documents',
          'exe': 'Executables',
          'bat': 'Executables',
          'sh': 'Executables',
          'msi': 'Executables',
          'py': 'Code',
          'js': 'Code',
          'java': 'Code',
          'c': 'Code',
          'cpp': 'Code',
          'html': 'Code',
          'css': 'Code',
          'php': 'Code',
          'rb': 'Code',
          'pl': 'Code',
          'go': 'Code',
          'vbs': 'Scripts',
          'ps1': 'Scripts',
          'cmd': 'Scripts',
          'bat': 'Scripts',
          'ttf': 'Fonts',
          'otf': 'Fonts',
          'woff': 'Fonts',
          'sql': 'Databases',
          'db': 'Databases',
          'mdb': 'Databases',
          'sqlite': 'Databases',
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

redirects = Redirects().redirects

def organize(directory, redirects):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir():
                continue

            extension = entry.name.split('.')[-1].lower()

            end = redirects.get(extension)
            if not end:
                continue

            end_path = os.path.join(directory, end)
            os.makedirs(end_path, exist_ok=True)

            shutil.move(entry.path, os.path.join(end_path, entry.name))

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
  x = input(f"{red}[root@kanji]$ ")

  if x == "1":
    organize(directory, redirects)
    print(f"{red}done!")

  elif x == "2":
    optimize()
    print(f"\n{red}done!")

  else:
    print(f"{red}Invalid choice!")
