# import essential functions
import Return
import Split_List
import dt
import Borrow

#DEFINE
def start():
    while(True):
        print("    !!!Welcome to the library management system!!!    ")
        print("------------------------------------------------------")
        print("To display, enter 1.")
        print("To borrow, enter 2.")
        print("To return a book, enter 3.")
        print("To exit, enter 4.")
        try:
            z=int(input("Choose from 1 to 4 options: "))
            print()
            if(z==1):
                Data=open("Book_List.txt","r") 
                lines=Data.readlines() 
                A=[] 
                for line in lines:
                    A.append(line.replace("\n","").split(","))
                Data.close() 
                for i in range(len(A)):
                    print(" Book Title: ",A[i][0],"\t\t AUTHOR: ",A[i][1],"\t\t QUANTITY: ",A[i][2],"\t\tPRICE: ",A[i][3])
                return A 
                
   
            elif(z==2):
                Split_List.listSplit()
                Borrow.borrowBook()
            elif(z==3):
                Split_List.listSplit()
                Return.returnBook()
            elif(z==4):
                print("********************************************************")
                print("     Thank you for using Library Management System")
                print("********************************************************")
                break
            else:
                print("Please select a valid option from 1 to 4.")
        except ValueError:
            print("Please input as directed.")
start() # Call function
