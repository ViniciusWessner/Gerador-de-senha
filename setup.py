import sys
from cx_Freeze import setup, executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    executable('Geradordesenha.py', base = base)
]

setup(name='Gerador de senhas', 
    version='1.0.0',
    desciption='App que gera senhas criptografadas', 
    executables = executables
)