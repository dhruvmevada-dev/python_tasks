contacts = {}


def add_contact(name, phone, email=""):
    contacts[name.lower()] = {"name": name, "phone": phone, "email": email}
    print(f"Contact '{name}' added.")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for c in contacts.values():
        print(f"{c['name']} | {c['phone']} | {c['email']}")


def search_contact(name):
    c = contacts.get(name.lower())
    if c:
        print(f"{c['name']} | {c['phone']} | {c['email']}")
    else:
        print("Contact not found.")


def update_contact(name, phone=None, email=None):
    c = contacts.get(name.lower())
    if not c:
        print("Contact not found.")
        return
    if phone:
        c["phone"] = phone
    if email:
        c["email"] = email
    print("Contact updated.")


def delete_contact(name):
    if contacts.pop(name.lower(), None):
        print("Contact deleted.")
    else:
        print("Contact not found.")


def main():
    menu = """
1. Add contact
2. View all contacts
3. Search contact
4. Update contact
5. Delete contact
6. Exit"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_contact(input("Name: "), input("Phone: "), input("Email: "))
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact(input("Name: "))
        elif choice == "4":
            update_contact(
                input("Name: "),
                input("New phone (blank to skip): ") or None,
                input("New email (blank to skip): ") or None,
            )
        elif choice == "5":
            delete_contact(input("Name: "))
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
