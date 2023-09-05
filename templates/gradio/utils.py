# some random functions

def make_list_param(*params):
    """useful function if you want list-like params or returns for gradio event
    example:
    [param0, [param1, param2], {param3, param4}] -> [param0, param1, param2, param3, param4]
    """
    result = []
    for param in params:
        if isinstance(param, list):
            for item in param:
                result.extend(make_list_param(item))
        elif isinstance(param, dict):
            for key in param:
                result.extend(make_list_param(param[key]))
        else:
            result.append(param)
    return result