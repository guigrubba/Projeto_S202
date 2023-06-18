from matter import Matter, MatterDAO
from student import Student

class SchoolCLI:
    def __init__(self, database):
        self.matter_dao = MatterDAO(database)

    def create_matter(self):
        name_matter = input('Digite o nome da materia')
        res = self.matter_dao.create(name_matter)
        print(f'{res.name} materia criada')

    def add_student(self):
        name_student = input('Digite o nome do estudante')
        register_number = int(input('Digite a matricula do estudante'))
        curse = ('Digite o curso do estudante')
        student = Student(register_number, name_student, curse)
        name_matter = input('Digite o nome da materia que o aluno sera adicionado')
        self.matter_dao.add_studentDAO(name_matter, student)
        print('Adicionado o aluno na materia desejada')


    def menu(self):
        while True:
            print('MENU PRINCIPAL:')
            print('1 - Criar materia')
            print('2 - Adicionar Aluno(a) a uma materia existente materia')
            print('3 - Adicionar Professor(a) a uma materia existente materia')
            print('4 - Consultar materia')
            print('5 - Atualizar nome da materia')
            print('6 - Deletar materia')
            print('7 - Remover um Aluno(a) da materia')
            print('8 - Remover um Professor(a) da materia')
            print('9 - Atualizar nota do(a) da materia')
            print('0 - Sair')
            opcao = input('Digite a opção desejada: ')
            if opcao == '1':
                self.criar()
            elif opcao == '2':
                self.ler()
            elif opcao == '3':
                self.atualizar()
            elif opcao == '4':
                self.deletar()
            elif opcao == '0':
                break
            else:
                print('Opção inválida!')
        print('Programa encerrado.')