import time

time.sleep(1)
print('Whatever number you enter, a series of arithmetic operations will turn it into 4')
time.sleep(1)
print('Enter your number ')
user_number = input()
time.sleep(1)
print('step 1:','number', user_number, 'multiplied by 2 equals', int(user_number) * 2)
number_2 = int(user_number) * 2
time.sleep(1)
print('step 2:','number',number_2,'plus 8 equals',number_2 + 8)
number_3 = number_2 + 8
time.sleep(1)
print('step 3: number',number_3,'devided by 2 equals',number_3/2)
number_4 = number_3 / 2
time.sleep(1)
print('step 4: number',number_4,'minus ',user_number,'equals',number_4 - int(user_number))
time.sleep(1)
print("As I've said, it is 4))")
time.sleep(2)
print("Wonna try again? :)")
a = input()
if a == 'yes':
    print('Enter a number: ')
    user_number = input()
    time.sleep(1)
    print('step 1:','number', user_number, 'multiplied by 2 equals', int(user_number) * 2)
    number_2 = int(user_number) * 2
    time.sleep(1)
    print('step 2:','number',number_2,'plus 8 equals',number_2 + 8)
    number_3 = number_2 + 8
    time.sleep(1)
    print('step 3: number',number_3,'devided by 2 equals',number_3/2)
    number_4 = number_3 / 2
    time.sleep(1)
    print('step 4: number',number_4,'minus ',user_number,'equals',number_4 - int(user_number))
    time.sleep(1)
    print("4 again!n\Okay, it's enough")
elif a == 'no':
    print('Giving up is a right choice')
    
else:
    print('Choose "yes" or "no"')
