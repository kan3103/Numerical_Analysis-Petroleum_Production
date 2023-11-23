import os 
import pandas as pd
import matplotlib.pyplot as plt
os.system("cls")

def p_x(p_xk):
    p_xk=0
    
def q_x(q_xk):
    q_xk=0

def main():
    name_file=input("Enter the path of file: ")
    file_excel = pd.read_excel(name_file) # Enter the true hyperlink to read excel file

    print("1 to print in the data in 2D")
    print("2 to Math modeling the data in your selection")
    print("3 to solve the f(x),f'(x) ,f\"(x) from 2 ")
    print("4 to calculate of the y'(x) or y\"(x) at a certain point ")
    print("5 to")
    num=int(input("Enter a number: "))

    if (num==1) :
        year = pd.DataFrame(file_excel,columns=['Year'])
        average= pd.DataFrame(file_excel,columns=['World Average Daily Production of Crude Oil includeing lease condensate (Mb/d)'])
        cumulative = pd.DataFrame(file_excel,columns=['Cumulative World Production Since 1980 (Mb)'])
        
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

        
main()