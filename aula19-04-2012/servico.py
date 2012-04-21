from SOAPpy import SOAPServer

produtos = {"codigo":"0001","descricao":"Coca-Cola","preco":"3.80","saldo":"50","estoque":"1"}

def saldoProduto(codigo,estoque):
    if produtos["codigo"] == codigo and produtos["estoque"] == estoque:
        return produtos["saldo"]
    else:
        return "Produto inexistente!"

def descricaoProduto(codigo):
    if produtos["codigo"] == codigo:
        return produtos["descricao"]
    else:
        return "Produto inexistente!"

def precoProduto(codigo):
    if produtos["codigo"] == codigo:
        return produtos["preco"]
    else:
        return "Produto inexistente!"

server = SOAPServer(("localhost", 8080))

server.registerFunction(saldoProduto)
server.registerFunction(descricaoProduto)
server.registerFunction(precoProduto)

server.serve_forever()
