## FAZER UMA CLASSE PARA LIDAR COM VALIDACOES DAS INFORMACOES DE UMA FORMA MELHOR ####

## VALIDAR O JSON TAMBEM ##

## GERAR DOCSTRING PARA CADA METODO##

import re
from datetime import date, datetime

class Validacoes():
    
    estados_brasileiros = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
    "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
    "RS", "RO", "RR", "SC", "SP", "SE", "TO"
]
    
    estados_civis = [
    "solteiro",
    "casado",
    "separado judicialmente",
    "divorciado",
    "viuvo",
    "em uniao estavel"
]
    
    orgaos_necessarios = ["coração", "rins",  "fígado", "pâncreas", "pulmão", "intestino", 
                   "córneas", "pele", "ossos", "válvulas cardíacas", "cartilagem", "medula óssea", 
                   "tendões", "vasos Sanguíneos", "sangue de cordão umbilical", "sangue universal"]
    
    tipo_sanguineos = ["a+", "a-", "b+", "b-", "ab+", "ab-", "o+", "o-"]
    
    gravidade_condicoes = ["leve", "moderada", "grave", "crítica"]
    
    
    centros_de_transplante = [
    "Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador", "Fortaleza",
    "Brasília", "Vitória", "Goiânia", "São Luís", "Cuiabá", "Campo Grande",
    "Belo Horizonte", "Belém", "João Pessoa", "Curitiba", "Recife",
    "Teresina", "Rio de Janeiro", "natal", "Porto Alegre", "Porto Velho",
    "Boa Vista", "Florianópolis", "São Paulo", "Aracaju", "Palmas"
]
    
    def __init__(self):
        pass
    
    @classmethod
    def validar_nome(cls, nome):
        
        #Verifica tipo
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser uma string.")
        
        #Verifica se tem numeros na string
        if any(char.isdigit() for char in nome):
            raise ValueError("O nome nao deve conter numeros")
        
    @classmethod
    def validar_idade(cls, idade):
        
        if not isinstance(idade, int):
            raise TypeError("A idade precisa ser um valor inteiro.")
        
        if idade > 130:
            raise ValueError("A idade não pode ser maior que 130.")
        if idade < 0:
            raise ValueError("A idade nao pode ser menor que 0")
        
    @classmethod
    def validar_sexo(cls, sexo):
        
        if not isinstance(sexo, str):
            raise TypeError("O sexo deve ser uma string.")
        
        if sexo.lower() not in ['m', 'f']:
            raise ValueError("O sexo necessariamente precisa ser m ou f")
        
    @classmethod
    def validar_data_nascimento(cls, data_nascimento):
        
        padrao_data = r"^\d{2}/\d{2}/\d{4}$"
        data_hoje = date.today()
        
        if not isinstance(data_nascimento, str):
            raise TypeError("A data deve ser uma string.")
        
        if not re.match(padrao_data, data_nascimento):
            raise ValueError("A data precisa estar no formato DD/MM/AAAA")
        
        data_obj = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        
        idade = data_hoje.year - data_obj.year
        
        if (data_hoje.month, data_hoje.day) < (data_obj.month, data_obj.day):
            idade -= 1
            
        return idade
        
    @classmethod
    def validar_cidade(cls, cidade):
          
        if not isinstance(cidade, str):
            raise TypeError("A cidade natal deve ser uma string.")
        
    @classmethod
    def validar_estado(cls, estado):
        
        if not isinstance(estado, str):
            raise TypeError("O estado natal deve ser uma string como \"DF\"")
        
        if estado not in cls.estados_brasileiros:
            raise ValueError("O estado inserido nao existe ou foi inserido incorretamente")
        
    @classmethod
    def validar_cpf(cls, cpf):
        
        if not isinstance(cpf, str):
            raise TypeError("O CPF deve ser uma string.")
        
        cpf = re.sub(r'[^0-9]', '', cpf)
        
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            raise ValueError("O CPF precisa conter 11 caracteres")
        
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10 % 11) % 10
        
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10 % 11) % 10
        
        if cpf[-2:] != f"{digito1}{digito2}":
            raise ValueError("CPF invalido, verifique se foi inserido corretamente")
        
    @classmethod
    def validar_profissao(cls, profissao):
        
        if not isinstance(profissao, str):
            raise TypeError("A profissão deve ser uma string.")
        
    @classmethod
    def valiar_estado_civil(cls, estado_civil):
        
        if not isinstance(estado_civil, str):
            raise TypeError("O estado civil deve ser uma string.")
        
        if estado_civil.lower() not in cls.estados_civis:
            raise ValueError("O estado civil inserido nao eh valido")
        
    @classmethod
    def validar_telefone(cls, telefone):
        pass
        # telefone = telefone.strip()
        # telefone_normalizado = re.sub(r"[^\d]", "", telefone)
        # padrao = re.compile(r"^(55)?\d{10,11}$")
        
        # if not padrao.match(telefone_normalizado):
        #     raise ValueError("O telefone nao foi inserido corretamente")
        
    @classmethod
    def validar_orgao(cls, orgao):
        
        if not isinstance(orgao, str):
            raise TypeError("O órgão necessário deve ser uma string.")
        
        if orgao.lower() not in cls.orgaos_necessarios:
            raise ValueError("Orgao inserido nao esta na lista de orgaos")
        
    @classmethod
    def validar_gravidade(cls, gravidade_condicao):
        
        if not isinstance(gravidade_condicao, str):
            raise TypeError("A gravidade da condição deve ser uma string.")
        
        if gravidade_condicao.lower() not in cls.gravidade_condicoes:
            raise ValueError("Gravidade inserido nao esta na lista de gravidades")
        
    @classmethod
    def validar_centro_transplante(cls, centro):
        
        if not isinstance(centro, str):
            raise TypeError("O centro de transplante vinculado deve ser uma string.")
        
        if centro not in cls.centros_de_transplante:
            raise ValueError("O centro de transplante inserido não foi econtrado na lista de centros de transplantes")
        
    
        
        
        
        
        
        
        
        
        
        
        