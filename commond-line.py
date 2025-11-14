tasks=[]
while True:
    print("\ntask manager")
    print("1.add a task")
    print("2.view tasks")
    print("3.remove task")
    print("4.exit")

    choice = input( "Enter your choice(1-4):" )

    if choice == '1':
        task=input("enter a task:")
        tasks.append(task)
        print("task add")


    elif choice == '2':
        print("Your tasks:", tasks)

    elif choice == '3':
        tasks=input("enter a task:")
        if task in tasks:
            tasks.remove(task)
            print("task remove")
        else:
            print("nothing")

    elif choice == '4':
        print("exit")
        break
