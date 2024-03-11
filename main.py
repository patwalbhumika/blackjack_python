import random
import arts


playGame=True
while(playGame):
    print("--------------------------------------------------------------------------------------------------------")
    print(arts.logo)
    print("\n")

    
    if(input("Do you want to Play BlackJack: (y/n)")=="y"):
        cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]
        dealerList=[random.choice(cards),random.choice(cards)]
        playerList=[random.choice(cards),random.choice(cards)]
        print("Player Cards: "+ str((playerList)))
        print("Dealer Cards: "+str((dealerList[1:])))
        print("\n")

        playerWin=False
        dealerWin=False

        
        while(True):
            choice=input("Hit[h] or Stay[s]: ")
            if(choice=="h"):
                playerList.append(random.choice(cards))
                if(sum(playerList)<21):
                    print("Player Cards: "+str((playerList)))
                    print("\n")
                    continue
                else:
                    if(sum(playerList)==21):
                        playerWin=True
                        break
                    else:
                        dealerWin=True
                        break


            elif(choice=="s"):
                break

            else:
                print("Invalid Choice")
                continue

        while(playerWin==False and True and dealerWin==False):
            if(sum(dealerList)<=16):
                dealerList.append(random.choice(cards))
                continue
            elif(sum(dealerList)<21):
                if(sum(dealerList)==sum(playerList)):
                    playerWin=True
                    dealerWin=True
                    break
                elif(sum(playerList)<sum(dealerList)):
                    dealerWin=True
                    break
                elif(sum(playerList)>sum(dealerList)):
                    playerWin=True
                    break
            elif(sum(dealerList)==21):
                dealerWin=True
                break
            elif(sum(dealerList)>21):
                playerWin=True
                break

        print("Player Cards: "+ str((playerList)))
        print("Dealer Cards: "+str((dealerList)))
        print("\n\n")
        if(dealerWin==True and playerWin==True):
            print("IT'S A TIE!!")
        elif(dealerWin==True and playerWin==False):
            print("DEALER WINS THE GAME!! \n GAME OVER!!!")
        else:
            print("PLAYER WINS THE GAME \n GAME OVER!!")
        print("--------------------------------------------------------------------------------------------------------")
        
    
    else:
        playGame=False




        





