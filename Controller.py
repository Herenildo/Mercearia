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


    def alterarProduto(self, codAlterar, novoCodProduto,novoDescricao,novoPreco,novoCategoria,novoQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novoCategoria, y))

        if len(h) > 0:
            est = list(filter(lambda x: x.produto.codProduto == codAlterar, x)) 

            if len(est) > 0:
                est = list(filter(lambda x: x.produto.codProduto == novoCodProduto, x))       

                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novoCodProduto,novoDescricao,novoPreco,novoCategoria),novoQuantidade) if(x.produto.codProduto == codAlterar) else(x), x))
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



class ControllerVenda:
    def cadastrarVenda(self, codProduto,nomeProduto, vendedor, comprador,quantidadeVendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False
        

        for i in x:
            if existe == False:
                if i.produto.descricao == nomeProduto:
                    existe = True
                    if int(i.quantidade) >=int(quantidadeVendida):
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                        vendido = Venda(Produtos(
                            i.produto.codProduto,
                            i.produto.descricao, 
                            i.produto.preco,
                            i.produto.categoria),
                            vendedor,
                            comprador,
                            quantidadeVendida)


                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)

                        DaoVenda.salvar(vendido)


            temp.append(Estoque(Produtos(i.produto.codProduto,i.produto.descricao, i.produto.preco,i.produto.categoria), i.quantidade))

        arq =  open('estoque.txt','w')
        arq.write('')

        for i.produtoi in temp:
            with open ('estoque.txt','a') as arq:
                arq.writelines(i.produto.codProduto +
                    "|"+ i.produto.descricao +
                    "|"+ i.produto.preco +
                    "|"+ i.produto.categoria +
                    "|"+ str(i.quantidade)
                    )

                arq.writelines('\n')

        if existe == False:
            print('O produto não existe')
            return None
        elif not quantidade:
            print('A quantidade vendida não contem em estoque')
            return None
        else:
            print('Venda cadastrada')
            return valorCompra


    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.itensVendidos.descricao
            quantidade = i.quantidadevendida
            tamanho = list(filter(lambda x: x['produto']== descricao, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': descricao,'quantidade': x['quantidade']+quantidade} 
                if (x['produto'] == descricao) else(x), produtos))
            else:
                produtos.append({'produto':descricao,'quantidade': quantidade})


            ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)

            print('Esses são os produtos mais vendidos')
            a = 1
           
            for i in ordenado:
                #print(i.['produto'], i['quantidade'])

                a += 1

#a = ControllerEstoque()
#a.cadastrarProduto('001','fruta-pao','5','Fruta',100)


b = ControllerVenda()
b.cadastrarVenda('100','fruta-pao','joao','jose',80)


                        

            
