name = "Doris"
print("Hello " + name +  ", would you like to learn some Python today?")

name = "doris"
#首字母大写
print(name.title())
#字符串小写
print(name.lower())
#字符串大写
print(name.upper())

name = "Albert Einstein"
speek = '"A person who nerver made a mistake nerver tried anything new."'
print(name + " once said, " + speek)

famous_person = "Albert Einstein"
message = famous_person + " is my favorite person"
print(message)

famous_person = " Albert \n\tEinstein "
#使用换行符+制表符
print(famous_person)
famous_person = " Doris "
#剔除末尾空格
print(famous_person.rstrip())
#剔除首部空格
print(famous_person.lstrip())
#剔除前后空格
print(famous_person.strip())


