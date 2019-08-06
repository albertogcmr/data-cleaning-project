import re

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
    # for nan cases
    try: 
        text = text.lower()
        dictionary = {
            'surf': 'Surfing', 
            'fish': 'Fishing', 
            'swim': 'Swimming', 
            'bath': 'Swimming', 
            'board': 'Boarding', 
            'snor': 'Diving', 
            'div': 'Diving', 
            'wadi': 'Wading', 
            'stand': 'Standing', 
            'scub': 'Diving', 
            'kaya': 'Kayaking', 
            'cano': 'Canoeing', 
            'row': 'Rowing', 
            'sail': 'Sailing', 
            'boat': 'Boating', 
            'float': 'Floating',             
            'crab': 'Crabbing', 
            'ski': 'Skiing', 
            'float': 'Floating', 
        }
        for key, value in dictionary.items(): 
            if key in text: 
                return value
        else: 
            return text.capitalize()
    except: 
        return None
        
def delete_columns(df, columns=[]):
    return df.drop(columns, axis=1) 

# auxiliar
def get_feets(text): 
    d = "\d+\.*\d*\s*"
    # res = re.findall("\d+\.*\d*\s*feet | \d\.*\d*\s*foot | \d+\.*\d*\s*'", text)
    res = re.findall("{}feet|{}foot|{}'".format(d, d, d), text)
    if len(res) > 0: 
        return float(re.sub("feet|foot|\s|'", '',res[0])), 'feet'
    else: 
        return None, None# 'unknown', 'unknown'

# auxiliar
def get_meters(text): 
    d = "\d*\.*\d+\s*"
    # res = re.findall("\d+\.*\d*\s*feet | \d\.*\d*\s*foot | \d+\.*\d*\s*'", text)
    res = re.findall("{}meter|{}meters|{}m".format(d, d, d), text)
    if len(res) > 0: 
        return float(re.sub("meters|meter|\s|m", '',res[0])), 'meters'
    else: 
        return None, None# 'unknown', 'unknown'
    
def get_units_qty(text): 
    try: 
        if any(word in text for word in ('feet', 'foot', "'")): 
            return get_feets(text)
        elif any(word in text for word in ('meter', 'meters', "m")): 
            return get_meters(text)
        else: 
            return None, None# 'unknown', 'unknown'
    except: 
        return None, None# 'unknown', 'unknown'
    else:
        pass
    finally: 
        pass