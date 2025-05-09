from datetime import date
import json

class IntencaoDeDoar():
    
    """
    Representa a intenção de uma pessoa em doar um órgão.
    Gerencia o armazenamento e registro de intenções em memória.
    """
    
    dict_intencao = {}
    intid = 0
    
    def __init__(self, status, orgao):
        """
        Inicializa uma nova intenção de doação com status, órgão e data atual.

        Args:
            status (str): Status da intenção (e.g., "ativo", "pendente").
            orgao (str): Órgão que o doador deseja doar.
        """
        
        IntencaoDeDoar.intid += 1
        self._id = f"intencao_{IntencaoDeDoar.intid}"
        self._data_intencao = str(date.today())
        self._status = status
        self._orgao = orgao
        
    @classmethod
    def registrar_intencao_doar(cls, status, orgao):
        
        """
        Registra uma nova intenção de doação e a armazena no dicionário da classe.

        Args:
            status (str): Status da intenção de doação.
            orgao (str): Órgão a ser doado.

        Returns:
            IntencaoDeDoar: Instância criada com os dados fornecidos.
        """
        
        intencao = IntencaoDeDoar(status, orgao)
        cls.dict_intencao[intencao._id] = {
                "status" : intencao._status,
                "data_intencao" : str(date.today()),
                "orgao" : intencao._orgao
        }
    
        return intencao
    
    @classmethod
    def listar(cls):
        """
        Exibe todas as intenções de doação cadastradas em formato JSON formatado.
        Informa se não houver intenções registradas.
        """
        
        if not cls.dict_intencao:
            print("Nenhum doador cadastrado.")
            return
        
        print(json.dumps(list(cls.dict_intencao.items()), indent=4, ensure_ascii=False))