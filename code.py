import random
while True:
    print("Welcome to the OG Odd or Even Game..!!!\nYou've got the honors.. Be prepared to choose..!!")
    print("IF YOU WANT TO DECLARE THE MATCH, TYPE 'd'.")
    Toss=["Heads", "Tails"]
    bowler_dict={"One":1, "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Spin":"Spin"}
    bowler_list=list(bowler_dict.keys())
    bater_dict={"One":1, "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Stroke":"Stroke"}
    bater_list=list(bater_dict.keys())
    if (Toss_choice:=random.choice(Toss)) == input("Heads or Tails: ").capitalize().strip():
        Toss = True
        if (Choice_1 := (input("Enter your choice. (Batting / Bowling): ").lower().strip())) == "batting":
            print(f"You had won the toss and decided on {Choice_1} first. Good Luck.")
            print("You have the following choices..\n", list(bater_dict.values()), sep='')
            Result = True
            wicket = 0
            Score_1 = 0
            balls = 0
            overs = 0 
            while wicket == 0:
                Run = input("Enter what you wanna bat for this ball: ").capitalize().strip()
                Ball = random.choice(bowler_list)
                if Run.lower().strip() == "d":
                    Result = None
                    break
                elif Run not in [str(i) for i in bater_dict.values()]:
                    print("Enter a valid option.")
                    balls -= 1
                elif (Run != 'Stroke' and Run != str(bowler_dict[Ball])) :
                    Score_1 += int(Run)
                elif (Run == 'Stroke' and bowler_dict[Ball] == 'Spin') or Run.lower().strip() == str(bowler_dict[Ball]) :
                    wicket = 1
                    print("Ops, You got OUT. :( ")
                    print(f"You scored {Score_1} runs.")
                elif (Run == 'Stroke' and bowler_dict[Ball] != 'Spin'):
                    Score_1 += bowler_dict[Ball]
                else:
                    print("LogicalError@1")
                balls+=1
                if balls%6 == 0:
                    overs += 1
                    balls = 0
                    print(f"In the end of {overs} overs, You scored {Score_1}.")
            if Run.lower().strip() == "d":
                break
            Score_2 = 0
            balls = 0
            overs = 0
            print("You have the following choices..\n", list(bowler_dict.values()), sep='')
            print(f"You've scored {Score_1}.\nNow you should Bowl.\nYou should score {Score_1+1} to win the match.")
            while wicket == 1:
                Ball = input("Enter what you wanna bowl for this ball: ").capitalize().strip()
                Run = random.choice(bater_list)
                if Ball.lower().strip() == "d":
                    Result = None
                    break
                elif Ball not in [str(i) for i in bowler_dict.values()]:
                    print("Enter a valid option.")
                    balls -= 1
                elif str(bater_dict[Run]) != 'Stroke' and str(bater_dict[Run]) != Ball:
                    Score_2 += int(bater_dict[Run])
                elif (Run == 'Stroke' and Ball == 'Spin') or Ball == str(bater_dict[Run]) :
                    print("You took the wicket.")
                    print(f"The opponent scored {Score_2} runs.")
                    wicket = 2
                elif str(bater_dict[Run]) == 'Stroke' and Ball != 'Spin':
                    Score_2 += int(Ball)
                else:
                    print("LogicalError@2")
                balls+=1
                if Score_2 > Score_1:
                    print("The match is won by the Opponent.")
                    Result = False
                    break
                if balls%6 == 0:
                    overs += 1
                    balls = 0
                    print(f"In the end of {overs} overs, The opponent scored {Score_2}.")
        elif Choice_1 == "bowling":
            print(f"You had won the toss and decided on {Choice_1} first. Good Luck.")
            print("You have the following choices..\n", list(bowler_dict.values()), sep='')
            Result = False
            wicket = 0
            Score_3 = 0
            balls = 0
            overs = 0
            while wicket == 0:
                Ball = input("Enter what you wanna bowl for this ball: ").capitalize().strip()
                Run = random.choice(bater_list)
                if Ball.lower().strip() == "d":
                    Result = None
                    break
                elif Ball not in [str(i) for i in bowler_dict.values()]:
                    print("Enter a valid option.")
                    balls -= 1
                elif str(bater_dict[Run]) != 'Stroke' and str(bater_dict[Run]) != Ball:
                    Score_3 += int(bater_dict[Run])
                elif (Run == 'Stroke' and Ball == 'Spin') or Ball == str(bater_dict[Run]) :
                    print("You took the wicket.")
                    print(f"The opponent scored {Score_3} runs.")
                    wicket = 1
                elif str(bater_dict[Run]) == 'Stroke' and Ball != 'Spin':
                    Score_3 += int(Ball)
                else:
                    print("LogicalError@3")
                balls+=1
                if balls%6 == 0:
                    overs += 1
                    balls = 0
                    print(f"In the end of {overs} overs, The opponent scored {Score_3}.")
            if Ball.lower().strip() == "d":
                break
            Score_4 = 0
            balls = 0
            overs = 0
            print("You have the following choices..\n", list(bater_dict.values()), sep='')
            print(f"The Opponent had scored {Score_3}.\nNow you should Bat.\nYou should score {Score_3+1} to win the match.")
            while wicket == 1:
                Run = input("Enter what you wanna bat for this ball: ").capitalize().strip()
                Ball = random.choice(bowler_list)
                if Run.lower().strip() == "d":
                    Result = None
                    break
                elif Run not in [str(i) for i in bater_dict.values()]:
                    print("Enter a valid option.")
                    balls -= 1
                elif (Run != 'Stroke' and Run != str(bowler_dict[Ball])) :
                    Score_4 += int(Run)
                elif (Run == 'Stroke' and bowler_dict[Ball] == 'Spin') or Run.lower().strip() == str(bowler_dict[Ball]) :
                    wicket = 1
                    print("Ops, You got OUT. :( ")
                    print(f"You scored {Score_4} runs.")
                elif (Run == 'Stroke' and bowler_dict[Ball] != 'Spin'):
                    Score_4 += bowler_dict[Ball]
                else:
                    print("LogicalError@4")
                balls+=1
                if Score_4 > Score_3:
                    print("The match is won by the User.")
                    Result = True
                    break
                if balls%6 == 0:
                    overs += 1
                    balls = 0
                    print(f"In the end of {overs} overs, You scored {Score_4}.")
        else:
            print("LogicalError@5")
    elif (Choice_2 := random.choice(["Batting", "Bowling"])) == "Bowling": 
        Toss = False
        print(f"You had lost the toss and your Opponent has decided on {Choice_2} first. Good Luck.")
        print("You have the following choices..\n", list(bater_dict.values()), sep='')
        Result = True
        wicket = 0
        Score_1 = 0
        balls = 0
        overs = 0 
        while wicket == 0:
            Run = input("Enter what you wanna bat for this ball: ").capitalize().strip()
            Ball = random.choice(bowler_list)
            if Run.lower().strip() == "d":
                    Result = None
                    break
            elif Run not in [str(i) for i in bater_dict.values()]:
                print("Enter a valid option.")
                balls -= 1
            elif (Run != 'Stroke' and Run != str(bowler_dict[Ball])) :
                Score_1 += int(Run)
            elif (Run == 'Stroke' and bowler_dict[Ball] == 'Spin') or Run.lower().strip() == str(bowler_dict[Ball]) :
                wicket = 1
                print("Ops, You got OUT. :( ")
                print(f"You scored {Score_1} runs.")
            elif (Run == 'Stroke' and bowler_dict[Ball] != 'Spin'):
                Score_1 += bowler_dict[Ball]
            else:
                print("LogicalError@6")
            balls+=1
            if balls%6 == 0:
                overs += 1
                balls = 0
                print(f"In the end of {overs} overs, You scored {Score_1}.")
        Score_2 = 0
        balls = 0
        overs = 0
        if Run.lower().strip() == "d":
            break
        Result = True
        print("You have the following choices..\n", list(bowler_dict.values()), sep='')
        print(f"You've scored {Score_1}.\nNow you should Bowl.\nYou should score {Score_1+1} to win the match.")
        while wicket == 1:
            Ball = input("Enter what you wanna bowl for this ball: ").capitalize().strip()
            Run = random.choice(bater_list)
            if Ball.lower().strip() == "d":
                    Result = None
                    break
            elif Ball not in [str(i) for i in bowler_dict.values()]:
                print("Enter a valid option.")
                balls -= 1
            elif str(bater_dict[Run]) != 'Stroke' and str(bater_dict[Run]) != Ball:
                Score_2 += int(bater_dict[Run])
            elif (Run == 'Stroke' and Ball == 'Spin') or Ball == str(bater_dict[Run]) :
                print("You took the wicket.")
                print(f"The opponent scored {Score_2} runs.")
                wicket = 2
            elif str(bater_dict[Run]) == 'Stroke' and Ball != 'Spin':
                Score_2 += int(Ball)
            else:
                print("LogicalError@7")
            balls+=1
            if Score_2 > Score_1:
                print("The match is won by the Opponent.")
                Result = False
                break
            if balls%6 == 0:
                overs += 1
                balls = 0
                print(f"In the end of {overs} overs, The opponent scored {Score_2}.")
    elif Choice_2 == "Batting":
        Toss = False
        print(f"You had lost the toss and your Opponent has decided on {Choice_2} first. Good Luck.")
        print("You have the following choices..\n", list(bowler_dict.values()), sep='')
        Result = False
        wicket = 0
        Score_3 = 0
        balls = 0
        overs = 0
        while wicket == 0:
            Ball = input("Enter what you wanna bowl for this ball: ").capitalize().strip()
            Run = random.choice(bater_list)
            if Ball.lower().strip() == "d":
                    Result = None
                    break
            elif Ball not in [str(i) for i in bowler_dict.values()]:
                print("Enter a valid option.")
                balls -= 1
            elif str(bater_dict[Run]) != 'Stroke' and str(bater_dict[Run]) != Ball:
                Score_3 += int(bater_dict[Run])
            elif (Run == 'Stroke' and Ball == 'Spin') or Ball == str(bater_dict[Run]) :
                print("You took the wicket.")
                print(f"The opponent scored {Score_3} runs.")
                wicket = 1
            elif str(bater_dict[Run]) == 'Stroke' and Ball != 'Spin':
                Score_3 += int(Ball)
            else:
                print("LogicalError@8")
            balls+=1
            if balls%6 == 0:
                overs += 1
                balls = 0
                print(f"In the end of {overs} overs, The opponent scored {Score_3}.")
        if Ball.lower().strip() == "d":
            break
        wicket = 0
        Score_4 = 0
        balls = 0
        overs = 0
        print("You have the following choices..\n", list(bater_dict.values()), sep='')
        print(f"The Opponent had scored {Score_3}.\nNow you should Bat.\nYou should score {Score_3+1} to win the match.")
        while wicket == 1:
            Run = input("Enter what you wanna bat for this ball: ").capitalize().strip()
            Ball = random.choice(bowler_list)
            if Run.lower().strip() == "d":
                    Result = None
                    break
            elif Run not in [str(i) for i in bater_dict.values()]:
                print("Enter a valid option.")
                balls -= 1
            elif (Run != 'Stroke' and Run != str(bowler_dict[Ball])) :
                Score_4 += int(Run)
            elif (Run == 'Stroke' and bowler_dict[Ball] == 'Spin') or Run.lower().strip() == str(bowler_dict[Ball]) :
                wicket = 1
                print("Ops, You got OUT. :( ")
                print(f"You scored {Score_4} runs.")
            elif (Run == 'Stroke' and bowler_dict[Ball] != 'Spin'):
                Score_4 += bowler_dict[Ball]
            else:
                print("LogicalError@9")
            balls+=1
            if Score_4 > Score_3:
                print("The match is won by the User.")
                Result = True
                break
            if balls%6 == 0:
                overs += 1
                balls = 0
                print(f"In the end of {overs} overs, You scored {Score_4}.")
    else:
        print("LogicalError@10")
    print("GOOD GAME. WELL PLAYED...!!!!!")
    print("Match Summary..")
    break
while True:
    if Toss:
        print(f"The user won the toss by calling {Toss_choice} and chose on {Choice_1} first.")
        if Choice_1 == "batting":
            print(f"The User chose to bat first and scored {Score_1}.")
            Difference = abs(Score_1 - Score_2)
        elif Choice_1 == "bowling":
            print(f"The User chose to bowl first and let the Opponent score {Score_3} runs.")
            Difference = abs(Score_3 - Score_4)
    else:
        print(f"The User lost the toss by calling {Toss_choice} and the Opponent chose on {Choice_2} first.")
        if Choice_2 == "batting":
            print(f"The Opponent chose to bat first and scored {Score_2}.")
        elif Choice_2 == "bowling":
            print(f"The Opponent chose to bowl first and let the User score {Score_4} runs.")
    if Result is None:
        print("\nRESULT : The match has won by the Opponent as the User Declared the Match.\n")
    elif Result is True:
        print(f"\nRESULT : USER WON THE MATCH BY {Difference} \n")
    else:
        print(f"\nRESULT : OPPONENT WON THE MATCH BY {Difference}\n")
    if input("Do you wanna play again..??(Yes/No) ").capitalize().strip() == "No":
        break
