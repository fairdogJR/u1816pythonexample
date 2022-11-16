# u1816pythonexample
U1816E python code  program directly using 32 bit DLL The 64 bit dll also works, just make sure you point to the 64bit dll see below
See Project Wiki https://github.com/fairdogJR/u1816pythonexample/wiki/U1816pythonexample-Wiki or python code for more detailed info

Make sure you install the complete U1816E Soft front panel. All code examples are there except python

If you want to use the 64 bit dll you will find it in 
"C:\Program Files (x86)\Keysight\U1816x\Dll" after installing the product's soft front panel.



HOWEVER:
One VERY important thing is the default directory "C:\Program Files (x86)\Keysight\U1816x\Dll" for the software will not work with python (DLL wont be found). because windows security restricts access , the Newer win 10 release does not allow user apps to access this space for some reason. When you move the dll to a user-created directory then the problem goes away


Manual for this is here and there is a software section near the end of the manual
https://www.keysight.com/ca/en/assets/9018-03932/user-manuals/9018-03932.pdf

thanks, 
-Tim Fairfield
