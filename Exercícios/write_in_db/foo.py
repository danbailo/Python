def option1():
    list_db = []
    list_db.append([str(input('Type the name of Data Base: ')).upper()])
    print(list_db)
    list_db.

def option2():
    print(option1)

def menu():
    menu_db = True
    while menu_db:
        print('-----------------------')
        print('          MENU         ')
        print('-----------------------')
        print('(1) Create a Data Base ')
        print('(2) Show all Data Bases ')
        print('(3) Connect a Data Base')
        print('(4) Operations in Data Base')
        print('(5) Write in Data Base Script')
        print('(6) Quit')
        option = int(input('Select an option: '))
        
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 6:
            menu_db = False

menu()