

def invert_string(string):
    return string[::-1]


def decorator():
    
    def internal_function(string):
        
        resultado = invert_string(string)
        
        return resultado
    
    return internal_function

