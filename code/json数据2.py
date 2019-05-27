# json数据   json格式的字符串


# str01 = """{"name":'zhangsan',"age":'14',"gender":'1'}"""
import json

list01 = [
    {'name': 'zhangsan', 'age': '14', 'gender': '1', 'hobby': ['chi', 'he', 'wan']},
    {'name': 'lisi', 'age': '14', 'gender': '1'},
    {'name': 'wangliu', 'age': '14', 'gender': '1'},
    {'name': 'zhangqi', 'age': '14', 'gender': '1'},
    {'name': 'halon', 'age': '14', 'gender': '1'}
]

print(type(list01))

# 字典转json字符串
str01 = json.dumps(list01)
print(type(str01))
print(str01)

# json字符串转字典
list02 = json.loads(str01)
print(type(list02))
print(list02)
