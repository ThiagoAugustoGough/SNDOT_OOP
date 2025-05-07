from models.Pessoa import Pessoa
import json

class Receptor(Pessoa):
    
    registros = []
    dict_receptores = {}
    cont_receptores = 0
    
    def __init__(self, orgao_necessario, gravidade_condicao, centro_transplante_vinculado, contato_emergencia, 
                 posicao_lista_espera, nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
                 cpf, profissao, cidade_residencia, estado_residencia, estado_civil):
        
        Receptor.cont_receptores += 1
        super().__init__(nome, idade, genero, data_nascimento, cidade_natal, estado_natal, cpf, profissao, cidade_residencia, estado_residencia, estado_civil, id = Receptor.cont_receptores)
        self._orgao_necessario = orgao_necessario
        self._gravidade_condicao = gravidade_condicao
        self._centro_transplante_vinculado = centro_transplante_vinculado
        self._contato_emergencia = contato_emergencia
        self._posicao_lista_espera = posicao_lista_espera
        self._id = f"receptor_{Receptor.cont_receptores}"
        
    @classmethod
    def cadastrar(cls, nome, idade, genero, data_nascimento, cidade_natal, estado_natal, cpf, profissao, cidade_residencia,
                  estado_residencia, estado_civil, orgao_necessario, gravidade_condicao, centro_transplante_vinculado, contato_emergencia, 
                 posicao_lista_espera):
        
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
        
        # Validar órgão necessário
        if not isinstance(orgao_necessario, str):
            raise TypeError("O órgão necessário deve ser uma string.")
        
        # Validar gravidade da condição
        if not isinstance(gravidade_condicao, str):
            raise TypeError("A gravidade da condição deve ser uma string.")
        
        # Validar centro de transplante vinculado
        if not isinstance(centro_transplante_vinculado, str):
            raise TypeError("O centro de transplante vinculado deve ser uma string.")
        
        # Validar contato de emergência
        if not isinstance(contato_emergencia, str):
            raise TypeError("O contato de emergência deve ser uma string.")
        
        # Validar posição na lista de espera
        if not isinstance(posicao_lista_espera, int):
            raise TypeError("A posição na lista de espera deve ser um número inteiro.")
        if posicao_lista_espera < 0:
            raise ValueError("A posição na lista de espera deve ser maior ou igual a 0.")
        
        receptor = Receptor(orgao_necessario, gravidade_condicao, centro_transplante_vinculado, contato_emergencia, 
                 posicao_lista_espera, nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
                 cpf, profissao, cidade_residencia, estado_residencia, estado_civil)
        
        cls.dict_receptores[receptor._id] = {
        "dados": {
            "nome": receptor._nome,
            "idade": receptor._idade,
            "sexo": receptor._genero,
            "data_nascimento": receptor._data_nascimento,
            "cidade_natal": receptor._cidade_natal,
            "estado_natal": receptor._estado_natal,
            "cpf": receptor._cpf,
            "profissao": receptor._profissao,
            "cidade_residencia": receptor._cidade_residencia,
            "estado_residencia": receptor._estado_residencia,
            "estado_civil": receptor._estado_civil,
            "contato_emergencia": receptor._contato_emergencia
        },
        "necessidade": {
            "orgao_necessario": receptor._orgao_necessario,
            "gravidade_condicao": receptor._gravidade_condicao,
            "centro_transplante": receptor._centro_transplante_vinculado,
            "posicao_lista_espera": receptor._posicao_lista_espera
        }
            }
        
        return receptor
    
    @classmethod
    def carregar_de_json(cls, json_data):
        for item in json_data:
            dados = item["dados"]
            necessidade = item["necessidade"]

            cls.cadastrar(
                nome=dados["nome"],
                idade=dados["idade"],
                genero=dados["sexo"],
                data_nascimento=dados["data_nascimento"],
                cidade_natal=dados["cidade_natal"],
                estado_natal=dados["estado_natal"],
                cpf=dados["cpf"],
                profissao=dados["profissao"],
                cidade_residencia=dados["cidade_residencia"],
                estado_residencia=dados["estado_residencia"],
                estado_civil=dados["estado_civil"],
                contato_emergencia=dados["contato_emergencia"],
                orgao_necessario=necessidade["orgao_necessario"],
                gravidade_condicao=necessidade["gravidade_condicao"],
                centro_transplante_vinculado=necessidade["centro_transplante"],
                posicao_lista_espera=necessidade["posicao_lista_espera"]
            )

    @classmethod
    def listar(cls):
        if not cls.dict_receptores:
            print("Nenhum receptor cadastrado.")
            return
        
        print(json.dumps(list(cls.dict_receptores.values()), indent=4, ensure_ascii=False))
        
    @classmethod
    def editar(cls, id, dados_ou_necessidade, campo, mudanca): # formato do dicionario (cada receptor ter campos de dados e de necessidade) fez com que seja necessario um parametro a mais
        if id in cls.dict_receptores.keys():
            cls.dict_receptores[id][dados_ou_necessidade][campo] = mudanca
        
        else:
            raise ValueError("id não foi inseriada corretamente ou nao existe")
    
    
    @classmethod
    def buscar(cls, id):
        if id in cls.dict_receptores.keys():
            print(json.dumps(cls.dict_receptores[id], indent=4, ensure_ascii=False))
        
        else:
            raise ValueError("id não foi inseriada corretamente ou nao existe")
        
    @classmethod
    def excluir(cls, id):
        if id in cls.dict_receptores.keys():
            del cls.dict_receptores[id]