from models.Pessoa import Pessoa
from models.Receptor import Receptor
from models.AdministradorSistema import AdministradorSistema
from models.Doador import Doador
from models.IntencaoDeDoar import IntencaoDeDoar
from models.Doacao import  Doacao
import json
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def menu():
    while True:
        limpar_tela()
        print("="*50)
        print("  SISTEMA NACIONAL DE DOAÇÃO DE ÓRGÃOS E TECIDOS")
        print("="*50)
        print("1. Registrar doador")
        print("2. Registrar receptor")
        print("3. Registrar doação")
        print("4. Listar doadores")
        print("5. Listar receptores")
        print("6. Listar doações")
        print("7. Buscar doador por ID")
        print("8. Buscar receptor por ID")
        print("9. Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar_doador()
        elif opcao == '2':
            registrar_receptor()
        elif opcao == '3':
            registrar_doacao()
        elif opcao == '4':
            listar_doadores()
        elif opcao == '5':
            listar_receptores()
        elif opcao == '6':
            listar_doacoes()
        elif opcao == '7':
            limpar_tela()
            id_doador = input("Digite o ID do doador: ")
            Doador.buscar(id_doador)
            input("Pressione ENTER para voltar ao menu.")
        elif opcao == '8':
            limpar_tela()
            id_receptor = input("Digite o ID do receptor: ")
            Receptor.buscar(id_receptor)
            input("Pressione ENTER para voltar ao menu.")
        elif opcao == '9':
            exit(0)
def registrar_doador():
    try:
        limpar_tela()
        print("\n--- Registro de Doador ---")

        nome = input("Nome: ")
        idade = int(input("Idade: "))
        genero = input("Sexo (M/F): ")
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
        cidade_natal = input("Cidade natal: ")
        estado_natal = input("Estado natal (sigla): ")
        cpf = input("CPF: ")
        profissao = input("Profissão: ")
        cidade_residencia = input("Cidade de residência: ")
        estado_residencia = input("Estado de residência (sigla): ")
        estado_civil = input("Estado civil: ")
        contato_emergencia = input("Telefone de contato de emergência (somente números): ")
        tipo_sanguineo = input("Tipo sanguíneo (ex: O+, A-, etc.): ")
        status_intencao = input("Status da intenção (S/N): ")
        orgao = input("Qual orgao deseja doar: ")

        intencao = IntencaoDeDoar(status=status_intencao, orgao=orgao, )

        doador = Doador.cadastrar(
            nome, idade, genero, data_nascimento, cidade_natal, estado_natal,
            cpf, profissao, cidade_residencia, estado_residencia, estado_civil,
            contato_emergencia, tipo_sanguineo, intencao
        )
        
        
        
        # Doador.cadastrar()

        print(f"\n✅ Doador cadastrado com sucesso! ID: {doador.getID}\n")
    except Exception as e:
        print(f"\n❌ Erro ao cadastrar doador: {e}\n")
    input("Pressione ENTER para voltar ao menu.")
    
def registrar_receptor():
    limpar_tela()
    try:
        print("\n--- Registro de Receptor ---")

        nome = input("Nome: ")
        idade = int(input("Idade: "))
        genero = input("Sexo (M/F): ")
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
        cidade_natal = input("Cidade natal: ")
        estado_natal = input("Estado natal (sigla): ")
        cpf = input("CPF: ")
        profissao = input("Profissão: ")
        cidade_residencia = input("Cidade de residência: ")
        estado_residencia = input("Estado de residência (sigla): ")
        estado_civil = input("Estado civil: ")

        orgao_necessario = input("Órgão necessário: ")
        gravidade_condicao = input("Gravidade da condição (leve, moderada, grave, crítica): ")
        centro_transplante_vinculado = input("Centro de transplante vinculado: ")
        contato_emergencia = input("Telefone de contato de emergência (somente números): ")
        # posicao_lista_espera = int(input("Posição na lista de espera (número inteiro ≥ 0): "))

        receptor = Receptor.cadastrar(
            nome=nome,
            idade=idade,
            genero=genero,
            data_nascimento=data_nascimento,
            cidade_natal=cidade_natal,
            estado_natal=estado_natal,
            cpf=cpf,
            profissao=profissao,
            cidade_residencia=cidade_residencia,
            estado_residencia=estado_residencia,
            estado_civil=estado_civil,
            orgao_necessario=orgao_necessario,
            gravidade_condicao=gravidade_condicao,
            centro_transplante_vinculado=centro_transplante_vinculado,
            contato_emergencia=contato_emergencia
        )

        print(f"\n✅ Receptor cadastrado com sucesso! ID: {receptor._id}\n")
    except Exception as e:
        print(f"\n❌ Erro ao cadastrar receptor: {e}\n")
    input("Pressione ENTER para voltar ao menu.")
    
def registrar_doacao():
    limpar_tela()
    try:
        print("\n--- Registro de Doação ---")

        doador_id = input("Digite o ID do doador (ex: doador_1): ").strip()
        receptor_id = input("Digite o ID do receptor (ex: receptor_1): ").strip()

        doador = Doador.recuperar_por_id(doador_id)
        receptor = Receptor.obter_receptor_por_id(receptor_id)

        if doador._intencao._orgao != receptor._orgao_necessario:
            print("\n⚠️ Aviso: O órgão doado não corresponde ao órgão necessário do receptor.")
            print("❌ Registro de doação cancelado.")
            return

        status = input("Status da doação (s, n): ").strip()

        doacao = Doacao.registrar_doacao(status, doador, receptor)

        print(f"\n✅ Doação registrada com sucesso! ID da doação: {doacao._id}\n")
    except Exception as e:
        print(f"\n❌ Erro ao registrar doação: {e}\n")

    input("Pressione ENTER para voltar ao menu.")
    
def listar_doadores():
    limpar_tela()
    Doador.listar()
    input("Pressione ENTER para voltar ao menu.")
    
def listar_receptores():
    limpar_tela()
    Receptor.listar()
    input("Pressione ENTER para voltar ao menu.")
    
def listar_doacoes():
    limpar_tela()
    Doacao.listar_doacoes()
    input("Pressione ENTER para voltar ao menu.")

        
if __name__ == "__main__":
    
    with open("doador.json", encoding="utf-8") as f:
        data = json.load(f)
    Doador.carregar_de_json(data)
    
    with open("receptor.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    Receptor.carregar_de_json(data)
    
    menu()
    # with open("admins.json", "r", encoding="utf-8") as f:
    #     lista_admins = json.load(f)

    # AdministradorSistema.carregar_de_json(lista_admins)
    # # AdministradorSistema.buscar("admin_3")
    # # AdministradorSistema.editar("admin_3", "acesso", "senha", "AQUIIIII!!")
    # # AdministradorSistema.buscar("admin_3")
    # AdministradorSistema.listar()

    with open("doador.json", encoding="utf-8") as f:
        data = json.load(f)
    Doador.carregar_de_json(data)
    # Doador.listar()

    with open("receptor.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    Receptor.carregar_de_json(data)
    # Receptor.listar()

    # intencao = IntencaoDeDoar.registrar_intencao_doar("s")
    # doador1 = Doador.cadastrar("thiago", 21, "m", "18-06-2003", "BH", "MG", "12312312312", "Estudante", "Brasilia", "DF", "Solteiro", "61-99999-1234", "0+", intencao)
    # Doador.listar()
    
    doacao = Doacao.registrar_doacao("s", Doador.obter_doador_por_id("doador_1"), Receptor.obter_receptor_por_id("receptor_3"))
    doacao = Doacao.registrar_doacao("s", Doador.obter_doador_por_id("doador_2"), Receptor.obter_receptor_por_id("receptor_3"))
    Doacao.listar_doacoes()