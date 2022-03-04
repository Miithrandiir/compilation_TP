import ply.lex as lex

tokens = ['NUMBER', 'IDENTIFICATEUR', 'MC', 'MC_OTHER', 'COMMENT', 'QUOTED', 'OP', 'SPVAR', 'NEWLINE','SPACE']

t_ignore = '\t'


def t_COMMENT(t):
    r'\#[a-zA-Z\ ]{0,}'
    return t


def t_SPVAR(t):
    r'(__)[a-zA-Z0-9]{0,}(__)'
    return t


def t_QUOTED(t):
    r'[\"|\'][a-zA-Z0-9 ]{0,}[\"|\']'
    return t


def t_OP(t):
    r'[\+|\-|\<|\>|\>\=|\=|\==|\[|\]|\:|\,|\(|\)|\.|\*|\;]'
    return t


def t_NUMBER(t):
    r'[0-9]{1,}'
    return t


def t_MC_OTHER(t):
    r'len|str|self'
    return t


def t_MC(t):
    r'if|else|elif|while|break|for|return|continue|import|class|in|not|unsigned|True|False|def|enumerate'
    return t


def t_IDENTIFICATEUR(t):
    r'[a-zA-Z|_][a-zA-Z_0-9]{0,}'
    return t


def t_NEWLINE(t):
    r'\n'
    t.value = '<br/>'
    t.lexer.lineno += 1
    return t


def t_error(t):
    t.lexer.skip(1)

def t_SPACE(t):
    r'\ '
    t.value = '&nbsp;'
    return t

lexer = lex.lex()

fichier = open('./test.py', 'r', encoding='UTF8')
s = fichier.read()
lexer.input(s)

body = "<html><body style=\"background-color:#2B2B2B;\"><H2> node.py </H2><CODE>"

# 'NUMBER', 'IMPORT', 'IDENTIFICATEUR', 'MC', 'MC_OTHER', 'COMMENT', 'QUOTED', 'OP', 'SPVAR'
while True:
    tok = lexer.token()
    if not tok:
        break

    color = "FFFFF"
    if tok.type == 'NUMBER':
        color = "6897BB"
    elif tok.type == 'MC':
        color = "CC7832"
    elif tok.type == 'IDENTIFICATEUR':
        color = "A9B7C6"
    elif tok.type == "SPVAR":
        color = "B200B2"
    elif tok.type == "COMMENT":
        color = "808080"
    elif tok.type == "QUOTED":
        color = "6A8759"
    elif tok.type == "MC_OTHER":
        color = "94558D"

    body += "<font color = " + color + ">" + str(tok.value) + "</font>"
    # print("Ligne " + str(tok.lineno) + " : " + str(tok.type) + " : " + str(tok.value))

    body += "</body></html>"
    fichier = open('./res.html', 'w', encoding='UTF8')
    fichier.write(body)
