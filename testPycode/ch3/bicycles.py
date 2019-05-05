bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#建立索引
print(bicycles[0])
#将列表中的第一个元素以首字母大写的方式进行打印
print(bicycles[0].title())
#打印列表的第二和第四个元素
print(bicycles[1])
print(bicycles[3])
#将索引定为-1，打印最后一个元素
print(bicycles[-1])
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)