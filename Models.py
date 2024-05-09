from datetime import datetime, date

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria


class Produtos:
    def __init__(self, codProduto, descricao, preco, categoria):
        self.codProduto = codProduto 
        self.descricao = descricao
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto:Produtos,quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    def __init__(self, itensVendidos:Produtos, vendedor, cliente, quantidadeVendida, data = datetime.now().strftime("%d/%m/%Y")):
        self.itensVendidos = itensVendidos
        self.vendedor = vendedor
        self.cliente = cliente
        self.quantidadeVendida = quantidadeVendida
        self.data = data


class Parceiro:
    def __init__(self, codParceiro,nome,cnpj,cpf, telefone, email,endereco):
        self.codParceiro = codParceiro
        self.nome = nome
        self.cnpj = cnpj
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        

class Vendedor():
    def __init__(self,cod_vendedor,nome, telefone,email,cpf,endereco):
        self.cod_vendedor = cod_vendedor
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.endereco = endereco



