import ply.lex as lex

tokens = ['GROUP', 'OP']

t_ignore = ' \t'

OP = r'[+\-*/]'
NOMBRE = r'[0-9]{1,}'
t_GROUP = r'' + NOMBRE + '\ ' + NOMBRE + '\ ' + OP
t_OP = OP


def t_error(t):
    print("Illegal character '%s" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

lexer.input("12 4 + 3 5 + *")
value = []
while True:
    tok = lexer.token()
    if not tok:
        break
    print("Ligne " + str(tok.lineno) + " : " + str(tok.type) + " : " + str(tok.value))
    if (str(tok.type) == 'GROUP'):
        res: str = str(tok.value).split(' ')
        if res[2] == '+':
            value.append(int(res[0]) + int(res[1]))
        elif tokens[2] == '-':
            value.append(int(res[0]) - int(res[1]))
        elif res[2] == '*':
            value.append(int(res[0]) * int(res[1]))
        elif tokens[2] == '/':
            value.append(int(res[0]) / int(res[1]))
    elif (str(tok.type) == 'OP'):
        res: float = 0
        if tok.value == '+':
            res = float(value[0]) + float(value[1])
        elif tok.value == '-':
            res = float(value[0]) - float(value[1])
        elif tok.value == '*':
            res = float(value[0]) * float(value[1])
        elif tok.value == '/':
            res = float(value[0]) / float(value[1])

        print("Résultat: " + str(res))
