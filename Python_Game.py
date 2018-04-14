###########################################################################
#                   Final Project – Battle Royale                         #
#                                                                         #
#                                                                         #
#   PROGRAMMED BY    Casey Floyd and Tyler Vier (April 30th, 2016)        #
#   CLASS            CS301, Spring 2016                                   #
#   INSTRUCTOR       Dean Zeller                                          #
#                                                                         #
#                                                                         #
#   DESCRIPTION                                                           #
#   This file contains a player vs player battle simulator in which the   #
#   players choose between three characters with different attributes     #
#   in order to try and win the fight                                     #
#                                                                         #
###########################################################################

import random
import time


#main function that begins the fight
def gameplay():
    answer = 'y'
    while answer == 'y':
        print("")
        play = input("Do you want to play against the computer or another person?(c/p): ")
        if play == 'c':
            playerVsComputer()
        elif play == 'p':
            time.sleep(1)
            print("")
            print("Player 1, pick a character:")
            print("   1 = Juggernaut (heavily defense based)")
            print("   2 = Crixus (heavily attack based)")
            print("   3 = Akali (skilled in both defense and attack)")
            c1 = input()
            time.sleep(1)
            print("")
            print("Player 2, pick a character:")
            print("   1 = Dreadnaut (heavily defense based)")
            print("   2 = Achilles (heavily attack based)")
            print("   3 = Daedalus (skilled in both defense and attack)")
            c2 = input()
            pvp(c1,c2)
        print("")
        answer = input("Do you want to play again? (y/n): ")
    print("Thanks for playing")

#implementing global variables
p1health1 = 200
p2health1 = 200
p1health2 = 100
p2health2 = 100
p1health3 = 150
p2health3 = 150

#function for player vs player
def pvp(c1,c2):

    global p1health1, p2health1, blockCount1, blockCount2
    global p1health2, p2health2, p1health3, p2health3

    if c1 == '1' and c2 == '1':
        c1 = "Juggernaut"
        c2 = "Dreadnaut"
        while p1health1 > 0 and p2health1 > 0: 
            time.sleep(2)
            print(str(c1)+ "'s health is", str(p1health1))
            print(str(c2)+ "'s health is", str(p2health1))
            print("")
            time.sleep(1)
            print(str(c1)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 5 and 15 damage")
            print("   2 = Kick - does between 10 and 25 damage")
            print("   3 = Heal - gives back between 15 and 20 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move1 = input()
            
            print("\n"*50)
        
            print(str(c2)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 5 and 15 damage")
            print("   2 = Kick - does between 10 and 25 damage")
            print("   3 = Heal - gives back between 15 and 20 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move2 = input()

            if move1 == '1' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")
                time.sleep(1)

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '1' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '1' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p2health1 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                    
            if move1 == '2' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                

            if move1 == '2' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '2' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p2health1 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p1health1 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p1health1 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p1health1 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p2health1 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '4' and move2 == '1':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 3:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(5,15)
                        p1health1 -= attack
                        print("")
                        print(str(c2)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health1 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health1 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '2':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 3:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(10,25)
                        p1health1 -= attack
                        print("")
                        print(str(c2)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health1 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health1 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '3':
                print(str(c1)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p2health1 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")


            if move2 == '4' and move1 == '1':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 3:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(5,15)
                        p2health1 -= attack
                        print("")
                        print(str(c1)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health1 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health1 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '2':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 3:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(10,25)
                        p2health1 -= attack
                        print("")
                        print(str(c1)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health1 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health1 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '3':
                print(str(c2)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p1health1 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

            if move1 == '4' and move2 == '4':
                time.sleep(1)
                print("Both players tried blocking")
                time.sleep(1)
                print("Both blocks fail")  
                
        
    elif c1 == '1' and c2 == '2':
        c1 = "Juggernaut"
        c2 = "Achilles"
        while p1health1 > 0 and p2health2 >0: 
            time.sleep(2)
            print(str(c1)+ "'s health is", str(p1health1))
            print(str(c2)+ "'s health is", str(p2health2))
            print("")
            time.sleep(1)
            print(str(c1)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 5 and 15 damage")
            print("   2 = Kick - does between 10 and 25 damage")
            print("   3 = Heal - gives back between 15 and 20 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move1 = input()
            
            print("\n"*50)
        
            print(str(c2)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 20 and 30 damage")
            print("   2 = Kick - does between 25 and 35 damage")
            print("   3 = Heal - gives back between 1 and 10 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move2 = input()

            if move1 == '1' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '1' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '1' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p2health2 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                    
            if move1 == '2' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '2' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                

            if move1 == '2' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p2health2 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p1health1 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p1health1 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p1health1 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p2health2 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '4' and move2 == '1':
                miss = random(1,5)
                time.sleep(1)
                if miss == 3:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(20,30)
                        p1health1 -= attack
                        print("")
                        print(str(c2)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health1 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health2 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '2':
                miss = random(1,5)
                time.sleep(1)
                if miss == 3:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(25,35)
                        p1health1 -= attack
                        print("")
                        print(str(c2)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health1 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health2 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '3':
                print(str(c1)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p2health2 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")


            if move2 == '4' and move1 == '1':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 1 or miss == 2 or miss == 4 or miss == 5:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(5,15)
                        p2health2 -= attack
                        print("")
                        print(str(c1)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health1 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health2 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '2':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 1 or miss == 2 or miss == 4 or miss == 5:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(10,25)
                        p2health2 -= attack
                        print("")
                        print(str(c1)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health1 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health2 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '3':
                print(str(c2)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p1health1 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

            if move1 == '4' and move2 == '4':
                time.sleep(1)
                print("Both players tried blocking")
                time.sleep(1)
                print("Both blocks fail")
                    
    elif c1 == '1' and c2 == '3':
        c1 = "Juggernaut"
        c2 = "Daedalus"
        while p1health1 > 0 and p2health3 >0: 
            time.sleep(2)
            print(str(c1)+ "'s health is", str(p1health1))
            print(str(c2)+ "'s health is", str(p2health3))
            print("")
            time.sleep(1)
            print(str(c1)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 5 and 15 damage")
            print("   2 = Kick - does between 10 and 25 damage")
            print("   3 = Heal - gives back between 15 and 20 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move1 = input()
            
            print("\n"*50)
        
            print(str(c2)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 15 and 25 damage")
            print("   2 = Kick - does between 20 and 30 damage")
            print("   3 = Heal - gives back between 5 and 15 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move2 = input()

            if move1 == '1' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '1' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                

            if move1 == '1' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p2health3 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                    
            if move1 == '2' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                

            if move1 == '2' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '2' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p2health3 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                

            if move1 == '3' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p1health1 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                

            if move1 == '3' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p1health1 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health1 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p1health1 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p2health3 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health1 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '4' and move2 == '1':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 3:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(15,25)
                        p1health1 -= attack
                        print("")
                        print(str(c2)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health1 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health3 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '2':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 3:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(20,30)
                        p1health1 -= attack
                        print("")
                        print(str(c2)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health1 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health3 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '3':
                print(str(c1)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p2health3 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")


            if move2 == '4' and move1 == '1':
                miss = random.randint(1,2)
                time.sleep(1)
                if miss == 1:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(5,15)
                        p2health3 -= attack
                        print("")
                        print(str(c1)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health1 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health3 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '2':
                miss = random.randint(1,2)
                time.sleep(1)
                if miss == 1:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(10,25)
                        p2health3 -= attack
                        print("")
                        print(str(c1)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health1 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health3 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '3':
                print(str(c2)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p1health1 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

            if move1 == '4' and move2 == '4':
                time.sleep(1)
                print("Both players tried blocking")
                time.sleep(1)
                print("Both blocks fail")

            
                    
    elif c1 == '2' and c2 == '1':
        c1 = "Crixus"
        c2 = "Dreadnaut"
        while p1health2 > 0 and p2health1 > 0: 
            time.sleep(1)
            print(str(c1)+ "'s health is", str(p1health2))
            print(str(c2)+ "'s health is", str(p2health1))
            print("")
            time.sleep(1)
            print(str(c1)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 20 and 30 damage")
            print("   2 = Kick - does between 25 and 35 damage")
            print("   3 = Heal - gives back between 1 and 10 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move1 = input()
            
            print("\n"*50)
        
            print(str(c2)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 5 and 15 damage")
            print("   2 = Kick - does between 10 and 25 damage")
            print("   3 = Heal - gives back between 15 and 20 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move2 = input()

            if move1 == '1' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '1' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '1' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p2health1 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                    
            if move1 == '2' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                

            if move1 == '2' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '2' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p2health1 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p1health2 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                

            if move1 == '3' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,1)
                    p1health2 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p1health2 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p2health1 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '4' and move2 == '1':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 3:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(20,30)
                        p1health2 -= attack
                        print("")
                        print(str(c2)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health2 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health1 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '2':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 3:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(25,35)
                        p1health2 -= attack
                        print("")
                        print(str(c2)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health2 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health1 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '3':
                print(str(c1)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p2health1 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")


            if move2 == '4' and move1 == '1':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 1 or miss == 2 or miss == 4 or miss == 5:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(5,15)
                        p2health1 -= attack
                        print("")
                        print(str(c1)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health2 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health1 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '2':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 1 or miss == 2 or miss == 4 or miss == 5:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(10,25)
                        p2health1 -= attack
                        print("")
                        print(str(c1)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health2 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health1 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '3':
                print(str(c2)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p1health2 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

            if move1 == '4' and move2 == '4':
                time.sleep(1)
                print("Both players tried blocking")
                time.sleep(1)
                print("Both blocks fail")
                
                    
    elif c1 == '2' and c2 == '2':
        c1 = "Crixus"
        c2 = "Achilles"
        while p1health2 > 0 and p2health2 > 0: 
            time.sleep(1)
            print(str(c1)+ "'s health is", str(p1health2))
            print(str(c2)+ "'s health is", str(p2health2))
            print("")
            time.sleep(1)
            print(str(c1)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 20 and 30 damage")
            print("   2 = Kick - does between 25 and 35 damage")
            print("   3 = Heal - gives back between 1 and 10 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move1 = input()
            
            print("\n"*50)
        
            print(str(c2)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 20 and 30 damage")
            print("   2 = Kick - does between 25 and 35 damage")
            print("   3 = Heal - gives back between 1 and 10 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move2 = input()

            if move1 == '1' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                

            if move1 == '1' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '1' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p2health2 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                    
            if move1 == '2' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '2' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '2' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p2health2 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                

            if move1 == '3' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p1health2 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                

            if move1 == '3' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p1health2 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,10)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p1health2 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p2health2 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '4' and move2 == '1':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 3 or miss == 1 or miss == 4 or miss == 2:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(20,30)
                        p1health1 -= attack
                        print("")
                        print(str(c2)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health1 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health1 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '2':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 3:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(25,35)
                        p1health1 -= attack
                        print("")
                        print(str(c2)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health1 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health1 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '3':
                print(str(c1)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p2health1 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")


            if move2 == '4' and move1 == '1':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 1 or miss == 2 or miss == 4 or miss == 5:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(20,30)
                        p2health2 -= attack
                        print("")
                        print(str(c1)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health2 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health2 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '2':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 1 or miss == 2 or miss == 4 or miss == 5:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(25,35)
                        p2health2 -= attack
                        print("")
                        print(str(c1)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health2 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health2 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '3':
                print(str(c2)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p1health2 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

            if move1 == '4' and move2 == '4':
                time.sleep(1)
                print("Both players tried blocking")
                time.sleep(1)
                print("Both blocks fail")
                    
    elif c1 == '2' and c2 == '3':
        c1 = "Crixus"
        c2 = "Daedalus"
        while p1health2 > 0 and p2health3 > 0: 
            time.sleep(1)
            print(str(c1)+ "'s health is", str(p1health2))
            print(str(c2)+ "'s health is", str(p2health3))
            print("")
            time.sleep(1)
            print(str(c1)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 20 and 30 damage")
            print("   2 = Kick - does between 25 and 35 damage")
            print("   3 = Heal - gives back between 1 and 10 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move1 = input()
            
            print("\n"*50)
        
            print(str(c2)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 15 and 25 damage")
            print("   2 = Kick - does between 20 and 30 damage")
            print("   3 = Heal - gives back between 5 and 15 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move2 = input()

            if move1 == '1' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '1' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                

            if move1 == '1' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p2health3 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                    
            if move1 == '2' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                

            if move1 == '2' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                

            if move1 == '2' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p2health3 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                

            if move1 == '3' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p1health2 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p1health2 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health2 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p1health2 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p2health3 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health2 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '4' and move2 == '1':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 3 or miss == 2 or miss == 1 or miss == 5:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(15,25)
                        p1health2 -= attack
                        print("")
                        print(str(c2)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health2 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health3 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '2':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 3:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(20,30)
                        p1health2 -= attack
                        print("")
                        print(str(c2)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health2 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health3 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '3':
                print(str(c1)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p2health3 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")


            if move2 == '4' and move1 == '1':
                miss = random.randint(1,2)
                time.sleep(1)
                if miss == 1:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(20,30)
                        p2health3 -= attack
                        print("")
                        print(str(c1)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health2 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health3 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '2':
                miss = random.randint(1,2)
                time.sleep(1)
                if miss == 1:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(25,35)
                        p2health3 -= attack
                        print("")
                        print(str(c1)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health2 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health3 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '3':
                print(str(c2)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p1health2 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

            if move1 == '4' and move2 == '4':
                time.sleep(1)
                print("Both players tried blocking")
                time.sleep(1)
                print("Both blocks fail")
                
        
    elif c1 == '3' and c2 == '1':
        c1 = "Akali"
        c2 = "Dreadnaut"
        while p1health3 > 0 and p2health1 > 0: 
            time.sleep(2)
            print(str(c1)+ "'s health is", str(p1health3))
            print(str(c2)+ "'s health is", str(p2health1))
            print("")
            time.sleep(1)
            print(str(c1)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 15 and 25 damage")
            print("   2 = Kick - does between 20 and 30 damage")
            print("   3 = Heal - gives back between 5 and 15 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move1 = input()
            
            print("\n"*50)
        
            print(str(c2)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 5 and 15 damage")
            print("   2 = Kick - does between 10 and 25 damage")
            print("   3 = Heal - gives back between 15 and 20 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move2 = input()

            if move1 == '1' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                time.sleep(1)
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                

            if move1 == '1' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '1' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p2health1 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                    
            if move1 == '2' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '2' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '2' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p2health1 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health1 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p1health3 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(5,15)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p1health3 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(10,25)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p1health3 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p2health1 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health1 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '4' and move2 == '1':
                miss = random.randint(1,2)
                time.sleep(1)
                if miss == 1:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(5,15)
                        p1health3 -= attack
                        print("")
                        print(str(c2)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health3 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health1 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '2':
                miss = random.randint(1,2)
                time.sleep(1)
                if miss == 1:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(10,25)
                        p1health3 -= attack
                        print("")
                        print(str(c2)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health3 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health1 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '3':
                print(str(c1)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p2health1 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")


            if move2 == '4' and move1 == '1':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 1:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(15,25)
                        p2health1 -= attack
                        print("")
                        print(str(c1)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health3 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health1 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '2':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 1:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(20,30)
                        p2health1 -= attack
                        print("")
                        print(str(c1)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health3 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health1 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '3':
                print(str(c2)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p1health3 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

            if move1 == '4' and move2 == '4':
                time.sleep(1)
                print("Both players tried blocking")
                time.sleep(1)
                print("Both blocks fail")

    elif c1 == '3' and c2 == '2':
        c1 = "Akali"
        c2 = "Achilles"
        while p1health3 > 0 and p2health2 >0: 
            time.sleep(2)
            print(str(c1)+ "'s health is", str(p1health3))
            print(str(c2)+ "'s health is", str(p2health2))
            print("")
            time.sleep(1)
            print(str(c1)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 15 and 25 damage")
            print("   2 = Kick - does between 20 and 30 damage")
            print("   3 = Heal - gives back between 5 and 15 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move1 = input()
            
            print("\n"*50)
        
            print(str(c2)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 20 and 30 damage")
            print("   2 = Kick - does between 25 and 35 damage")
            print("   3 = Heal - gives back between 1 and 10 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move2 = input()

            if move1 == '1' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '1' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

            if move1 == '1' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p2health2 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                    
            if move1 == '2' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '2' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '2' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p2health2 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health2 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p1health3 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p1health3 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(25,35)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p1health3 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p2health2 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health2 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '4' and move2 == '1':
                miss = random.randint(1,2)
                time.sleep(1)
                if miss == 1:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(20,30)
                        p1health3 -= attack
                        print("")
                        print(str(c2)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health3 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health2 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '2':
                miss = random.randint(1,2)
                time.sleep(1)
                if miss == 1:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(25,35)
                        p1health3 -= attack
                        print("")
                        print(str(c2)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health3 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health2 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '3':
                print(str(c1)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(1,10)
                    p2health2 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")


            if move2 == '4' and move1 == '1':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 1 or miss == 2 or miss == 4 or miss == 5:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(15,25)
                        p2health2 -= attack
                        print("")
                        print(str(c1)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health3 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health2 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '2':
                miss = random.randint(1,5)
                time.sleep(1)
                if miss == 1 or miss == 2 or miss == 3 or miss == 4:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(20,30)
                        p2health2 -= attack
                        print("")
                        print(str(c1)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health1 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health1 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '3':
                print(str(c2)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p1health3 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

            if move1 == '4' and move2 == '4':
                time.sleep(1)
                print("Both players tried blocking")
                time.sleep(1)
                print("Both blocks fail")
                    
    elif c1 == '3' and c2 == '3':
        c1 = "Akali"
        c2 = "Daedalus"
        while p1health3 > 0 and p2health3 > 0: 
            time.sleep(1)
            print(str(c1)+ "'s health is", str(p1health3))
            print(str(c2)+ "'s health is", str(p2health3))
            print("")
            time.sleep(1)
            print(str(c1)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 15 and 25 damage")
            print("   2 = Kick - does between 20 and 30 damage")
            print("   3 = Heal - gives back between 5 and 15 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move1 = input()
            
            print("\n"*50)
        
            print(str(c2)+", its your turn")
            print("")
            print("Select one of the following moves:")
            print("   1 = Punch - does between 15 and 25 damage")
            print("   2 = Kick - does between 20 and 30 damage")
            print("   3 = Heal - gives back between 5 and 15 health")
            print("   4 = Block - blocks opponents attack (decreases 25% accuracy each time you use it)")
            move2 = input()

            if move1 == '1' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '1' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '1' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p2health3 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                    
            if move1 == '2' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '2' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '2' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p2health3 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p2health3 -= attack
                    print("")
                    print(str(c1)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '1':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p1health3 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Punch missed")
                    print("")
                else:
                    attack = random.randint(15,25)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Punch did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '2':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p1health3 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Kick missed")
                    print("")
                else:
                    attack = random.randint(20,30)
                    p1health3 -= attack
                    print("")
                    print(str(c2)+"'s Kick did "+str(attack)+" damage")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '3' and move2 == '3':
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p1health3 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break
                
                miss = random.randint(1,10)
                time.sleep(1)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p2health3 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")

                if p1health3 <= 0:
                    print("Congratulations "+str(c2)+", you win!")
                    break
                elif p2health3 <= 0:
                    print("Congratulations "+str(c1)+", you win!")
                    break

            if move1 == '4' and move2 == '1':
                miss = random.randint(1,2)
                time.sleep(1)
                if miss == 1:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(15,25)
                        p1health3 -= attack
                        print("")
                        print(str(c2)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health3 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health3 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '2':
                miss = random.randint(1,2)
                time.sleep(1)
                if miss == 1:
                    print(str(c1)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c2)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(20,30)
                        p1health3 -= attack
                        print("")
                        print(str(c2)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health3 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health3 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c1) + " blocked your attack")

            if move1 == '4' and move2 == '3':
                print(str(c1)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c2)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(15,20)
                    p2health3 += heal
                    print("")
                    print(str(c2)+"'s Heal gave back "+str(heal)+" health")
                    print("")


            if move2 == '4' and move1 == '1':
                miss = random.randint(1,2)
                time.sleep(1)
                if miss == 1:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Punch missed")
                        print("")
                    else:
                        attack = random.randint(15,25)
                        p2health3 -= attack
                        print("")
                        print(str(c1)+"'s Punch did "+str(attack)+" damage")
                        print("")

                    if p1health3 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health3 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '2':
                miss = random.randint(1,2)
                time.sleep(1)
                if miss == 1:
                    print(str(c2)+ " tried blocking but it failed")
                    miss = random.randint(1,10)
                    if miss == 7:
                        print("")
                        print(str(c1)+"'s Kick missed")
                        print("")
                    else:
                        attack = random.randint(20,30)
                        p2health3 -= attack
                        print("")
                        print(str(c1)+"'s Kick did "+str(attack)+" damage")
                        print("")

                    if p1health3 <= 0:
                        print("Congratulations "+str(c2)+", you win!")
                        break
                    elif p2health3 <= 0:
                        print("Congratulations "+str(c1)+", you win!")
                        break
                    
                else:
                    print(str(c2) + " blocked your attack")

            if move2 == '4' and move1 == '3':
                print(str(c2)+ "'s block failed")
                miss = random.randint(1,10)
                if miss == 7:
                    print("")
                    print(str(c1)+"'s Heal failed")
                    print("")
                else:
                    heal = random.randint(5,15)
                    p1health3 += heal
                    print("")
                    print(str(c1)+"'s Heal gave back "+str(heal)+" health")
                    print("")

            if move1 == '4' and move2 == '4':
                time.sleep(1)
                print("Both players tried blocking")
                time.sleep(1)
                print("Both blocks fail")


#function for player vs computer
playerHealth = 100
computerHealth = 100
def playerVsComputer():
    global playerHealth, computerHealth
    print("")
    player = input("Enter your name: ")
    print("")
    while playerHealth > 0 and computerHealth > 0:
        player1(player)
        if computerHealth <= 0:
            print("")
            print("Congrats "+str(player)+", you win!")
            print("")
            playerHealth = 100
            computerHealth = 100
            break
        elif playerHealth <= 0:
            print("")
            print("Sorry "+str(player)+", but the computer won")
            print("")
            playerHealth = 100
            computerHealth = 100
            break
        computer(player)
        if computerHealth <= 0:
            print("")
            print("Congrats "+str(player)+", you win!")
            print("")
            playerHealth = 100
            computerHealth = 100
            break
        elif playerHealth <= 0:
            print("")
            print("Sorry "+str(player)+", but the computer won")
            print("")
            playerHealth = 100
            computerHealth = 100
            break

def player1(player):
    global playerHealth, computerHealth
    print(str(player)+ "'s health is", str(playerHealth))
    print("The Computer's health is", str(computerHealth))
    print("")    
    print(str(player)+", its your turn")
    print("")
    print("Select one of the following moves:")
    print("   1 = Punch - does between 10 and 20 damage")
    print("   2 = Kick - does between 1 and 30 damage")
    print("   3 = Heal - gives back between 5 and 10 health")

    move = input()

    if move == '1':
        miss = random.randint(1,10)
        if miss == 7:
            print("")
            print("Punch missed")
            print("")
        else:
            attack = random.randint(10,20)
            computerHealth -= attack
            print("")
            print("Punch did "+str(attack)+" damage")
            print("")
    elif move == '2':
        miss = random.randint(1,10)
        if miss == 7:
            print("")
            print("Kick missed")
            print("")
        else:
            attack = random.randint(1,30)
            computerHealth -= attack
            print("")
            print("Kick did "+str(attack)+" damage")
            print("")
    elif move == '3':
        miss = random.randint(1,10)
        if miss == 7:
            print("")
            print("Heal failed")
            print("")
        else:
            heal = random.randint(5,10)
            playerHealth += heal
            print("")
            print("Heal gave you "+str(heal)+" health")
            print("")
    
    
def computer(player):
    global playerHealth, computerHealth
    print(str(player)+ "'s health is", str(playerHealth))
    print("The Computer's health is", str(computerHealth))
    print("")
    print("It's the computer's turn now")
    move = random.randint(1,3)
    if move == 1:
        miss = random.randint(1,10)
        if miss == 7:
            print("")
            print("The computer chose Punch but it missed")
            print("")
        else:
            attack = random.randint(10,20)
            playerHealth -= attack
            print("")
            print("The computer chose Punch and it did "+str(attack)+" damage")
            print("")
    elif move == 2:
        miss = random.randint(1,10)
        if miss == 7:
            print("")
            print("The computer chose Kick but it missed")
            print("")
        else:
            attack = random.randint(1,30)
            playerHealth -= attack
            print("")
            print("The computer chose Kick and it did "+str(attack)+" damage")
            print("")
    elif move == 3:
        miss = random.randint(1,10)
        if miss == 7:
            print("")
            print("The computer tried to Heal but failed")
            print("")
        else:
            heal = random.randint(5,10)
            computerHealth += heal
            print("")
            print("The computer used Heal and got back "+str(heal)+" health")
            print("")

gameplay()
