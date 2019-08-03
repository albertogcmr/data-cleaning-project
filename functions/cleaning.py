def clean_fatal(x): 
    
    if 'y' in str(x).lower(): 
        return 'fatal'
    elif x != 'UNKNOWN': 
        return 'not fatal'
    else: 
        return None

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
        return None

def shark_name(text, sharks=[]): 
    text = str(text).lower()
    for shark in sharks: 
        if shark in text: 
            return '{} shark'.format(shark)
    else: 
        return None

def is_provoked(text): 
    return text.lower() == 'provoked'

def clean_activity(text): 
    dictionary = {
        'surf': 'Surfing', 
        'fish': 'Fishing', 
        'swim': 'Swimming', 
        'board': 'Boarding', 
        'snor': 'Diving', 
        'surf': 'Surfing', 
        'surf': 'Surfing', 
        'surf': 'Surfing', 
        
    }
    return text
