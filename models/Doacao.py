from datetime import date

class Doacao:
    
    cont_doacao = 0
    
    def __init__(self, status):
        cont_doacao += 1
        self._status = status
        self._id = f"doacao_{cont_doacao}"
        self._data_doacao = str(date.today())
    
    @classmethod
    def registrar_doacao(cls, status):
        doacao = Doacao("y")
        return doacao