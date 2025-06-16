import pandas as pd
from abc import ABC, abstractmethod

df = pd.read_csv('hotels.csv', dtype={'id': str})
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')
df_cards_security = pd.read_csv('card_security.csv', dtype=str)


class Hotel:
    watermark = "The real estate company"
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
    
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        return False


class Ticket(ABC):

    @abstractmethod
    def generate(self):
        pass 

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
    
    @property
    def the_customer_name(self):
        name = self.customer_name.strip().title()
        return name
    
    @staticmethod
    def convert(amount):
        return amount  * 1.2

class DigitalTicket(ReservationTicket):

    def generate(self):
        content = super().generate()
        content += f"\nYour digital ticket will be sent to: {self.email}"
        return content


hotel = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")

print(hotel.name)
print(hotel2.name)
print(Hotel.watermark)
print(hotel.watermark)  # Accessing the class variable through an instance

ticket = ReservationTicket(customer_name="john doe", hotel=hotel)
print(ticket.the_customer_name)

converted = ReservationTicket.convert(100)
print(converted)  # Should print 120.0