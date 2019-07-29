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

# species

sharks = ['white', 'bull', 'tiger', 'wobbegong', 'blue', 'mako', 'dusky', 'blacktip', 
          'hooked', 'Zambesi', 'grey nurse', 'silky', 'thresher', 'dogfish', 
          'Reef', 'Raggedtooth', 'Goblin', 'blacktip', 'Spinner', 'Porbeagle', 
          'Porbeagle', 'stingray']
 
def shark_type(text): 
    text = str(text).lower()
    for shark in sharks: 
        if shark.lower() in text.lower(): 
            return '{} shark'.format(shark.lower())
    else: 
        return text