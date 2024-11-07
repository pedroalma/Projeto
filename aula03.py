#condicionais if-elif-else 
'''
No python, quando temos condicoes para realizarmos açoes, usando o if-eif-else 
SE | if |
SENAO SE | elif |
SENAO | else |

sintaxa :
if *condicao*:
    *acao*
elif* condicao*
    *acao*
else:
    *acao*

****OBS: o python e uma linguagem de **IDENTACAO OBRIGATORIA** , onde e possivel demarcar
        cada bloco com base no recuo da linha           
          
'''
print("1 - Aluno")
print("2 - Funcionario")
print("3 - Visitante")
tipoAcesso = input("Selecione uma opção: ")
if tipoAcesso == "1" or tipoAcesso == "2":
    print("Acesso liberado")
elif tipoAcesso == "3":
    print("Faça um cadastro para entrar!")
else:
    print("Acesso Negado!")        