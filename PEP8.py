"""
PEP 8 - Index of Python Enhancement Proposals (índices de Propostas de aprimoramento Python)
"""
"""
O que são PEP's?
 - São arquivos que apresentam propostas de melhoria para a Linguagem Python.
 - https://www.python.org/dev/peps/

Regras mais utilizadas:
1) O pycharm vem com padrão de reconhecimento de palavras em inglês.
 - Para o pycharm reconhecer palavras em portugues faça:
   File - settings - Inspections - Proofreading - Desmarque Typo
   
2)Indentação (Organizar o código):
 - Utiliza 4 espaços para cada código dentro de blocos como funções, condicionais, classes, dentre outros.
Ex (Condicionais):
if x< 10:
    if y> 10:
        y=5
Obs: Sempre utilize 4 espaços ao invés da tecla TAB.
3) Linhas em branco: 
 - Seu programa deve haver sempre uma linha em branco no final
 - Separe funções e classes com duas linhas em branco.
Ex:
def x():
    pass


def y():
    pass
4) Importação: 
 - Se você deseja fazer importação de duas bibliotecas, importe uma por vez e logo no
   inicio do programa (Após os comentários iniciais e antes da declaração da primeira variavel/função)
Ex:
Modo Certo:
import x
import y
Modo errado:
import x,y

5) Uso de espaços:
 - Nunca utilize espaços antes ou depois de chaves, colchetes ou parenteses.
 - Use um espaço antes e depois quando declarar uma variável ou usar um operador do tipo <,>,==,dentre outros.
Ex:
def x():
    pass


y = 10
6) Nomeclatura de variáveis:
 - Utilizar letras Minusculas separadas por underline(_)
 - Utilizar letras Maiusculas separadas por underline(_)
 - Utilizar palavras começando com letras Maiusculas.
Ex:
Modo certo:
idadeJoao = 17
idade_joao = 17
IDADE_JOAO = 17
Modo errado:
idadejoao = 17
"""
