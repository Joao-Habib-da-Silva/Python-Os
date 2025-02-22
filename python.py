import os as os
print(os.environ)
print(os.environ['Username'])
print(os.getcwd())
os.mkdir('Teste')
caminho = r'C:\Users\joaoh\Downloads\pra lançar no github\Teste'
os.chdir(caminho)
outro = r'C:\Users\joaoh\Downloads\pra lançar no github\teste\agua\funcionou'
os.makedirs(outro)