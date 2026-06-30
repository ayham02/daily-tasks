import mysql.connector as mc
from email_validator import validate_email

try:
    co = mc.connect(host='localhost',port=3306,user='root',password='root',database='intern_db')
    cursor = co.cursor()

    def display_student(data):
        print (f"""
        ID : {data[0]}
        Name : {data[1]}
        Age : {data[2]}
        Emadatal : {data[3]}
        Course : {data[4]}
        Phone Number : {data[5]}
    """)

    def get_all_students(cursor):
        cursor.execute("select * from students")
        a2 = cursor.fetchall()
        if a2:
            for i in a2:
                display_student(i)
        else:
            print('No Students Found')

    def get_students_by_id(cursor):
        user_input = int(input("Enter The ID of the student you want to retrieve: "))
        cursor.execute(f"select * from students where student_id = {user_input}")
        data = cursor.fetchone()
        if data:
            display_student(data)
        else:
            print(f"Student of ID {user_input} not found")

    def create_student(cursor, co):
        input_name = str(input("Enter The Name of the student:"))
        if not input_name:
            print(f"Name cannot be empty")
            return
            
        input_age = int(input("Enter The Age of the student : "))
        if input_age < 18 :
            print(f"Age cannot be empty or less than 18")
            return
        

        input_mail = str(input("Enter The Mail of the student :"))
        if not validate_email(input_mail):
            print("Email should be in correct format")
            return
                    
        input_course = str(input("Enter The Course of the student : "))
        if not input_course:
            print(f'Course cannot be emtpy')
            return
        

        input_phone_number = str(input("Enter The Phone Number of the student : "))
        if not input_phone_number or (not len(input_phone_number) == 10) or not input_phone_number.isdigit():
            print(f'Phone number cannot be empty or should be 10 digits')
            return
        
        query = """
        insert into students (s_name,age,email,course,phone)
        values(%s,%s,%s,%s,%s)
        """
        values = (input_name,input_age,input_mail,input_course,input_phone_number)
        cursor.execute(query,values)
        co.commit()
        print('Student Created Succesfully')

    def update_student(cursor, co):
        user_input = int(input("Enter the ID of student you want to update details : "))
        cursor.execute(f"select * from students where student_id = {user_input}")
        data = cursor.fetchone()
        if data is None:
            print(f"Student of ID {user_input} Not Found")
            return
        print("What do you want to update: 1. Name, 2. Age, 3. Email, 4. Course, 5. Phone Number")
        dict1 = {1:"s_name",2:"age",3:"email",4:"course",5:"phone"}
        print(dict1)
        user_input_2 =  int(input("Type the number of field to update your details"))
        
        if user_input_2 not in dict1:
            print("Invalid Choice")
            return
        
        field = dict1[user_input_2]
        new_value = input("Enter new value: ")

        if field == "age":
            if not new_value.isdigit() or int(new_value) < 18:
                print(f"Age shoul be 18 or above")
                return

        elif field == "phone":
            if not new_value.isdigit() or len(new_value) != 10:
                print(f'Phone number cannot be more or less than 10')
                return
        
        elif field in ["course","s_name"]:
            if not new_value:
                print("Course or Name cannot be empty")
                return
            
        elif field == "email":
            if not validate_email(new_value):
                print("Email should be in correct format")
                return
        
        query = f'''
        update students 
        set {field} = %s 
        where student_id = %s
        '''
        values = (new_value,user_input)
        cursor.execute(query,values)
        co.commit()
        print("Student Updated Successfully")

    def delete_student(cursor,co):
        user_input = int(input("Enter the ID of student you want to delete : "))
        cursor.execute(f"select * from students where student_id = {user_input}")
        data = cursor.fetchone()
        if data is None:
            print(f"Student of ID {user_input} Not Found")
            return
        query = '''
        delete from students 
        where student_id = %s'''

        values = (user_input)

        cursor.execute(query,user_input)
        co.commit()
        print("Student deleted successfully")

    while True:
        print("""
        1. Get All Students
        2. Get Student By ID
        3. Create Student
        4. Update Student
        5. Delete Student
        6. Exit
        """)

        if choice == 1:
            get_all_students(cursor)

        elif choice == 2:
            get_students_by_id(cursor)

        elif choice == 3:
            create_student(cursor, co)

        elif choice == 4:
            update_student(cursor, co)

        elif choice == 5:
            delete_student(cursor, co)

        elif choice == 6:
            print("Goodbye")
            break

        else:
            print("Invalid choice")

            choice = int(input("Enter your choice: "))
    
except ConnectionError:
    print('something')