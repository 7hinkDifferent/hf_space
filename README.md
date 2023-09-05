structure:
- .gitignore
- template
  - Dockerfile
  - Django (secret key)
  - gradio
- README.md
- a simple case.md
- checklist.md
- git.md
- python.md # conda
- hf_space.md # different levels of usage
- gradio.md
- devtools.md
- html.md
- css.md
- django.md
- nginx.md
- uwsgi.md
- server.md
  - port
- misc.md


steps:
1. finish deployment
2. write template
   1. Dockerfile # just a docker, you need to handle the rest of the settings for the specific project
3. write docs
（得先在本地测试过再说，还是不能完全做到一步到位，还是得进去改一下配置）


LICENSE, terms of use


checklist



backend
Django, Flask


deployment
Nginx


## Walkthrough
directory:
- api/ # backend
  - requirements.txt # your project requirements.txt
- templates/ # 
- gradio-app/ # 
  - README.md
  - requirements.txt

1. create a repo <your-gradio-app> on huggingface and clone it.
2. in one cmd. create a virtual env with <your-gradio-app>/requirements.txt.
3. run `python3 templates/main.py --type gradio --path <your-gradio-app>` to copy necessary scripts to <your-gradio-app>.
4. run `gradio <your-gradio-app>/app.py` to start <your-gradio-app> locally.
5. in another cmd. create a virtual env with templates/requirements.txt.
6. run `django-admin startproject api` to create a django project `api/`.
7. run `python3 templates/main.py --type django` to copy necessary scripts to api/
8. run `python3 api/manage.py runserver` to start django project locally.
9. custom <your-gradio-app>. checkout server variable in session.py. modify requirements.txt.
10. custom django project. modify requirements.txt.
11. make sure you can run the whole project successfully locally before you move to next steps.
12. change server variable in session.py
13. change DEBUG=False
14. `git push` <your-gradio-app> and set SERVER secret in settings page.
15. upload Dockerfile, api/ and templates/ to your private server. make sure they are in the same directory. # install docker and open the port
16. run `python3 templates/main.py --type server` to copy necessary scripts to specific directories.
17. run `some_docker.sh` to start the docker image.
18. run `docker exec -it` to start the docker container.
19. checklist
20. have fun!