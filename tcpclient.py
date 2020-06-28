# yan shkolnik 314182072
# mishel musayev 204365225
# we create game of rock, paper, scissors between server and client in protocol tcp ip
# you need to run server first and then client
# choose rock, paper, scissors or q to quit the game


import socket


def Main():
    host='127.0.0.1' #ip adderes
    port=5000      #port
    rockPaperCissorsList = ["rock", "paper", "scissors"]  #list for checking speling
    playerPoints=0
    computerPoints=0

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create socket
    s.connect((host,port))  #create connnection with the server in ip 127.0.0.1 and port 5000

    message= input("enter rock,scissors,paper or q to quit: ") #input from user

    while message not in rockPaperCissorsList:  #if message not in list ask for input on more time
        if message == "q":
            s.send(message.encode('utf-8'))
            break
        print("bad value try again")
        message = input("enter rock,scissors,paper or q to quit: ")
    while message!='q':
        s.send(message.encode('utf-8')) #send massage to server
        data=s.recv(1024).decode('utf-8')  # recive data from server the choice of the computer
        print("computer choice: " + str(data))  #print comouter choice
        data = s.recv(1024).decode('utf-8')  #recive from server the results of the game
        print("from server: " + str(data))
        message=input("enter rock,scissors,paper or q to quit: ") # ask for input again

        while message not in rockPaperCissorsList: #checking again if speling ok in input
            if message == "q":
                s.send(message.encode('utf-8'))
                break
            print("bad value try again")
            message = input("enter rock,scissors,paper or q to quit: ")

    playerPoints = s.recv(1024).decode('utf-8')   #recive the player point if the game end
    computerPoints = s.recv(1024).decode('utf-8') #recive computer points if the game is end
    print(f"Player score: {playerPoints}")     # print the point of player
    print(f"Computer score: {computerPoints}")  #print the point of computer
        # cheking who win in the game and print
    if playerPoints>computerPoints:
        print(f"\nplayer win with {playerPoints} points")
    elif playerPoints==computerPoints:
        print("the game ended in tie")

    elif playerPoints < computerPoints:
        print(f"\ncomputer win with {computerPoints} points")

    print("your game has ended bye bye")
    s.close() #close concction with server

if __name__=='__main__':    #file run only from this file
    Main()

