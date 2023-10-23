from ply import lex
from ply import yacc
import sys
import os
os.system('cls') or None
tokens = [
    'INT',
    'FLOAT',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'PARENTHESES_L',
    'PARENTHESES_R',
    'POTENCY'
]

t_ignore = r' '
t_PLUS   = r'\+'
t_MINUS  = r'\-'
t_DIVIDE = r'\/'
t_MULTIPLY  = r'\*'
t_EQUALS = r'\='
t_POTENCY = r'\^'
t_PARENTHESES_L = r'\('
t_PARENTHESES_R = r'\)'

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t

def t_error(t):
    print ("Illegal caracters!")
    t.lexer.skip(1)
    
lexer = lex.lex()
precedence = (
    ('left','PLUS','MINUS'),
    ('left','MULTIPLY','DIVIDE')
)

def p_cal(p):
    '''
    calc : expression
         | var_assign
         | empty
    '''
    print(p[1])

def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression
    '''
    p[0] = ('=', p[1], p[3])
    
def p_empression(p):
    '''     
    expression : expression MULTIPLY expression
               | expression DIVIDE expression 
               | expression PLUS expression
               | expression MINUS expression
               | expression POTENCY expression
    '''
    p[0] = (p[2],p[1],p[3])

def p_empression_int_float(p):
    '''     
    expression : INT
               | FLOAT
     '''
    p[0] = p[1]

def p_expression_parentheses(p):
    '''
    expression : PARENTHESES_L expression PARENTHESES_R
    '''
    p[0] = p[2]

def p_empression_var(p):
    '''     
    expression : NAME
    '''
    p[0] = (p[1])

def p_error(p):
    print("Syntax error found!")
    
def p_empty(p):
    '''
    empty : 
    '''
    p[0] = None
    
parser = yacc.yacc()
while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    print("\nAnálise Léxica\n")
    lexer.input(s)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
    print("\nAnálise Sintática\n")
    parser.parse(s,debug=False)
    print("\n")