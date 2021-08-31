import datetime

# Funções
def show_msg(msg):
    print('%s: %s' % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")), msg))

show_msg('Mensagem de teste')