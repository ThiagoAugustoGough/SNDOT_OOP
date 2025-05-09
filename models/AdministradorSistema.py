from models.Pessoa import Pessoa
from models.Validacoes import Validacoes
import json

class AdministradorSistema(Pessoa):
    cont_admin = 0
    dict_admins = {}
    list_admins = []
    logado = None
    
    def __init__(self, nome, idade, genero, data_nascimento, cidade_natal,
                 estado_natal, cpf, profissao, cidade_residencia, estado_residencia,
                 estado_civil, nome_usuario, senha):
        
        """
        Inicializa um novo administrador do sistema com os dados pessoais e de acesso.

        Args:
            nome (str): Nome completo do administrador.
            idade (int): Idade do administrador.
            genero (str): Gênero do administrador.
            data_nascimento (str): Data de nascimento no formato "dd/mm/aaaa".
            cidade_natal (str): Cidade natal.
            estado_natal (str): Estado natal.
            cpf (str): CPF válido.
            profissao (str): Profissão.
            cidade_residencia (str): Cidade de residência.
            estado_residencia (str): Estado de residência.
            estado_civil (str): Estado civil.
            nome_usuario (str): Nome de usuário para login.
            senha (str): Senha para acesso.
        """
        
        AdministradorSistema.cont_admin += 1
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
        self._nome_usuario = nome_usuario
        self._senha = senha
        self._id = f"admin_{AdministradorSistema.cont_admin}"
        
    @classmethod
    def cadastrar(cls, nome, idade, genero, data_nascimento, cidade_natal,
                 estado_natal, cpf, profissao, cidade_residencia, estado_residencia,
                 estado_civil, nome_usuario, senha):
        
        """
        Valida os dados e cadastra um novo administrador do sistema.

        Returns:
            AdministradorSistema: Instância criada do administrador.
        
        Raises:
            ValueError: Se alguma validação falhar.
        """
        
        Validacoes.validar_nome(nome)
        Validacoes.validar_idade(idade)
        Validacoes.validar_sexo(genero)
        
        # Validacao de idade
        idade_baseada_data = Validacoes.validar_data_nascimento(data_nascimento)
        
        if idade_baseada_data != idade:
            raise ValueError("A data inserida nao condiz com a idade inserida...")
        # Fim validacao de idade
        
        Validacoes.validar_cidade(cidade_natal)
        Validacoes.validar_estado(estado_natal)
        Validacoes.validar_cpf(cpf)
        Validacoes.validar_profissao(profissao)
        Validacoes.validar_cidade(cidade_residencia)
        Validacoes.validar_estado(estado_residencia)
        Validacoes.valiar_estado_civil(estado_civil)
        
        
        admin = AdministradorSistema(nome, idade, genero, data_nascimento, cidade_natal,
                 estado_natal, cpf, profissao, cidade_residencia, estado_residencia,
                 estado_civil, nome_usuario, senha)
        
        cls.dict_admins[admin._id] = {
        "dados": {
            "nome": admin._nome,
            "idade": admin._idade,
            "sexo": admin._genero,
            "data_nascimento": admin._data_nascimento,
            "cidade_natal": admin._cidade_natal,
            "estado_natal": admin._estado_natal,
            "cpf": admin._cpf,
            "profissao": admin._profissao,
            "cidade_residencia": admin._cidade_residencia,
            "estado_residencia": admin._estado_residencia,
            "estado_civil": admin._estado_civil
        },
        "acesso": {
            "nome_usuario": admin._nome_usuario,
            "senha": admin._senha
        }
            }
        
        # cls.list_admins.append(cls.dict_admins[admin._id])
        return admin
        
    @classmethod
    def listar(cls):
        
        """
        Lista todos os administradores cadastrados com seus dados e credenciais.
        """

        if not cls.dict_admins:
            print("Nenhum administrador cadastrado.")
            return
        
        # for elem in cls.list_admins:
        #     print(json.dumps(cls.list_admins))
        print(json.dumps(list(cls.dict_admins.items()), indent=4, ensure_ascii=False))
    
    @classmethod
    def buscar(cls, id):
        
        """
        Busca e exibe os dados de um administrador específico pelo ID.

        Args:
            id (str): ID do administrador.
        
        Raises:
            ValueError: Se o ID não existir.
        """
        
        if id in cls.dict_admins.keys():
            print(json.dumps(cls.dict_admins[id], indent=4, ensure_ascii=False))
        
        else:
            raise ValueError("id não foi inseriada corretamente ou nao existe")
    
    @classmethod
    def excluir(cls, id):
        
        """
        Remove um administrador do sistema pelo ID.

        Args:
            id (str): ID do administrador.
        """
        
        if id in cls.dict_admins.keys():
            del cls.dict_admins[id]
    
    @classmethod
    def editar(cls, id, dados_ou_acesso, campo, mudanca): # formato do dicionario (cada receptor ter campos de dados e de necessidade) fez com que seja necessario um parametro a mais
        
        """
        Edita um campo específico de um administrador.

        Args:
            id (str): ID do administrador.
            dados_ou_acesso (str): 'dados' ou 'acesso', dependendo do tipo de informação a ser editada.
            campo (str): Campo a ser alterado.
            mudanca: Novo valor a ser atribuído ao campo.
        
        Raises:
            ValueError: Se o ID for inválido.
        """
        
        if id in cls.dict_admins.keys():
            cls.dict_admins[id][dados_ou_acesso][campo] = mudanca
        
        else:
            raise ValueError("id não foi inseriado corretamente ou nao existe")
        
    @classmethod
    def login(cls, nome_usuario, senha):
        
        """
        Realiza login no sistema se as credenciais forem válidas.

        Args:
            nome_usuario (str): Nome de usuário.
            senha (str): Senha.
        
        Raises:
            ValueError: Se o nome de usuário ou senha estiverem incorretos.
        """
        
        for _, info in cls.dict_admins.items():
            acesso = info.get("acesso", {})
            if acesso.get("nome_usuario") == nome_usuario and acesso.get("senha") == senha:
                print("Realizando Log in...")
                cls.logado = nome_usuario
                break
        else:
            raise ValueError("Usuario ou Senha errados")
        
    @classmethod
    def logout(cls):
        
        """
        Realiza logout do administrador atualmente logado.
        """
        
        cls.logado = None

    @classmethod
    def carregar_de_json(cls, json_data):
        
        """
        Carrega múltiplos administradores a partir de uma lista de dados em formato JSON.

        Args:
            json_data (list): Lista de dicionários com dados e acesso de administradores.
        """
        
        for admin_info in json_data:
            dados = admin_info.get("dados", {})
            acesso = admin_info.get("acesso", {})

            try:
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
                    nome_usuario=acesso.get("nome_usuario"),
                    senha=acesso.get("senha")
                )
            except Exception as e:
                print(f"Erro ao carregar administrador {dados.get('nome')}: {e}")
        
    @classmethod
    def recuperar_senha(cls, nome_usuario, cpf):
        
        """
        Recupera a senha de um administrador baseado no nome de usuário e CPF.

        Args:
            nome_usuario (str): Nome de usuário.
            cpf (str): CPF do administrador.
        
        Returns:
            str: Senha do administrador.
        
        Raises:
            ValueError: Se o nome de usuário ou CPF estiver incorreto.
        """
        
        for _, info in cls.dict_admins.items():
            acesso = info.get("acesso", {})
            dados = info.get("dados", {})
            if acesso.get("nome_usuario") == nome_usuario and dados.get("cpf") == cpf:
                print(f"Senha recuperada com sucesso: {acesso.get('senha')}")
                return acesso.get("senha")
        
        raise ValueError("Nome de usuário ou CPF incorretos.")