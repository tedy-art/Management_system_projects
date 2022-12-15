db = {
    101:{'name':'Jay', 'marks': 88, 'roll': 101, 'fees':20000},
    102:{'name':'Tom', 'marks': 80, 'roll': 102, 'fees':15000},
    103:{'name':'Devid', 'marks': 77, 'roll': 103, 'fees':25000}
}

def dashboard():
    print('Welcome to student Management system by batch 459')
    print("""
                        menu
                        1) Create student Record
                        2) Read Student Record
                        3) Update student record
                        4) Delete student record
    """)

def create_student():
    u_name = input('Enter student name : ')
    u_roll = eval(input('Enter student roll number : '))
    u_marks = eval(input('Enter student marks : '))
    u_fees = eval(input('Enter student fees : '))

    chotu_dict = {}

    chotu_dict['name'] = u_name
    chotu_dict['roll'] = u_roll
    chotu_dict['marks'] = u_marks
    chotu_dict['fees'] = u_fees

    db[u_roll] = chotu_dict
    print(f"Student {u_name} added successfully in db...")
    print('*'*65)
    print()

def read_student():
    print('-'*65)
    print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r = 'roll number', n ='Name', m = 'Marks', f='fees'))
    print('-'*65)
    for i in db:
        print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r = db[i]['roll'], n =db[i]['name'], m = db[i]['marks'], f=db[i]['fees']))
        print('-'*65)

def update_student():
    pass

def delete_student():
    pass

while True:
    dashboard()
    choice = eval(input("Enter your choice [1, 2, 3, 4] : "))

    if choice == 1:
        create_student()

    elif choice == 2:
        if db == 0:
            print("Database is empty...")
        else:
            read_student()


    elif choice == 3:
        update_student()
    
    elif choice == 4:
        
        delete_student()

    else:
        print("Invalid choice...")

    ch = input('Do you want to continue [y/n] : ')

    if ch.lower() != 'y':
        print(db)
        break