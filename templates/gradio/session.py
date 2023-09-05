import requests
import pickle
import os

SESSION = requests.session() # start a session connection
CSRF_TOKEN = None # to store csrf token for post request

# get remote server
# server = "http://localhost:8000/" # uncomment this if debug locally
server = os.getenv("SERVER") # uncomment this if deploy
if server[-1] != "/": server += "/"

def get_csrf_token(refresh=False):
    """return csrf token either by local variable or from the backend.
    """
    global CSRF_TOKEN
    if (CSRF_TOKEN == None or refresh):
        response = get("csrf/")
        CSRF_TOKEN = response["csrf_token"]
    return CSRF_TOKEN

def format_content(content: dict = {}):
    """format params for get request.
    """
    result = ""
    has_content = False
    for key in content:
        has_content = True
        result += "{}={}".format(key, content[key])
    if has_content: result = "?" + result

    return result

def pickle_loads(response: requests.Response):
    """load content from response. try pickle.loads if possible.
    """
    if (not response.ok):
        raise RuntimeError("API request failed with response status {} and text:\n {}".format(response.status_code, response.text))
    else:
        try:
            content = pickle.loads(response.content)
        except BaseException as error:
            content = response.content.decode()
        return content

def get(url: str, content: dict = {}):
    """get request. return content from backend.
    """
    full_path = server + url + format_content(content)
    try:
        response = SESSION.get(full_path)
        content = pickle_loads(response)
    except BaseException as error:
        raise RuntimeError(f"GET request to {url} failed with error:\n {error}")
    return content

def post_step(url: str, content):
    """naive post request. return response from backend.
    """
    SESSION.headers.update({"X-CSRFTOKEN": get_csrf_token()})
    return SESSION.post(url, content)


def post(url: str, content):
    """post request. return content from backend. handle csrf token problem.
    """
    full_path = server + url

    def check_csrf(response):
        new_response = response
        if (not response.ok and response.status_code == 403):
            get_csrf_token(True)
            new_response = post_step(full_path, pickle.dumps(content))
        return new_response
    
    try:
        response = post_step(full_path, pickle.dumps(content))
        response = check_csrf(response)
        content = pickle_loads(response)
    except BaseException as error:
        raise RuntimeError(f"POST request to {url} failed with error:\n {error}")
    return content

