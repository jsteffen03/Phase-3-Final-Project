# lib/cli.py

from companies import (
    Clients,
    Sales,
    Salesman
)

def main():
    menu()
    choice = input(">")
    if choice =="1":
        signinUser()
    elif choice =="2":
        signinSales()
    elif choice =="3":
        print("Goodbye!")
        exit()
    else:
        print("Invalid Choice")
        main()


def signinUser():
    name = input("Enter your name: ")
    client = Clients.get_by_name(name)
    
    if client:
        print(f"Welcome, {client.name}!")
        clientMenu(client)
    else:
        print("Client not found. Would you like to create a new client? (yes/no)")
        choice = input(">").strip().lower()
        if choice == "yes":
            budget = int(input("Enter your budget: "))
            phone = int(input("Please enter your 10 digit phone number:"))
            new_client = Clients.create_client(name, phone, budget)
            print(f"Client created successfully. Welcome, {new_client.name}!")
            clientMenu(new_client)
        else:
            print("Bye Bye")
            main()


def signinSales():
    print("1. Trevin - Zebrascapes")
    print("2. Justin - Zebrascapes")
    print("3. Josh   - Zebrascapes")
    print("4. David  - Zebrascapes")
    id = input("Enter your id: ")
    salesman = Salesman.get_by_id(id)
    if salesman:
        print(f"Welcome, {salesman.name}!")
        Salesmenu(salesman)
    else:
        print("Not valid salesman")
        signinSales()

        

def clientMenu(client):
    print(f"Welcom to your page, {client.name}")
    print("What would you like to do? ")
    print("1. Create Sale")
    print("2. Head to main menu")
    choice = input(">").strip().lower()
    if choice == "1":
        print('''
Salesmen: 
1. Trevin - Zebrascapes
2. Justin - Zebrascapes
3. Josh   - Zebrascapes
4. David  - Zebrascapes
              ''')
        sale_id = int(input("Please choose a salesman and enter their id: "))
        client_id = client.id
        price = client.budget
        Sales.create_sale(sale_id, client_id, price)
        print(f"Sale Created!, we will reach out to you shortly, Thank you {client.name}!")
        main()

    elif choice == "2":
        main()
    else:
        print("invalid choice")

def Salesmenu(salesman):
    print("What would you like to do? ")
    print("1. View all sales")
    print("2. Choose sale by id")
    print("3. Head to main menu")
    choice = input(">").strip().lower()
    id = salesman.id
    if choice == "1":
        all_sales = Sales.get_sales_by_salesman(id)
        for sale in all_sales:
            print(sale)
        Salesmenu(salesman)
    elif choice == "2":
        sale_id = int(input("Enter sale id: "))
        sale = Sales.get_one_by_id(sale_id)
        if sale:
            print(sale)
            print("What would you like to do? ")
            print("1. Update next appointment")
            print("2. Update last contact")
            print("3. Update progress")
            print("4. Delete sale")
            print("5. Head to main menu")
            choice = input(">").strip().lower()
            if choice == "1":
                new_date = input("Enter new next appointment date: ")
                Sales.update_next_appointment(sale_id, new_date)
                Salesmenu(salesman)
            elif choice == "2":
                new_date = input("Enter new last contact date: ")
                Sales.update_last_contact(sale_id, new_date)
                Salesmenu(salesman)
            elif choice == "3":
                new_progress = input("Enter new progress: ")
                Sales.update_progress(sale_id, new_progress)
                Salesmenu(salesman)
            elif choice == "4":
                print("Sale Deleted")
                Sales.delete_sale(sale_id)
                Salesmenu(salesman)
            elif choice == "5":
                main()
            else: 
                print("Invalid choice")
                Salesmenu(salesman)
    elif choice == "3":
        main()
    else:
        print("Invalid Input")
        Salesmenu(salesman)


def menu():
    print("Please select an option:")
    print("1. Sign in as Client")
    print("2. Sign in as Salesman")
    print("3. Exit Program")


if __name__ == "__main__":
    main()
