def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

first_name = input("请输入名字: ")
last_name = input("请输入姓氏: ")
musician = get_formatted_name(first_name, last_name)
print(musician)