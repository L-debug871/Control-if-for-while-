# First Day of Year
# Stephan Jamieson
# 19/12/2014

# Gauss's Algorithm
# R(1 + 5R(A-1,4) + 4R(A-1,100) + 6R(A-1,400),7)
# R(y, m)=y%m


def main():
        
        year=eval(input('Enter the year: '))

        if year>=0:
                A=year
                A=A-1
                day=6*(A%400)
                day+=4*(A%100)
                day+=5*(A%4)
                day=(1+day)%7
                
                if day==0:
                        print(f"The 1st of January {year} falls on a Sunday")
                elif day==1:
                        print(f"The 1st of January {year} falls on a Monday")
                elif day ==2:
                        print(f"The 1st of January {year} falls on a Tuesday")
                elif day==3:
                        print(f"The 1st of January {year} falls on a Wednesday")
                elif day==4:
                        print(f"The 1st of January {year} falls on a Thursday")
                elif day==5:
                        print(f"The 1st of January {year} falls on a Friday")
                elif day==6:
                        print(f"The 1st of January {year} falls on a Satuday")
                                        
        else:
                print("FINISHED")
main()
