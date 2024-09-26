import csv, copy
from table_comissao import database_final

def create_variable_payments(library_payments): # function que atribui a uma variavel os valores dos pagamentos realizados

    payments_original = []

    with open(library_payments, "r") as read_payments:
        temp = csv.reader(read_payments,delimiter=",")

        for i in temp:
            payments_original.append(i) 

    return payments_original

def verify_rows(variable): # function que lê e exibe a quantidade de linhas
    print(len(variable))

def delete_columns(variable): # excluindo colunas
    del variable[0]
    return variable

def delete_internal_data(variable_payments_original): # function que exclui os dados de datas no código

    for reg_int in variable_payments_original:
        cont = 0
        for value in reg_int:
            if cont == 0:
                del reg_int[0]
            
            cont += 1

    return variable_payments_original

def create_table_treated(variable_payments_original): # function que modifica o type dos dados referente aos valores
    payments_treated = []

    for internal_index in variable_payments_original:
        temp_list = []
        cont = 0
        for value in internal_index:
            if cont == 1:
                temp = float(value.replace("R$ ","").replace(",","."))
                temp_list.append(temp)
            else:
                temp_list.append(value)

            cont += 1

        payments_treated.append(temp_list)
    return payments_treated

def clonar_correxts_payments(database_final): # function que copia os dados da variavle que tem os valores corretos de comissão corretos
    return copy.deepcopy(database_final)

def del_internal_payments(variable_correct_payments): # function que apaga os dados de comissão bruto

    for internal_index in variable_correct_payments:
        cont = 0
        for value in internal_index:
            if cont == 1:
                del internal_index[1]
                cont += 1

            cont += 1

    return variable_correct_payments

def order_variable(variable): # function que ordena variaveis
    return sorted(variable)

def create_variable_final(payments_original_treated,correct_payments): #criando variavel final que tem os dados que precisamos
    variavel_temp = []
    cont = 0

    for internal_index in payments_original_treated:
        
        if internal_index != correct_payments[cont]:
            internal_index.append(correct_payments[cont][1])
            variavel_temp.append(internal_index)

        cont += 1

    return variavel_temp

def insert_columns_final(variable_final): # inserindo colunas na variavel final
    names_columns_payments = ["names_sellers","incorrect_payments","correct_payments"]

    variable_final.insert(0,names_columns_payments)
    return variable_final

def create_table_csv(variable_final,library):

    with open(library, "w") as writer_payments_csv:
        writer = csv.writer(writer_payments_csv)

        writer.writerows(variable_final)

library_payments = "../data_raw/pagamentos.csv"
library_new_payments_csv = "../data_processed/new_payments.csv"

print("     ***  LOG  ***     ")

print("\nAtribuindo dados de pagamentos efetuados a uma variavel")
payments_made = create_variable_payments(library_payments)

print("\nExibindo a quantidade de linhas da variavel que recebeu os pagamentos efetuados")
verify_rows(payments_made)

print("\nExibindo a quantidade de linhas da variavel que contém os valores de comissão corretos")
verify_rows(database_final)

print("\nExcluindo a coluna da variavel que tem as comissões pagas")
payments_made = delete_columns(payments_made)

print("\nExcluindo os dados referente a datas na variavel que contém os valores originais")
payments_made = delete_internal_data(payments_made)

print("\nExibindo quantidade de linhas na variavel após realizar o delete dos dados referente as datas")
verify_rows(payments_made)

print("\nCriando variavel que tem os dados referente a valores convertidos de 'STR' para 'FLOAT'")
payments_original_treated = create_table_treated(payments_made)

print("\nExibindo quantidade de linhas na variavel após realizar conversão de tipos de dados na variavel de valores efetuados")
verify_rows(payments_original_treated)

print("\nCopiando dados da variavel que tem os valores das comissões corretos e atribuindo a uma nova variavel")
correct_payments = clonar_correxts_payments(database_final)

print("\nExibindo quantidade de linhas na variavel após realizar copia dos dados e atribuir a uma outra variavel")
verify_rows(correct_payments)

print("\nExcluindo a coluna da variavel que tem as comissões corretas")
correct_payments = delete_columns(correct_payments)

print("\nExibindo quantidade de linhas na variavel após realizar o delete das colunas")
verify_rows(correct_payments)

print("\nExcluindo os valores bruto das comissões")
correct_payments = del_internal_payments(correct_payments)

print("\nExibindo quantidade de linhas na variavel após realizar o delete dos valores de comissões brutos")
verify_rows(correct_payments)

print("\nOrdenando a variavel de pagamentos tratados")
payments_original_treated = order_variable(payments_original_treated)

print("\nOrdenando a variavel de pagamentos efetuados")
correct_payments = order_variable(correct_payments)

print("\nCriando variavel que tem os dados prontos para ser exportados")
variable_final = create_variable_final(payments_original_treated, correct_payments)

print("\nInserindo colunas na variavel final")
variable_final = insert_columns_final(variable_final)

print("\nVerificando a quantidade de linha da variavel após o insert")
verify_rows(variable_final)

print("\nCriando database .csv e inserindo os dados da variavel final")
create_table_csv(variable_final,library_new_payments_csv)