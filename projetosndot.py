from models.Pessoa import Pessoa
from models.Receptor import Receptor
from models.AdministradorSistema import AdministradorSistema
from models.Doador import Doador
from models.IntencaoDeDoar import IntencaoDeDoar

    
if __name__ == "__main__":
    
#     intencao = IntencaoDeDoar.registrar_intencao_doar("s")
#     doador1 = Doador.cadastrar("thiago", 21, "m", "18-06-2003", "BH", "MG", "12312312312", "Estudante", "Brasilia", "DF", "Solteiro", "61-99999-1234", "0+", intencao)
#     Doador.listar()
    
#     admin1 = AdministradorSistema.cadastrar(
#     nome="Carlos Henrique",
#     idade=35,
#     genero="Masculino",
#     data_nascimento="1989-07-14",
#     cidade_natal="Campinas",
#     estado_natal="SP",
#     cpf="12345678901",
#     profissao="Administrador Hospitalar",
#     cidade_residencia="São Paulo",
#     estado_residencia="SP",
#     estado_civil="Casado",
#     nome_usuario="carlos_admin",
#     senha="segura123"
# )

#     admin2 = AdministradorSistema.cadastrar(
#     nome="Renata Oliveira",
#     idade=42,
#     genero="Feminino",
#     data_nascimento="1982-03-22",
#     cidade_natal="Curitiba",
#     estado_natal="PR",
#     cpf="98765432100",
#     profissao="Coordenadora de Saúde",
#     cidade_residencia="Curitiba",
#     estado_residencia="PR",
#     estado_civil="Solteira",
#     nome_usuario="renata_oliveira",
#     senha="senhaForte2025"
# )

#     print(AdministradorSistema.listar())
#     AdministradorSistema.editar("admin_1", "acesso", "nome_usuario", "TESTE")
#     print(AdministradorSistema.listar())
#     print(AdministradorSistema.buscar("admin_1"))
#     AdministradorSistema.login("chilr", "lau")
#     AdministradorSistema.excluir("admin_1")
#     AdministradorSistema.listar()

    receptor1 = Receptor.cadastrar(
    nome="Juliana Mendes",
    idade=29,
    genero="Feminino",
    data_nascimento="1995-05-10",
    cidade_natal="Belo Horizonte",
    estado_natal="MG",
    cpf="23456789012",
    profissao="Professora",
    cidade_residencia="Belo Horizonte",
    estado_residencia="MG",
    estado_civil="Solteira",
    orgao_necessario="Rim",
    gravidade_condicao="Alta",
    centro_transplante_vinculado="Hospital das Clínicas BH",
    contato_emergencia="31999998888",
    posicao_lista_espera=3
)

    receptor2 = Receptor.cadastrar(
    nome="Felipe Rocha",
    idade=45,
    genero="Masculino",
    data_nascimento="1979-09-02",
    cidade_natal="Recife",
    estado_natal="PE",
    cpf="34567890123",
    profissao="Engenheiro",
    cidade_residencia="Recife",
    estado_residencia="PE",
    estado_civil="Casado",
    orgao_necessario="Fígado",
    gravidade_condicao="Crítica",
    centro_transplante_vinculado="Instituto de Medicina Integral Prof. Fernando Figueira",
    contato_emergencia="81988887777",
    posicao_lista_espera=1
)
    print(Receptor.listar())
    
    Receptor.editar("receptor_1", "dados", "sexo", "AQUI")
    
    print(Receptor.listar())
    print('-' * 100)
    print(Receptor.buscar("receptor_1"))
    Receptor.excluir("receptor_1")