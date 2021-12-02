import mysql.connector

def conexao():
    db = mysql.connector.connect(
        host="localhost",
        database="projeto_1",
        user="root",
        password="lucas26"
    )
    return db
    

def cadastro_cliente_db(db, nome, sobrenome, cpf, telefone):
    sql = 'INSERT INTO clientes (nome, sobrenome, cpf, telefone) VALUES (%s, %s, %s, %s)'
    info = (nome, sobrenome, cpf, telefone)
    try:
        cursor = db.cursor()
        cursor.execute(sql, info)
        db.commit()
        cursor.close()
        print('Registro feito!')
    except Exception as error:
        print(error)


def visualizar_clientes_db(db):
    sql = "select * from clientes"
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    except Exception as error:
        print(error)


def alterar_clientes_db(db, id, nome, cpf, sobrenome, telefone):
    info = (nome, sobrenome, cpf, telefone, id)
    sql = 'update clientes set nome = %s, sobrenome = %s, cpf = %s, telefone = %s where id = %s'
    try:
        cursor = db.cursor()
        cursor.execute(sql, info)
        db.commit()
        cursor.close()
    except Exception as error:
        print(error)
    

def deletar_clientes_db(db, id):
    sql = f'delete from clientes where id = {id}'
    try:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            cursor.close()
    except Exception as error:
        print(error)


def selecionar_clientes(db, id):
    sql = f"select * from clientes where id = {id}"
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchone()
        cursor.close
        return resultado
    except Exception as error:
        print(error)


def cadastro_pet_db(db, nome, especie, raca, idade, sexo):
    sql = 'INSERT INTO animais (nome, especie, raca, idade, sexo) VALUES (%s, %s, %s, %s, %s)'
    info = (nome, especie, raca, idade, sexo)
    try:
        cursor = db.cursor()
        cursor.execute(sql, info)
        db.commit()
        cursor.close()
        print('Registro feito!')
    except Exception as error:
        print(error)
    

def visualizar_pet_db(db):
    sql = 'select * from animais'
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    except Exception as error:
        print(error)
    

def alterar_pet_db(db, id, nome, especie, raca, idade, sexo):
    info = (nome, especie, raca, idade, sexo, id)
    sql = 'update animais set nome = %s, especie = %s, raca = %s, idade = %s, sexo = %s where id = %s'
    try:
        cursor = db.cursor()
        cursor.execute(sql, info)
        db.commit()
        cursor.close()
    except Exception as error:
        print(error)


def deletar_pet_db(db, id):
    sql = f'delete from animais where id = {id}'
    try:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            cursor.close()
    except Exception as error:
        print(error)
    

def selecionar_pet_db(db, id):
    sql = f"select * from animais where id = {id}"
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchone()
        cursor.close
        return resultado
    except Exception as error:
        print(error)
    
