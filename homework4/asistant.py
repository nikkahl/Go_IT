def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name]=phone  
    return "Contact added."

def change_contact(args, contacts):
    name,phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error: Contact not found."

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    
    return "Error: Contact not found."

def show_all(contacts):
    res = ""
    for name, phone in contacts.items():
        res += f"{name}: {phone}\n"
    return res.strip()


def main():
    contacts={}
    print("hello bro")
    
    print(" commands:")
    print(" - hello")
    print(" - add [name] [phone]")
    print(" - change [name] [phone]")
    print(" - phone [name]")
    print(" - all")
    print(" - help")
    print(" - exit або close")
    print("-" * 20)
    
    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            continue
            
        command,*args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "help":
            print("Commands: hello, add [name] [phone], change [name] [phone], phone [name], all, exit")
        elif command=="add":
            print(add_contact(args, contacts))
        elif command == "change":
             print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()