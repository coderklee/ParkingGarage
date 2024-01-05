class ParkingGarage:
    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = 10
        self.parkingSpaces = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.currentTicket = {'Paid': False}
        self.unavailableSpaces = []
        
    def takeTicket(self):             
        if float(self.tickets) > 0 or len(self.parkingSpaces) > 0:
            self.tickets -= 1 
            takenSpace = self.parkingSpaces.pop()
            self.unavailableSpaces.append(takenSpace)
            print(f"Please proceed to space {takenSpace}")
        elif float(self.tickets) == 0 or len(self.parkingSpaces) == 0:
            print("There are no more spaces avaiable.")
        
    def payForParking(self):
        fee = float(input("Please enter the fee amount on your ticket. "))
        if fee > 0:
            self.currentTicket['Paid'] = True
            print("Your ticket has been paid, you will have 15 minutes to exit the garage.")
        else:
            print("Invalid entry. Fee must be greater than 0.")
                   
    def leaveGarage(self):
        if self.currentTicket['Paid'] == True:
            self.tickets += 1
            emptySpace = self.unavailableSpaces.pop()
            self.parkingSpaces.append(emptySpace)
            print("Thank you! Have a nice day!")
        else:
            print("Please pay your fee.")

car = ParkingGarage(1, 1, False)

def run():
    while True:
        response = input("What would you like to do? Park/Pay/Leave ")   
        if response.lower() == 'park':
            car.takeTicket()
        elif response.lower() == 'pay':
            car.payForParking()
        elif response.lower() == 'leave':
            car.leaveGarage()
        else:
            print("Invalid entry, please enter Park/Pay/Leave")
        
run()