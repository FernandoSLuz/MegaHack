
def check_json(json_data, json_keys):
    print(json_keys)
    print(json_data)
    try:
        for key in json_keys:
            if(key not in json_data): return False
            else: 
                if(json_data[key] == ""): return False
        return True
    except:
        return False