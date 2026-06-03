import random
# Print welcome message on screen
print("🚆 Welcome to Indian Railway Booking System 🚆")
# Total seats available in train
available_seats = 5
# Show available seats to user
print("Available Seats :", available_seats)
# Ask user how many seats they want
seats_required = int(input("\nHow many seats do you want to book? "))

station = input("\nFrom which station do you need train? ->> ")
end = input("\nAt which station will you leave the train? ->> ")

train_name = random.choice([
    "Sangamitra Express",
    "Vande Bharat",
    "Garib Rath Express",
    "Jodhpur Howrah",
    "Purusuttam Express",
    "Magadh express",
    "Jodpur superfast express",
    "Superfast express",
    "Aimrit bharat",
    "Prayagraj special"
])
# Check if enough seats are available
if seats_required <= available_seats:
    # Empty list to store passenger names
    passenger_names = []
    # Empty list to store passenger ages
    passenger_ages = []
    # Variable to store total bill amount
    total_bill = 0
    # Show train class menu
    print("\nChoose Train Class")
    # Sleeper class option
    print("1. Sleeper - ₹300")
    # AC class option
    print("2. AC - ₹800")
    # First class option
    print("3. First Class - ₹1500")
    # Take class choice from user
    choice = int(input("Enter your choice: "))
    # If user selects Sleeper
    if choice == 1:
        # Store class name
        class_name = "Sleeper"
        # Set base fare
        base_fare = 300
    # If user selects AC
    elif choice == 2:
        # Store class name
        class_name = "AC"
        # Set base fare
        base_fare = 800
    # If user selects First Class
    elif choice == 3:
        # Store class name
        class_name = "First Class"
        # Set base fare
        base_fare = 1500
    # If wrong choice entered
    else:
        # Print error message
        print("❌ Invalid Choice")
        # Stop program
        exit()
    # Default tatkal charge is 0
    tatkal_charge = 0
    # Ask user for tatkal booking
    tatkal = input("\nDo you want Tatkal booking? (yes/no): ")
    # Check if user selected yes
    if tatkal.lower() == "yes":
        # Tatkal charge for Sleeper
        if class_name == "Sleeper":
            tatkal_charge = 100
        # Tatkal charge for AC
        elif class_name == "AC":
            tatkal_charge = 200
        # Tatkal charge for First Class
        elif class_name == "First Class":
            tatkal_charge = 300
    # Default food charge is 0
    food_charge = 0
    # Ask user for food option
    food = input("Do you want food? (yes/no): ")
    # Check if user wants food
    if food.lower() == "yes":
        # Food charge for Sleeper
        if class_name == "Sleeper":
            food_charge = 80
        # Food charge for AC
        elif class_name == "AC":
            food_charge = 150
        # Food charge for First Class
        elif class_name == "First Class":
            food_charge = 250
    # Print heading for passenger details
    print("\n===== Enter Passenger Details =====")
    # Loop runs according to number of seats
    for i in range(seats_required):
        # Show passenger number
        print(f"\nPassenger {i+1}")
        # Take passenger name
        name = input("Enter Name: ")
        # Take passenger age
        age = int(input("Enter Age: "))
        # Store name in list
        passenger_names.append(name)
        # Store age in list
        passenger_ages.append(age)
        # Default discount is 0
        discount = 0
        # If child age less than 5
        if age < 5:
            # Full ticket free
            discount = base_fare
            # Print message
            print("🎉 Child Ticket Free!")
        # If senior citizen
        elif age >= 60:
            # Give 30% discount
            discount = base_fare * 0.30
            # Print message
            print("👴 Senior Citizen Discount Applied!")
        # Calculate passenger subtotal
        subtotal = base_fare - discount + tatkal_charge + food_charge
        # Calculate GST (5%)
        gst = subtotal * 0.05
        # Final amount after GST
        final_amount = subtotal + gst
        # Add passenger bill into total bill
        total_bill += final_amount
    # Reduce booked seats from available seats
    available_seats -= seats_required
    # Print final ticket heading
    print("\n==============================")
    # Ticket title
    print("🎫 TRAIN BOOKING DETAILS")
    print("==============================")
    # Print selected class
    print("Class :", class_name)
    # Print booked seats
    print('From station :',station)
    # Print from which station needs train.
    print('To station :',end)
    # print to which station leave the train.
    print("Seats Booked    :", seats_required)
    # Print ticket status
    print("Train name :",train_name)
    print("Ticket Status   : Confirmed")
    # Passenger detail heading
    print("\n----- PASSENGER DETAILS -----")
    # Loop for printing passenger details
    for i in range(seats_required):
        # Print passenger name and age
        print(f"{i+1}. {passenger_names[i]} - Age {passenger_ages[i]}")
    # Show remaining seats
    print("\nRemaining Seats :", available_seats)
    # Print final total bill
    print("\n💰 TOTAL BILL : ₹", round(total_bill, 2))
    # Thank you message
    print("\n✅ Thank You For Booking!")
    # Journey message
    print("🚆 Have a Safe Journey 🙏🏻!")
# If seats are not available
else:
    # Print sorry message
    print("\n❌ Sorry!")
    # Show seat not available message
    print("Not enough seats available.")
    # Ticket goes to waiting list
    print("Ticket Status : Waiting List")