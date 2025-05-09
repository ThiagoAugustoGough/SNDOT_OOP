from datetime import date
from models.Doador import Doador
from models.Receptor import Receptor
import json
        
class Doacao:
    
    cont_doacao = 0
    dict_doacoes = {}
    
    def __init__(self, status, doador: Doador, receptor: Receptor):
        Doacao.cont_doacao += 1
        self._status = status
        self._id = f"doacao_{self.cont_doacao}"
        self._data_doacao = str(date.today())
        self._doador = doador._nome
        self._receptor = receptor._nome
    
    @classmethod
    def registrar_doacao(cls, status, doador: Doador, receptor: Receptor):
        doacao = Doacao(status, doador, receptor)
        
        cls.dict_doacoes[doacao._id] = {
            "status": status,
            "doador": doador._id,
            "receptor": receptor._id
        }
        return doacao
    
    @classmethod
    def listar_doacoes(cls):
        
        print(json.dumps(list(cls.dict_doacoes.values()), indent=4, ensure_ascii=False))