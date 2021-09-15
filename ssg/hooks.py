_calbacks = {}

def register(hook,order = 0):
    def register_callback(func):
        return func
    return register_callback

