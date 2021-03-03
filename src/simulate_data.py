import string
from random import randint, choice
import pandas as pd

def random_word(min_length = 2, max_length = 5, upper = False):
    ' Generate random word '
    if upper:
        # Used for biomarker
        letters = string.ascii_uppercase + string.digits
    else:
        # used by disease
        letters = string.ascii_lowercase
    
    return ''.join(choice(letters) for _ in range(randint(min_length, max_length)))

def random_sentence(min_length = 1, max_length = 3, upper = False):
    '''Random sentence -- upper (True) generates letters and digits, 
      letters only for lower
    '''
    return ' '.join(random_word(upper = upper) for _ in range(randint(min_length, max_length)))

diseases = {"id":['00001', '00261'],
        'name':['angiocarcoma', 'shrimp allergy']}
biomarkers = {'Entry_name':['TRGV2', 'TRGJ1'],
          'CA':['3BHS1 HSD3B1 3BH HSDB3', '3BP1 SH3BP1 IF']}

N = 10000
for i in range(N):
    diseases['id'].append(str(i+300).zfill(5))
    diseases['name'].append(random_sentence(min_length = 1, max_length = 5, upper = False))
    biomarkers['Entry_name'].append(random_word(4, 5, True))
    biomarkers['CA'].append(random_sentence(2, 6, True))
    
df_disease = pd.DataFrame(diseases)
df_biomarker = pd.DataFrame(biomarkers)



