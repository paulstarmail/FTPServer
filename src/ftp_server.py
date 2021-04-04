
# For more info see the following link:
# https://pyftpdlib.readthedocs.io/en/latest/tutorial.html#a-base-ftp-server

import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from termcolor import colored
import colorama
from getpass import getpass

def main():
    # Asking for ip address.
    ip_address = str(input("\nEnter the IPv4 address of this system in LAN (Run \"ipconfig\" in \"cmd\" for more info): "))
    port = str(input("Enter the desired port (>1024, Typically 8002): "))
    choice = str(input("Enter 1 for anonymous read-only user or 2 for registered read/write user: "))
    colorama.init()
    print("URL to be entered in the client: " + colored("ftp://" + str(ip_address) + ":" + str(port), 'cyan'))
    
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only anonymous user
    if(choice == "1"):
        # anonymous user
        print("\n")
        authorizer.add_anonymous(os.getcwd())
    else:
        username = str(input("Enter a one-time username: "))
        password = getpass(prompt = "Enter a one-time password: ", stream = None)
        print("\n")
        # username followed by password
        authorizer.add_user(username, password, '.', perm='elradfmwMT')
    

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    #handler.masquerade_address = '151.25.42.11'
    #handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = (ip_address, port)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()

if __name__ == '__main__':
    main()
