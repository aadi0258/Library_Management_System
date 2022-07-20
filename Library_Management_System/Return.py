# IMPORT essential functions
import Split_List
import dt

def returnBook():
    name=input("Enter name of the borrower: ")
    z="Borrower-"+name+".txt"
    try:
        with open(z,"r") as f:
            lines=f.readlines()
            lines=[z.strip("$") for z in lines]
    
        with open(z,"r") as f:
            data=f.read()
            print(data)
    except:
        print("Name of the borrower is incorrect.")
        returnBook()

    # Return file creation
    y="Return-"+name+".txt"
    with open(y,"w+")as f:
        f.write("********************************************************** \n")
        f.write("                Library Management System \n")
        f.write("**********************************************************")
        f.write("                   Returned By: "+ name+"\n")
        f.write("    Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
        f.write("S.N.\t\t\tBookname\t\tCost\n")

    # For total cost
    total=0.0
    for i in range(3):
        if Split_List.bookName[i] in data:
            with open(y,"a") as f:
                f.write(str(i+1)+"\t\t"+Split_List.bookName[i]+"\t\t$"+Split_List.cost[i]+"\n")
                Split_List.quantity[i]=int(Split_List.quantity[i])+1
            total+=float(Split_List.cost[i])
            
    print("\t\t\t\t\t\t\t"+"$"+str(total))
    print("Is the book return date expired?")
    print("Press 'Y' for Yes and 'N' for No")
    stat=input()
    if(stat.upper()=="Y"):
        print("Number of days delayed to return the book?")
        day=int(input())
        penalty=2*day
        with open(y,"a")as f:
            f.write("\t\t\t\t\tFine: $"+ str(penalty)+"\n")
        total=total+penalty
    


    print("Final Total: "+ "$"+str(total))
    with open(y,"a")as f:
        f.write("\t\t\t\t\tTotal: $"+ str(total))
    
        
    with open("Book_List.txt","w+") as f:
            for i in range(3):
                f.write(Split_List.bookName[i]+","+Split_List.authorName[i]+","+str(Split_List.quantity[i])+","+"$"+Split_List.cost[i]+"\n")
