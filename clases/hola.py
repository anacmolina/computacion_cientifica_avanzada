#!/usr/bin/env python3

import sys

#Lista de parametros
#print(sys.argv)

s = 'Hello, World!'

if len(sys.argv)>=2:
    if sys.argv[1]=='-S':
        s = s.replace('Hello', 'Hola').replace('World', '!Mundo')

print(s)


# En el setup.py --> Details scripts=['/bin/hello'] (GitHub abc123 restrepo)
# Carpeta bin en el bin se adiciona automaticamente al PATH
# Si queres otra carpeta ejecutable toca agregarla al PATH
# export PATH="$HOME/bin:$PATH"

#Revisar todo lo de parser
#Revisar lo de bash
#ahhhh
