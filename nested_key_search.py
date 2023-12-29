# rika
# py 3.10
# simple recursive search for value from key in nested dictionaries & lists

def nested_key_search(input, key):
    if not isinstance(key, str):
        raise TypeError("second argument should be a string; the key to search for")
    
    if isinstance(input, dict):
        for k, v in input.items():
            if k == key:
                return v
            if isinstance(v, list) or isinstance(v, dict):
                recurse = nested_key_search(v, key)
                if recurse != None:
                    return recurse
        else:
            return None
                
    elif isinstance(input, list):
        for item in input:
            if isinstance(item, list) or isinstance(item, dict):
                recurse = nested_key_search(item, key)
                if recurse != None:
                    return recurse
        else:
            return None
        
    else:
        raise TypeError("first argument should be a dictionary or a list; the thing to search through")
