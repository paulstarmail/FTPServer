
FTPServer

Windows 11 64-bit application to transfer folders/files between computers (also between computers and mobile phones, provided an FTP enabled app is installed in the mobile phones, such as "Cx File Explorer" for example) in a wired/wireless LAN such as home/work network.

Pre-requisites
==============
1. A working installation of "python 3" which is added to "Path".
2. All the dependencies in "ftp_server.py" installed through "pip3".
3. Executable of "python 3" in the installation directory, allowed for Outbound connection, in the Firewall.

Steps to use the software
=========================

1. Place "ftp_server.py" inside the parent folder of the folder to be transferred or inside the containing folder of the file to be transferred (This is the Server computer).
2. Run "ftp_server.py" on the Server computer by double clicking it and follow the instructions (All the input suggestions are editable).
3. Go to the location bar of the file explorer in the Client computer and enter the URL generated in the Server computer.
4. Enter the credentials.
5. "Copy/Cut - Paste" the desired folder/file as the case may be, in the Client computer to desired location.
6. Close "ftp_server.py" in Server computer after transfer ("Copy/Cut - Paste") completion, to finish the entire process (FTPServer is terminated now).
