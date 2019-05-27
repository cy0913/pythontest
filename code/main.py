import json

import pymysql
from flask import Flask, jsonify, redirect, url_for, render_template

# static_url_path  静态文件访问的时的url匹配时，路由规则里的路径名字 默认值是/static
from sqlalchemy.orm import sessionmaker

app = Flask(__name__, static_url_path='/static')

print(app.url_map)  # <Rule '/abc/<filename>' (GET, HEAD, OPTIONS) -> static>]


@app.route('/')
def index():
    return 'hello  flask'


@app.route('/profile.html')
def profile():
    """处理登录的逻辑"""

    # profile.html并且返回user_id
    with open('profile.html') as f:
        content = f.read()

    return content


@app.route('/profile_v2/<user_id>')
def profile2(user_id):
    print(user_id)
    """处理登录的逻辑"""

    # profile.html并且返回
    with open('profile.html') as f:
        content = f.read()
        # 替换xxx_name 为传入的名字
        # 会显示对应的名字和头像，不要忘记前段文件里修改标记
        content = content.replace('xxx_name', user_id)

    return content


# 使用模板
@app.route('/profile_v3/<user_id>')
def profile3(user_id):
    return render_template('profile.html')


# 给模板传数据
@app.route('/profile_v4/<user_id>')
def profile4(user_id):
    return render_template('profile.html', xxx_name=user_id)


# 从数据库查询数据
@app.route('/profile_v5/<user_id>')
def profile5(user_id):
    # 1连接数据库
    connect = pymysql.connect(host='localhost', port=3306, user='root', password='mysql', database='flask_test1',
                              charset='utf8')

    # 2 获取cursor
    cursor = connect.cursor()
    # 3执行sql语句 防注入 params是列表 里面是填充sql占位符的数据
    params = [user_id]
    cursor.execute('select * from  user where user_id = %s', params)
    result = cursor.fetchone()
    print(result)
    # (1, 'halon', 'halon', 'halon.jpg', 'halon，山东人，属蛇，喜欢吃北京烤鸭，可是太胖，不能多吃,哈哈')

    # 4关闭cursor
    cursor.close()
    # 5关闭连接
    connect.close()

    return render_template('profile.html', xxx_name=user_id)


# 从数据库查询数据 并且传给模板
@app.route('/profile_v6/<user_id>')
def profile6(user_id):
    # 1连接数据库
    connect = pymysql.connect(host='localhost', port=3306, user='root', password='mysql', database='flask_test1',
                              charset='utf8')

    # 2 获取cursor
    cursor = connect.cursor()
    # 3执行sql语句 防注入 params是列表 里面是填充sql占位符的数据
    params = [user_id]
    cursor.execute('select * from  user where user_id = %s', params)
    result = cursor.fetchone()
    print(result)
    # (1, 'halon', 'halon', 'halon.jpg', 'halon，山东人，属蛇，喜欢吃北京烤鸭，可是太胖，不能多吃,哈哈')

    # 4关闭cursor
    cursor.close()
    # 5关闭连接
    connect.close()

    return render_template('profile.html', user_name=result[2], short_description=result[4], head_img=result[3])


# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# # 获取引擎  连接数据库
# engine = create_engine('mysql+pymysql://root:mysql@localhost:3306/flask_test1')
# # 获取Base 模型类基类
# Base = declarative_base()
#
#
# # 模型类 model
# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
#     user_id = Column(String(50), nullable=False)
#     user_name = Column(String(50), nullable=False)
#     head_img = Column(String(200), nullable=True)
#     short_description = Column(String(300), nullable=True)

# 用导入模块的形式  使用模型类
from models.models import engine, User


# 从数据库查询数据 并且传给模板
@app.route('/profile_v7/<user_id>')
def profile7(user_id):
    # 获取数据库会话类
    DBSession = sessionmaker(bind=engine)
    # 创建会话对象
    session = DBSession()
    # 根据userid查询到user对象
    user = session.query(User).filter(User.user_id == user_id).one()
    # 会话关闭
    session.close()
    print(user.user_name)

    return render_template('profile.html', user_name=user.user_name, short_description=user.short_description
                           , head_img=user.head_img)


# 返回JSON
@app.route('/testjson')
def testjson():
    json_dict = {
        "user_id": 1,
        "user_name": "halon"
    }
    # 不要用json.dumps  不符合 html协议 响应头信息不对
    # return json.dumps(json_dict)
    # jsonify 在转换json过程 会添加响应头信息  content-type  application/json
    return jsonify(json_dict)


# 重定向
@app.route('/demo1')
def demo1():
    return redirect('http://www.itheima.com')


# 重定向 跳转到个人主页  profile.html
@app.route('/demo2')
def demo2():
    return redirect('profile.html')


# 重定向 跳转到个人主页 通过视图函数的名字 profile跳转
# url_for('profile')  根据视图函数的名字 找到对应的url路径
@app.route('/demo3')
def demo3():
    return redirect(url_for('profile'))


# 重定向 传入参数
@app.route('/demo4')
def demo4():
    print(url_for('profile2', user_id='halon'))  #
    return redirect(url_for('profile2', user_id='halon'))


@app.route('/demo5')
def demo5():
    # 自定义一个状态码  后台和前段 要协商好 做什么
    return '状态码为 666', 666


if __name__ == '__main__':
    # 运行服务器
    app.run()
num1 =1
