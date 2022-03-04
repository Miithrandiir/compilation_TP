import ply.lex as lex

tokens = ['NO', 'LIB', 'NB', 'VIRG', 'PT']

t_ignore = ' \t'

mots_simples = ['FACTURE', 'TOTAL']
tokens += mots_simples

t_NB = r'[0-9]+'
t_VIRG = ','
t_PT = r'\.'

t_FACTURE = 'FACTURE'
t_TOTAL = 'TOTAL'


def t_NO(t):
    r'[a-zA-z]{2}(\d){3}'
    return t


def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1


def t_LIB(t):
    r'[a-zA-Z]+'
    if t.value in mots_simples:
        t.type = t.value
    return t


def t_error(t):
    print("Illegal character '%s" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

lexer.input("FACTURE JA001\n"
            "Pomme 3 10,\n"
            "Orange 5 7,\n"
            "TOTAL 65.")
while True:
    tok = lexer.token()
    if not tok:
        break
    print("Ligne " + str(tok.lineno) + " : " + str(tok.type))
