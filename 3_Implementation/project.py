import csv
import sys
from IPython.display import clear_output


global DATA, MAIN_DATA
FILE_NAME = "contact.csv"
file_login = open(FILE_NAME, mode='r',encoding="utf8")
main_data = file_login.read()
main_data = main_data.split('\n')
main_data = (list(filter(None, main_data)))
#print(main_data)

class Admin():
    def __init__(self, user_id=0, name='', email='', gender='', mobile_no=0, age=0, address=''):

        self.user_id = user_id
        self.name = name
        self.email = email
        self.gender = gender
        self.moile_no = mobile_no
        self.age = age
        self.address = address

    def admin_login():
        """Admin login"""
        print("Welcome Admin\nPlease Enter your details")
        user_id = input("Enter User Number: ")
        password_id = input("Enter Password: ")
        clear_output()
        with open('login.csv', mode='r', encoding="utf8") as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                if row == [user_id, password_id]:
                    print('Successfully logged in!')
                    return True
            print('Wrong User ID or Password')
            return False

    def write_file(self, list_data):
        """"""
        file_contact = open(FILE_NAME, mode="w",encoding="utf8")

        all_data = str()

        for data in list_data:

            all_data += data+'\n'

        file_contact.write(all_data)

        file_contact.close()

        return True

    def add_contact(self):

        user_id = input("Creat User ID :")

        name = input("Enter Name :")

        email = input("Enter Email :")

        gender = input("Enter Gender :")

        moile_no = input("Enter Mobile_no :")

        age = input("Enter Age :")

        address = input("Enter Address :")

        data = user_id+','+name+','+email+','+gender + \
            ','+moile_no+','+age+','+address+'\n'

        file_xlsx = open(FILE_NAME,mode="a",encoding="utf8")

        file_xlsx.write(data)

        file_xlsx.close()

        print("Contact Added Succeffully")

    def edit_contact(self, No):

        print("User ID :", No)

        name = input("Enter Name :")

        email = input("Enter Email :")

        gender = input("Enter Gender :")

        moile_no = input("Enter Mobile_no :")

        age = input("Enter Age :")

        address = input("Enter Address :")

        new_value = No+','+name+','+email+','+gender+','+moile_no+','+age+','+address

        for data in main_data:

            split_data = data.split(',')

            if No == split_data[0]:

                main_data[main_data.index(data)] = new_value

                self.write_file(main_data)

                print("Successfully Updated")

                return True

        print("Try Again!!")

    def remove_contact(self, No):

        for data in main_data:

            split_data = data.split(',')

            if No == split_data[0]:

                main_data.remove(data)

                break

        if self.write_file(main_data):

            print("Successfully Deleted !")

        else:

            print("Try Again!! ")

    def search_id(self, No):

        for data in main_data:

            split_data = data.split(',')

            if No == split_data[0]:

                return True

        return False


class User(Admin):
    def __init__(self):
        super().__init__()

    def show_contact(self,search):
        #perti_cular = search.main_data
        for data in main_data:
            split_data = data.split(',')
        # print(split_data)
        print("User ID :", split_data[0])

        print("Name :", split_data[1])

        print("Email :", split_data[2])

        print("Gender :", split_data[3])

        print("Mobile no. :", split_data[4])

        print("Age :", split_data[5])

        print("Address :", split_data[6])


class Main(User):
    def __init__(self):
        super().__init__()

    def admin_select():
        admin_class = Admin()
        print("Choose the operation from the following\n" 
       "1.Add Contact  2. Edit Contact  3. Remove Contact  4. Exit")

        try:

            user_input = int(input("Please Enter option from above (1-4) : "))

        except ValueError:

            print("That is not true.")

        finally:

            print("")

        if user_input == 1:

            admin_class.add_contact()

        elif user_input == 2:

            num = input("Enter User ID for edit :")

            if admin_class.search_id(num):

                admin_class.edit_contact(num)

            else:

                print("Incorrect User ID!!")

        elif user_input == 3:

            num1 = input("Enter User ID for delete :")

            if admin_class.search_id(num1):

                admin_class.remove_contact(num1)

            else:

                print("Incorrect User ID!!")

        elif user_input == 4:

            print("Thank you!")
            sys.exit()
            

        else:
            print("Invalid Input!!")

    def user_select():
        p = User()
        search_id = input("Enter the search id")
        p.show_contact(search_id)


if __name__ == "__main__":

    mode = input("Hey! Who are you\nPress 1 for Admin and 2 for User")

    if mode == "1":
        if Admin.admin_login() is True:
            Main.admin_select()
        else:
            print("Please try again!")
    elif mode == "2":
        Main.user_select()
    else:
        print("Sorry!")
