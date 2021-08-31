import datetime
from ftplib import FTP
import urllib.request

http_url='http://servidor.intranket/arquivo_rh.zip'
ftp_server='ftp.empresa.com'
ftp_user='user_ftp'
ftp_passwd='password_ftp'
ftp_file_name='EMPRESA_%s.zip' % datetime.datetime.now().strftime('%Y%m%d')

try:
    #abre conexao com o servidor web
    request=urllib.request.Request(http_url)
except Exception:
    print('Falha ao abrir conexão com o servidor web') 
    exit()   

try:
    #envia request para fazer o download do arquivo
    response=urllib.request.urlopen(request)
    print('Inicio do download do arquivo')
except Exception:
    print('Falha na request de download do arquivo')  
    exit()  

try:
    #abre arquivo local em modo binario para escrita
    local_file=open(ftp_file_name, 'wb')
except Exception:
    print('Falha ao abrir %s o arquivo para escrita' % ftp_file_name)
    exit()

try:
    #grava dados recebidos via HTTP
    local_file.write(response.read())
    local_file.close()
    print('Download do arquivo %s concluido com sucesso' % ftp_file_name)
except Exception:
    print('Falha no download do arquivo')
    exit()

try:
    #abre o arquivo gravado em modo binario para leitura
    local_file=open(ftp_file_name, 'rb')
except Exception:
    print('Falha ao abrir o arquivo gravado')
    exit()

print('Inicio do upload do arquivo para %s' % ftp_server)

try:
    ftp_client=FTP(ftp_server)

    #faz login com o servidor FTP
    ftp_client.login(ftp_user, ftp_passwd)
except Exception as e:
    print('Falha na tentativa de conexão com o servidor FTP') 
    exit()   

try:
    #envia arquivo em modo binario
    ftp_client.storbinary('STOR %s' % ftp_file_name, local_file)
    print('Upload do arquivo %s concluido com sucesso' % ftp_file_name)
    local_file.close()
except Exception:
    print('Falha ao enviar o arquivo para o servidor FTP')
    exit()