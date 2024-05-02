from Models import *
from DAO import *
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso')
        else:
            print('A categoria que deseja cadastra já existe')

    def removerCategoria(self, categoriaRemover):
        x= DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover,x))

        if len(cat) <= 0:
            print('A categoria que deseja remover não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria ==categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso')
        #TODO:COLOCAR SEN CATEGORIA NO ESTOQUE

            with open('categoria.txt','w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada,x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x))
                print('Categoria alterada com sucesso')
                #TODO: ALTERAR A CATEGORIA TAMBEM DO ESTOQUE
            else:
                print("A categoria para qual deseja alterar já existe")
        else:
            print('A categoria que deseja alterar não existe')

        with  open('categoria.txt','w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Categoria Vazia!')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')


class ControllerEstoque:
    def cadastrarProduto(self, codProduto, descricao, preco,categoria,quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()

        
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.codProduto == codProduto, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(codProduto,descricao,preco,categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso') 
            else:
                print('Produto já existe em estoque')
        else:
            print('Categoria não existe')


    def removerProduto(self,codProduto):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.codProduto == codProduto, x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.codProduto == codProduto:
                    del x[i]
                    break
            print('O produto foi removido com sucesso!')
        else:
            print('O produto não existe')

        
        with open('estoque.txt','w') as arq:
            for i in x:
                arq.writelines(
                i.produto.codProduto +
                "|" + i.produto.descricao +
                "|" + i.produto.preco + 
                "|" + i.produto.categoria + 
                "|" + str(i.quantidade))
            arq.writelines('\n')


    def alterarProduto(self, codAlterar, novoCodProduto,novoDescricao,novoCategoria,novoQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novoCategoria, y))

        if len(h) > 0:
            est = list(filter(lambda x: x.produto.codProduto == codAlterar, x)) 

            if len(est) > 0:
                est = list(filter(lambda x: x.produto.codProduto == novoCodProduto, x))       

                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novoCodProduto,novoDescricao,novoCategoria),novoQuantidade)
                    if(x.produto.codProduto == codAlterar) else(x),x))
                    print('Produto alterado com sucesso')

                else:
                    print('Produto já cadastrado')

            else:
                print('O produto que deseja alterar não existe')


        with open('estoque.txt') as arq:
            for i in x:
                arq.writelines(
                i.produto.codProduto +
                "|" + i.produto.descricao +
                "|" + i.produto.preco + 
                "|" + i.produto.categoria + 
                "|" + str(i.quantidade))
            arq.writelines('\n')
                




a = ControllerEstoque()
a.cadastrarProduto('256','caju','7','frutas','20')