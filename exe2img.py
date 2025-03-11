import sys
import os
import subprocess
from wand.image import Image

ICON = "temp.ico"
CONFIG = "config.txt"

def create_icon(img: str):
    with Image(filename=img) as img:
        img.resize(512, 512)

        img.save(filename=ICON)

def create_archive(exe: str, img: str):
    create_icon(img)

    with open(CONFIG, "w") as f:
        contents = f"""
            Setup={img}
            Setup={exe}
            TempMode
            Silent=1
            Overwrite=1
            Update=U
        """

        f.write(contents.strip().replace(" ", ""))

    temp = "temp.exe"

    commands = [
        f"rar a -sfx -z{CONFIG} {temp} {exe} {img}",
        f'ResourceHacker.exe -open {temp} -save {temp} -action delete -res ICONGROUP,1,',
        f'ResourceHacker.exe -open {temp} -save out.exe -action add -res temp.ico -mask ICONGROUP,1,'
    ]

    for command in commands:
        subprocess.run(["cmd", "/c", command]) 

    os.remove(ICON)
    os.remove(CONFIG)
    os.remove(temp)

def main():
    args = sys.argv[1:]

    if len(args) != 2:
        raise Exception("Only 2 arguments should be supplied")

    create_archive(*args)
  

if __name__ == "__main__":
    main()