from models.Pessoa import Pessoa
import json

class Doador(Pessoa):
    
    registros = []
    dict_doadores = {}
    cont_doadores = 0
    
    def __init__(self, contato_emergencia, tipo_sanguineo, 
                 nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
                 cpf, profissao, cidade_residencia, estado_residencia, estado_civil):
        
        Doador.cont_doadores += 1
        super().__init__(nome, idade, genero, data_nascimento, cidade_natal, estado_natal, cpf, profissao, cidade_residencia, estado_residencia, estado_civil, id = Doador.cont_doadores)
        self._contato_emergencia = contato_emergencia
        self._tipo_sanguineo = tipo_sanguineo
        self._id = f"doador_{Doador.cont_doadores}"
        
    @classmethod
    def cadastrar(cls, nome, idade, genero, data_nascimento, cidade_natal, estado_natal, cpf, profissao, cidade_residencia,
                  estado_residencia, estado_civil, contato_emergencia, tipo_sanguineo, intencao):
        
        #validar nome
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser uma string.")
        
        #validar idade
        if not isinstance(idade, int):
            raise TypeError("A idade precisa ser um valor inteiro.")
        if idade < 0:
            raise ValueError("A idade precisa ser maior que 0.")
        
        #validar genero
        if not isinstance(genero, str):
            raise TypeError("O genero deve ser uma string.")
        
        #validar data
        if not isinstance(data_nascimento, str):
            raise TypeError("A data deve ser uma string.")
        
        if not isinstance(cidade_natal, str):
            raise TypeError("A cidade natal deve ser uma string.")
        
        # Validar estado natal
        if not isinstance(estado_natal, str):
            raise TypeError("O estado natal deve ser uma string.")
        
        # Validar CPF
        if not isinstance(cpf, str):
            raise TypeError("O CPF deve ser uma string.")
        
        # Validar profissão
        if not isinstance(profissao, str):
            raise TypeError("A profissão deve ser uma string.")
        
        # Validar cidade de residência
        if not isinstance(cidade_residencia, str):
            raise TypeError("A cidade de residência deve ser uma string.")
        
        # Validar estado de residência
        if not isinstance(estado_residencia, str):
            raise TypeError("O estado de residência deve ser uma string.")
        
        # Validar estado civil
        if not isinstance(estado_civil, str):
            raise TypeError("O estado civil deve ser uma string.")
        
        # Validar contato de emergência
        if not isinstance(contato_emergencia, str):
            raise TypeError("O contato de emergência deve ser uma string.")
        
        doador = Doador(contato_emergencia, tipo_sanguineo, nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
                 cpf, profissao, cidade_residencia, estado_residencia, estado_civil)
        
        cls.dict_doadores[doador._id] = {
        "dados": {
            "nome": doador._nome,
            "idade": doador._idade,
            "sexo": doador._genero,
            "data_nascimento": doador._data_nascimento,
            "cidade_natal": doador._cidade_natal,
            "estado_natal": doador._estado_natal,
            "cpf": doador._cpf,
            "profissao": doador._profissao,
            "cidade_residencia": doador._cidade_residencia,
            "estado_residencia": doador._estado_residencia,
            "estado_civil": doador._estado_civil,
            "contato_emergencia": doador._contato_emergencia
        },
        "intencao": {
            "status" : intencao._status,
            "data" : intencao._data_intencao
        }
            }
        
        return doador
    
    @classmethod
    def listar(cls):
        if not cls.dict_doadores:
            print("Nenhum doador cadastrado.")
            return
        
        print(json.dumps(list(cls.dict_doadores.values()), indent=4, ensure_ascii=False))
        
    @classmethod
    def editar(cls, id, dados_ou_intencao, campo, mudanca): # formato do dicionario (cada doador ter campos de dados e de intencao) fez com que seja necessario um parametro a mais
        if id in cls.dict_doadores.keys():
            cls.dict_doadores[id][dados_ou_intencao][campo] = mudanca
        
        else:
            raise ValueError("id não foi inseriada corretamente ou nao existe")
    
    
    @classmethod
    def buscar(cls, id):
        if id in cls.dict_doadores.keys():
            print(json.dumps(cls.dict_doadores[id], indent=4, ensure_ascii=False))
        
        else:
            raise ValueError("id não foi inseriada corretamente ou nao existe")
        
    @classmethod
    def excluir(cls, id):
        if id in cls.dict_receptores.keys():
            del cls.dict_receptores[id]
        
    @property    
    def getID(self):
        return self._id