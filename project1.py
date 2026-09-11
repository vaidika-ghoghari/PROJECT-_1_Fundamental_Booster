print("\nWelcome to the Interactive Personal Data Collector ! ")

#take a name from user
name=input("\nPlease enter your name : ")

#take a age from user
age =int(input("Please enter your age : "))

#take a height from user
height=float(input("Please enter Your height in meters : "))

#take a favourite number from user
fav_num=int(input("Please enter your favourite number : "))

print("--"*50)
#print a thank you message for inputing information
print("Thank you! Here is the information we collected :")


#print a user's detail with the data type and memory address
print("\nName : ",name)
print("Data Type : ",type(name))
print("Memory Address : ",id(name))

print(" \nAge : ",age)
print("Data Type : ",type(age))
print("Memory Address : ",id(age))

print("\nHeight : ",height)
print("Data Type : ",type(height))
print("Memory Address : ",id(height))

print("\nFavourite Number : ",fav_num)
print("Data Type : ",type(fav_num))
print("Memory Address : ",id(fav_num))

'''
#print user details  with f-string
print(f"\nName : {name}  ,  (Data Type  :  {type(name) } )  ,  (Memory Address  :  {id(name)})")
print(f"Age : {age}  ,  (Data Type  :  {type(age) } )  ,  (Memory Address  :  {id(age)})")
print(f"Height : {height}  ,  (Data Type  :  {type(height) } )  ,  (Memory Address  :  {id(height)})")
print(f"Favourite Number  : {fav_num}  ,  (Data Type  :  {type(fav_num) } )  ,  (Memory Address  :  {id(fav_num)})")
'''

print("--"*50)
#calculation of birth year
current_year=2026
year_of_birth=current_year-age
#print a birth year
print(f"Your birth year is approximately :{year_of_birth} (based on your age of {age} ) ")

#print a final thank you message 
print("\nThank you for using the Personal Data Collecter. Goodbye !")
