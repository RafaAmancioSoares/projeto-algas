import time
import datetime
from sys import getsizeof
import mysql.connector
from mysql.connector import errorcode
import random

print("------------------------------------------------------------------------------------------------------------\n" +
      "PROJETO ALGAS -- RAFAELA AMANCIO SOARES -- GRUPO 3\n\n" +
      "Projeto: Analisar os dados de saúde para seguradoras/convênios através dos dados gerados pelo smart watch\n\n" +
      "Análise - Sample 2\n"
      "------------------------------------------------------------------------------------------------------------")

sample2 = range(1, 1441) # 1 usuário
dataList = []

for n in sample2:
    dataList.append(random.randint(0, 191))
print("Criando lista com valores de entrada\n\n")

try:
    inicio = time.time()
    db_connection = mysql.connector.connect(
        host='34.201.245.104', 
        user="root",
        password="urubu100",
        database="algas_transactions")
    print("Iniciando conexão com database\n")
    
    cursor = db_connection.cursor()
    
#     cursor.execute("TRUNCATE TABLE passos_adulto")
    print("Limpando histórico da tabela\n")
    

    print("Iniciando transações\n\n")
    print("---- Without Memoryview Sample 2 ----")
    vwWithoutMemorySample2 = []
    count = 0
    for n in sample2:
        data = dataList[n-1]
        b = data
        start = time.time()
        max_mem = 0
        min_mem = 0
        while b:
            if n == len(str(b)):
                max_mem = getsizeof(b) - getsizeof('')
            elif len(str(b)) == 1:
                min_mem = getsizeof(b) - getsizeof('')
            b = str(b)[1:]
        stop = time.time()
        count += 1
        
        final_time = stop-start
        max_mem = max_mem/10**3
#         print(f'{count}º Transação {n} {final_time} - Max mem {max_mem} KB - Min mem {min_mem} B')
        vwWithoutMemorySample2.append(stop-start)
        
        query = "INSERT INTO passos_adulto(data) " \
                "VALUES(%s)"
        args = (data, )
    
        cursor.execute(query, args)
        db_connection.commit()
        
    
    print("\n\n---- With Memoryview Sample 2 ----")
    vwMemorySample2 = []
    count = 0
    for n in sample2:
        data = b'dataList[n-1]'
        b = memoryview(data)
        start = time.time()
        max_mem = 0
        min_mem = 0
        while b:
            if n == len(str(b)):
                max_mem = getsizeof(b) - getsizeof('')
            elif len(str(b)) == 1:
                min_mem = getsizeof(b) - getsizeof('')
            b = str(b)[1:]
        stop = time.time()
        count += 1
        
        final_time = stop-start
        max_memory = max_mem/10**3
#         print(f'{count}º Transação {n} {final_time} - Max mem {max_memory} KB - Min mem {min_mem} B')
        vwMemorySample2.append(stop-start)
        
    final = time.time()

    print(f"\n\nTempo de execução: {final - inicio}s")
    data_atual = datetime.datetime.now()
    temp_exec = final - inicio
    
    query = "INSERT INTO execucoes_algas(data_exec, tempo_exec) " \
                "VALUES(%s,%s)"
    args = (data_atual, temp_exec, )
    
    cursor.execute(query, args)
    db_connection.commit()

    # Plot everything
#     import matplotlib.pyplot as plt
#     plt.plot(vwWithoutMemorySample2, 'x-', label='Without Memoryview Sample 2')
#     plt.plot(vwMemorySample2, 'o--', label='With Memoryview Sample 2')
#     plt.xlabel('Size of Bytearray')
#     plt.ylabel('Time (s)')
#     plt.legend()
#     plt.show()
    
finally:
    db_connection.close()