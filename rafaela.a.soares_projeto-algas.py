import time
import datetime
from sys import getsizeof
import mysql.connector
from mysql.connector import errorcode
import random

print("------------------------------------------------------------------------------------------------------------\n" +
      "PROJETO ALGAS -- RAFAELA AMANCIO SOARES -- GRUPO 3\n\n" +
      "Projeto: Analisar os dados de saúde para seguradoras/convênios através dos dados gerados pelo smart watch\n\n" +
      "Análise - Sample\n"
      "------------------------------------------------------------------------------------------------------------")

sample = range(1, 1441) # 1 usuário
dataList = []

for n in sample:
    dataList.append(random.randint(0, 191))
print("Criando lista com valores de entrada\n\n")

try:
    inicio = time.time()
    db_connection = mysql.connector.connect(
        host="localhost", 
        port="3306",
        user="root",
        password="urubu100",
        database="algas_transactions")
    print("Iniciando conexão com database\n")
    
    cursor = db_connection.cursor()
    
    # cursor.execute("TRUNCATE TABLE passos_adulto")
    # print("Limpando histórico da tabela\n")

    print("Iniciando transações\n\n")
    print("---- Without Memoryview Sample ----")
    vwWithoutMemorysample = []
    count = 0
    for n in sample:
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
        vwWithoutMemorysample.append(stop-start)
        
        
        query = "INSERT INTO transaction_without_memory(transacao, tempo_exec, max_mem, min_mem) " \
                "VALUES(%s,%s,%s,%s)"
        args = (n, final_time, max_mem, min_mem)
    
        cursor.execute(query, args)
        db_connection.commit()

        query = "INSERT INTO passos_adulto(data) " \
                "VALUES(%s)"
        args = (data, )
    
        cursor.execute(query, args)
        db_connection.commit()
        
    
    print("\n\n---- With Memoryview Sample ----")
    vwMemorysample = []
    count = 0
    for n in sample:
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
        vwMemorysample.append(stop-start)

        query = "INSERT INTO transaction_with_memory(transacao, tempo_exec, max_mem, min_mem) " \
                "VALUES(%s,%s,%s,%s)"
        args = (n, final_time, max_mem, min_mem)
    
        cursor.execute(query, args)
        db_connection.commit()
        
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
#     plt.plot(vwWithoutMemorysample, 'x-', label='Without Memoryview Sample')
#     plt.plot(vwMemorysample, 'o--', label='With Memoryview Sample')
#     plt.xlabel('Size of Bytearray')
#     plt.ylabel('Time (s)')
#     plt.legend()
#     plt.show()
    
finally:
    db_connection.close()