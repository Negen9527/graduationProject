# graduationProject
开发环境
python3 + djiango2 + mysql8  
下载DjangoUeditor3  
```angular2html
git clone https://github.com/Negen9527/DjangoUeditor3.git
```
# 安装DjangoUeditor3
```angular2html
cd DjangoUeditor3
python setup.py install 
```
## 屏蔽boundfield.py  第93行(renderer=self.form.renderer) 
```angular2html
   \Python37\lib\site-packages\django\forms\boundfield.py
```


# 创建数据库
在数据库中创建数据库:graduation_project

项目根目录下执行以下命令创建数据表
```angular2html
python manage.py makemigrations
python manage.py migrate
```

# 创建管理员账号（admin）
```angular2html
python manage.py createsuperuser
```
按照提示输入账号名、密码
完成创建

# 测试  
### 启动项目
```angular2html
python manage.py runserver 0.0.0.0:8000
```
### 浏览器输入   
localhost:8000/admin







