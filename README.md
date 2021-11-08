# python + mysql +django
练习
#安装配置django
pip  install django
python -m django --version 查看版本信息
django-admin startproject 项目名称
python manage.py runserver   运行项目

#setting 配置
#ALLOWED_HOSTS 配置可以访问的ip地址

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = '/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False
#创建app程序
python manage.py startapp '程序模块名称'
url.py 是路由设置的入口文件
urlpatterns列表变量中添加路由信息
#没有db.sqlite3执行命令
python manage.py migrate
#当修改表的定义时候执行 也就是说是模块下面的 models.py
python manage.py makemigratetions [模块名称]
  
#创建超级用户
#指令
python manage.py createsuperuser
#api路由需要自己手动配置
#请求方式 : Get Post Put Delet
#手动配置他们路由到那个函数下面 
#静态服务
#在根目录下 添加
from django.conf.urls.static import static
urlpattenns = [
] + static('/'document_root = './根目录的前端静态网页')
#取消csrf校验
#在settng中 MIDDLEWARE 配置中注释掉
'django.middleware.csrf.CsrfViewMiddleware',
