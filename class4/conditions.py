# is

# NUMBER1 = 10
# NUMBER2 = 10

# NUMBER1 is NUMBER2

# if NUMBER1 is NUMBER2:
#     print("They are equal")
# else:
#     print("They are not equal")

# if NUMBER1 is not NUMBER2:
#     print("They are not equal")
# else:
#     print("They are equal")    

# # in
# """
#     in operator
# """
# HIDDEN_FRUIT = "kiwi"

# FRUIT_LIST1 = ["apple", "pear", "banana"]
# print(type(FRUIT_LIST1))
# FRUIT_LIST2 = ("mango", "melon", "cherry")
# print(type(FRUIT_LIST2))
# FRUIT_LIST3 = {"peach", "apricot", "kiwi"}
# print(type(FRUIT_LIST3))

# if HIDDEN_FRUIT in FRUIT_LIST1:
#     print("Hidden fruit is in List1")
# elif HIDDEN_FRUIT in FRUIT_LIST2:
#     print("Hidden fruit is in List2")
# elif HIDDEN_FRUIT in FRUIT_LIST3:
#     print("Hidden fruit is in List3")      
# else:
#     print("Hidden fruit is not found")   



while True:
    try:
        RESPONSE = int(input("When were you born? e.g 'year' : "))
        if RESPONSE >= 2000 and RESPONSE <= 2022:
            print("You were born in 21st century")
        elif RESPONSE >= 1900 and RESPONSE <= 1999:
            print("You were born in 20th century")
        elif RESPONSE == 1899 or RESPONSE <= 1898:
            print("You should not be running this.")    
        else: 
            print("Please give me a number")
        break        
    except TypeError:
        print("Error: did you provide digit e.g 1")
    except ValueError:
        print("Did you enter the right value? ")




# [ ]
# COMMAND + ] move to the right
# COMMAND + [ move to the left
# test


ANSWER = "no"
while ANSWER != "yes":
    ANSWER = input("Are you crazy? ")
    if ANSWER == "yes":
        print("I knew that")