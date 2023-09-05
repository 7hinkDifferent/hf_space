```bash
docker volume create gradio

docker run -itd -p 8000:8000 --restart=always -v gradio:/home/workspace --name gradio 7hink/project:1.1

docker run -itd -p 8000:8000 --restart=always --name gradio gradio:1.1

docker exec -it gradio /bin/bash

nohup python3 -m pip install -r requirements.txt &

```

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
