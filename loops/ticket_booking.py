# Topic : Ticket Booking
seats = 8

while seats > 0:
    print("Available seats:", seats)
    
    book = input("Do you want to book a seat? (yes/no): ").lower()
    
    if book == "yes":
        seats -= 1
        print("Seat booked successfully!\n")
    else:
        print("Thank you! Visit again.")
        break

if seats == 0:
    print("All seats are booked.")