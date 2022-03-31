"""
Wederson Anthony Arruda Neto-UTF-8 - 30-03
"""

#Estrutura de Controle - Tomada de Decisão

try: #Decisão
    nome = input('Digite seu nome:')
    disciplina = input('Digite o nome da disciplina:')
    nota = float(input('Digite sua nota:'))                                         
    if len(nome)== 0:
        print('Digite um nome válido')
    if len(disciplina)== 0:
        print('Digite uma disciplina cadastrada')
except ValueError:
    print('Digite uma nota válida')
finally:
    print('Bloco finalizado')        
if nota >= 60:    
    mensagem = 'Você passou. Parabéns!!!'
else:
    mensagem = 'Você está de exame' 
print('Acadêmico):',nome)
print('Disciplina:', disciplina)
print('Nota do semestre:', nota)
print('Situação na disciplina:', mensagem)
