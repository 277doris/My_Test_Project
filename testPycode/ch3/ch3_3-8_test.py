citys = ['shanghai', 'beijing', 'hongkong', 'changsha', 'newyork']
print("This is original list:")
print(citys)
#使用sort()进行排序
print("\nThis is sorted list:")
print(sorted(citys))
#打印原来排序，证实sroted只是临时排序
print("\nThis is original list:")
print(citys)
#使用srot按字母相反顺序排列打印，同时不要修改列表
print("\nThis is sorted list order by desc:")
citys.reverse()
print(sorted(citys))
