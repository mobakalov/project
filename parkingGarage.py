# Start Your Code here

class Garage():
    tickets = [{1:""}, {2:""}, {3:""}, {4:""}, {5:""}]
    parking_spaces = [{1:""}, {2:""}, {3:""}, {4:""}, {5:""}]
    current_ticket = {}

    def take_tickets(self):
        if self.tickets:
            print("Happy Parking")
            print(self.tickets[0])
            self.current_ticket.update(self.tickets[0])
            del self.tickets[0]
            self.taken_parking = self.parking_spaces[0]
            del self.parking_spaces[0]
        else:
            print("Garage is currently full, please try again later")

    def pay_for_parking(self):
        if self.parking_spaces:
            print("What is your ticket number?")
            print(self.tickets[0])
            self.current_ticket.update(self.tickets[0])



        


    def leave_garage(self):
        if self.current_ticket:
            print("What is your ticket number?")
            if 0 < self.tickets < 10: 
                print("Thanks you, have a nice day")
                print(self.tickets[0])
        
                self.current_ticket.update(self.ticket[0])
            else: 
                print("Invalid entry, please try again")
                 


    def UI(self):
            while True:
                response = str(input("\n What would you like to do? Enter, Pay, Exit, or Quit \n")).lower()
                if response == "enter":
                    self.take_tickets()
                if response == "pay":
                    self.pay_for_parking
                if response == " exit":
                    self.leave_garage
                if response == "quit":
                    print("Have a nice day!")
                    break
                else:
                    print("Invalid answer, please try again!")

print("testing")

                




test = Garage()
test.UI()







# Your parking gargage class should have the following methods:
# - takeTicket
#    - This should decrease the amount of tickets available by 1
#    - This should decrease the amount of parkingSpaces available by 1
# - payForParking
#    - Display an input that waits for an amount from the user and store it in a variable
#    - If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
#    - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
#    - If the ticket has been paid, display a message of "Thank You, have a nice day"
#    - If the ticket has not been paid, display an input prompt for payment
#       - Once paid, display message "Thank you, have a nice day!"
#    - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
#    - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary