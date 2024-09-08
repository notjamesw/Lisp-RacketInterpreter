# converts inputs into a list, 
def tokenizeProgram(chars: str) -> list:
    L = chars.replace("(", " ( ").replace(")", " ) ").split()
    return L

