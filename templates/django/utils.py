from scripts.config import *
from scripts.utils import get_solver
from django.http import HttpRequest, HttpResponse
from django.middleware.csrf import get_token
import pickle

def csrf(request: HttpRequest):
    """get csrf token before post request.
    """
    return HttpResponse(pickle.dumps({"csrf_token": get_token(request)}))

def process_request(request: HttpRequest):
    """return content of the request. try pickle.loads.
    """
    if request.method == "GET":
        content = request.GET
    elif request.method == "POST":
        try:
            content = pickle.loads(request.body)
        except BaseException:
            content = request.body.decode()
    else:
        raise NotImplementedError
    return content

def process_response(content, *args, **kwargs):
    """return HttpResponse object with pickle.dumps(content).
    """
    return HttpResponse(pickle.dumps(content), *args, **kwargs)