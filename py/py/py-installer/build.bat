python pyinstaller-2.0\pyinstaller.py -p src -o output -n ConvertMib -i ico\tool.ico -a -F src\main.py

del *.log /f /q

@echo 二进制生成成功

pause