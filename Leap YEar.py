x= int (input("Enter a year"))
ly= "Leap Year" if x%400==0 else "Leap Year" if x%4==0 and x%100!=0 else "Not a Leap Year"
print(ly);
