import os
import shutil
import datetime

#arquivo que contem a lista
path_server_list = 'C:\python_scripts\Arquivos e diretorios\Cópia de arquivos entre multiplos servidores'
file_server_list = 'server_list.txt'
path_and_file_server_list = '%s\%s' % (path_server_list,file_server_list)

#diretorio que contem os arquivos a serem copiados
bin_dir = r'C:\Bin_test'

#funcao padrao para mostrar mensagens com data e hora
def show_msg(msg):
      print('%s: %s' % (str(datetime.datetime.now().strftime
      ("%Y-%m-%d %H:%M:%S")), msg))

#verifica se o diretório com a lista de servidores existe
if not os.path.exists(path_server_list):
      show_msg('Diretório %s nao encontrado' % (path_server_list))
      exit(1)
else:
      # Muda para o diretório com a listagem de servers
      os.chdir(path_server_list)
      #verifica se o arquivo com a lista de servidores existe
      if not os.path.exists(file_server_list):
            show_msg('Arquivo %s nao encontrado no diretório %s' % (file_server_list,path_server_list))
            exit(1)

#verifica se o diretorio com os arquivos a serem copiados existe
if not os.path.exists(bin_dir):
      show_msg('Diretorio %s nao encontrado' % (bin_dir))
      exit(1)

#lista os arquivos a serem copiados
bin_files = os.listdir(bin_dir)

#verifica se existem arquivos a serem copiados
if len(bin_files) == 0:
      show_msg('Nenhum arquivo encontrado em %s para ser copiado'
       % (bin_dir))
      exit(1)

#abre o arquivo que contem a lista de servidores
servers = open(path_and_file_server_list, 'r')

#monta loop que executara os comandos para cada servidor
for entry in servers:
      (server, dir) = entry.rstrip().split('|')
      path = r'\\%s\%s' % (server, dir)

      #se o diretorio de destino nao existir, crie
      if not os.path.exists(path):
            os.mkdir(path)
      #monta loop que copiara cada arquivo para o servidor de destino
      for file in bin_files:
            shutil.copy(os.path.join(bin_dir, file), os.path.join(path, file))
            show_msg('Arquivo %s copiado para o servidor %s' % (file, server))

servers.close()