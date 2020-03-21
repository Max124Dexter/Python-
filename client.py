import socket
import time
import threading

key = 8631
shutdown = False
join = False
def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))

               # decrypt = ""
                # k = False
                # for i in data.decode("utf-8"):
                   # if i == ":":
                      #  k = True
                     #   decrypt += i
                    #elif k == False or i == " ":
                   #     decrypt += i
                  #  else:
                 #       decrypt += chr(ord(i)*key)
                #    print(decrypt)


                time.sleep(0.6)
        except:
            pass
        #Crypted
hosta = socket.gethostbyname(socket.gethostname())
porta = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ("192.168.1.10", 9090)

sock.bind((hosta, porta))
sock.setblocking(0)

username = input("Name: ")
routing = threading.Thread(target= receving, args=("RecvThread", sock))
routing.start()

while shutdown == False:
    if join == False:
        sock.sendto(("[" + username + "=>>> JOIN IN CHATROOM").encode("utf-8"), server)
        join = True
    else:
        try:
            msg = input(": ")

            #crypt = ""
            #for i in msg:
                #crypt += chr(ord(i)*key)
            #msg = crypt

            if msg != "":
                sock.sendto(("[" + username + "] ::> " + msg).encode("utf=-8"), server)
            else:
                sock.sendto(("[" + username + "<<<= LEFT FROM CHATROOM" ).encode("utf-8"), server)
                shutdown == True
        except:
            pass
routing.join()
sock.close()