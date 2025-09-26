def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# 测试几个例子
print("=== 姓名格式化测试 ===")

# 测试1
first_name = "jimi"
last_name = "hendrix"
musician = get_formatted_name(first_name, last_name)
print(f"输入: '{first_name}', '{last_name}' -> 输出: '{musician}'")

# 测试2
first_name = "taylor"
last_name = "swift"
musician = get_formatted_name(first_name, last_name)
print(f"输入: '{first_name}', '{last_name}' -> 输出: '{musician}'")

# 测试3
first_name = "john"
last_name = "doe"
musician = get_formatted_name(first_name, last_name)
print(f"输入: '{first_name}', '{last_name}' -> 输出: '{musician}'")

print("\n程序运行正常！")