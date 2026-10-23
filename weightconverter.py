# kg = float(input("\nEnter weight in kilogram:"))
# pounds = kg_to_pounds=(kg)
# print(f"\n{kg}={pounds:.2f}pounds.")

# pounds = float(input('\nEnter weight in pounds'))
# kg = pounds_to_kg=(pounds)
# print(f"\n{pounds}={kg:.2f}kilograms.")

# updated version with strip and split
pounds_value=2.2046
print("""1.convert your weight from pound to kg \n 2.convert your weight from kg to pounds (lbs) """)
user_option=input('option >>> ').strip().lower()
if user_option == '1':
    user_weight_lbs=input('enter your weight in pounds >>> ').strip('lbs').lower()
    splitted_user_weight=user_weight_lbs.split('lbs')
    print(splitted_user_weight)
    ansa=float(splitted_user_weight [0])//pounds_value
    print(f'your weight in pounds is {ansa}lbs')

elif user_option == '2':
    user_weight_in_kg=input('enter your weight in  kg >>> ').strip().lower()
    splitted_user_weight=user_weight_in_kg.split('kg')
    print(splitted_user_weight)
    ansa=float(splitted_user_weight[0])*pounds_value
    print(f"your weight in kg to pounds is {ansa}lbs")

else:
    print('invalid input')






# Build a cbt test base application
