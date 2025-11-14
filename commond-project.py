tasks=[]
while True:
    print("\n1.add contect")
    print("2.view contect")
    print("3.search contect")
    print("4.delete contect")
    print("5.exit")

    choice=input("enter your choice[1-5]:")

    if choice == '1':
        name=input("enter a name :")
        num=input("enter a num :")

        with open("contect.txt","a") as file:
            file.write(name+","+num+"\n")   
            print("contect add")             

    elif choice == '2':
        with open("contect.txt","r") as file:
            print("\n----contect----")
            print(file.read())   
               

    elif choice == '3':
        name=input("search name:")

        with open("contect.txt","r") as file:
            for line in file:
                if name.lower() in line.lower():
                    print("search:",line)
                    break 

    elif choice == '4':
        delete=input("delete a contect:")

        with open("contect.txt","r") as file:
            lines=file.readlines()

        with open("contect.txt","w") as file:
            for line in lines:
                if not line.lower().startwith(delete.lower()):
                    file.write(line)
            

    elif choice == '5':
        print("exit")
        break