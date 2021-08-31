import paramiko, os, pass_ssh

#inicia o cliente SSH
ssh = paramiko.SSHClient()
#define que as chaves publicas serao aceitas automaticamente
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#usuario e senha de conexao
user=pass_ssh.user
password=pass_ssh.password

# Obtem o caminho 
path = os.get_exec_path()
print(path[0])
exit()
project_path = '%s\%s' % (os.getcwd(),'Comandos remotos Linux')

#lista de servidores a serem verificados
server_list = '%s\%s' % (project_path,'server_list.txt')

#lista de usuarios que podem ser root
root_list = '%s\%s' % (project_path,'root.txt')

#cria lista vazia para receber os usuarios que podem ser root
root_allowed = []

#abre arquivo com relacao de usuarios que podem ser root
root_users = open(root_list, 'r')

#le a lista de usuarios que podem ser root e adiciona a uma lista em memoria
for root in root_users:
    #remove caractere \n do final do nome do servidor
    root = root.rstrip()
    if len(root) > 0:
        root_allowed.append(root)

root_users.close()

#abre arquivo com relacao de servidores que devem ser verificados
servers = open(server_list, 'r')

#monta loop que executara os comandos para cada servidor
for server in servers:
    #se o nome do servidor estiver em branco, pare o loop
    if len(server) == 0:
        break
    #remove caractere \n do final do nome do servidor
    server = server.rstrip()

    #se conecta com o servidor
    ssh.connect(server, username=user, password=password)
    #executa o comando no servidor
    (stdin, stdout, stderr) = ssh.exec_command('cat /etc/passwd')
    user_list = stdout.readlines()

    #monta loop para ler cada linha retornada do arquivo /etc/passwd
    for user in user_list:
        #faz o split da linha utilizando o separador ":"
        user_fields = user.split(':')
        if len(user_fields) < 5:
            continue

        #obtem nome e id de usuario
        user_name = user_fields[0]
        user_id = int(user_fields[2])

        #se id igual a 0 e nome de usuario nao estiver
        #na lista de permitidos
        if user_id == 0 and user_name not in root_allowed:
            print('Servidor %s: Usuario %s possui permissao de root indevidamente' % (server, user_name))
servers.close()