# IMPORT essential functions
import dt
import Split_List

def borrowBook():
    success=False
    while(True):
        firstName=input("Enter the first name of the borrower: ")
        if firstName.isalpha():
            break
        print("please input alphabet from A-Z")
    while(True):
        lastName=input("Enter the last name of the borrower: ")
        if lastName.isalpha():
            break
        print("please input alphabet from A-Z")
            
    # Create borrowers text file        
    t="Borrower-"+firstName+".txt"
    with open(t,"w+") as f:
        f.write("********************************************************** \n")
        f.write("               Library Management System  \n")
        f.write("**********************************************************")
        f.write("                   Borrowed By: "+ firstName+" "+lastName+"\n")
        f.write("    Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
        f.write("BookID \t\t\t Bookname \t\t      Authorname \n" )
    
    while success==False:
        print("Please select a option below:")
        for i in range(len(Split_List.bookName)):
            print("Enter", i, "to borrow book", Split_List.bookName[i])
    
        try:   
            z=int(input())
            try:
                if(int(Split_List.quantity[z])>0):
                    print("The book is available")
                    with open(t,"a") as f:
                        f.write("1. \t\t"+ Split_List.bookName[z]+"\t\t  "+Split_List.authorName[z]+"\n")

                    Split_List.quantity[z]=int(Split_List.quantity[z])-1
                    with open("Book_List.txt","w+") as f:
                        for i in range(3):
                            f.write(Split_List.bookName[i]+","+Split_List.authorName[i]+","+str(Split_List.quantity[i])+","+"$"+Split_List.cost[i]+"\n")


                    # Code to maintain multiple book borrowing system.
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Do you wish to borrow any other books? However, you are not permitted to borrow the same book again.\nPress 'y' for yes and 'n' for no: "))
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("\nPlease select an option below: ")
                            for i in range(len(Split_List.bookName)):
                                print("Enter", i, "to borrow book", Split_List.bookName[i])
                            z=int(input())
                            if(int(Split_List.quantity[z])>0):
                                print("The book is available")
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t\t"+ Split_List.bookName[z]+"\t\t  "+Split_List.authorName[z]+"\n")

                                Split_List.quantity[z]=int(Split_List.quantity[z])-1
                                with open("Book_List.txt","w+") as f:
                                    for i in range(3):
                                        f.write(Split_List.bookName[i]+","+Split_List.authorName[i]+","+str(Split_List.quantity[i])+","+"$"+Split_List.cost[i]+"\n")
                                        success=False
                            else:
                                loop=False
                                break
                        elif (choice.upper()=="N"):
                            print ("Thank you for borrowing books from us. ")
                            print("")
                            loop=False
                            success=True
                        else:
                            print("Please choose as instructed.")
                        
                else:
                    print("The book is not available")
                    borrowBook()
                    success=False
            except IndexError:
                print("")
                print("Please choose book in accordance with their number.")
        except ValueError:
            print("")
            print("Please choose as suggested.")
