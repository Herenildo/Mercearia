from Models import *

class DaoCategoria:
    
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt','a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt','r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x:x.replace('\n','',),cls.categoria))
        

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
            
        return cat
        
        

class DaoVenda:
    @classmethod
    def salvar(cls, venda:Venda):
        with open('venda.txt', 'a') as arq:
            arq.writelines(
                venda.itensVendidos.codProduto + 
                "|" + venda.itensVendidos.descricao +
                "|" + venda.itensVendidos.preco + 
                "|" + venda.itensVendidos.categoria + 
                "|" + venda.vendedor + 
                "|" + venda.cliente + 
                "|" + str(venda.quantidadeVendida) + 
                "|" + venda.data)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n','',), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'),cls.venda))
        
        
        vend = []
        for i in cls.venda:
            vend.append(Venda(Produtos(
                i[0], 
                i[1], 
                i[2], 
                i[3]),
                i[4],
                i[5],
                i[6],
                i[7]
                ))
            
            
        return vend

class DaoEstoque:

    @classmethod
    def salvar (cls, produto:Produtos,quantidade):
        with open('estoque.txt','a') as arq:
            arq.writelines(
                produto.codProduto +
                "|" + produto.descricao +
                "|" + produto.preco + 
                "|" + produto.categoria + 
                "|" + str(quantidade))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        
        est=[]
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque
                (Produtos(
                    i[0],
                    i[1],
                    i[2],
                    i[3]),
                    i[4]))
        return est

class DaoParceiro:
    @classmethod
    def salvar(cls, parceiro:Parceiro):
        with open('parceiro.txt','a') as arq:
            arq.writelines(
                      parceiro.codParceiro +
                "|" + parceiro.nome +
                "|" + parceiro.cnpj + 
                "|" + parceiro.cpf + 
                "|" + parceiro.telefone +                
                "|" + parceiro.email +
                "|" + parceiro.endereco     
            )
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('parceiro.txt','r') as arq:
            cls.parceiro = arq.readlines()

        cls.parceiro = list(map(lambda x: x.replace('\n', ''), cls.parceiro))
        cls.parceiro = list(map(lambda x: x.split('|'), cls.parceiro))
        parc =[]
        for i in cls.parceiro:
            parc.append(Parceiro(
                i[0],
                i[1],
                i[2],
                i[3],
                i[4],
                i[5],
                i[6]
                
            ))
        print(list[parc])
        return parc
        
class DaoVendedor:
    @classmethod
    def salvar(cls,vendedor:Vendedor):
        with open('vendedor.txt', 'a') as arq:
            arq.writelines(
                parceiros.cod_vendedor + 
                "|" + parceiro.nome + 
                "|" + parceiro.telefone + 
                "|" + parceiro.email +
                "|" + parceiro.cpf + 
                "|" + parceiro.endereco)
            arq.writelines("\n")
    
    @classmethod
    def ler(cls):
        with open('vendedor.txt', 'r') as arq:
            cls.parceiro = arq.readlines()

        cls.vendedor = list(map(lambda x: x.replace('\n', ''), cls.vendedor))
        cls.vendedor = list(map(lambda x: x.split('|'), cls.vendedor))            

        vendd=[]
        for i in cls.vendedor:
            vendedor.append(vendedor(
                i[0],
                i[1],
                i[2],
                i[3],
                i[4],
                i[5]
            ))
        return vendd



DaoParceiro.ler()
