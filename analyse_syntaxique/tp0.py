import ply.yacc as yacc
import ply.lex as lex

# LEX

tokens = ['NUM', 'FOIS', 'PARG', 'PLUS', 'DIV', 'MOINS', 'PARD']

t_ignore = ' \t\n'

t_FOIS = r'\*'
t_PARG = r'\('
t_PARD = r'\)'
t_PLUS = r'\+'
t_DIV = r'\/'
t_MOINS = r'\-'




def t_NUM(t):
    r'[-]?\d+'
    return t



def t_error(t):
    print("Illegal character '%s" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

lexer.input("3*(8-4)")
while True:
    tok = lexer.token()
    if not tok:
        break
    print("Ligne " + str(tok.lineno) + " : " + str(tok.type))


# YACC

precedence = (
 ('left', 'PLUS', 'MOINS'),
 ('left', 'FOIS', 'DIV'),
)

def p_expression(p):
    r'''expression ::= expression PLUS expression
    | expression DIV expression
    | expression MOINS expression
    | expression FOIS expression
    | PARG expression PARD
    | NUM'''


def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()
result = parser.parse('(-5 + 4)*3- 2')
print(result)
