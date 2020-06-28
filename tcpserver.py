# yan shkolnik 314182072
# mishel musayev 204365225
# we create game of rock, paper, scissors between server and client in protocol tcp ip
# you need to run server first and then client
# choose rock, paper, scissors or q to quit the game

import socket
import random

def Main():
    host='127.0.0.1'  #ip adderes
    port=5000    #port
    serverPoints = 0  #server points counter
    clientPoints = 0  #client points counter
    rockPaperCissorsList = ["rock","paper","scissors"] # list for choose random value for computer
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #create socket with tcp protocol
    s.bind((host,port)) # conecction to port 5000 and host "127.0.0.1"
    s.listen(1)  # listening for 1 connection
    print("Server has started")
    c,addr =s.accept() # accpet the connectin
    print("connection from: " + str(addr))  #print the address of the connectin
    while True:
        computer = random.choice(rockPaperCissorsList) #choose random object from list
        print("-------------------------------------------------------------------")
        print("server choose: " + computer) #print the what we choose from list
        player=c.recv(1024).decode('utf-8')  #recive from client what he choose
        if player == 'q': #if he choose q quiet the connection
            break
        print("plyayer choose: " + player) #print what the plkayer choose
        if not player: #if we not recv data the connectin close
            print("there is not data from the client")
            break
                             # all the choices for rock scissors paper for the game
        if player == "rock":
            if computer == "rock":
                print(f"client Points = {clientPoints}\nserver points = {serverPoints}\n")
                result = f"rock vs rock\nplayer Points = {clientPoints}\ncomputer points = {serverPoints}\ntie\n"

            elif computer == "paper":
                serverPoints += 1
                print("paper win")
                print(f"clientPoints = {clientPoints}\nserver points = {serverPoints}\n")
                result=f"rock vs paper\nplayer Points = {clientPoints}\ncomputer points = {serverPoints}\npaper win\n"

            elif computer == "scissors":
                clientPoints += 1
                print("rock win")
                print(f"nclientPoints ={clientPoints}\nserver points = {serverPoints}\n")
                result = f"rock vs scissors\nplayer Points ={clientPoints}\ncomputer points = {serverPoints}\nrock win\n"

        if player == "paper":
            if computer == "paper":
                print(f"clientPoints = {clientPoints}\nserver points = {serverPoints}\n")
                result = f"paper vs paper\nplayer Points = {clientPoints}\ncomputer points = {serverPoints}\ntie\n"

            elif computer == "scissors":
                serverPoints += 1
                print("scissors win")
                print(f"clientPoints = {clientPoints}\nserver points = {serverPoints}\n")
                result = f"paper vs scissors\nplayer Points = {clientPoints}\ncomputer points = {serverPoints}\nscissors win\n"

            elif computer == "rock":
                clientPoints += 1
                print("paper win")
                print(f"clientPoints = {clientPoints}\nserver points = {serverPoints}\n")
                result = f"paper vs rock\nplayer Points = {clientPoints}\ncomputer points = {serverPoints}\npaper win\n"

        if player == "scissors":
            if computer == "scissors":
                print(f"clientPoints = {clientPoints}\nserver points = {serverPoints}\n")
                result = f"scissors vs scissors\nplayer Points = {clientPoints}\ncomputer points = {serverPoints}\ntie\n"
            elif computer == "rock":
                serverPoints += 1
                print("rock win")
                print(f"clientPoints = {clientPoints}\nserver points = {serverPoints}\n")
                result = f"scissors vs rock\nplayer Points = {clientPoints}\ncomputer points = {serverPoints}\nrock win\n"

            elif computer == "paper":
                clientPoints += 1
                print("scissors win")
                print(f"clientPoints = {clientPoints}\nserver points = {serverPoints}\n")
                result = f"scissors vs paper\nplayer Points = {clientPoints}\ncomputer points = {serverPoints}\nscissors win\n"

        #print("from connected user:" + str(player))
        # data=str(data).upper()
        #print("sending: " +str(player))
        c.send(computer.encode('utf-8'))  # sending the choice of computer
        c.send(result.encode('utf-8'))   #sending the results of the game
        print("-------------------------------------------------------------------")
    c.send(str(clientPoints).encode('utf-8'))  #sending clients points
    c.send(str(serverPoints).encode('utf-8'))  #sending server points
    c.close()
    print("server is ended") # print when connectin end

if __name__== '__main__' :    #file run only from this file
    Main()