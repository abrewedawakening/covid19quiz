while True:
    import time
    #type one letter by one letter saying a welcome
    string = "WELCOME TO THE COVID 19 QUIZ!"
    for start_sentance in string:
        print(start_sentance, end='')
        time.sleep(.05)
        #confirm start
    confirm = input("\npress ENTER to start ...")
    if confirm == "":
        #sets amount of cases per correct question
        cases_var = 50
        #sets current cases
        count = 0
        #set cure percentage complete
        cure = 0
        #type one letter by one letter saying enjoy the game
        string = "Enjoy the game!"
        for enjoy_game in string:
            print(enjoy_game, end='')
            time.sleep(0.05)
        #waits 2 seconds before displaying next screen
        time.sleep(2)
        #loading screen
        string = "\nGame Loading!"
        for gameloading in string:
            print(gameloading, end='')
            time.sleep(0.05)
        #waits 2 seconds before displaying next screen
        time.sleep(2)
        #displays a loading bar
        string = "\n-----"
        for load in string:
            print(load, end='')
            time.sleep(1)
        time.sleep(0.75)
        #speeds up loading bar
        string = "-----"
        for load in string:
            print(load, end='')
            time.sleep(0.05)
        time.sleep(1)
        #tells the user the game has loaded
        string = "\nLoaded!"
        for loaded in string:
            print(loaded, end='')
            time.sleep(0.05)
        time.sleep(2)
        #explains the game printing one charachter at a time
        string = "\nI will ask you a series of questions, each correct answer you give, \na certain amount of people get COVID 19, try to get as many people infected as possible!\nEach answer you get wrong, the cure for Covid 19 is developed! You have the ability to power up by using cases,\nBy buying power ups with current cases, it creates more cases developed with a correct answer!"
        for explain in string:
            print(explain, end='')
            time.sleep(0.05)
        time.sleep(2)
        #displays ready? one charachter at a time
        string = "\nReady?"
        for ready in string:
            print(ready, end='')
            time.sleep(.05)
        time.sleep(1)
        #displays set! one charachter at a time
        string = "\nSet!"
        for ready_set in string:
            print(ready_set, end='')
            time.sleep(.05)
        time.sleep(1)
        #displays Go! one charachter at a time
        string = "\nGo!"
        for go in string:
            print(go, end='')
            time.sleep(.05)
        time.sleep(1)
        #question one
        one = input("\nCOVID 19 is a _____").strip().lower()
        if one == "virus":
            #prints correct and adds 10 infected people
            string = "correct"
            for correct in string:
                print(correct, end='')
                time.sleep(.05)
                count += cases_var
            print("\n{} people have been infected with COVID 19!".format(count))
            #asks if the user wants to buy a power up
            ask_powerup1 = input("would you like to buy a 2x powerup for 250 cases?\n").strip().lower()
            if ask_powerup1 == "yes" and count >= 250:
                cases_var *= 2
                count -= 250
                #if they do not have enough cases to buy power up do not proceed with purchace
            elif ask_powerup1 == "yes" and count <= 250:
                string = "You Do Not Have Enough Cases!"
                for denied in string:
                    print(denied, end='')
                    time.sleep(.05)
            else:
                print("Ok You have not bought the 2x power up!")
        elif cure >= 100:
            print(" You have lost the game!")
            break
        else:
            #prints wrong and displays cure progress and people infected and adds 10 to the cure
            cure += 25
            string = "Wrong\n{} people have been infected with COVID 19, the cure is {}% complete".format(count, cure)
            for wrong in string:
                print(wrong, end='')
                time.sleep(.05)
        two = input("\nCovid 19 fills the _____ with mucus? ").strip().lower()
        if two == "lungs":
            string = "correct"
            for correct in string:
                print(correct, end='')
                time.sleep(.05)
                count += cases_var
            print("\n{} people have been infected with COVID 19!".format(count))
            #asks if the user wants to buy a power up
            ask_powerup2 = input("would you like to buy a 2x powerup for 750 cases?\n").strip().lower()
            if ask_powerup2 == "yes" and count >= 750:
                cases_var *= 2
                count -= 1000
            #if they do not have enough cases to buy power up do not proceed with purchace
            elif ask_powerup2 == "yes" and count <= 750:
                string = "You Do Not Have Enough Cases!"
                for denied in string:
                    print(denied, end='')
                    time.sleep(.05)
            else:
                print("Ok You have not bought the 2x power up!")
        elif cure >= 100:
            print(" You have lost the game!")
            break
        else:
            cure += 25
            string = "Wrong\n{} people have been infected with COVID 19, the cure is {}% complete".format(count, cure)
            for wrong in string:
                print(wrong, end='')
                time.sleep(.05)
            if cure >= 100:
                print(" You have lost the game!")
                break
        three = input("\nwhat country did covid 19 originate? ").strip().lower()
        if three == "china":
            string = "correct"
            for correct in string:
                print(correct, end='')
                time.sleep(.05)
                count += cases_var
            print("\n{} people have been infected with COVID 19!".format(count))
            #asks if the user wants to buy a power up
            ask_powerup3 = input("would you like to buy a 2x powerup for 1000 cases?\n").strip().lower()
            if ask_powerup3 == "yes" and count >= 1000:
                cases_var *= 2
                count -= 1000
            #if they do not have enough cases to buy power up do not proceed with purchace
            elif ask_powerup3 == "yes" and count <= 1000:
                string = "You Do Not Have Enough Cases!"
                for denied in string:
                    print(denied, end='')
                    time.sleep(.05)
            else:
                print("Ok You have not bought the 2x power up!")
        else:
            cure += 25
            string = "Wrong\n{} people have been infected with COVID 19, the cure is {}% complete".format(count, cure)
            for wrong in string:
                print(wrong, end='')
                time.sleep(.05)
            if cure >= 100:
                print(" You have lost the game!")
                break
        four = input("\nTrue or False? Can Covid 19 affect animals? ").strip().lower()
        if four == "true":
            string = "correct"
            for correct in string:
                print(correct, end='')
                time.sleep(.05)
                count += cases_var
            print("\n{} people have been infected with COVID 19!".format(count))
            #asks if the user wants to buy a power up
            ask_powerup4 = input("would you like to buy a 2x powerup for 1500 cases?\n").strip().lower()
            if ask_powerup4 == "yes" and count >= 1500:
                cases_var *= 2
                count -= 1500
            #if they do not have enough cases to buy power up do not proceed with purchace
            elif ask_powerup4 == "yes" and count <= 5000:
                print("\nYou Do Not Have Enough Cases!")
            else:
                print("Ok You have not bought the 2x power up!")
        else:
            cure += 25
            string = "Wrong\n{} people have been infected with COVID 19, the cure is {}% complete".format(count, cure)
            for wrong in string:
                print(wrong, end='')
                time.sleep(.05)
            if cure >= 100:
                print(" You have lost the game!")
                break
        five = input("\nWhat Month did we start our first covid 19 lockdown in NZ? (full name)").strip().lower()
        if five == "march":
            string = "correct"
            for correct in string:
                print(correct, end='')
                time.sleep(.05)
                count += cases_var
            print("\n{} people have been infected with COVID 19!".format(count))
            #asks if the user wants to buy a power up
            ask_powerup5 = input("would you like to buy a 5x powerup for 2000 cases?\n").strip().lower()
            if ask_powerup5 == "yes" and count >= 2000:
                cases_var *= 5
                count -= 2000
            #if they do not have enough cases to buy power up do not proceed with purchace
            elif ask_powerup5 == "yes" and count <= 2000:
                string = "You Do Not Have Enough Cases!"
                for denied in string:
                    print(denied, end='')
                    time.sleep(.05)
            else:
                print("Ok You have not bought the 5x power up!")
        else:
            cure += 25
            string = "Wrong\n{} people have been infected with COVID 19, the cure is {}% complete".format(count, cure)
            for wrong in string:
                print(wrong, end='')
                time.sleep(.05)
            if cure >= 100:
                print(" You have lost the game!")
                break
        six = input("\nTrue or False, Covid 19 is airborn? ").strip().lower()
        if six == "true":
            string = "correct"
            for correct in string:
                print(correct, end='')
                time.sleep(.05)
                count += cases_var
            print("\n{} people have been infected with COVID 19!".format(count))
            #asks if the user wants to buy a power up
            ask_powerup6 = input("would you like to buy a 10x powerup for 2500 cases?\n").strip().lower()
            if ask_powerup6 == "yes" and count >= 2500:
                cases_var *= 10
                count -= 2500
            #if they do not have enough cases to buy power up do not proceed with purchace
            elif ask_powerup6 == "yes" and count <= 2500:
                string = "You Do Not Have Enough Cases!"
                for denied in string:
                    print(denied, end='')
                    time.sleep(.05)
            else:
                print("Ok You have not bought the 10x power up!")
        else:
            cure += 25
            string = "Wrong\n{} people have been infected with COVID 19, the cure is {}% complete".format(count, cure)
            for wrong in string:
                print(wrong, end='')
                time.sleep(.05)
            if cure >= 100:
                print(" You have lost the game!")
                break
        seven = input("\nWhat type animal was believed to have given humans the virus? ").strip().lower()
        if seven == "bat":
            string = "correct"
            for correct in string:
                print(correct, end='')
                time.sleep(.05)
                count += cases_var
            print("\n{} people have been infected with COVID 19!".format(count))
            #asks if the user wants to buy a power up
            ask_powerup7 = input("would you like to buy a 10x powerup for 3000 cases?\n").strip().lower()
            if ask_powerup7 == "yes" and count >= 3000:
                cases_var *= 10
                count -= 3000
            #if they do not have enough cases to buy power up do not proceed with purchace
            elif ask_powerup7 == "yes" and count <= 3000:
                string = "You Do Not Have Enough Cases!"
                for denied in string:
                    print(denied, end='')
                    time.sleep(.05)
            else:
                print("Ok You have not bought the 10x power up!")
        else:
            cure += 25
            string = "Wrong\n{} people have been infected with COVID 19, the cure is {}% complete".format(count, cure)
            for wrong in string:
                print(wrong, end='')
                time.sleep(.05)
            if cure >= 100:
                print(" You have lost the game!")
                break
        eight = input("\nDonald _____ was the president of the United States of America when the virus started ").strip().lower()
        if eight == "trump":
            string = "correct"
            for correct in string:
                print(correct, end='')
                time.sleep(.05)
                count += cases_var
            print("\n{} people have been infected with COVID 19!".format(count))
            #asks if the user wants to buy a power up
            ask_powerup8 = input("would you like to buy a 10x powerup for 3500 cases?\n").strip().lower()
            if ask_powerup8 == "yes" and count >= 3500:
                cases_var *= 10
                count -= 3500
            #if they do not have enough cases to buy power up do not proceed with purchace
            elif ask_powerup8 == "yes" and count <= 3500:
                string = "You Do Not Have Enough Cases!"
                for denied in string:
                    print(denied, end='')
                    time.sleep(.05)
            else:
                print("Ok You have not bought the 10x power up!")
        else:
            cure += 25
            string = "Wrong\n{} people have been infected with COVID 19, the cure is {}% complete".format(count, cure)
            for wrong in string:
                print(wrong, end='')
                time.sleep(.05)
            if cure >= 100:
                print(" You have lost the game!")
                break
        nine = input("\nTrue Or False: Covid 19 is a pandemic ").strip().lower()
        if nine == "true":
            string = "correct"
            for correct in string:
                print(correct, end='')
                time.sleep(.05)
                count += cases_var
            print("\n{} people have been infected with COVID 19!".format(count))
            #asks if the user wants to buy a power up
            ask_powerup9 = input("would you like to buy a 10x powerup for 4000 cases?\n").strip().lower()
            if ask_powerup9 == "yes" and count >= 4000:
                cases_var *= 10
                count -= 4000
            #if they do not have enough cases to buy power up do not proceed with purchace
            elif ask_powerup9 == "yes" and count <= 4000:
                string = "You Do Not Have Enough Cases!"
                for denied in string:
                    print(denied, end='')
                    time.sleep(.05)
            else:
                print("Ok You have not bought the 10x power up!")
        else:
            cure += 25
            string = "Wrong\n{} people have been infected with COVID 19, the cure is {}% complete".format(count, cure)
            for wrong in string:
                print(wrong, end='')
                time.sleep(.05)
            if cure >= 100:
                print(" You have lost the game!")
                break
        ten = input("\nWhat year did COVID 19 start? ").strip().lower()
        if ten == "2019":
            string = "correct"
            for correct in string:
                print(correct, end='')
                time.sleep(.05)
                count += cases_var
            print("\n{} people have been infected with COVID 19!".format(count))
            #asks if the user wants to buy a power up
            ask_powerup10 = input("would you like to buy a 10x powerup for 4500 cases?\n").strip().lower()
            if ask_powerup10 == "yes" and count >= 4500:
                cases_var *= 10
                count -= 4500
            #if they do not have enough cases to buy power up do not proceed with purchace
            elif ask_powerup10 == "yes" and count <= 4500:
                string = "You Do Not Have Enough Cases!"
                for denied in string:
                    print(denied, end='')
                    time.sleep(.05)
            else:
                print("Ok You have not bought the 10x power up!")
        else:
            cure += 25
            string = "Wrong\n{} people have been infected with COVID 19, the cure is {}% complete".format(count, cure)
            for wrong in string:
                print(wrong, end='')
                time.sleep(.05)
            if cure >= 100:
                print(" You have lost the game!")
                break
    print("Congratulations, You Have Won the Game, You Have Infected Many People With the virus without the cure being fully developed!")
    break
