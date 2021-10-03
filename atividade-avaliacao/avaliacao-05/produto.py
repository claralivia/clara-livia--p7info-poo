"""
    Módulo produto
    Classe Produto
    Atributos :
        id            - informado
        codigo        - informado
        descricao     - informado
        valorUnitario - informado. 
"""
class Produto():

    def __init__(self, id, codigo, descricao, valorUnitario):
        self._id = id
        self._codigo=codigo
        self._descricao=descricao
        self._valorUnitario=valorUnitario
        
    def getDescricao(self):
        return self._descricao
    
    def getValorUnitario(self): 
        return self._valorUnitario
        
    def str(self):
        string="\nId={3} Codigo={2} Descricao={1} Valor Unitario={0}".format(self._valorUnitario, self._descricao, self._codigo, self._id)
        return string
    
   
    
if __name__ == '__main__':
    produto=Produto(1,100,'Arroz', 5.5)        
    print(produto.str())
        
        
