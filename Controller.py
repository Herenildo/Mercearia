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

        estoque = DaoEstoque.ler()

        estoque = list(map(lambda x: Estoque(Produtos(x.produtos.nome, x.produtos.descricao,x.produtos.preco,"Sem categoria"),x.quantidade)
                            if(x.produtos.categoria == categoriaRemover) else (x), estoque ))


        with open ('estoque.txt','w') as arq:
            for i in estoque:
                arq.writelines(
                i.produto.codProduto +
                "|" + i.produto.descricao +
                "|" + i.produto.preco + 
                "|" + i.produto.categoria + 
                "|" + str(i.quantidade))
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




        estoque = DaoEstoque.ler()

        estoque = list(map(lambda x: Estoque(Produtos(x.produtos.nome, x.produtos.descricao,x.produtos.preco,categoriaAlterar),x.quantidade)
                            if(x.produtos.categoria == categoriaAlterar) else (x), estoque ))


        with open ('estoque.txt','w') as arq:
            for i in estoque:
                arq.writelines(
                i.produto.codProduto +
                "|" + i.produto.descricao +
                "|" + i.produto.preco + 
                "|" + i.produto.categoria + 
                "|" + str(i.quantidade))
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


    def relatorioVendas(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.itensVendidos.descricao
            quantidade = i.quantidadeVendida
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
                print(f'+++++++++++++Produto[{a}]+++++++++++++')
                print(f"{i['produto']} -> {i['quantidade']}\n")
                a += 1


    def mostrarVenda(self, dataInicio,dataTermino):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1
                                    and datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino1, vendas ))

        print(f"VendasSelecionadas: {vendasSelecionadas}")                            
        if len(vendas) == 0:
            print('Naõ existe vendas no periodo solitado.')
        else:
            cont = 1
            total = 0



            
            for i in vendasSelecionadas:
                print(f"{cont} -> {i.data} -> {i.itensVendidos.codProduto} |-> {i.itensVendidos.descricao} |-> Valor: {int(i.itensVendidos.preco)} |-> Quant.: {int(i.quantidadeVendida)} Total: {int(i.itensVendidos.preco) * int(i.quantidadeVendida)}") 
                total += (int(i.itensVendidos.preco) * int(i.quantidadeVendida))
                cont += 1      

        print(f"Total Vendido: {total}")


class ControllerParceiro:
    def cadastrarParceiro(self,codParceiro,nome,cnpj,cpf, telefone,email,endereco):
        x = DaoParceiro.ler()

        a = list(filter(lambda x: x.cnpj == cnpj, x))
        
        if len(a) == 0:
            
            parceiro = Parceiro(codParceiro, nome, cnpj, cpf, telefone, email, endereco)
            DaoParceiro.salvar(parceiro)
            
            print('Parceiro cadastrado com sucesso')
        else:
            print('Parceiro ja cadastrado')

    def removerParceiro(self, cnpj):
        x = DaoParceiro.ler()

    # Filtrando os parceiros com o CNPJ fornecido
        buscacnpj = list(filter(lambda p: p.cnpj == cnpj, x))

        if buscacnpj:
        # Criando uma nova lista sem os parceiros com o CNPJ fornecido
            x = [p for p in x if p.cnpj != cnpj]
        
        # Escrevendo a nova lista no arquivo
            with open('parceiro.txt', 'w') as arq:
                for parceiro in x:
                    arq.write(
                        parceiro.codParceiro + "|" + 
                        parceiro.nome + "|" + 
                        parceiro.cnpj + "|" + 
                        parceiro.cpf + "|" + 
                        parceiro.telefone + "|" + 
                        parceiro.email + "|" + 
                        parceiro.endereco + "\n"
                    )

            print('Parceiro removido com sucesso')
        else:
            print('Parceiro não encontrado')

    


    def alterarParceiro(self,alterarCnpj,novocodParceiro,novoNome,novoCnpj,novoCpf,novoTelefone,novoEmail,novoEndereco):
        x = DaoParceiro.ler()

        p = list(filter(lambda x: x.cnpj == alterarCnpj, x))

        if len(p) > 0:
            altParc = list(filter(lambda x: x.cnpj == novoCnpj,x))

            if len(altParc) == 0:
                x = list(map(lambda x: Parceiro(novocodParceiro,novoNome,novoCnpj,novoCpf,novoTelefone,novoEmail,novoEndereco) if (x.cnpj == alterarCnpj) else(x),x))
                print("Parceiro alterado com sucesso")
                

            else:
                print("CNPJ ja cadastrado")

        else:
            print("CNPJ não encontrado")


        with open('parceiro.txt', 'w') as arq:
                for parceiro in x:
                    arq.write(
                        parceiro.codParceiro + "|" + 
                        parceiro.nome + "|" + 
                        parceiro.cnpj + "|" + 
                        parceiro.cpf + "|" + 
                        parceiro.telefone + "|" + 
                        parceiro.email + "|" + 
                        parceiro.endereco + "\n"
                    )

    def mostrarParceiros(self):

        with open('parceiro.txt', 'r') as arq:
            for linha in arq:
                # Dividindo a linha em partes separadas pelo caractere '|'
                partes = linha.strip().split('|')
                # Extraindo as informações de cada parte
                codParceiro, nome, cnpj, cpf, telefone, email, endereco = partes
                # Exibindo as informações do parceiro
                print(f"Código do Parceiro: {codParceiro}")
                print(f"Nome: {nome}")
                print(f"CNPJ: {cnpj}")
                print(f"CPF: {cpf}")
                print(f"Telefone: {telefone}")
                print(f"Email: {email}")
                print(f"Endereço: {endereco}")
                print()  # Adicionando uma linha em branco entre os parceiros


class ControllerVendedor:
    def cadastrarVendedor(self,cod_vendedor,nome, telefone,email,cpf,endereco):
        x = DaoVendedor.ler()
        a = list(filter(lambda x: x.cpf == cpf,x))
        if len(a) == 0:
            vendedor = Vendedor(cod_vendedor,nome, telefone,email,cpf,endereco)
            DaoVendedor.salvar(vendedor)
            print('Vendedor cadastrado com sucessso')
        else:
            print('Vendedor ja cadastrado')

            
    def removerVendedor(self, cpf):
        x = DaoVendedor.ler()
        buscavend = list(filter(lambda x: x.cpf == cpf, x))
        
        if buscavend:
            x = [v for v in x if v.cpf != cpf]

            with open('vendedor.txt','w') as arq:
                for vendedor in x:
                    arq.writelines(
                        vendedor.cod_vendedor + "|"+
                        vendedor.nome + "|"+
                        vendedor.telefone + "|"+
                        vendedor.email + "|"+
                        vendedor.cpf + "|"+
                        vendedor.endereco + "\n"
                    )

            print('Vendedor removido com sucesso')
        else:
            print('Vendedor não encontrado')



    def alterarVendedor(self,alterarCpf,novocod_vendedor,novoNome, novoTelefone,novoEmail,novoCpf,novoEndereco):
        x = DaoVendedor.ler()

        v = list(filter(lambda x: x.cpf == alterarCpf,x))

        if len(v) > 0:
            altvend = list(filter(lambda x: x.cpf == novoCpf, x))

            if len(altvend) == 0:
                x = list(map(lambda vendedor : Vendedor(novocod_vendedor,novoNome, novoTelefone,novoEmail,novoCpf,novoEndereco) if (vendedor.cpf == alterarCpf) else(vendedor),x))
                print("Vendedor alterado com sucesso")

            
                with open('Vendedor.txt', 'w') as arq:
                    for vendedor in x:
                        arq.writelines(
                        vendedor.cod_vendedor + "|"+
                        vendedor.nome + "|"+
                        vendedor.telefone + "|"+
                        vendedor.email + "|"+
                        vendedor.cpf + "|"+
                        vendedor.endereco + "\n"
                    )

            else:

                print('Vendedor não cadastrado')






#a = ControllerVendedor()
#a.alterarParceiro('2222','33333','Nyotech','88888','11111','071333','rrr@gg.com','rua teste')

#a.alterarVendedor('54454','C0008','Danadinho','7778999','passepasse@oiko.com','55555','Rua de baixo')

                        

            
