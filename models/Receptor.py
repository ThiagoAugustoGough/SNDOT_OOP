from models.Pessoa import Pessoa
from models.Validacoes import Validacoes
import json

class Receptor(Pessoa):
    
    """
    Classe que representa um receptor no sistema de transplantes, herdando de Pessoa.
    Armazena informações pessoais e médicas necessárias para gerenciamento da fila de espera.
    """
    
    
    registros = []
    dict_receptores = {}
    cont_receptores = 0
    
    def __init__(self, orgao_necessario, gravidade_condicao, centro_transplante_vinculado, contato_emergencia, 
                nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
                 cpf, profissao, cidade_residencia, estado_residencia, estado_civil):
        
        """
        Inicializa um novo receptor com informações pessoais e necessidades médicas.

        Args:
            orgao_necessario (str): Órgão que o receptor necessita.
            gravidade_condicao (str): Grau de gravidade da condição médica.
            centro_transplante_vinculado (str): Nome do centro de transplante.
            contato_emergencia (str): Telefone de emergência.
            nome (str): Nome completo do receptor.
            idade (int): Idade.
            genero (str): Gênero.
            data_nascimento (str): Data de nascimento no formato "dd/mm/aaaa".
            cidade_natal (str): Cidade natal.
            estado_natal (str): Estado natal.
            cpf (str): CPF.
            profissao (str): Profissão.
            cidade_residencia (str): Cidade onde reside.
            estado_residencia (str): Estado onde reside.
            estado_civil (str): Estado civil.
        """
        
        Receptor.cont_receptores += 1
        super().__init__(nome, idade, genero, data_nascimento, cidade_natal, estado_natal, cpf, profissao, cidade_residencia, estado_residencia, estado_civil, id = Receptor.cont_receptores)
        self._orgao_necessario = orgao_necessario
        self._gravidade_condicao = gravidade_condicao
        self._centro_transplante_vinculado = centro_transplante_vinculado
        self._contato_emergencia = contato_emergencia
        # self._posicao_lista_espera = posicao_lista_espera
        self._id = f"receptor_{Receptor.cont_receptores}"
        self._posicao_lista_espera = Receptor.cont_receptores
        
    @classmethod
    def cadastrar(cls, nome, idade, genero, data_nascimento, cidade_natal, estado_natal, cpf, profissao, cidade_residencia,
                  estado_residencia, estado_civil, orgao_necessario, gravidade_condicao, centro_transplante_vinculado, contato_emergencia, 
                 ):
        
        """
        Valida os dados fornecidos e cadastra um novo receptor no sistema.

        Returns:
            Receptor: Instância criada do receptor.

        Raises:
            ValueError: Se alguma validação falhar.
        """
        
        Validacoes.validar_nome(nome)
        Validacoes.validar_idade(idade)
        Validacoes.validar_sexo(genero)
        
        
        # idade_baseada_data = Validacoes.validar_data_nascimento(data_nascimento)
        # if idade_baseada_data != idade:
        #     raise ValueError("A data inserida nao condiz com a idade inserida...")
        
        Validacoes.validar_cidade(cidade_natal)
        Validacoes.validar_estado(estado_natal)
        Validacoes.validar_cpf(cpf)
        Validacoes.validar_profissao(profissao)
        Validacoes.validar_cidade(cidade_residencia)
        Validacoes.validar_estado(estado_residencia)
        Validacoes.valiar_estado_civil(estado_civil)
        Validacoes.validar_orgao(orgao_necessario)
        Validacoes.validar_gravidade(gravidade_condicao)
        Validacoes.validar_centro_transplante(centro_transplante_vinculado)
        Validacoes.validar_telefone(contato_emergencia)
        
        # Validar posição na lista de espera
        # if not isinstance(posicao_lista_espera, int):
        #     raise TypeError("A posição na lista de espera deve ser um número inteiro.")
        # if posicao_lista_espera < 0:
        #     raise ValueError("A posição na lista de espera deve ser maior ou igual a 0.")
        
        receptor = Receptor(orgao_necessario, gravidade_condicao, centro_transplante_vinculado, contato_emergencia, 
                 nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
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
        
        """
        Carrega múltiplos receptores a partir de uma lista de dados em JSON.

        Args:
            json_data (list): Lista de dicionários com informações dos receptores.
        """
        
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
                centro_transplante_vinculado=necessidade["centro_transplante"]
            )

    @classmethod
    def listar(cls):
        
        """
        Lista todos os receptores cadastrados no sistema.
        """
        
        if not cls.dict_receptores:
            print("Nenhum receptor cadastrado.")
            return
        
        print(json.dumps(list(cls.dict_receptores.values()), indent=4, ensure_ascii=False))
        
    @classmethod
    def editar(cls, id, dados_ou_necessidade, campo, mudanca): # formato do dicionario (cada receptor ter campos de dados e de necessidade) fez com que seja necessario um parametro a mais
        
        """
        Edita um campo específico de um receptor cadastrado.

        Args:
            id (str): ID do receptor.
            dados_ou_necessidade (str): 'dados' ou 'necessidade', dependendo da categoria da informação.
            campo (str): Nome do campo a ser alterado.
            mudanca: Novo valor para o campo.

        Raises:
            ValueError: Se o ID não existir.
        """
        
        if id in cls.dict_receptores.keys():
            cls.dict_receptores[id][dados_ou_necessidade][campo] = mudanca
        
        else:
            raise ValueError("id não foi inseriada corretamente ou nao existe")
    
    
    @classmethod
    def buscar(cls, id):
        
        """
        Exibe as informações de um receptor com base no ID.

        Args:
            id (str): ID do receptor.

        Raises:
            ValueError: Se o ID não existir.
        """
        
        if id in cls.dict_receptores.keys():
            print(json.dumps(cls.dict_receptores[id], indent=4, ensure_ascii=False))
        
        else:
            raise ValueError("id não foi inseriada corretamente ou nao existe")
        
    @classmethod
    def excluir(cls, id):
        
        """
        Remove um receptor do sistema com base no ID.

        Args:
            id (str): ID do receptor.
        """
        
        if id in cls.dict_receptores.keys():
            del cls.dict_receptores[id]
            
    @classmethod
    def obter_receptor_por_id(cls, id):
        
        """
        Retorna uma instância da classe Receptor reconstruída a partir do dicionário `dict_receptores`.

        Args:
            id (str): ID do receptor.

        Returns:
            Receptor: Instância do receptor com os dados preenchidos.

        Raises:
            ValueError: Se o ID não for encontrado no dicionário.
        """
        
        if id not in cls.dict_receptores:
            raise ValueError("ID do receptor não encontrado.")

        dados = cls.dict_receptores[id]["dados"]
        necessidade = cls.dict_receptores[id]["necessidade"]

        # Cria a instância sem chamar __init__
        receptor = cls.__new__(cls)

        # Inicializa manualmente a parte da superclasse (Pessoa)
        Pessoa.__init__(
            receptor,
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
            id=id
        )

        # Define os atributos específicos de Receptor
        receptor._orgao_necessario = necessidade["orgao_necessario"]
        receptor._gravidade_condicao = necessidade["gravidade_condicao"]
        receptor._centro_transplante_vinculado = necessidade["centro_transplante"]
        receptor._contato_emergencia = dados["contato_emergencia"]
        receptor._posicao_lista_espera = necessidade["posicao_lista_espera"]
        receptor._id = id

        return receptor