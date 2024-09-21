# defines the main program
from components.parse import parse
from components.evaluation import eval

def repl(prompt='Racket.py> '):
    "A prompt-read-eval-print loop."
    while True:
        val = eval(parse(input(prompt)))
        if val is not None: 
            print(schemestr(val))

def schemestr(exp):
    "Convert a Python object back into a Scheme-readable string."
    if isinstance(exp, list):
        return '(' + ' '.join(map(schemestr, exp)) + ')' 
    else:
        return str(exp)
    
repl()