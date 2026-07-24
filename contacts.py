# 1. Create the contacts dictionary
contacts = {
    "Sibusiso": "0821112222",
    "Thabo": "0734445555",
    "Lerato": "0847778888"
}

# 2. Ask the user for input
search_name = input("Enter the name of the friend you want to look up: ").strip()

# 3 & 4. Conditional check using the 'in' keyword
if search_name in contacts:
    print(f"Found! {search_name}'s number is {contacts[search_name]}")
else:
    print("Contact not found.")