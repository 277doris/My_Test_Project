# #3-4,创建一个列表，邀请这些人与共进晚餐
# guests = ['tom', 'jojo', 'ben', 'doris', 'jane']
# person1 = guests[0].title()
# person2 = guests[1].title()
# person3 = guests[-2].title()
# print("Can I have a dinner with you? " + person1)
# print("Can I have a dinner with you? " + person2)
# print("Can I have a dinner with you? " + person3)
# print("I want to have a dinner with " + person1 + " and " + person2 + " and " + person3 + "!")

# #3-5-1有位嘉宾无法赴约，指出哪位嘉宾无法赴约并打印一条消息
# guests = ['tom', 'jojo', 'ben', 'doris', 'jane']
# #把不能赴约的嘉宾放变量miss_guest中
# miss_guest = 'tom'
# #用函数remove将不能赴约的嘉宾删除
# guests.remove(miss_guest)
# print(guests)
# print(miss_guest.title() + " can't have a dinner with me!" )

# #3-5-2修改嘉宾名单，将无法赴约的嘉宾姓名替换为新邀请的嘉宾的姓名
# guests = ['tom', 'jojo', 'ben', 'doris', 'jane']
# #使用索引付元素的值进行替换
# guests[0] = 'jack'
# print(guests)
# #3-5-3再打印一条消息，向名单中的每位嘉宾发出邀请
# print("Can I have a dinner with you, " + guests[0].title() + "?")
# print("Can I have a dinner with you, " + guests[1].title() + "?")
# print("Can I have a dinner with you, " + guests[2].title() + "?")
# print("Can I have a dinner with you, " + guests[3].title() + "?")
# print("Can I have a dinner with you, " + guests[4].title() + "?")

# #3-6-1末尾添加一条信息，打印你找到一个更大的餐桌
# guests = ['tom', 'jojo', 'ben', 'doris', 'jane']
# print("I find a bigger desk for dinner.")
# #3-6-2使用insert添加一个新嘉宾至名单开头
# guests.insert(0, 'mick')
# #3-6-3使用insert添加一位新嘉宾至名单中间
# guests.insert(3, 'mary')
# #3-6-4使用append将最后一位新嘉宾添加至名单末尾
# guests.append('herry')
# print(guests)
# print("Can I have a dinner with you, " + guests[0].title() + "?")
# print("Can I have a dinner with you, " + guests[1].title() + "?")
# print("Can I have a dinner with you, " + guests[2].title() + "?")
# print("Can I have a dinner with you, " + guests[3].title() + "?")
# print("Can I have a dinner with you, " + guests[4].title() + "?")
# print("Can I have a dinner with you, " + guests[5].title() + "?")
# print("Can I have a dinner with you, " + guests[6].title() + "?")
# print("Can I have a dinner with you, " + guests[7].title() + "?")

#3-7-1打印你只能邀请两名嘉宾的信息
guests = ['tom', 'jojo', 'ben', 'doris', 'jane']
print("I'm sorry to tell you, that I can only invite two guests to have a dinner with me! ")
#3-7-2使用pop（）函数删除名单中的嘉宾，把那个打印一条抱歉信息告知嘉宾
uninvit = guests.pop(-1)
print("I'm so sorry, I can't have a dinner with you, " + uninvit.title())
uninvit = guests.pop(-1)
print("I'm so sorry, I can't have a dinner with you, " + uninvit.title())
uninvit = guests.pop(-1)
print("I'm so sorry, I can't have a dinner with you, " + uninvit.title())
#3-7-2对余下的两位嘉宾打印一条消息，指出他依然受人邀请
print("Can I have a dinner with you, " + guests[0].title() + "?")
print("Can I have a dinner with you, " + guests[1].title() + "?")
#3-7-3使用del将最后两位嘉宾从名单中删除，核实结束时名单是空的,索引从大到小删除
del guests[1]
del guests[0]
print(guests)



