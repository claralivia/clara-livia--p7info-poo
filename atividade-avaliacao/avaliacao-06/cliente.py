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
from BANCO import bancodados

class Cliente(bancodados.Molel):
    __tablename__ = 'TB_CLIENTE'
    id = bancodados.Column(bancodados.Integer, primary_key=True)
    nome = bancodados.Column(bancodados.String, nullable=False)
    codigo = bancodados.Column(bancodados.Integer, nullable=False)
    cnpjcpf = bancodados.Column(bancodados.String, nullable=False)
    tipo = bancodados.Column(bancodados.Integer, nullable=False)

    def __init__(self, id, nome, codigo, cnpjcpf, tipo):
        super().__init__(id=id, nome=nome, codigo=codigo, cnpjcpf=cnpjcpf, tipo=tipo)
        
    def str(self):
        string="\nId={4} Codigo={2} Nome={3} CNPJ/CPF={1} Tipo={0}".format(self._tipo, self._cnpjcpf, self._codigo, self._nome, self._id)
        return string
    
if __name__ == '__main__':
    cliente=Cliente(1, "Jose Maria", 100, '200.100.345-34', TipoCliente.PESSOA_FISICA)
    print(cliente.str())
        
    
