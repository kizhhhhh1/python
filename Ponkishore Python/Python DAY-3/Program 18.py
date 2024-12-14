def calculate_simple_interest(principal, time, is_senior_citizen):
    senior_citizen_roi = 0.15
    regular_customer_roi = 0.12
    roi = senior_citizen_roi if is_senior_citizen else regular_customer_roi
    return principal * roi * time

principal = float(input("enter the principal amount:"))
time = float(input("enter the time(in years):"))
is_senior_citizen = input("Is the customer a senior citizen?(yes/no):").strip().lower() == 'yes'

simple_interest = calculate_simple_interest(principal, time, is_senior_citizen)
print(f"The Simple Interest is {simple_interest:.2f}")
