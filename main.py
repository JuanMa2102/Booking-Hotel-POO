import pandas as pd
df = pd.read_csv('hotels.csv', dtype={'id': str})

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == hotel_id, 'name'].squeeze()
        

    def book(self):
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        return False

class ReservationTicket:
    def __init__(self, customer_name, hotel):
        self.customer_name = customer_name
        self.hotel = hotel

    def generate(self):
        content = f"""
            Thank you for booking with us!
            Here are your reservation details:
            Customer Name: {self.customer_name}
            Hotel name: {self.hotel.name}
        """
        return content


print(df)
hotel_id = input("Enter hotel ID: ")
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation = ReservationTicket(name, hotel)
    print( reservation.generate() )
else:
    print("Sorry, this hotel is not available.")
    