from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade, genero, data_nascimento, cidade_natal,
                 estado_natal, cpf, profissao, cidade_residencia, estado_residencia,
                 estado_civil, id):        
        
        self._nome = nome
        self._idade = idade
        self._genero = genero
        self._data_nascimento = data_nascimento
        self._cidade_natal = cidade_natal
        self._estado_natal = estado_natal
        self._cpf = cpf
        self._profissao = profissao
        self._cidade_residencia = cidade_residencia
        self._estado_residencia = estado_residencia
        self._estado_civil = estado_civil
        
    @abstractmethod
    def cadastrar():
        pass
    
    @abstractmethod
    def listar():
        pass
    
    @abstractmethod
    def editar():
        pass
    
    @abstractmethod
    def buscar():
        pass
    
    @abstractmethod
    def excluir():
        pass