# json数据   json格式的字符串


# str01 = """{"name":'zhangsan',"age":'14',"gender":'1'}"""
import json

dict01 = {'name': 'zhangsan', 'age': '14', 'gender': '1'}

print(type(dict01))

# 字典转json字符串
str01 = json.dumps(dict01)
print(type(str01))
print(str01)

# json字符串转字典
dict02 = json.loads(str01)
print(type(dict02))
print(dict02)
