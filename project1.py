print("Welcome to the Interactive Personal Data Collecter ! ")

name=input("Please enter your name : ")
age =int(input("Please enter your age : "))
height=float(input("Please enter Your height in meters : "))
fav_num=int(input("Please enter your favourite number : "))

print("\n Thank you! Here is the information we collected :")

print("\Name : ",name, "  (type : ",type(name),", Memory Address : ",id(name),")")
print("\n Age : ",age, "  (type : ",type(age),", Memory Address : ",id(age),")")
print("\n Height : ",height, "  (type : ",type(height),", Memory Address : ",id(height),")")
print("\n Favourite Number : ",fav_num, "  (type : ",type(fav_num),", Memory Address : ",id(fav_num),")")

present_year=2026
year_of_birth=present_year-age
print(f"\nYour birth year is approximately :{year_of_birth} (based on your age of {age} ) ")

print("\n Thank you for using the Personal Data Collecter. Goodbye !")
