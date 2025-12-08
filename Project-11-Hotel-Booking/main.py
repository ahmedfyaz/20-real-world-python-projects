import pandas as pd

df = pd.read_csv('hotels.csv',dtype={"id":str})
class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        pass

    def book(self):
        """Book the Hotel by changing its availablity to no"""
        df.loc[df["id"] == self.hotel_id,"available"] = "no"
        df.to_csv("hotels.csv",index=False)
        pass

    def available(self):
        """Check the availablity of the Hotel """
        availablity = df.loc[df["id"]==self.hotel_id,"available"].squeeze()
        if availablity == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self,customer_name,hotel_object):
        pass
    def generate(self):
        pass


print(df)
hotel_ID = input("Enter the id of the hotel")
hotel = Hotel(hotel_ID)
if hotel.available():
    hotel.book()
    name = input("Enter your name")
    reservation_ticket = ReservationTicket(name,hotel)
else:
    print("Hotel isn't free")