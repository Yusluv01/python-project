# First project
# Hospital payment portal
# Co-operative society portal


# print("HOSPITAL PAYMENT PORTAL")
# hosp_page=("""      WELCOME TO F.M.C TEACHING HOSPITAL
#                 select:
#                 1: Login as an Existing Patient
#                 2: Register as a New Patient
#                 3: Exit
        
#     """)
# print(hosp_page)
# users=[]
# pat_opt=input('option>>')
# if pat_opt == '1':
#     for form_num in range(1):
#         login_name=input('Enter your Name>>')
#         form_no=input('Enter your Form Number>>')
#         pwd=input('Enter your password')
#         users.extend((login_name, form_no, pwd))

#     if login_name and form_no and pwd in users:
#         print('login successful')
#     else:
#         print('invalid credentials')
    
# elif pat_opt == '2':
#     for reg_name in range(1):
#         name=input('enter your full name>>')
#         pword=input('create a unique password')
#         confirm_pword=input('rewrite your password')
#         print('Hello'+ name,'you have registered successfully' )

# elif pat_opt == '3':
#     print('Thank you for using this application, Goodbye!')
    



# Patient_register =[]

# class patient:
#     def __init__(self, fname, lname, pay=0, date=None):
#             self.fname =fname
#             self.lname =lname
#             self.pay = pay
#             self.date = date

#     def make_payment(self):
#         payment_amount = input('Enter amount been paid')
#         if payment_amount.isdigit():
#             self.pay += int(payment_amount)
#             return(f"${payment_amount} payment successful. Your total payment is now ${self.pay}.")
#         else:
#             return "Invalid payment amount. Please enter a valid number ."
        
        
#     def landing_page():
#                 while True:
#                     print("""
#                                             WELCOME TO F.M.C TEACHING HOSPITAL

#                                                                 select
#                                                                 1. Login
#                                                                 2. Register
#                                                                 3. Exit
#                 """)
#                     user_opt = input('Enter option>>> ')
#                     if user_opt == '1':
#                         patient.login_page()
#                     elif user_opt == '2':
#                         patient.register_page()
#                     elif user_opt == '3':
#                         print('Good Bye')
#                         break
#                     else:
#                         print("Invalid option. Please select 1, 2, or 3.")
            


#     def login_page():
#         username = input('Enter username>>> ')
#         pwd = input('Enter password>>> ')
#         for patient in Patient_register:
#             if patient['username'] == username and patient['passwd'] == pwd:
#                 print(f"Login successful!! Welcome, {patient['fullname']}\nKindly proceed to make your payment.")
                
#                 p = patient(patient['fullname'], "", 0)
#                 print(p.make_payment())
#                 return
#         print('Invalid credentials or not registered. Please register first.')


    
#     def register_page():

#             fullname = input("Enter fullname>>> ")
#             username = input("Enter username>>> ")
#             pwd = input("Enter password>>> ")
#             gen = input('Male or Female>>> ')
#             Patient_register.append({'fullname': fullname, 'username': username, 'passwd': pwd, 'Gender': gen})
#             print('Registration completed\nSelect 1. Login\n        2. Exit')


# patient.landing_page()


# import pymysql as pyms
 
# mycon = pyms.connect(host="127.0.0.1", user="root", passwd="yusluv@0408", db="hospital_payment_db")
# mycursor = mycon.cursor()

# # print("connected sucessfully")


# mycursor.execute("""
# CREATE TABLE IF NOT EXISTS patients (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     fullname VARCHAR(100) NOT NULL,
#     username VARCHAR(50) NOT NULL UNIQUE,
#     password VARCHAR(100) NOT NULL,
#     gender ENUM('Male', 'Female') NOT NULL,
#     reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# )
# """)

# # Step 3: Create `staff` table
# mycursor.execute("""
# CREATE TABLE IF NOT EXISTS staff (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     fullname VARCHAR(100) NOT NULL,
#     username VARCHAR(50) NOT NULL UNIQUE,
#     password VARCHAR(100) NOT NULL,
#     role ENUM('Doctor', 'Nurse', 'Admin') NOT NULL,
#     department VARCHAR(100),
#     reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# )
# """)

# # Step 4: Create `appointments` table
# mycursor.execute("""
# CREATE TABLE IF NOT EXISTS appointments (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     patient_id INT NOT NULL,
#     staff_id INT,
#     appointment_date DATETIME NOT NULL,
#     purpose TEXT,
#     status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (patient_id) REFERENCES patients(id),
#     FOREIGN KEY (staff_id) REFERENCES staff(id)
# )
# """)

# # Step 5: Create `payments` table
# mycursor.execute("""
# CREATE TABLE IF NOT EXISTS payments (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     patient_id INT NOT NULL,
#     amount DECIMAL(10, 2) NOT NULL,
#     payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     payment_method VARCHAR(50),
#     FOREIGN KEY (patient_id) REFERENCES patients(id)
# )
# """)

# # Step 6: Create `medical_records` table
# mycursor.execute("""
# CREATE TABLE IF NOT EXISTS medical_records (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     patient_id INT NOT NULL,
#     staff_id INT,
#     diagnosis TEXT,
#     treatment TEXT,
#     prescription TEXT,
#     record_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (patient_id) REFERENCES patients(id),
#     FOREIGN KEY (staff_id) REFERENCES staff(id)
# )
# """)

# # Finalize
# # print("✅ All tables created successfully in `hospital_db`.")
# mycon.close()


# Patient_register = []

# class patient:
#     def __init__(self, fname, lname, pay=0, date=None):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
#         self.date = date

#     def make_payment(self):
#         payment_amount = input('Enter amount being paid: ')
#         if payment_amount.isdigit():
#             self.pay += int(payment_amount)
#             return f"${payment_amount} payment successful. Your total payment is now ${self.pay}."
#         else:
#             return "Invalid payment amount. Please enter a valid number."


#     def landing_page():
#         while True:
#             print("""
#                                             WELCOME TO F.M.C TEACHING HOSPITAL

#                                                                 select
#                                                                 1. Register
#                                                                 2. Login
#                                                                 3. Exit
#             """)
#             user_opt = input('Enter option>>> ')
#             if user_opt == '1':
#                 patient.register_page()
#             elif user_opt == '2':
#                 patient.login_page()
#             elif user_opt == '3':
#                 print('Good Bye')
#                 break
#             else:
#                 print("Invalid option. Please select 1, 2, or 3.")
#     def register_page():
#         fullname = input("Enter fullname>>> ")
#         username = input("Enter username>>> ")
#         pwd = input("Enter password>>> ")
#         gen = input('Male or Female>>> ')
        
#         Patient_register.append({'fullname': fullname, 'username': username, 'passwd': pwd, 'Gender': gen})
#         print('Registration completed\nSelect 1. Login\n        2. Exit')

       
#         for pat in Patient_register:
#             if pat['username'] == username and pat['passwd'] == pwd:
#                 print(f"Login successful!! Welcome, {pat['fullname']}\nKindly proceed to make your payment.")
                
#                 name_parts = pat['fullname'].split(" ", 1)
#                 fname = name_parts[0]
#                 lname = name_parts[1] if len(name_parts) > 1 else ""

#                 p = patient(fname, lname, 0)  
#                 print(p.make_payment())
#                 return
        
#         print('Invalid credentials or not registered. Please register first.')
    
#     def login_page():
#         username = input('Enter username>>> ')
#         pwd = input('Enter password>>> ')


# # Run the program
# patient.landing_page()



# # import mysql.connector
# # cnx = mysql.connector.connect(
# # user='Yusluv',
# # password='yusluv@0408'
# # host='127.0.0.1'
# # port=3306,
# # database='my database'
# # )





import pymysql

# Function to connect to MySQL (without selecting a database yet)
def connect_to_mysql():
    return pymysql.connect(host="127.0.0.1", user="root", password="yusluv@0408")


# Function to create database if it doesn't exist
def create_database():
    con = connect_to_mysql()
    cur = con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS hospital_payment_db")
    con.commit()
    con.close()


# Function to connect to the actual hospital database
def connect_to_hospital_db():
    return pymysql.connect(host="127.0.0.1", user="root", password="yusluv@0408", db="hospital_payment_db")


# Function to create tables
def create_tables():
    con = connect_to_hospital_db()
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        fullname VARCHAR(100) NOT NULL,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(100) NOT NULL,
        gender ENUM('Male', 'Female') NOT NULL,
        reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS staff (
        id INT AUTO_INCREMENT PRIMARY KEY,
        fullname VARCHAR(100) NOT NULL,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(100) NOT NULL,
        role ENUM('Doctor', 'Nurse', 'Admin') NOT NULL,
        department VARCHAR(100),
        reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INT AUTO_INCREMENT PRIMARY KEY,
        patient_id INT NOT NULL,
        staff_id INT,
        appointment_date DATETIME NOT NULL,
        purpose TEXT,
        status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (patient_id) REFERENCES patients(id),
        FOREIGN KEY (staff_id) REFERENCES staff(id)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS payments (
        id INT AUTO_INCREMENT PRIMARY KEY,
        patient_id INT NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        payment_method VARCHAR(50),
        payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (patient_id) REFERENCES patients(id)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS medical_records (
        id INT AUTO_INCREMENT PRIMARY KEY,
        patient_id INT NOT NULL,
        staff_id INT,
        diagnosis TEXT,
        treatment TEXT,
        prescription TEXT,
        record_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (patient_id) REFERENCES patients(id),
        FOREIGN KEY (staff_id) REFERENCES staff(id)
    )
    """)

    con.commit()
    con.close()


class Patient:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def make_payment(self, patient_id):
        try:
            amount = input("Enter amount being paid: ")
            if not amount.isdigit():
                print(" Invalid amount.")
                return
            amount = float(amount)
            method = input("Enter payment method (Cash/Card/Transfer): ")

            con = connect_to_hospital_db()
            cur = con.cursor()
            cur.execute("INSERT INTO payments (patient_id, amount, payment_method) VALUES (%s, %s, %s)",
                        (patient_id, amount, method))
            con.commit()
            con.close()

            print(f" Payment of ${amount} recorded successfully.")
        except Exception as e:
            print(" Payment error:", e)


    def landing_page():
        while True:
            print("""
                ===== WELCOME TO F.M.C TEACHING HOSPITAL =====

                Please select an option:
                1. Register as Patient
                2. Login as Patient
                3. Exit
            """)
            option = input("Enter your choice (1/2/3): ")

            if option == '1':
                Patient.register()
            elif option == '2':
                Patient.login()
            elif option == '3':
                print(" Thank you. Goodbye!")
                break
            else:
                print(" Invalid selection. Try again.")

    
    def register():
        try:
            fullname = input("Full name: ")
            username = input("Username: ")
            password = int(input("Password: "))
            gender = input("Gender (Male/Female): ")

            con = connect_to_hospital_db()
            cur = con.cursor()
            cur.execute("INSERT INTO patients (fullname, username, password, gender) VALUES (%s, %s, %s, %s)",
                        (fullname, username, password, gender))
            con.commit()
            con.close()

            print(" Registration successful! You can now log in.")
        except Exception as e:
            print(" Registration failed:", e)


    def login():
        try:
            username = input("Username: ")
            password = input("Password: ")

            con = connect_to_hospital_db()
            cur = con.cursor()
            cur.execute("SELECT id, fullname FROM patients WHERE username = %s AND password = %s",
                        (username, password))
            result = cur.fetchone()
            con.close()

            if result:
                patient_id, fullname = result
                fname, *rest = fullname.split(" ")
                lname = rest[0] if rest else ""
                print(f" Welcome back, {fullname}!")
                pat = Patient(fname, lname)
                pat.make_payment(patient_id)
            else:
                print(" Invalid login. Please try again or register if you haven't.")
        except Exception as e:
            print(" Login error:", e)


create_database()
create_tables()
Patient.landing_page()




