"""
    Módulo cliente -
    Classe Cliente - 
    Atributos:
        _id       - chave primária    - informado
        _nome     - nome do cliente   - informado
        _codigo   - codigo do cliente - informado
        _cnpjcpf  - cnpj ou cpf       - informado
        _tipo     - tipo do cliente   - informado
                    (Pessoa Fisica ou Juridica)
        
"""

from tipocliente  import TipoCliente

class Cliente():
    def __init__(self, id, nome, codigo, cnpjcpf, tipo):
        self._id = id
        self._nome = nome
        self._codigo = codigo
        self._cnpjcpf = cnpjcpf
        self._tipo = tipo
        
    def str(self):
        string="\nId={4} Codigo={2} Nome={3} CNPJ/CPF={1} Tipo={0}".format(self._tipo,
                                                                           self._cnpjcpf,
                                                                           self._codigo,
                                                                           self._nome,
                                                                           self._id)
        return string
    
if __name__ == '__main__':
    cliente=Cliente(1, "José Simão da Silva", 1234, "200.100.345-34", TipoCliente.PESSOA_FISICA)
    print(cliente.str())
        
    
