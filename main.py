import pandas as pd
df = pd.read_csv('hotels.csv', dtype={'id': str})
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')

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

class CreditCard:
    def __init__(self, number ):
        self.number = number
    
    def validate(self, expiration_date, holder, cvc):
        card_data = {"number": self.number, "expiration_date": expiration_date, "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        return False

print( df )
hotel_id = input("Enter hotel ID: ")
hotel = Hotel(hotel_id)
if hotel.available():
    # card_number = input("Enter your credit card number: ")
    
    credit_card = CreditCard( number = "1234-5678-9012-3456" )
    if credit_card.validate(
        expiration_date = "12/25",  # Placeholder for expiration date
        holder= "John Doe",  # Placeholder for card holder name
        cvc = "123"  # Placeholder for CVC
    ):
        hotel.book()
        name = input("Enter your name: ")
        reservation = ReservationTicket(name, hotel)
        print( reservation.generate() )
    else:
        print("Invalid credit card details.")
else:
    print("Sorry, this hotel is not available.")
    