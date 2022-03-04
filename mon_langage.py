import ply.lex as lex

tokens = [
    'COMMENT',
    'MC',
    'ID',
    'PTVIRG',
    'PARG',
    'PARD',
    'CHAINE',
    'EGAL',
    'MOINS',
    'PLUS',
    'MUL',
    'REEL'
]

t_ignore = ' '


def t_error(t):
    print("Illegal character '%s" % t.value[0])
    t.lexer.skip(1)


def t_EGAL(t):
    r'\='
    return t


def t_MOINS(t):
    r'\-'
    return t


def t_PLUS(t):
    r'\+'
    return t


def t_MUL(t):
    r'\*'
    return t


def t_REEL(t):
    r'[0-9]{1,}\.[0-9]{1,2}'
    return t


def t_CHAINE(t):
    r'\"[a-zA-Z\ \'éè\"\.îô]{0,}\"'
    return t


def t_PTVIRG(t):
    r';'
    return t


def t_PARG(t):
    r'\('
    return t


def t_PARD(t):
    r'\)'
    return t


def t_COMMENT(t):
    r'\/\/[a-zA-Z\ \'éè\"\.îô]{0,}'
    return t


def t_MC(t):
    r'DECLARATIONS|CODE|double|int|read|write'
    return t


def t_ID(t):
    r'[a-zA-Z0-9]{1,}'
    return t


def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1


lexer = lex.lex()
fichier = open('./langage.ml', 'r', encoding='UTF8')
s = fichier.read()
lexer.input(s)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(str(tok.lineno) + " " + str(tok.type) + " " + str(tok.value))
