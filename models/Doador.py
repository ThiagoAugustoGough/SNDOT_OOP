from models.Pessoa import Pessoa
from models.Validacoes import Validacoes
import json

class Doador(Pessoa):
    
    """
    Representa um doador de órgãos, herdando atributos e comportamentos da classe Pessoa.
    Mantém registros dos doadores e oferece métodos para cadastro, listagem, busca, edição e exclusão.
    """
    
    registros = []
    dict_doadores = {}
    cont_doadores = 0
    
    def __init__(self, contato_emergencia, tipo_sanguineo, 
                nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
                cpf, profissao, cidade_residencia, estado_residencia, estado_civil, intencao, id=None):
        
        """
        Inicializa uma instância da classe Doador com os dados pessoais, informações de saúde
        e intenção de doação.

        Args:
            contato_emergencia (str): Número de telefone de emergência.
            tipo_sanguineo (str): Tipo sanguíneo do doador.
            nome (str): Nome completo.
            idade (int): Idade do doador.
            genero (str): Gênero.
            data_nascimento (str): Data de nascimento.
            cidade_natal (str): Cidade natal.
            estado_natal (str): Estado natal.
            cpf (str): CPF do doador.
            profissao (str): Profissão.
            cidade_residencia (str): Cidade onde reside.
            estado_residencia (str): Estado onde reside.
            estado_civil (str): Estado civil.
            intencao (object): Objeto que representa a intenção de doar (com atributos _status, _data_intencao, _orgao).
            id (int, optional): Identificador único. Se não fornecido, será gerado automaticamente.
        """
        
        if id is None:
            Doador.cont_doadores += 1
            id = Doador.cont_doadores
        else:
            # Garante que o contador não se atrase em relação ao ID máximo usado
            Doador.cont_doadores = max(Doador.cont_doadores, int(str(id).split("_")[-1]))

        super().__init__(nome, idade, genero, data_nascimento, cidade_natal, estado_natal, cpf, profissao, cidade_residencia, estado_residencia, estado_civil, id=id)
        self._contato_emergencia = contato_emergencia
        self._tipo_sanguineo = tipo_sanguineo
        self._id = f"doador_{id}"
        self._intencao = intencao
    
    @classmethod
    def cadastrar(cls, nome, idade, genero, data_nascimento, cidade_natal, estado_natal, cpf, profissao, cidade_residencia,
                  estado_residencia, estado_civil, contato_emergencia, tipo_sanguineo, intencao):
        
        """
        Cadastra um novo doador após validar os dados fornecidos.
        Armazena o doador no dicionário de doadores da classe.

        Returns:
            Doador: Instância criada do doador.
        """
        
        #validar nome
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
        Validacoes.validar_telefone(contato_emergencia)
        
        doador = Doador(contato_emergencia, tipo_sanguineo, nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
                 cpf, profissao, cidade_residencia, estado_residencia, estado_civil, intencao)
        
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
            "contato_emergencia": doador._contato_emergencia,
            "tipo_sanguineo": doador._tipo_sanguineo
        },
        "intencao": {
            "status" : intencao._status,
            "data" : intencao._data_intencao,
            "orgao" : intencao._orgao
        }
            }
        
        return doador
    
    @classmethod
    def carregar_de_json(cls, lista_json):
        """
        Carrega múltiplos doadores a partir de uma lista em formato JSON.

        Args:
            lista_json (list): Lista de dicionários contendo os dados dos doadores.
        """
        
        for item in lista_json:
            dados = item["dados"]
            intencao = item["intencao"]

            intencao_obj = type("Intencao", (), {})()  # objeto dinâmico só com os atributos necessários
            intencao_obj._status = intencao.get("status")
            intencao_obj._data_intencao = intencao.get("data", "")  # "" se não estiver no JSON
            intencao_obj._orgao = intencao.get("orgao")

            cls.cadastrar(
                nome=dados.get("nome"),
                idade=dados.get("idade"),
                genero=dados.get("sexo"),
                data_nascimento=dados.get("data_nascimento"),
                cidade_natal=dados.get("cidade_natal"),
                estado_natal=dados.get("estado_natal"),
                cpf=dados.get("cpf"),
                profissao=dados.get("profissao"),
                cidade_residencia=dados.get("cidade_residencia"),
                estado_residencia=dados.get("estado_residencia"),
                estado_civil=dados.get("estado_civil"),
                contato_emergencia=dados.get("contato_emergencia"),
                tipo_sanguineo=dados.get("tipo_sanguineo"),
                intencao=intencao_obj
            )
    
    @classmethod
    def listar(cls):
        """
        Exibe todos os doadores cadastrados em formato JSON formatado.
        Se não houver doadores, informa isso ao usuário.
        """
        if not cls.dict_doadores:
            print("Nenhum doador cadastrado.")
            return
        
        print(json.dumps(list(cls.dict_doadores.values()), indent=4, ensure_ascii=False))
        
    @classmethod
    def editar(cls, id, dados_ou_intencao, campo, mudanca): # formato do dicionario (cada doador ter campos de dados e de intencao) fez com que seja necessario um parametro a mais
        
        """
        Edita um campo específico dos dados ou da intenção de um doador existente.

        Args:
            id (str): ID do doador (e.g. "doador_1").
            dados_ou_intencao (str): Se o campo pertence aos "dados" ou à "intencao".
            campo (str): Nome do campo a ser modificado.
            mudanca (str): Novo valor para o campo.
        
        Raises:
            ValueError: Se o ID não for encontrado.
        """
        
        if id in cls.dict_doadores.keys():
            cls.dict_doadores[id][dados_ou_intencao][campo] = mudanca
        
        else:
            raise ValueError("id não foi inseriada corretamente ou nao existe")
    
    
    @classmethod
    def buscar(cls, id):
        
        """
        Busca e exibe os dados de um doador com base no ID.

        Args:
            id (str): ID do doador.
        
        Raises:
            ValueError: Se o ID não for encontrado.
        """
        
        if id in cls.dict_doadores.keys():
            print(json.dumps(cls.dict_doadores[id], indent=4, ensure_ascii=False))
        
        else:
            raise ValueError("id não foi inseriada corretamente ou nao existe")
        
    @classmethod
    def excluir(cls, id):
        
        """
        Remove um doador do registro com base no ID.

        Args:
            id (str): ID do doador.
        
        Obs:
            Este método tem um bug: está tentando deletar de `dict_receptores`, mas deveria usar `dict_doadores`.
        """
        
        if id in cls.dict_receptores.keys():
            del cls.dict_receptores[id]
        
    @property    
    def getID(self):
        
        """
        Retorna o identificador único do doador.

        Returns:
            str: ID do doador.
        """
        
        return self._id
    
    @classmethod
    
    def recuperar_por_id(cls, id):
        
        """
        Recupera uma instância de Doador a partir do seu ID, reconstruindo o objeto com base nos dados armazenados.

        Args:
            id (str): ID do doador.

        Returns:
            Doador: Instância reconstruída do doador.
        
        Raises:
            ValueError: Se o ID não for encontrado.
        """
        
        if id not in cls.dict_doadores:
            raise ValueError("ID não encontrado.")

        dados = cls.dict_doadores[id]["dados"]
        intencao_data = cls.dict_doadores[id]["intencao"]

        # Recriar o objeto Intencao com atributos esperados
        intencao_obj = type("Intencao", (), {})()
        intencao_obj._status = intencao_data.get("status")
        intencao_obj._data_intencao = intencao_data.get("data")
        intencao_obj._orgao = intencao_data.get("orgao")

        return cls(
            contato_emergencia=dados.get("contato_emergencia"),
            tipo_sanguineo=dados.get("tipo_sanguineo"),
            nome=dados.get("nome"),
            idade=dados.get("idade"),
            genero=dados.get("sexo"),
            data_nascimento=dados.get("data_nascimento"),
            cidade_natal=dados.get("cidade_natal"),
            estado_natal=dados.get("estado_natal"),
            cpf=dados.get("cpf"),
            profissao=dados.get("profissao"),
            cidade_residencia=dados.get("cidade_residencia"),
            estado_residencia=dados.get("estado_residencia"),
            estado_civil=dados.get("estado_civil"),
            intencao=intencao_obj,
            id=int(id.split("_")[-1])  # extrai apenas o número do ID "doador_3" → 3
    )