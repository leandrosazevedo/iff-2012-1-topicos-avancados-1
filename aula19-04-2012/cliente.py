# encoding: utf-8
#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
proxy = SOAPProxy("http://localhost:8080")

print str(proxy.saldoProduto("0001","1"))
print str(proxy.descricaoProduto("0001"))
print str(proxy.precoProduto("0001"))

print str(proxy.saldoProduto("0001","2"))
print str(proxy.descricaoProduto("0002"))
print str(proxy.precoProduto("0002"))
