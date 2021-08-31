# Leitura/Escrita de arquivos
# “r” para leitura, “w” para escrita, “a” para escrita com append
path = r'C:\teste.txt'
file = open(path, 'r')

for row in file:
    # rstrip remove o enter no fim da saída do comando print
    print(row.rstrip())