import requests
import sqlite3

#-------------------REQUEST--------------------------------
cep = input('Digite seu CEP: ')
url = 'https://viacep.com.br/ws/{user_cep}/json/'.format(user_cep = cep)
res = requests.get(url).json()
rua = res['logradouro']
bairro = res['bairro']
cidade = res['localidade']

#-------------------BANCO DE DADOS-------------------------
conn = sqlite3.connect('ceps.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS ceps(rua TEXT PRIMARY KEY NOT NULL, bairro TEXT NOT NULL, cidade TEXT NOT NULL)')
cur.execute("INSERT INTO ceps(rua, bairro, cidade) VALUES ('{}', '{}', '{}')".format(rua, bairro, cidade))

cursor = cur.execute('SELECT * FROM ceps')
for i in cursor:
    print("RUA:", i[0])
    print("BAIRRO:", i[1])
    print("CIDADE:", i[2])

cur.close()