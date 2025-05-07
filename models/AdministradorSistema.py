from models.Pessoa import Pessoa
import json

class AdministradorSistema(Pessoa):
    cont_admin = 0
    dict_admins = {}
    list_admins = []
    logado = None
    
    def __init__(self, nome, idade, genero, data_nascimento, cidade_natal,
                 estado_natal, cpf, profissao, cidade_residencia, estado_residencia,
                 estado_civil, nome_usuario, senha):
        
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
        if not cls.dict_admins:
            print("Nenhum administrador cadastrado.")
            return
        
        # for elem in cls.list_admins:
        #     print(json.dumps(cls.list_admins))
        print(json.dumps(list(cls.dict_admins.items()), indent=4, ensure_ascii=False))
    
    @classmethod
    def buscar(cls, id):
        if id in cls.dict_admins.keys():
            print(json.dumps(cls.dict_admins[id], indent=4, ensure_ascii=False))
        
        else:
            raise ValueError("id não foi inseriada corretamente ou nao existe")
    
    @classmethod
    def excluir(cls, id):
        if id in cls.dict_admins.keys():
            del cls.dict_admins[id]
    
    @classmethod
    def editar(cls, id, dados_ou_acesso, campo, mudanca): # formato do dicionario (cada receptor ter campos de dados e de necessidade) fez com que seja necessario um parametro a mais
        if id in cls.dict_admins.keys():
            cls.dict_admins[id][dados_ou_acesso][campo] = mudanca
        
        else:
            raise ValueError("id não foi inseriado corretamente ou nao existe")
        
    @classmethod
    def login(cls, nome_usuario, senha):
        
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
        cls.logado = None

    @classmethod
    def carregar_de_json(cls, json_data):
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
        for _, info in cls.dict_admins.items():
            acesso = info.get("acesso", {})
            dados = info.get("dados", {})
            if acesso.get("nome_usuario") == nome_usuario and dados.get("cpf") == cpf:
                print(f"Senha recuperada com sucesso: {acesso.get('senha')}")
                return acesso.get("senha")
        
        raise ValueError("Nome de usuário ou CPF incorretos.")