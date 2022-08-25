import requests
from requests.auth import HTTPBasicAuth
import pyodbc
from datetime import datetime
import time
from OpenSSL import SSL

def get_dados_clp(slot):
    url = f"http://IP_GATEWAY_ADVANTECH_WISE/di_value/{slot}"
    user = "USUARIO_AQUI"
    passw = "SENHA_DEFAULT_AQUI"

    res = requests.get(url, auth=HTTPBasicAuth(user, passw))

    return res.json()


def connect_db():
    server = 'IP_SERVIDOR_AQUI' 
    database = 'NOME_DO_BANCO_AQUI' 
    username = 'LOGIN_BANCO_AQUI' 
    password = 'SENHA_USER_AQUI' 
    string_connection = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    connection = pyodbc.connect(string_connection)
    return connection

try:
    connection = connect_db()
    cursorobj = connection.cursor()
    print("Conectado com o banco")
except:
    print("erro de conexão com o banco")
    print("Tentando reconectar ...")
    connection = connect_db()
    cursorobj = connection.cursor()
    raise

contador = 0

while True:
    try:
        time.sleep(1)
        res = get_dados_clp("slot_0")
        DIVal = res["DIVal"]

        valores = tuple(item["Val"] for item in DIVal)
        data_hora = datetime.now()
        data_hora_formatada = (data_hora.strftime('%d/%m/%Y %H:%M:%S'), ) # transforma em tupla para que posse ser adicionada no inicio
        valores_completos = data_hora_formatada + valores

        sql = """
        INSERT INTO [WISE_4051_26E] (codigo, data_hora, canal_1, canal_2, canal_3, canal_4, canal_5, canal_6, canal_7, canal_8) 
        VALUES ('01', ? , ?, ?, ?, ?, ?, ?, ?, ?)
        """

        counter = cursorobj.execute(sql, valores_completos).rowcount
        contador = contador + counter
        connection.commit()
        print(f"{contador}  adicionado com sucesso")
        

    except KeyboardInterrupt:
        print("\nPrograma terminado")
        break
    except Exception as ex:
        print("Algum erro aconteceu", ex)
        continue
    

cursorobj.close()
connection.close()