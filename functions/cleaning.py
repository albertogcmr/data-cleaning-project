def clean_fatal(x): 
    
    if 'y' in str(x).lower(): 
        return 'fatal'
    elif x != 'UNKNOWN': 
        return 'not fatal'
    else: 
        return 'unknown'

def clean_age(x): 
    try: 
        return int(x)
    except: 
        return None

def clean_sex(text): 
    text = str(text)
    if text.startswith('M'): 
        return 'male'
    elif text.startswith('F'): 
        return 'female'
    else: 
        return 'unknown'