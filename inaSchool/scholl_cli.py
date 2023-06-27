from matter import Matter, MatterDAO
from student import Student
from teacher import Teacher

class SchoolCLI:
    def __init__(self, database):
        self.matter_dao = MatterDAO(database)

    def create_matter(self):
        name_matter = input('Digite o nome da materia ')
        matter = Matter(name=name_matter)
        self.matter_dao.create(matter)

    def add_student(self):
        name_student = input('Digite o nome do estudante ')
        register_number = int(input('Digite a matricula do estudante '))
        curse = ('Digite o curso do estudante ')
        student = Student(register_number, name_student, curse)
        name_matter = input('Digite o nome da materia que o aluno sera adicionado ')
        self.matter_dao.add_studentDAO(name_matter, student)
        print('Adicionado o aluno na materia desejada ')

    def add_teacher(self):
        name_teacher = input("Digite o nome do Professor ")
        cpf_teacher = input("Digite o cpf do Professor ")
        teacher = Teacher(name_teacher, cpf_teacher)
        name_matter = input('Digite a materia do Professor ')
        self.matter_dao.add_teacherDAO(name_matter, teacher)
        print('Adicionado o o professor na materia desejada ')

    def read_matter(self):
        name_matter = input("Digite o nome da Materia ")
        print(self.matter_dao.read(name_matter))
        
    def update_matter(self):
        old_name_matter = input("Digite o nome da Materia que deseja atualizar ")
        new_name_matter = input("Digite o nome da nova materia ")
        self.matter_dao.update(old_name_matter, new_name_matter)

    def delete_matter(self):
        name_matter = input('Digite o nome da materia que deseja apagar ')
        self.matter_dao.delete(name_matter)

    def remove_student(self):
        name_matter = input('Digite o nome da materia ')
        name_student = input('Digite o CPF do professor que deseja remover ')
        self.matter_dao.remove_teacher(name_matter, name_student)

    def remove_teacher(self):
        name_matter = input('Digite o nome da materia ')
        cpf_teacher = input('Digite o CPF do professor que deseja remover ')
        self.matter_dao.remove_teacher(name_matter, cpf_teacher)




    def update_note(self):
        name_matter = input('Digite o nome da materia ')
        name_student = input('Digite o nome do estudante ')
        note_student = input('Digite a nota do aluno ')
        self.matter_dao.update_note_student(name_matter, name_student, note_student)


    def menu(self):
        while True:
            print('MENU PRINCIPAL: ')
            print('1 - Criar materia ')
            print('2 - Adicionar Aluno(a) a uma materia existente materia: ')
            print('3 - Adicionar Professor(a) a uma materia existente materia: ')
            print('4 - Consultar materia: ')
            print('5 - Atualizar nome da materia: ')
            print('6 - Deletar materia: ')
            print('7 - Remover um Aluno(a) da materia: ')
            print('8 - Remover um Professor(a) da materia: ')
            print('9 - Atualizar nota do(a) da materia: ')
            print('0 - Sair')
            opcao = input('Digite a opção desejada: ')
            if opcao == '1':
                self.create_matter()
            elif opcao == '2':
                self.add_student()
            elif opcao == '3':
                self.add_teacher()
            elif opcao == '4':
                self.read_matter()
            elif opcao == '5':
                self.update_matter()
            elif opcao == '6':
                self.delete_matter()
            elif opcao == '7':
                self.remove_student()
            elif opcao == '8':
                self.remove_teacher()
            elif opcao == '9':
                self.update_note()
            elif opcao == '0':
                break
            else:
                print('Opção inválida!')
        print('Programa encerrado.')