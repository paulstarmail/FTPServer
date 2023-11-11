FTPServer
=========
Windows 11 64-bit application to transfer folders/files between computers (also between computers and mobile phones, provided an FTP enabled app is installed in the mobile phones, such as "Cx File Explorer" for example) in a wired/wireless LAN such as home/work network.

Pre-requisites
==============
1. A working installation of "python 3" whose directory is added to "Path".
2. All the dependencies in "ftp_server.py" installed through "pip3".
3. "Local port" used by "ftp_server.py" (Typically, 2121) set, and, "Remote port" set to "All Ports"; are allowed for "Inbound Rules", in "Firewall", for "TCP".
    
   ![image](https://github.com/paulstarmail/FTPServer/assets/60135524/4180572f-6cb8-4537-a32f-02ce9e5424b3)

4. "Local port" used by "ftp_server.py" (Typically, 2121) set, and, "Remote port" set to "All Ports"; are allowed for "Outbound Rules", in "Firewall", for "TCP".
   
   ![image](https://github.com/paulstarmail/FTPServer/assets/60135524/fd247230-5c88-45a9-9c33-43724344e22d)


Steps to use the software
=========================
1. Place "ftp_server.py" inside the parent folder of the folder to be transferred or inside the containing folder of the file to be transferred (This is the Server computer).
2. Run "ftp_server.py" on the Server computer by double clicking it and follow the instructions (All the input suggestions are editable).
3. Go to the location bar of the file explorer in the Client computer and enter the URL generated in the Server computer.
4. Enter the credentials.
5. "Copy/Cut - Paste" the desired folder/file as the case may be, in the Client computer to desired location.
6. Close "ftp_server.py" in Server computer after transfer ("Copy/Cut - Paste") completion, to finish the entire process (FTPServer is terminated now).
