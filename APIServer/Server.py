import subprocess
import socket
import ssl
import re



#Check for openssl in the system
try:
    subprocess.run(["openssl"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except:
    raise ModuleNotFoundError("Openssl is not available on the host")


class Server:
    """Server standalone for Entsog API tracker to batch data out to destination"""
    
    def __init__(self, dest_host:str, dest_port:int, port:int) -> None:
        self.__port = port
        self.__ip = "0.0.0.0"
        self.__dest_host = dest_host
        self.__dest_port = dest_port

    def __init__(self, dest_addr:str, port:int) -> None:
        self.__port = port
        self.__ip = "0.0.0.0"
        self.__dest_addr = dest_addr
    
    def reconfigure(method):
        """Reset configuration"""
        def inner(self, *args, **kwargs):
            method(self, *args, **kwargs)
            if hasattr(self, '__dest_addr'):
                self.__dest_host = ":".split(self.__dest_addr)[0]
                self.__dest_port = int(":".split(self.__dest_addr)[1])
            elif hasattr(self, '__dest_host') and hasattr(self, '__dest_port'):
                self.__dest_addr = f"{self.__dest_host}:{self.__dest_port}"
        return inner

    def set_destination(self, dest_host:str, dest_port:int):
        """Method used to modify host and port of destination"""
        if re.search("^(([0-1]?[0-9]?[0-9]|2([0-4][0-9]|5[0-5]))(\.|$)){4}", dest_host):
            self.__dest_host = dest_host
        else:
            raise Exception(f"Incorrect destination host format: {dest_host}")
        if dest_port < 65536:
            self.__dest_port = dest_port
        else:
            raise Exception(f"Port invalid: {dest_port}")

    def set_destination(self, dest_addr:str):
        """Method used to modify destination address"""
        if re.search("^(([0-1]?[0-9]?[0-9]|2([0-4][0-9]|5[0-5]))(\.|:)){4}[0-9]+$", dest_addr):
            self.dest_addr = dest_addr
        else:
            raise Exception(f"Invalid Destination Address: {dest_addr}")


    def start(self) -> object:
        """Method used to start the Entsog-Tracker service"""
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.__ip, self.__port))
        server.listen(5)
        print("[*] Server is listening on %s:%d" % (self.__ip, self.__port))
        return server
