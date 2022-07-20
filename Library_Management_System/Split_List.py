# Function to split list from .txt file and store it in lists.

def listSplit():
    global bookName
    global authorName
    global quantity
    global cost
    bookName=[]
    authorName=[]
    quantity=[]
    cost=[]
    with open("Book_List.txt","r") as f:
        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            arm=0
            for z in lines[i].split(','):
                if(arm==0):
                    bookName.append(z)
                elif(arm==1):
                    authorName.append(z)
                elif(arm==2):
                    quantity.append(z)
                elif(arm==3):
                    cost.append(z.strip("$"))
                arm+=1
