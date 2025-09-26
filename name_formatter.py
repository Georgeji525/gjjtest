def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
musician = get_formatted_name(first_name, last_name)
print(musician)