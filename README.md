MANIPULAÇÕES DE DADOS PARA ENCONTRAR DIVERGÊNCIAS EM PAGAMENTOS.

O projeto analisa duas tabelas .csv que estão armazenadas dentro da pasta
'data_raw', no qual uma está preenchida com dados referente a vendas de
vendedores com o nome de 'vendas.csv', e o outro arquivo armazena dados de
pagamentos aos vendedores referente às comissões sobre as vendas Intitulado de
'pagamentos.csv'.

FUNCIONALIDADES

O projeto tem dois pipelines de dados que se encontram dentro da pasta 'scripts',
no qual o denominado de nome 'table_comissao.py' analisa os dados do arquivo
.csv que tem as vendas e gera um novo arquivo .csv que tem as colunas de nome
dos vendedores, comissões sem descontos e o valor a ser pago.

O segundo arquivo, denominado 'table_payments.py', é um pipeline que compara os
dados do arquivo 'pagamentos.csv', identificando as diferenças nos pagamentos
e criando um novo arquivo .csv que tem as colunas com os nomes dos vendedores,
o valor pago incorretamente e o valor que deveria ter sido pago. 

O resultado dos pipelines de dados se encontram dentro da pasta 'data_processed'

INSTALAÇÕES

Para rodar o projeto, é necessário instalações de métodos, os requisitos estão
expostos no arquivo 'requirements.txt'

PASSO A PASSO

1° Clone o repositório:

git clone https://github.com/Flavio-Luis/generate-table-docx.git

2° Navegue até o diretório do projeto:

cd name_library

3° Instale as dependências:

pip install -r requirements.txt