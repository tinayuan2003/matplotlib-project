<<<<<<< HEAD
import re

class PropertyList:

    def __init__(self, property_list):
        self.property_list = property_list

    def add_property(self, mls_number, address, owner_name, number_bedrooms, description):
        if not re.search("^[A-Z][0-9]{5,7}$", mls_number.strip()):
            raise ValueError("The MLS number is invalid")

        if re.search("^[0-9]{2,5}[a-zA-Z0-9 .,-]+[A-Z][0-9][A-Z] [0-9][A-Z][0-9][, ]*[A-Z]{2}$", address) and re.search(
                "(.{2,},){3}", address) and not re.search(",,", address):
            pass
        else:
            raise ValueError("The address is invalid")

        if not re.search("^[A-Za-z]{2,}[a-zA-Z ]*$", owner_name):
            raise TypeError("The owner's name is invalid")

        if not re.search("^[0-9]+$", number_bedrooms.strip()):
            raise TypeError("The number of bedrooms must be digits")

        if not re.search("^.{5,}$", description, re.I):
            raise ValueError("Description is invalid")

        this_dict = dict()
        this_dict["MLS Number"] = mls_number
        this_dict["Address"] = address
        this_dict["owners_name"] = owner_name
        this_dict["bedrooms_number"] = number_bedrooms
        this_dict["desc"] = description

        self.property_list.append(this_dict)


    def list_properties(self):
        """
        View the list of all properties. Each property should be displayed on a single line format
        :param this_list: the list of dictionaries
        :return: None
        """
        for item in self.property_list:
            print(
                f"The property with MLS {item.get('MLS Number')}, the owner is {item.get('owners_name')}, the property at {item.get('Address')} has {item.get('bedrooms_number')} bedrooms. {item.get('desc')}")

    def find_property(self, owner_name):
        """
        Find a property by the owner’s name. This should find all the properties with the owner’s name that match the entered name.
        :param owner_name: the owner's name
        :param this_list: the list of dictionaries
        :return: None
        """
        if not re.search("^[A-Za-z]{2,}[a-zA-Z ]*$", owner_name):
            raise ValueError("invalid name")

        owner_name_found = False
        for item in self.property_list:
            if owner_name.lower() in item['owners_name'].lower():
                owner_name_found = True
                print(
                    f"The property with MLS {item.get('MLS Number')}, the owner is {item.get('owners_name')}, the property at {item.get('Address')} has {item.get('bedrooms_number')} bedrooms. {item.get('desc')}")

        if not owner_name_found:
            print("No properties found")

    def remove_property(self, mls_number):
        """
        Complete the property sale. Enter the MLS Number of the property. This should remove the property with the given MLS number from the list
        :param mls_number: the property's MLS number
        :param this_list: the list of dictionaries
        :return: this list of dictionaries
        """
        if not re.search("^[A-Z][0-9]{5,7}$", mls_number):
            raise ValueError("invalid MLS number")
        else:
            found = False
            for index in range(len(self.property_list) - 1, -1, -1):
                if mls_number == self.property_list[index]["MLS Number"]:
                    found = True
                    self.property_list.pop(index)
                    print(f"Property with the MLS Number {mls_number} is sold")
            if not found:
                print("No property was found")

    def quit_app(self):
        """
        If the user chooses to quit, then the properties data should be stored in a txt file called properties.txt as required format
        :param this_list: the list of dictionaries
        :return: None
        """
        with open("properties.txt", "w") as file:
            for item in self.property_list:
                file.write("{\n")
                file.write(f'"MLS_Number": {item["MLS Number"]},\n')
                file.write(f'"Address": "{item["Address"]}",\n')
                file.write(f'"owners_name": "{item["owners_name"].title()}",\n')
                file.write(f'"bedrooms_number": "{item["bedrooms_number"]}",\n')
                file.write(f'"desc": "{item["desc"]}"\n')
                file.write("}\n")
        print("The properties data has been stored in properties.txt")


def main():
    property_list = []

    quit_program = False
    try:
        property_all = PropertyList(property_list)
        while not quit_program:
            add_answer = input("Would you like to add a property? (y/n) ")
            if add_answer.lower() == "y":
                mls_number = input("Enter the MLS Number: ")
                address = input("Enter the Address: ")
                owner_name = input("Enter the owner's name: ")
                number_bedrooms = input("Enter the number of bedrooms: ")
                description = input("Enter the description: ")
                property_all.add_property(mls_number, address, owner_name, number_bedrooms, description)

            list_answer = input("Would you like to view the list of properties? (y/n) ")
            if list_answer.lower() == "y":
                property_all.list_properties()

            find_answer = input("Would you like to find a property? (y/n) ")
            if find_answer.lower() == "y":
                owner_name = input("Enter the owner's name: ")
                property_all.find_property(owner_name)

            remove_answer = input("Would you like to remove a property? (y/n) ")
            if remove_answer.lower() == "y":
                mls_number = input("Enter the MLS Number: ")
                property_all.remove_property(mls_number)

            quit_answer = input("Would you like to quit? (y/n) ")
            if quit_answer.lower() == "y":
                quit_program = True
                property_all.quit_app()

    except (ValueError, TypeError) as e:
        print(e)

    except:
        print("Something went wrong")

    finally:
        print("The program is finished")


if __name__ == '__main__':
    main()
=======
import re

class PropertyList:

    def __init__(self, property_list):
        self.property_list = property_list

    def add_property(self, mls_number, address, owner_name, number_bedrooms, description):
        if not re.search("^[A-Z][0-9]{5,7}$", mls_number.strip()):
            raise ValueError("The MLS number is invalid")

        if re.search("^[0-9]{2,5}[a-zA-Z0-9 .,-]+[A-Z][0-9][A-Z] [0-9][A-Z][0-9][, ]*[A-Z]{2}$", address) and re.search(
                "(.{2,},){3}", address) and not re.search(",,", address):
            pass
        else:
            raise ValueError("The address is invalid")

        if not re.search("^[A-Za-z]{2,}[a-zA-Z ]*$", owner_name):
            raise TypeError("The owner's name is invalid")

        if not re.search("^[0-9]+$", number_bedrooms.strip()):
            raise TypeError("The number of bedrooms must be digits")

        if not re.search("^.{5,}$", description, re.I):
            raise ValueError("Description is invalid")

        this_dict = dict()
        this_dict["MLS Number"] = mls_number
        this_dict["Address"] = address
        this_dict["owners_name"] = owner_name
        this_dict["bedrooms_number"] = number_bedrooms
        this_dict["desc"] = description

        self.property_list.append(this_dict)


    def list_properties(self):
        """
        View the list of all properties. Each property should be displayed on a single line format
        :param this_list: the list of dictionaries
        :return: None
        """
        for item in self.property_list:
            print(
                f"The property with MLS {item.get('MLS Number')}, the owner is {item.get('owners_name')}, the property at {item.get('Address')} has {item.get('bedrooms_number')} bedrooms. {item.get('desc')}")

    def find_property(self, owner_name):
        """
        Find a property by the owner’s name. This should find all the properties with the owner’s name that match the entered name.
        :param owner_name: the owner's name
        :param this_list: the list of dictionaries
        :return: None
        """
        if not re.search("^[A-Za-z]{2,}[a-zA-Z ]*$", owner_name):
            raise ValueError("invalid name")

        owner_name_found = False
        for item in self.property_list:
            if owner_name.lower() in item['owners_name'].lower():
                owner_name_found = True
                print(
                    f"The property with MLS {item.get('MLS Number')}, the owner is {item.get('owners_name')}, the property at {item.get('Address')} has {item.get('bedrooms_number')} bedrooms. {item.get('desc')}")

        if not owner_name_found:
            print("No properties found")

    def remove_property(self, mls_number):
        """
        Complete the property sale. Enter the MLS Number of the property. This should remove the property with the given MLS number from the list
        :param mls_number: the property's MLS number
        :param this_list: the list of dictionaries
        :return: this list of dictionaries
        """
        if not re.search("^[A-Z][0-9]{5,7}$", mls_number):
            raise ValueError("invalid MLS number")
        else:
            found = False
            for index in range(len(self.property_list) - 1, -1, -1):
                if mls_number == self.property_list[index]["MLS Number"]:
                    found = True
                    self.property_list.pop(index)
                    print(f"Property with the MLS Number {mls_number} is sold")
            if not found:
                print("No property was found")

    def quit_app(self):
        """
        If the user chooses to quit, then the properties data should be stored in a txt file called properties.txt as required format
        :param this_list: the list of dictionaries
        :return: None
        """
        with open("properties.txt", "w") as file:
            for item in self.property_list:
                file.write("{\n")
                file.write(f'"MLS_Number": {item["MLS Number"]},\n')
                file.write(f'"Address": "{item["Address"]}",\n')
                file.write(f'"owners_name": "{item["owners_name"].title()}",\n')
                file.write(f'"bedrooms_number": "{item["bedrooms_number"]}",\n')
                file.write(f'"desc": "{item["desc"]}"\n')
                file.write("}\n")
        print("The properties data has been stored in properties.txt")


def main():
    property_list = []

    quit_program = False
    try:
        property_all = PropertyList(property_list)
        while not quit_program:
            add_answer = input("Would you like to add a property? (y/n) ")
            if add_answer.lower() == "y":
                mls_number = input("Enter the MLS Number: ")
                address = input("Enter the Address: ")
                owner_name = input("Enter the owner's name: ")
                number_bedrooms = input("Enter the number of bedrooms: ")
                description = input("Enter the description: ")
                property_all.add_property(mls_number, address, owner_name, number_bedrooms, description)

            list_answer = input("Would you like to view the list of properties? (y/n) ")
            if list_answer.lower() == "y":
                property_all.list_properties()

            find_answer = input("Would you like to find a property? (y/n) ")
            if find_answer.lower() == "y":
                owner_name = input("Enter the owner's name: ")
                property_all.find_property(owner_name)

            remove_answer = input("Would you like to remove a property? (y/n) ")
            if remove_answer.lower() == "y":
                mls_number = input("Enter the MLS Number: ")
                property_all.remove_property(mls_number)

            quit_answer = input("Would you like to quit? (y/n) ")
            if quit_answer.lower() == "y":
                quit_program = True
                property_all.quit_app()

    except (ValueError, TypeError) as e:
        print(e)

    except:
        print("Something went wrong")

    finally:
        print("The program is finished")


if __name__ == '__main__':
    main()
>>>>>>> 191c5806b58c9a04d17324628bdb347456d37eca
