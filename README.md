# IconGenerator
Android开发中批量生成多种尺寸Icon的脚本    

运行环境 Python3    
依赖包 pillow    

使用方法    
修改size_list文件,每种尺寸一行,按照*宽度,高度*的格式编写,例如

    512,512
    128,128
    48,48

运行脚本时需要调整的图片文件路径作为参数,例如

    python IconGenerator.py ./icon.png

生成的文件放在脚本的当前目录下,以尺寸命名,例如icon_192X192.png