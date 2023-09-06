```bash
docker volume create gradio

docker run -itd -p 8000:8000 --restart=always -v gradio:/home/workspace --name gradio 7hink/project:1.1

docker run -itd -p 8000:8000 --restart=always --name gradio gradio:1.1

docker exec -it gradio /bin/bash

nohup python3 -m pip install -r requirements.txt &

```
https://wenku.csdn.net/answer/sc3qkaw0yo#:~:text=ImportError%3A%20libGL.so.1%3A%20cannot%20open%20shared%20object%20file%3A%20No,%E6%82%A8%E5%8F%AF%E4%BB%A5%E9%80%9A%E8%BF%87%E5%AE%89%E8%A3%85cv2%E7%9A%84%E4%BE%9D%E8%B5%96%E9%A1%B9%E6%9D%A5%E8%A7%A3%E5%86%B3%E6%AD%A4%E9%97%AE%E9%A2%98%E3%80%82%20%E6%82%A8%E5%8F%AF%E4%BB%A5%E5%9C%A8Docker%E5%AE%B9%E5%99%A8%E4%B8%AD%E5%AE%89%E8%A3%85libgl1%E4%BE%9D%E8%B5%96%E9%A1%B9%EF%BC%8C%E4%BD%BF%E7%94%A8%E4%BB%A5%E4%B8%8B%E5%91%BD%E4%BB%A4%3A%20%22apt-get%20update%20%26%26%20apt-get%20install%20libgl1%22%E3%80%82
you need to check python manage.py runserver still works in the container

---
一些需求：
templates/ -> /root/templates/
- 使用一次dockerfile就能完成所有的东西，包括一些必要的设置，和项目的专门设置
- nginx, vim
  ```bash
  apt-get update
  apt-get install -y nginx vim

  cat default >> /etc/nginx/sites-enabled/default
  ```
- supervisor
  ```bash
  pip3 install supervisor

  cp supervisord.conf /etc/supervisord.conf
  ```
- uwsgi
  ```bash
  pip3 install uwsgi

  uwsgi.ini
  ```
- django start（just copy，debug locally，need a scripts to start everything，copy utils）
  ```bash
  # utils.py urls.py settings.py
  cp api/ /home
  ```
- project file
- gpu
