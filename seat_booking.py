seats = {'A1': 'available', 'A2': 'available', 'A3': 'available', 'A4': 'available', 'A5': 'available',
    'B1': 'available', 'B2': 'available', 'B3': 'available', 'B4': 'available', 'B5': 'available',
    'C1': 'available', 'C2': 'available', 'C3': 'available', 'C4': 'available', 'C5': 'available',}

users = {'user1': 'password1','user2': 'password2','user3': 'password3'}

while True:
    print("\nWelcome to Seat Reservation System")
    print("1. Login")
    print("2. Register")
    print("3. Reserve a Seat")
    print("4. Exit")

    ch =int(input("Enter your choice: "))

    if ch == 1:
        print("Enter username and password to login:")
        username = input("Username: ")
        password = input("Password: ")
        if users.get(username) == password:
            print("Login successful!")
            while True:
                print("\nAvailable seats:")
                for seat in seats.keys():
                    if seats.get(seat) == 'available':
                        print(seat)
                seat_choice = input("Enter seat to reserve (e.g: A1), or type 'back' to go back: ")
                if seat_choice.lower() == 'back':
                    break
                if seats.get(seat_choice) == 'available':
                    seats[seat_choice] = 'reserved'
                    print("Seat",seat_choice," reserved successfully!")
                else:
                    print("Seat",seat_choice," is not available.")
        else:
            print("Login failed. Invalid username or password.")

    elif ch == 2:
        print("Enter new username and password to register:")
        new_username = input("Username: ")
        new_password = input("Password: ")
        users[new_username] = new_password
        print("Registration successful!")

    elif ch == 3:
        print("\nAvailable seats:")
        for seat in seats.keys():
            if seats.get(seat) == 'available':
                print(seat)
        seat_choice = input("Enter seat to reserve(eg:'B4') : ")
        if seats.get(seat_choice) == 'available':
            seats[seat_choice] = 'reserved'
            print("Seat",seat_choice," reserved successfully!")
        else:
            print("Seat", seat_choice," is not available.")

    elif ch == 4:
        print("Thank you for using the Seat Reservation System. Goodbye")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")