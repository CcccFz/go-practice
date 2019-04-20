python工程冻结为二进制。方便python生成exe的小工程。

Requirements
------------
- Python: 
   * 2.3 - 2.7 (Python 3 is not supported)

- Windows (32bit/64bit):
   * Windows XP or newer.
   * pywin32_ when using Python 2.6+
    
- Linux (32bit/64bit)
   * ldd: console application to print the shared libraries required 
     by each program or shared library.
   * objdump: Console application to display information from 
     object files.

- Mac OS X (32/64bit):
   * Mac OS X 10.4 (Tiger) or newer (Leopard, Snow Leopard, Lion).


使用：  
将python工程代码放入src，双击build.bat，生成的exe在output\dist目录   
   
   
选项：  
-p 所依赖模块的跟路劲  
-o 输出路劲  
-n exe的名字  
-i 图标所在路劲  
-F 入口模块  
-a 需将依赖的包链入exe  