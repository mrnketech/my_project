while True:
    print("1. Multiply a number")
    print("2. Whats your name")
    print("3. Say hello")
    print("4. Exit")
    choice = input("Choose between the numbers (1-4): ")

    if choice == "1":
        num1 = int(input("Give me a number: "))
        num2 = int(input("give me another number: "))
        total = num1 * num2
        print(f"The combined numbers sums up to... {total} ")

    elif choice == "2":
        name = input("What is your name?: ")
        print(f"Your name is {name}, hope you enjoy my menu!")

    elif choice == "3":
        name1 = input("Whats your gamertag /  nickname?: ")
        print(f"Hello {name1}")

    elif choice == "4":
        print(f"good bye, come back next time!")
        break
    
    else:
        print("Invalid option, please select the number between (1-4)")