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
    pass

def read_student():
    pass

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
        read_student()

    elif choice == 3:
        update_student()
    
    elif choice == 4:
        delete_student()

    else:
        print("Invalid choice...")

    ch = input('Do you want to continue [y/n] : ')

    if ch.lower() != 'y':
        break