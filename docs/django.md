TODO:
1. 为什么有后端，django
2. 基本概念和如何使用（数据库感觉可以不用管）
3. utils.py使用

路径问题实在是很难受，如何更好地迁移？

需要一个本地调试的方案

you need to register the session. how to do it automatically?

前后端的对齐，后端要多做一点检查，所以接口还是以后端为准吧

还得把服务器的端口开开


naive ver:
https://www.gradio.app/guides/running-gradio-on-your-web-server-with-nginx

set debug=False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


python requests No connection adapters were found for
use http://



---

