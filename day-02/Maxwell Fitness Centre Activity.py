# amount due before VAT
def amount_due(facility_code, hours):

    rates = {
        "squa": 13.00,
        "swim": 12.00,
        "gym": 11.00,
        "wei": 8.00
    }

    amount = rates[facility_code] * hours

    return amount

# final amount including 14% VAT
def final_amount_due(amount):

    vat = amount * 0.14
    final_amount = amount + vat

    return final_amount


# Display the customer's name and final amount
def display(name, final_amount):
   
    print("********************")
    print("Customer's invoice")
    print("Customer Name:", name)
    print(f"Final amount payable: R{final_amount:.2f}")

# Process the payment
def process_payment():

    name = input("Enter your name: ")
    facility_code = input("Enter facility code (squa, swim, gym, wei): ")
    hours = float(input("Enter number of hours used: "))

    amount = amount_due(facility_code, hours)

    final_amount = final_amount_due(amount)

    display(name, final_amount)

process_payment()