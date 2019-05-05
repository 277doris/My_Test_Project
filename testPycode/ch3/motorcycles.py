# #1、修改列表的第一个元素，通过索引值改变
# motorcycles = ['handa', 'yamaha', 'suzuki']
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)
#
# #2、在列表添加元素，通过append函数添加至末尾
# motorcycles = ['handa', 'yamaha', 'suzuki']
# motorcycles.append('ducati')
# print(motorcycles)
# motorcycles = []
# motorcycles.append('handa')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# motorcycles.append('ducati')
# print(motorcycles)
#
# #3、在列表中插入元素，通过insert给索引赋值的方式
# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert(0, 'ducati')
# print(motorcycles)
#
# #4、从列表中删除元素,通过del函数删除变量索引指向的值
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)
# del motorcycles[1]
# print(motorcycles)

# #5、使用pop方式删除元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# popped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycles)
# motorcycles = ['honda', 'yamaha', 'suzuki']
# last_owned = motorcycles.pop()
# print("The last motorcycle I owned was a " + last_owned.title() + ".")

# #6、使用pop加元素的索引删除列表中的元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# first_owned = motorcycles.pop(0)
# print("The first motorcycle I owned was a " + first_owned.title() + ".")
# #使用pop()时，弹出的元素将不在列表中
# print(motorcycles)
#
# #7、根据值删除
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

#8、根据值删除元素——remove函数
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print("\nA " + too_expensive.title() + " is too expensive for me.")


