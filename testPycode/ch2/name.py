name = "ada lovelace"
#将字符串类型的name变量以首字母大写方式打印
print(name.title())

name = "Ada Lovelace"
#将字符串改为全部大写
print(name.upper())
#将字符串改为全部小写
print(name.lower())
#将字符串首字母大写
print(name.title())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)
print(full_name)
print("Hello, " + full_name.title() + "!")

print("Python")

#添加制表符
print("\tPython")

#换行符\n
print("Language:\nPython\nC\nJavaScript")

#换行符\n+制表符\t
print("Language:\n\tPython\n\tC\n\tJavaScript")

#删除空白
favorite_language = "python "
print(favorite_language)
#去掉字符串开头和末尾的多余空白
print(favorite_language.rstrip())

favorite_language = ' python '
#rstrip()——删除末尾的空白符
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = ' python '
#lstrip()——删除开头的空白符
favorite_language = favorite_language.lstrip()
print(favorite_language)

favorite_language = ' python '
#strip()——删除前后两端的空白符
favorite_language = favorite_language.lstrip()
print(favorite_language)
