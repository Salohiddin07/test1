import sqlite3


class DataBase:
    def __init__(self, path_to_db='main.db'):
        self.path_to_db = path_to_db
        self.db.create_table_brands()
        self.db.create_table_models()


def add_brand():
    brand = input("Brand nomini kiriting: ")
    db.insert_brand(brand)
    yes_no = input("Yana brand qo'shasizmi? yes/no: ").lower()
    if yes_no == 'yes':
        add_brand()


def del_brand():
    view_brands()
    brand = input("O'chirmoqchi bo'lgan brand nomini kiriting: ")
    db.delete_brand(brand)
    yes_no = input("Yana brand o'chirasizmi? yes/no: ").lower()
    if yes_no == 'yes':
        del_brand()


def view_brands():
    brands = db.select_brands()
    for brand in brands:
        print(brand[0], brand[1])


def add_model():
    model = input("Model nomini kiriting: ")
    color = input("Model rangini kiriting: ")
    price = int(input("Model narxini kiriting: "))
    view_brands()
    brand_id = int(input("Brand id sini kiriting: "))
    db.insert_model(model, color, price, brand_id)
    yes_no = input("Yana model qo'shasizmi? yes/no: ").lower()
    if yes_no == 'yes':
        add_model()

def view_models():
    models = db.select_models()
    for model in models:
        model_id, model, color, price, brand = model
        print(model_id, model, color, price, brand)


def run():
    while True:
        command = input("Nima qilmoqchisiz? : ").lower()
        if command == 'add brand':
            add_brand()

        if command == 'del brand':
            del_brand()

        if command == 'view brands':
            view_brands()

        if command == 'add model':
            add_model()

        if command == 'view models':
            view_models()

        if command == 'stop':
            break



if __name__ == '__main__':
    run()

    def execute(self, sql: str, parameters: tuple=None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = sqlite3.connect(self.path_to_db)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_brands(self):
        sql = '''CREATE TABLE IF NOT EXISTS brands(
            brand_id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand_name VARCHAR(15) UNIQUE
        )'''
        self.execute(sql, commit=True)

    def insert_brand(self, brand_name):
        sql = '''INSERT INTO brands(brand_name) VALUES (?)'''
        self.execute(sql, parameters=(brand_name,), commit=True)

    def select_brands(self):
        sql = '''SELECT * FROM brands'''
        return self.execute(sql, fetchall=True)

    def delete_brand(self, brand_name):
        sql = '''DELETE FROM brands WHERE brand_name = ?'''
        self.execute(sql, parameters=(brand_name,), commit=True)

    def create_table_models(self):
        sql = '''CREATE TABLE IF NOT EXISTS models(
            model_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name VARCHAR(30) UNIQUE,
            color VARCHAR(10),
            price INTEGER,
            brand_id INTEGER REFERENCES brands(brand_id)
        )'''
        self.execute(sql, commit=True)

    def insert_model(self, model_name, color, price, brand_id):
        sql = '''INSERT INTO models(model_name, color, price, brand_id) VALUES (?, ?, ?, ?)'''
        self.execute(sql, parameters=(model_name, color, price, brand_id), commit=True)

    def select_models(self):
        sql = '''SELECT model_id, model_name, color, price, brand_name FROM models
        JOIN brands ON models.brand_id = brands.brand_id'''
        return self.execute(sql, fetchall=True)

    def create_table_employee(self):
        sql = '''CREATE TABLE IF NOT EXISTS employee(
            employee_id INTEGER PRIMARY KEY,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            birth_date DATE,
            phone_number INTEGER,
            email VARCHAR(29),
            country VARCHAR(15),
            city VARCHAR(15)
        )'''
        self.execute(sql, commit=True)

    def insert_employee(self, employee_id, first_name, last_name, birth_date, phone_number, email, country, city):
        sql = '''INSERT INTO employee(employee_id, first_name, last_name, birth_date,
        phone_number, email, country, city) 
        VALUES(?, ?, ?, ?, ?, ?, ?)'''
        self.execute(sql, parameters=(employee_id, first_name, last_name, birth_date, phone_number, email, country, city))

    def create_table_customers(self):
        sql = '''CREATE TABLE IF NOT EXISTS customers(
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
	        birth_date DATE,
	        phone_number VARCHAR(15),
	        email VARCHAR(30),
	        country VARCHAR(30),
	        city VARCHAR(30)
        )'''
        self.execute(sql, commit=True)

    def insert_customers(self, first_name, last_name, birth_date, phone_number, email, country, city):
        sql = '''INSERT INTO customers(first_name, last_name, birth_date, phone_number, email, country, city)
        VALUES(?, ?, ?, ?, ?, ?, ?)'''
        self.execute(sql, parameters=(first_name, last_name, birth_date, phone_number, email, country, city))

    def create_table_orders(self):
        sql = '''CREATE TABLE IF NOT EXISTS orders(
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
	        customer_id INTEGER REFERENCES customers(customer_id),
	        employee_id INTEGER REFERENCES employees(employee_id),
	        model_id INTEGER REFERENCES models(model_id),
	        car_count INTEGER,
	        order_date DATE
        )'''

    def insert_orders(self,  car_count, order_date):
        sql = '''INSERT INTO orders(
            car_count, order_date) VALUES(?, ?)
        '''
        self.execute(sql, parameters=(car_count, order_date))


db = DataBase()
print('The end')