from conecxao import criar_conexao, fechar_conexao

def insere_fornecedor():
    con = criar_conexao("localhost","root","admin","estoque")
    cursor = con.cursor()
    sql = "INSERT INTO fornecedor (cnpj_fornecedor,nome_fornecedor,end_fornecedor) values (%s,%s,%s)"
    valores = 4031,"Gabriel","Ilheus"
    cursor.execute(sql,valores)
    cursor.close()
    con.commit()
    fechar_conexao(con)

def insere_tipo_pro():
    con = criar_conexao("localhost","root","admin","estoque")
    cursor = con.cursor()
    sql = "INSERT INTO tipopro (desc_tipo_produto,apagar) values (%s,%s)"
    valor = 'peza','apagar'
    cursor.execute(sql,valor)
    cursor.close()
    con.commit()
    fechar_conexao(con)

def insere_produto():
    con = criar_conexao("localhost","root","admin","estoque")
    cursor = con.cursor()
    sql ="INSERT INTO produto (desc_produto,teste) values (%s,%s)"
    valor = 'sabao','teste'
    cursor.execute(sql,valor)
    cursor.close()
    con.commit()
    fechar_conexao(con)

def insere_preco():
    con = criar_conexao("localhost","root","admin","estoque")
    cursor = con.cursor()
    sql ="INSERT INTO preco (id_produto,id_fornecedor,data_preco,vlr_unitario_prd_estoque,ativo) values (%s,%s,%s,%s,%s)"
    valores = 1,1,20221010,30,1
    cursor.execute(sql,valores)
    cursor.close()
    con.commit()
    fechar_conexao(con)

def insere_movimento():

    con = criar_conexao("localhost","root","admin","estoque")
    cursor = con.cursor()
    sql ="INSERT INTO movimento (id_produto,data_movimento,qtd_produto_estoque,tipo_movimento) values (%s,%s,%s,%s)"
    valores = 1,20221010,30,1
    cursor.execute(sql,valores)
    cursor.close()
    con.commit()
    fechar_conexao(con)

insere_movimento()

"""insere_produto()
insere_preco()
insere_tipo_pro()
def insere_preco():
    con = criar_conexao("localhost","root","admin","estoque")
    cursor = con.cursor()
    sql = "INSERT INTO preco ("")


insere_preco()"""