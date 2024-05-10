import Controller
import os.path

def criarArquivos(*nome):
    for i in nome:
        if  not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write('')


criarArquivos("categoria.txt",
            "parceiros.txt",
            "estoque.txt",
            "venda.txt",
            "vendedor.txt")


if __name__ == "__main__":
    while True:
        local = int(input(
            "Digite 1 para acessar ( Categorias )\n"
            "Digite 2 para acessar ( Estoque)\n"
            "Digite 3 para acessar ( Parceiro ) \n"
            "Digite 4 para acessar ( Vendedor ) \n"
            "Digite 5 para acessar ( Vendas ) \n"
            "Digite 6 para sair \n"

        ))


    if local ==1:
        cat = Controller.ControllerCategoria()
        while True:
            decidir = int(input(
                "Digite 1 para cadastrar uma categoria\n"
                "Digite 2 para remover uma categoria\n"
                "Digite 3 para alterar uma categoia \n"
                "Digite 4 para listar as categorias cadastradas\n"
                "Digite 5 para sair\n"
            ))
            if decidir == 1:
                categoria = input("Digite a categoria que deseja cadastrar\n")
                cat.cadastrarCategoria(categoria)
            elif decidir == 2:
                categoria = input("Digite a categoria que deseja remover\n")
                cat.removerCategoria(categoria)
            elif decidir == 3:
                categoria = input("Digite a categoria que deseja alterar\n")
                categoriaNova = input("Digite a nova categoria\n")
                cat.alterarCategoria(categoria, categoriaNova)
            elif decidir == 4:
                cat.listarCategoria()
            elif decidir == 5:
                break



    if local == 2:
        estoque = Controller.ControllerEstoque()
        while True:
            decidir = int(input(
                "Digite 1 para cadastrar um produto\n"
                "Digite 2 para remover um produto\n"
                "Digite 3 para alterar um produto \n"
                "Digite 4 para listar os produtos cadastrados\n"
                "Digite 5 para sair\n"
                ))


            if decidir == 1:
                codProduto = input("Digite o codigo do produto\n")
                descricao = input("Digite a descrição do produto\n")
                preco = input("Digite o preco do produto\n")
                categoria = input("Digite a categoria do produto\n")
                quantidade = input("DIgite a quantidade para o produto\n")
                cat.cadastraCategoria(codProduto,descricao,preco,categoria,quantidade)
            
            elif decidir == 2:
                
                codProduto = input("Digite o codigo do produto que deseja remover\n")
                cat.removerProduto(codProduto)
            
            elif decidir == 3:
                
                codAlterar = input("Digite o codigo do Produto que deseja alterar\n")
                novoCodProduto = input("Digite o novo codigo para o produto\n")
                novoDescricao = input("Digite uma nova descrição para o produtro\n")
                novoPreco = input("Digite um novo preço para o produto\n")
                novoCategoria = input("Digite uma nova categoria para o produtoa\n")
                novoQuantidade = input("Digite uma quantidade para o produto\n")
                cat.alterarProduto(codAlterar,codProduto,novoDescricao,novoPreco,novoCategoria,novoQuantidade)


            elif decidir == 4:
                cat.listarProdutos()

            elif decidir == 5:
                break


    if local == 3:
        produtos = Controller.ControllerParceiro()

        while True:
            decidir = input("Digite 1 para cadastrar um novo parceiro\n")
            decidir = input("Digite 2 para remover parceiro\n")
            decidir = input("Digite 3 para alterar um parceiro\n")
            decidir = input("Digite 4 para listar os parceiros\n")
            decidir = input("Digite 5 para Sar\n")
            if decidir == 1:
                codParceiro = input("Digite o codigo do parceiro\n")
                nome = input("Digite o nome do parceiro\n")
                cnpj = input("Digite o CNPJ do Parceiro\n")
                cpf = input("Digite o CPF do parceiro\n")
                telefone = input("Digite o telefone do parceiro\n")
                email = input("Digite o email do parceiro\n")
                endereco = input("Digite o endereço do parceiro\n")
                cat.cadastrarParceiro(codParceiro,nome,cnpj,cpf,telefone,email,endereco)

            if decidir == 2:
                codRemover = input("Digite o codigo do parceiro que deseja remover\n")
                cat.removerParceiro(codRemover)

            if decidir == 3:
                codAlterar = input("Digite o codigo do parceiro que deseja alterar\n")
                novocodParceiro = input("Digite o novo codigo para o parceiro\n")
                novoNome = input("Digite o novo nome para o parceiro\n")
                novoCnpj = input("Digite o novo CNPJ para o parceiro\n")
                novoCpf = input("Digite o novo CPF para o parceiro\n")
                novoTelefone = input("Digite um novo telefone para o parceiro\n")
                novoEmail = input("Digite um novo email para o parceiro\n")
                novoEndereco = input("Digite um novo endereço para o parceiro\n")
                cat.alterarParceiro(codAlterar,novocodParceiro,novoNome,novoCnpj,novocpf,novoTelefone,novoEmail,novoEndereco)

            if decidir == 4:
                cat.listarParceiro()

            if decidir == 5:
                break

        if local == 4:
            while True:
                decidir = input("Digite 1 para cadastrar um Vendedor\n")
                decidir = input("Digite 2 para remover um Vendedor\n")
                decidir = input("Digite 3 para alterar o cadastro de um vendedor\n")
                decidir = input("Digite 4 para listar os vendedores cadastradosa\n")
                decidir = input("Digite 5 para Sar\n")
                if decidir == 1:
                    cod_vendedor = input("Digite um codigo para o vendedor\n")
                    nome = input("Digite o nome do vendedor\n")
                    telefone = input("Digite o numero de Telefone para o vendedor\n")
                    email = input("Digite o email do vendedor\n")
                    endereco = input("Digite o endereço para o Vendedor\n")
                    cat.cadastrarVendedor(cod_vendedor,nome,telefone,email,endereco)
                if decidir == 2:
                    cpf = input("Digite o numero do cpf do vendedor que deseja remover\n")
                    cat.removerVendedor(cpf)
                if decidir == 3:
                    alterarVendedor = input("Digite o codigo do vendedor que deseja alterar\n")
                    novoCodVendedor = input("Digite o novo codigo para o vendedor\n")
                    novoNome = input("Digite o novo nome do Vendedor\n")
                    novoTelefone = input("Digite o novo telefone para o vendedor\n")
                    novoEmail = input("Digite o novo email para o vendedor\n")
                    novocpf = input("Digite o novo cpf para o vendedor\n")
                    novoEndereco = input("Digite o novo endereço do vendedor\n")
                    cat.alterarVendedor(alterarVendedor,novoNome,novoTelefone,novoEmail,novoCpf,novoEndereco)

                if decidir == 4:
                    cat.listarVendedor()

                if decidir == 5:
                    break

            if local == 5:
                while True:
                    decidir = input("Digite 1 para cadastrar uma venda\n")
                    decidir = input("Digite 2 para o relatorio de vendas\n")
                    decidir = input("Digite 3 para listar as vendas do periodo\n")
                    decidir = input("Digite 4 para Sair\n")
                    if decidir == 1:
                        codProduto = input("Digite o codigo do produto para venda\n")
                        nomeProduto = input("Digite a descrição do produto para venda\n")
                        vendedor = input("Digite o nome do vendedor\n")
                        comprador = input("Digite o nome do Cliente\n")
                        quantidadeVendida = input("Digite a quantidade vendida\n")
                        cat.cadastrarVenda(codProduto,nomeProduto,vendedor,comprador,quantidadeVendida)
                    if decidir == 2:
                        cat.relatorioVendas()
                    if decidir == 3:
                        dataInicial = input("Digite a data inicial\n")
                        dataFinal = input("Digite a data final\n")
                        cat.listarVendasPeriodo(dataInicial,dataFinal)
                    if decidir == 4:
                        break

            if local == 6:
                break
                





        
                   




                

