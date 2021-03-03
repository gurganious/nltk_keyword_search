from itertools import product
import ahocorasick as ahc

def make_aho_automaton(keywords):
    A = ahc.Automaton()  # initialize
    for (key, cat) in keywords:
        A.add_word(key, (cat, key)) # add keys and categories
    A.make_automaton() # generate automaton
    return A

class Finder():
    def  __init__(self, df_disease, df_biomarker):
        ' Initialize Automatons for Disease and biomarkers '
        #   Disease and biomarker Keywords
        #      Pairs of (name, id) with name as key and id as category
        #      note: used underscore on variable names (e.g. _id) to ensure against shadowing builtins
        disease_keys = ((_name.lower(), _id) for _name, _id in zip(df_disease['name'], df_disease['id']))
        #     Pairs of (CA, Entry_name) with CA as key and Entry_name as category
        biomarker_keys = (
            (_ca_entry, _entry_name) 
            for _ca, _entry_name in zip(df_biomarker['CA'], df_biomarker['Entry_name']) 
            for _ca_entry in _ca.split() if len(_ca_entry) >= 3
        )
        
        # Create Aho-Corasick automatons
        #    Surround keywords with space so we find only only word boundaries
        self.disease_automaton = make_aho_automaton((f' {keyw} ', cat) for keyw, cat in disease_keys)
        self.biomarker_automaton = make_aho_automaton((f' {keyw} ', cat) for keyw, cat in biomarker_keys)
        
    def find_keywords(self, line, A):
        ' Finds key words in line that exist in Automaton A (as generator)'
        # ensure line has space at beginning and end, but remove from key
        return ((keyw.strip(), cat) for end_index, (cat, keyw) in A.iter(f' {line} '))
    
    def process(self, nltk_sentence):
        sentence = f' {nltk_sentence} '  # ensures sentence as space at both ends (for keyword matching)
        for d, m in product(self.find_keywords(sentence, self.disease_automaton), 
                            self.find_keywords(sentence, self.biomarker_automaton)):
            yield d, m
  
def format_result(d, m):
    ' Format results for printing '
    return print(f'Match_found: Disease: name {d[0].title()} with id {d[1]}, Biomarker CA {m[0]} with Entry_name {m[1]}')
