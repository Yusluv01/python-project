# import time

# class member:
#     def __init__(self, number_id, name, email, phone_number, share_amount):
#         self.number_id = number_id
#         self.name = name
#         self.email = email
#         self.phone_number = phone_number
#         self.share_amount = share_amount

#     def display_number_info(self):
#             print(f"Member ID: (self.number_id)")
#             print(f"Name: (self.name)")
#             print(f"email: (self.email)")
#             print(f"phone_number: (self.phone_number)")
#             print(f"share_amount: (self.share_amount)")


#     class cooperative:
#                 def __init__(self, cooperative_name):
#                     self.cooperative_name = cooperative_name
#                     self.members = []

#                 def add_number (self, Number):
#                         self.numbers.append(Number)

#                 def remove_number(self, member_id):
#                         self.members_id = member_id




import time

class Member:
    def __init__(self, number_id, name, email, phone_number, share_amount):
        self.number_id = number_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.share_amount = share_amount

    def display_member_info(self):
        print(f"Member ID: {self.number_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Share Amount: {self.share_amount}")

class Cooperative:
    def __init__(self, cooperative_name):
        self.cooperative_name = cooperative_name
        self.members = []

    def add_member(self, member):
        self.members.append(member)
        print(f"{member.name} has been added to {self.cooperative_name}.")

    def remove_member(self, member_id):
        for member in self.members:
            if member.number_id == member_id:
                self.members.remove(member)
                print(f"Member {member.name} (ID: {member_id}) has been removed.")
                return
        print("Member ID not found.")

    def display_all_members(self):
        if not self.members:
            print("No members in the cooperative.")
        else:
            print(f"\nMembers of {self.cooperative_name}:")
            for member in self.members:
                member.display_member_info()
                print("-" * 20)

# Example Usage
cooperative = Cooperative("Savings Cooperative")

# Adding members
member1 = Member(101, "John Doe", "john@example.com", "123-456-7890", 500)
member2 = Member(102, "Joy Smith", "joyexample.com", "987-654-3210", 700)

cooperative.add_member(member1)
cooperative.add_member(member2)

# Display all members
cooperative.display_all_members()

# Removing a member
cooperative.remove_member(101)

# Display members after removal
cooperative.display_all_members()



# import re

# class Member:
#     def __init__(self, number_id, name, email, phone_number, share_amount):
#         if not self.validate_email(email):
#             raise ValueError("Invalid email format.")
#         if not self.validate_phone(phone_number):
#             raise ValueError("Invalid phone number format.")
#         if share_amount <= 0:
#             raise ValueError("Share amount must be greater than zero.")
        
#         self.number_id = number_id
#         self.name = name
#         self.email = email
#         self.phone_number = phone_number
#         self.share_amount = share_amount

#     def display_member_info(self):
#         print(f"Member ID: {self.number_id}")
#         print(f"Name: {self.name}")
#         print(f"Email: {self.email}")
#         print(f"Phone Number: {self.phone_number}")
#         print(f"Share Amount: {self.share_amount}")

#     @staticmethod
#     def validate_email(email):
#         return re.match(r"[^@]+@[^@]+\.[^@]+", email)

#     @staticmethod
#     def validate_phone(phone_number):
#         return re.match(r"^\d{3}-\d{3}-\d{4}$", phone_number)


# class Cooperative:
#     def __init__(self, cooperative_name):
#         self.cooperative_name = cooperative_name
#         self.members = {}

#     def add_member(self, member):
#         if member.number_id in self.members:
#             print(f"Member ID {member.number_id} already exists. Cannot add duplicate.")
#             return
#         self.members[member.number_id] = member
#         print(f"{member.name} has been added to {self.cooperative_name}.")

#     def remove_member(self, member_id):
#         if member_id in self.members:
#             removed_member = self.members.pop(member_id)
#             print(f"Member {removed_member.name} (ID: {member_id}) has been removed.")
#         else:
#             print("Member ID not found.")

#     def display_all_members(self):
#         if not self.members:
#             print("No members in the cooperative.")
#         else:
#             print(f"\nMembers of {self.cooperative_name}:")
#             for member in self.members.values():
#                 member.display_member_info()
#                 print("-" * 20)

#     def find_member(self, member_id):
#         return self.members.get(member_id, "Member not found.")




