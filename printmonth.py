# Lerato Moholo
# 21/08/2024
month = input("Enter the month ('January', ..., 'December'):\n")
input_day = input("Enter the start day ('Monday', ..., 'Sunday'):\n")

# Assigning the months to their maximum dates    
if month == "January":
    end = 31
elif month == "February":
    end = 28
elif month == "March":
    end = 31
elif month == "April":
    end = 30
elif month == "May":
    end = 31
elif month == "June":
    end = 30
elif month == "July":
    end = 31
elif month == "August":
    end = 31
elif month == "September":
    end = 30
elif month == "October":
    end = 31
elif month == "November":
    end = 30
elif month == "December":
    end = 31

#Assigning the selected days to a number
if input_day == "Monday":
    day = 1
elif input_day == "Tuesday":
    day = 2
elif input_day == "Wednesday":
    day = 3
elif input_day == "Thursday":
    day = 4
elif input_day == "Friday":
    day = 5
elif input_day == "Saturday":
    day = 6 
elif input_day == "Sunday":
    day = 7
    
print(month)
print("Mo Tu We Th Fr Sa Su")

str_day = 1 # assigning the days to 1
                             
for i in range(6):   
    for j in range(1,8):          #rows and columns
        
        if i == 0:      
            if j >= day:  # if the column is greater than the str_day
                if str_day > 9:
                    print("{} ".format(str_day),end="")
                else:
                    print(" {} ".format(str_day),end="")
                str_day += 1 
            else:
                print("   ",end="")
        else:
            if str_day < end+1:           
                if str_day > 9:
                    print("{} ".format(str_day),end="")
                else:
                    print(" {} ".format(str_day),end="")
            else:
                print("",end="")
            str_day += 1
    if str_day == end:
        break
    print()