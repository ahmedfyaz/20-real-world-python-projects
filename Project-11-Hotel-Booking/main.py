import pandas as pd

df = pd.read_csv('hotels.csv')
class Hotel:
    def __init__(self,hotel_id):
        pass

    def book(self):
        pass

    def avaliable(self):
        pass


class ReservationTicket:
    def __init__(self,customer_name,hotel_object):
        pass
    def generate(self):
        pass


print(df)
hotel_id = input("Enter the id of the hotel")
hotel = Hotel(hotel_id)
if hotel.avaliable():
    hotel.book()
    name = input("Enter your name")
    reservation_ticket = ReservationTicket(name,hotel)
else:
    print("Hotel isn't free")