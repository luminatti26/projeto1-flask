'''projeto de adoção

1 - cadastro de pessoas
2 - cadastro de pets (caso seja para doar um pet)
3 - selecionar um pet (caso seja para adotar um pet)

'''
from flask import Flask, render_template, request, redirect
from repositorio import cadastro_cliente_db, visualizar_clientes_db, alterar_clientes_db, deletar_clientes_db, selecionar_clientes
from repositorio import conexao, cadastro_pet_db, visualizar_pet_db, alterar_pet_db, deletar_pet_db, selecionar_pet_db

projeto = Flask(__name__)

@projeto.route("/")
def pag_inicial():
    db = conexao()
    lista_pet = visualizar_pet_db(db)
    return render_template("index.html", lista_pet_db= lista_pet)


@projeto.route("/cadastro")
def pag_cadastro():
    return render_template("cadastro.html") 


@projeto.route("/doação")
def pag_doacao():
    db = conexao()
    lista_pet = visualizar_pet_db(db)
    return render_template("doação.html", lista_pet_db= lista_pet)


@projeto.route("/clientes")
def pag_clientes():
    db = conexao()
    lista_clientes = visualizar_clientes_db(db)
    return render_template("clientes.html", lista_clientes_db= lista_clientes)
    

@projeto.route("/animais")
def pag_animais():
    db = conexao()
    lista_pet = visualizar_pet_db(db)
    return render_template("animais.html", lista_pet_db= lista_pet)


@projeto.route("/salvar/cliente", methods=["POST"])
def salvar_cliente():
    db = conexao()
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    cpf = request.form["cpf"]
    telefone = request.form["telefone"]
    cadastro_cliente_db(db, nome, sobrenome, cpf, telefone)
    return redirect("/clientes")

@projeto.route("/salvar/doacao", methods=["POST"])
def salvar_animal():
    db = conexao()
    nome = request.form["nome"]
    especie = request.form["especie"]
    raca = request.form["raca"]
    idade = request.form["idade"]
    sexo = request.form["sexo"]
    cadastro_pet_db(db, nome, especie, raca, idade, sexo)
    return redirect("/")


@projeto.route("/deletarcliente")
def deletar_cliente():
    db = conexao()
    id = int(request.args["id"])
    deletar_clientes_db(db, id)
    return redirect("/clientes")


@projeto.route("/deletarpet")
def deletar_pet():
    db = conexao()
    id = int(request.args["id"])
    deletar_pet_db(db, id)
    return redirect("/")

@projeto.route("/atualizarcliente")
def pag_atualizar_cliente():
    db = conexao()
    id = int(request.args["id"])
    registro = selecionar_clientes(db, id)
    return render_template("atualizar_clientes.html", id=registro[0], nome=registro[1], sobrenome=registro[2], cpf=registro[3], telefone=registro[4])

@projeto.route("/atualizarcliente/salvar", methods=["POST"])
def atualizar_cliente():
    db = conexao()
    id = request.form["id"]
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    cpf = request.form["cpf"]
    telefone = request.form["telefone"]
    alterar_clientes_db(db, id, nome, sobrenome, cpf, telefone)    
    return redirect("/clientes")


@projeto.route("/atualizarpet")
def pag_atualizar_pet():
    db = conexao()
    id = int(request.args["id"])
    registro = selecionar_pet_db(db, id)
    return render_template("atualizar_animais.html", id=registro[0], nome=registro[1], especie=registro[2], raca=registro[3], idade=registro[4])

@projeto.route("/atualizarpet/salvar", methods=["POST"])
def atualizar_pet():
    db = conexao()
    id = int(request.form["id"])
    nome = request.form["nome"]
    especie = request.form["especie"]
    raca = request.form["raca"]
    idade = request.form["idade"]
    sexo = request.form["sexo"]
    alterar_pet_db(db, id, nome, especie, raca, idade, sexo)   
    return redirect("/animais")


projeto.run(debug=True)
