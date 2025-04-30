from datetime import date
import json

class IntencaoDeDoar():
    
    dict_intencao = {}
    intid = 0
    
    def __init__(self, status):
        IntencaoDeDoar.intid += 1
        self._id = f"intencao_{IntencaoDeDoar.intid}"
        self._data_intencao = str(date.today())
        self._status = status
        
    @classmethod
    def registrar_intencao_doar(cls, status):
        intencao = IntencaoDeDoar(status)
        cls.dict_intencao[intencao._id] = {
                "status" : intencao._status,
                "data_intencao" : str(date.today()) 
        }
    
        return intencao
    
    @classmethod
    def listar(cls):
        if not cls.dict_intencao:
            print("Nenhum doador cadastrado.")
            return
        
        print(json.dumps(list(cls.dict_intencao.items()), indent=4, ensure_ascii=False))