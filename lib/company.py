import sqlite3

import sqlite3
connection = sqlite3.connect("company.db")
cursor = connection.cursor()

class Clients:

    def __init__(self, name, phone, budget, id=None):
        self.id = id
        self.name = name 
        self.phone = phone
        self.budget = budget

    def get_name(self):
        return self._name 
    
    def set_name(self, value):
        if type(value) is str and len(value) > 1:
            self._name = value
        else:
            raise ValueError("Please enter a name greater than 1 letter")

    name = property(get_name, set_name)

    def get_phone(self):
        return self._phone 
    
    def set_phone(self, value):
        if type(value) is int and value > 1000000000:
            self._phone = value
        else:
            raise ValueError("Please enter a 10 digit Phone Number")

    phone = property(get_phone, set_phone)

    def get_budget(self):
        return self._budget 
    
    def set_budget(self, value):
        if type(value) is int:
            self._budget = value
        else:
            raise ValueError("Please Enter a Number")

    budget = property(get_budget, set_budget)

    def save_client(self):
        cursor.execute('''
        INSERT INTO clients(name, phone, budget)
        VALUES(?, ?, ?);
        ''', (self.name, self.phone, self.budget))
        connection.commit()
        all_clients = Clients.get_all()
        self.id = all_clients[-1].id

    @classmethod
    def get_all(cls):
        res = cursor.execute("SELECT * FROM clients")
        data = res.fetchall()
        all_clients =[]
        for client in data:
            cl = Clients(
                id = client[0],
                name = client[1],
                phone = client[2],
                budget = client[3]
            )
            all_clients.append(cl)
        print(all_clients)
        return all_clients

    def __repr__(self):
        return (
            f"<Client {self.id}: {self.name}, {self.phone}, " +
            f"Budget: {self.budget}>"
        )

class Salesman:

    def __init__(self, name, company_name, id=None):
        self.id = id
        self.name = name
        self.company_name = company_name

    def get_sales(self):
        return Sales.get_sales_by_salesman(self.id)

    @classmethod
    def get_all(cls):
        res = cursor.execute("SELECT * FROM salesmen")
        data = res.fetchall()
        all_salesmen =[]
        for salesmen in data:
            cl = Salesman(
                id = salesmen[0],
                name = salesmen[1],
                phone = salesmen[2],
                budget = salesmen[3]
            )
            all_salesmen.append(cl)
        print(all_salesmen)
        return all_salesmen

class Sales:

    def __init__(self, sales_id, client_id, price, next_appointment, last_contact, progress, id=None):
        self.id = id
        self.sales_id = sales_id
        self.client_id = client_id
        self.price = price
        self.next_appointment = next_appointment
        self.last_contact = last_contact
        self.progress = progress
    
    def get_sales_id(self):
        return self._sales_id

    def set_sales_id(self, value):
        # Assuming this method checks if sales_id exists in the salesman table
        res = cursor.execute("SELECT id FROM salesman WHERE id = ?", (value,))
        if res.fetchone() is None:
            raise ValueError("Not a Salesmen")
        self._sales_id = value
        
    sales_id = property(get_sales_id, set_sales_id)
        
    def get_client_id(self):
        return self._client_id

    def set_client_id(self, value):
        # Assuming this method checks if client_id exists in the clients table
        res = cursor.execute("SELECT id FROM clients WHERE id = ?", (value,))
        if res.fetchone() is None:
            raise ValueError("Not a Client")
        self._client_id = value
    
    client_id = property(get_client_id, set_client_id)
        
    def get_price(self):
        return self._price 
    
    def set_price(self, value):
        if type(value) is int:
            self._price = value
        else:
            raise ValueError("Please Enter a Number")

    price = property(get_price, set_price)

    def get_next_appointment(self):
        return self._next_appointment 
    
    def set_next_appointment(self, value):
        if type(value) is str and len(value) == 10 and "-" in value:
            self._next_appointment = value
        else:
            raise ValueError("Please enter date in format YYYY-MM-DD")

    next_appointment = property(get_next_appointment, set_next_appointment)

    def get_last_contact(self):
        return self._last_contact 
    
    def set_last_contact(self, value):
        if type(value) is str and len(value) == 10 and "-" in value:
            self._last_contact = value
        else:
            raise ValueError("Please enter date in format YYYY-MM-DD")
            
    last_contact = property(get_last_contact, set_last_contact)

    def get_progress(self):
        return self._progress
    
    def set_progress(self, value):
        if type(value) is str and (value == "In Progress" or value == "Sold!" or value == "Lost"):
            self._progress = value
        else:
            raise ValueError('''Please enter one of the following: "Sold!", "In Progress", "Lost";''')

    progress = property(get_progress, set_progress)

    def save_sale(self):
        cursor.execute('''
        INSERT INTO sales(sales_id, client_id, price, next_appointment, last_contact, progress)
        VALUES(?, ?, ?, ?, ?, ?);
        ''', (self.sales_id, self.client_id, self.price, self.next_appointment, self.last_contact, self.progress))
        connection.commit()
        all_sales = Sales.get_all()
        self.id = all_sales[-1].id

    @classmethod
    def get_all(cls):
        res = cursor.execute("SELECT * FROM sales")
        data = res.fetchall()
        all_sales =[]
        for sale in data:
            sal = Sales(
                id = sale[0],
                sales_id = sale[1],
                client_id = sale[2],
                price = sale[3],
                next_appointment = sale[4],
                last_contact = sale[5],
                progress = sale[6]
            )
            all_sales.append(sal)
        print(all_sales)
        return all_sales

    @classmethod
    def get_sales_by_salesman(cls, sales_id):
        res = cursor.execute("SELECT * FROM sales WHERE sales_id = ?", (sales_id,))
        data = res.fetchall()
        my_sales =[]
        for sale in data:
            sal = Sales(
                id = sale[0],
                sales_id = sale[1],
                client_id = sale[2],
                price = sale[3],
                next_appointment = sale[4],
                last_contact = sale[5],
                progress = sale[6]
            )
            my_sales.append(sal)
        print(my_sales)
        return my_sales
    
    @classmethod #Class method to access a sale by id for salesman changes
    def get_one_by_id(cls, id):
        res = cursor.execute(f'''
        SELECT * FROM sales
        WHERE id = {id}
        ''')
        data = res.fetchone()
        if data:
            my_sale = Sales(
                id = data[0],
                sales_id = data[1],
                client_id = data[2],
                price = data[3],
                next_appointment = data[4],
                last_contact = data[5],
                progress = data[6]
            )
        print(my_sale)
        return my_sale
    
    @classmethod
    def update_next_appointment(cls, sale_id, new_date):
        cursor.execute('''
        UPDATE sales
        SET next_appointment = ?
        WHERE id = ?;
        ''', (new_date, sale_id))
        connection.commit()
    
    @classmethod
    def update_next_appointment(cls, sale_id, new_date):
        cursor.execute('''
        UPDATE sales
        SET next_appointment = ?
        WHERE id = ?;
        ''', (new_date, sale_id))
        connection.commit()

    @classmethod
    def update_last_contact(cls, sale_id, new_contact):
        cursor.execute('''
        UPDATE sales
        SET last_contact = ?
        WHERE id = ?;
        ''', (new_contact, sale_id))
        connection.commit()

    @classmethod
    def update_progress(cls, sale_id, new_progress):
        cursor.execute('''
        UPDATE sales
        SET progress = ?
        WHERE id = ?;
        ''', (new_progress, sale_id))
        connection.commit()

    @classmethod
    def delete_sale(cls, sale_id):
        cursor.execute('''
        DELETE FROM sales
        WHERE id = ?;
        ''', (sale_id,))
        connection.commit()

    def __repr__(self):
        return (
            f"<Salesmen: {self.sales_id}, " +
            f"Client: {self.client_id}, " +
            f"Information: " +
            f"Price: {self.price}; Last Contact: {self.last_contact}; Next Appointment: {self.next_appointment}; Progress: {self.progress}>"
        )

if __name__ == "__main__":
    # print("Testing save_client method")

    # # Creating a new client instance
    # new_client = Clients(name="John Doe", phone=1234567890, budget=5000)
    
    # # Save the client to the database
    # new_client.save_client()
    
    # # Verify the client was saved
    # cursor.execute("SELECT * FROM clients")
    # all_clients = cursor.fetchall()
    # for client in all_clients:
    #     print(client)

    # salesman_trevin = Salesman(name="Trevin", company_name="Zebrascapes", id=1)
    # trevin_sales = salesman_trevin.get_sales()

    # print(f"Sales for salesman {salesman_trevin.name}:")
    # for sale in trevin_sales:
    #     print(sale)

    # sale_id = 1  # The ID of the sale you want to update
    # new_date = "2024-09-01"  # The new next_appointment date
    # new_contact = "2024-09-01"
    # new_progress = "Sold!"

    # Sales.update_next_appointment(sale_id, new_date)
    # Sales.update_last_contact(sale_id, new_contact)
    # Sales.update_progress(sale_id, new_progress)
    # # Print all sales to verify the update
    # print("All Sales after update:")
    # for sale in Sales.get_all():
    #     print(sale)
    pass