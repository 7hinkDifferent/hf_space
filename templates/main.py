import os, sys, pathlib, shutil, subprocess
import argparse

# path
ROOT = pathlib.Path(__file__).resolve().parents[1]
TEMPLATES = pathlib.Path(__file__).resolve().parents[0]
DJANGO = os.path.join(TEMPLATES, "django")
GRADIO = os.path.join(TEMPLATES, "gradio")
SERVER = os.path.join(TEMPLATES, "server")

def cp_django(path):
    """expected directory structure
    /home/
        api/
            api/
                +++utils.py
            +++*
    """
    if path == None:
        path = os.path.join(ROOT, "api")

    files = os.listdir(DJANGO)
    for file in files:
        if file == "urls.py" or file == "utils.py":
            shutil.copy(os.path.join(DJANGO, file), os.path.join(path, "api"))
        else:
            shutil.copy(os.path.join(DJANGO, file), path)

def cp_gradio(path):
    """expected directory structure
    /home/
        gradio-app/
            +++*
    """
    if path == None:
        path = os.path.join(ROOT, "gradio-app")

    files = os.listdir(GRADIO)
    for file in files:
        shutil.copy(os.path.join(GRADIO, file), path)

def cp_server(path):
    """expected directory structure
    /
        etc/
            /nginx/sites-enabled/
                +++default
            +++supervisord.conf
        root/
            +++*
        +++start.sh
    """
    files = os.listdir(SERVER)
    for file in files:
        if file == "default":
            subprocess.Popen(f"cat {os.path.join(SERVER, file)} >> /etc/nginx/sites-enabled/default", shell=True)
        elif file == "start.sh":
            subprocess.Popen(f"cp {os.path.join(SERVER, file)} /{file}", shell=True)
        elif file == "supervisord.conf":
            subprocess.Popen(f"cp {os.path.join(SERVER, file)} /etc/{file}", shell=True)
        else:
            subprocess.Popen(f"cp {os.path.join(SERVER, file)} /root/{file}", shell=True)


def main(args):
    """copy template files to specific project folder
    """
    try:
        path = args.path
        globals()["cp_"+args.type](path)
        print("files copied successfully!")

    except BaseException as error:
        raise RuntimeError(
            "Couldn't copy template files to specific project folder. "
            "Are you sure you have followed the README.md to organize the directories? "
            "Are you sure the templates/ folder is complete? "
            "Try --path argument to specify the project folder. "
        ) from error



def args_parse():
    """args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, required=False, help="relative path to your desired directory.")
    parser.add_argument("--type", choices=["django", "gradio", "server"], type=str, required=True)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = args_parse()
    main(args)