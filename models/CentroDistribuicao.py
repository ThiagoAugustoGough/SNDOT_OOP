
class CentroDistribuicao:
    cont_centros = 0
    dict_centros = {}

    def __init__(self, cidade, estado, endereco, telefone):
        CentroDistribuicao.cont_centros += 1
        self._id = f"centro_{CentroDistribuicao.cont_centros}"
        self._cidade = cidade
        self._estado = estado
        self._endereco = endereco
        self._telefone = telefone

    @classmethod
    def cadastrar_centro(cls, cidade, estado, endereco, telefone):
        if not all(isinstance(x, str) for x in [cidade, estado, endereco, telefone]):
            raise TypeError("Todos os campos devem ser strings.")

        centro = cls(cidade, estado, endereco, telefone)
        cls.dict_centros[centro._id] = {
            "cidade": centro._cidade,
            "estado": centro._estado,
            "endereco": centro._endereco,
            "telefone": centro._telefone
        }
        return centro

    @classmethod
    def listar_centros(cls):
        if not cls.dict_centros:
            print("Nenhum centro de distribuição cadastrado.")
        else:
            from pprint import pprint
            pprint(cls.dict_centros)

    @classmethod
    def gerenciar_estoque(cls, id_centro):
        if id_centro in cls.dict_centros:
            print(f"Gerenciando estoque do centro: {id_centro}")
            # Aqui você pode expandir com lógica real de estoque.
        else:
            raise ValueError("Centro de distribuição não encontrado.")