import csv # importando modulo

library_sales = "../data_raw/vendas.csv" # criando variaveis que recebem arquivos de origem
library_new_csv = "../data_processed/vendas_trat.csv" # criando variavel que recebe diretório de destino

def read_database(library_database): # criando function que recebe a database de origem
    sales = []

    with open(library_database, "r") as read_sales:
        temp_sales = csv.reader(read_sales,delimiter=",")
        for reg in temp_sales:
            sales.append(reg)
    return sales

def verify_rows(variable): # function que retorna a quantidade de linhas
    print(len(variable))

def del_row(variable_for_del): # deletando o primeiro registro da lista
    del variable_for_del[0]
    return variable_for_del

def temp_database(sales): # criando database temporária
    temp_database_sales = []

    for sale in sales:
        temp_data = []
        cont = 0
        for data in sale:
            if cont == 1 or cont == 4:
                temp_data.append(data)
            elif cont == 2:
                temp_processed_data = data.replace("R$ ","").replace(".","").replace(",",".")
                modify_type = float(temp_processed_data)
                temp_data.append(modify_type)  
            cont += 1
        
        temp_database_sales.append(temp_data)

    return temp_database_sales

def ordering_data(database): # function que orderna por nome meus dados
    database.sort()
    return database

def names_sellers(database_group): # function que colhe os nomes dos vendedores
    list_name = []

    for reg in database_group:
        list_name.append(reg[0])


    list_name = set(list_name)
    return list_name

def group_commission(database_sales,list_name_sellers): # function que cria database agrupado por vendedores com comissões
    new_database_list = []

    for name in list_name_sellers:
        value = 0
        list_temp = []
        for reg in database_sales:
            if name == reg[0]:
                value += reg[1]
                type_salle = reg[2]
        
        list_temp.append(name)
        list_temp.append(value)
        list_temp.append(type_salle)

        new_database_list.append(list_temp)
    return new_database_list

def create_final_database(new_database_list): # criando nova database com os valores corretos
    database_final = []

    for commission_value in new_database_list:
        temp = []
        cont = 0
        for value in commission_value:
            if cont == 1:
                value = (value * 10) / 100
                temp.append(value)
                cont += 1

            elif cont == 2 :
                if commission_value[1] >= 1500 :
                    if value == "Online":
                        new_value_commission = temp[1] - ((temp[1] * 30) / 100)
                    else:
                        new_value_commission = temp[1] - ((temp[1] * 10) / 100)
                    temp.append(new_value_commission)
                elif value == "Online":
                    new_value_commission = temp[1] - ((temp[1] * 20) / 100)
                    temp.append(new_value_commission)
                else:
                    temp.append(temp[1])

            else:
                temp.append(value)
                cont += 1
            
            
        database_final.append(temp)
    return database_final

def insert_column(database_final,name_columns_original): # function que retorna minha database com colunas e valores corretos
    database_final.insert(0,name_columns_original)
    return database_final

def create_database_csv(database_final,library_new_csv): # function que cria nova database .csv

    with open(library_new_csv, "w") as new_database:
        writer = csv.writer(new_database)

        writer.writerows(database_final)

print("***LOG***")

print("\nLendo database de origem e atribuindo a uma variavel...")
sales = read_database(library_sales)

print("\nVerificando quantidade de linhas da variavel que contém os dados do banco original...")
verify_rows(sales)

print("\nApagando primeiro registro da variavel que contém os dados do banco original...")
del_row(sales)

temp_database_sales = []

print("\nCriando nova variavel e modificando a estrutura...")
temp_database_sales = temp_database(sales)

print("\nLendo quantidade de linhas da nova variavel...")
verify_rows(temp_database_sales)

print("\nLendo quantidade de linhas da nova variavel...")
verify_rows(temp_database_sales)

print("\nOrdenando os dados para agrupar...")
database_group = ordering_data(temp_database_sales)

print("\nVerificando nomes de todos os vendedores...")
list_name = names_sellers(database_group)

print("\nCriando uma nova lista que tem o total de vendas agrupado por vendedor...")
new_database_list = group_commission(database_group,list_name)

print("\nAjustando os valores para finalmente ter os dados que o projeto precisa...")
database_final = create_final_database(new_database_list)

name_columns_original = ["name_seller","commission_value","pay"]

print("\nInserindo cabeçalho na minha database final...")
database_final = insert_column(database_final,name_columns_original)

print("\nCriando e exportando nova database .csv...")
create_database_csv(database_final,library_new_csv)