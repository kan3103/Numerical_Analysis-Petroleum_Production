import os 
import pandas as pd
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve
os.system("cls")

def linear_function(x, a, b):
    return a * x + b

def main():
    name_file=input("Enter the path of file: ")
    file_excel = pd.read_excel(name_file) # Enter the true hyperlink to read excel file
    year = pd.DataFrame(file_excel,columns=['Year'])
    average= pd.DataFrame(file_excel,columns=['World Average Daily Production of Crude Oil includeing lease condensate (Mb/d)'])
    cumulative = pd.DataFrame(file_excel,columns=['Cumulative World Production Since 1980 (Mb)'])
    
    print("1 to print in the data in 2D")
    print("2 to Math modeling the data in your selection")
    print("3 to solve the f(x),f'(x) ,f\"(x) from 2 ")
    print("4 to calculate of the y'(x) or y\"(x) at a certain point ")
    print("5 to")
    num=int(input("Enter a number: "))

    if (num==1) :
        fig, ax1 = plt.subplots()
        ax1.plot(year, average, linestyle='-', color='r', label='Average')
        ax1.set_xlabel('Năm')
        ax1.set_ylabel('Sản lượng Dầu (Mb/d)', color='r')
        ax1.tick_params('y', colors='r')
        ax1.set_title("Sản lượng dầu")

        fig, ax2 = plt.subplots()
        ax2.plot(year, cumulative, linestyle='-', color='r', label='Average')
        ax2.set_xlabel('Năm')
        ax2.set_ylabel('Cumulative World Production Since 1980 (Mb)', color='r')
        ax2.tick_params('y', colors='r')
        ax2.set_title("Sản lượng tích lũy")
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')

        plt.show()
    if(num==2) :
        print("Enter 1 for x")
        print("Enter 2 for x^2")
        print("Enter 3 for x^3")
        print("Enter 4 for a^x")
        select_model= int(input("Enter your selection: "))
        
        if( select_model == 1 ):
            a= year["Year"].shape[0]
            b=c=d=e=0
            for i in range(0,a):
                b+=year["Year"][i]
                c+=cumulative["Cumulative World Production Since 1980 (Mb)"][i]
                d+=year["Year"][i]**2
                e+=year['Year'][i]*cumulative['Cumulative World Production Since 1980 (Mb)'][i]
                print(a,b,c,d,e)
            x, y = symbols('x y')
            # Khai báo phương trình
            eq1 = Eq(a*x + b*y, c)
            eq2 = Eq(b*x + d*y, e)
            solution = solve((eq1, eq2), (x, y))
            y_values=linear_function(year,solution[y],solution[x])
            print(solution[x] , "+" ,solution[y],"x")   
            plt.plot(year,y_values, color="red" , label='Model')
            plt.plot(year,cumulative, color="blue",label='Data')
            plt.xlabel('Year')
            plt.ylabel('Cumulative World Production Since 1980 (Mb)')
            plt.title('Linear Model vs. Data')
            plt.legend()
            plt.show()
        
main()