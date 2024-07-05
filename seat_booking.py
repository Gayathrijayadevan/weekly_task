# Initialize bus seats using a dictionary (seat_number: availability)
bus_seats = {}

# Assume the bus has 20 seats
for seat_number in range(1, 21):
    bus_seats[seat_number] = 'available'  # 'available' or 'reserved'

def display_seating():
    print("   Seats")
    print(" 1 2 3 4 5")
    for i in range(20):
        if i % 5 == 0:
            print()
            print(f'{i + 1:2}', end=' ')
        if bus_seats[i + 1] == 'available':
            print('O', end=' ')
        else:
            print('X', end=' ')
    print()

def reserve_seat(seat_number):
    if seat_number not in bus_seats.keys():
        print("Invalid seat number. Please choose between 1 and 20")
    elif bus_seats[seat_number] == 'reserved':
        print("Sorry, this seat is already reserved. Please select another seat.")
    else:
        bus_seats[seat_number] = 'reserved'
        print(f"Seat number {seat_number} has been successfully reserved.")
        display_seating()

# Example usage:

while True:
        print("\nBus Seat Reservation System")
        display_seating()
        seat_choice = input("Enter seat number to reserve (or 'q' to quit): ")
        
        if seat_choice.lower() == 'q':
            print("Thank you for using our bus reservation system.")
            break
        
        try:
            seat_number = int(seat_choice)
            reserve_seat(seat_number)
        except ValueError:
            print("Invalid input. Please enter a seat number.")