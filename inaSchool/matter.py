from teacher import Teacher
from student import Student

class Matter:
    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.teachers = []
        
        
    def to_dict(self):
        return {
            "name": self.name,
            "students": self.students,
            "teachers": self.teachers,
        }

    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)

    def add_student(self, student: Student):
        self.students.append(student)
        
class MatterDAO:
    def __init__(self,database):
        self.db = database
        
    def create(self, matter):
        try:
            res = self.db.collection.insert_one(matter.__dict__)
            print(f'Materia adicionado com sucesso! {res.inserted_id}')
            return res.inserted_id
        except Exception as e:
            print(f'Erro ao adicionar materia: {e}')
            return None
        
    def read(self, name: str):
        try:
            res = self.db.collection.find_one({'name': name})
            print(f'Materia encontrada!')
            return res
        except Exception as e:
            print(f'Erro na leitura da materia: {e}')
            return None
        
    def update(self, old_name: str, new_name: str):
        try:
            res = self.db.collection.find_one({'name': old_name})
            print(res._id)
            self.db.collection.update_one({'_id':res._id}, {'$set':{'name': new_name}})
            print(f'Nome da Materia atualizado!')
            return res
        except Exception as e:
            print(f'Erro ao atualizar: {e}')
            return None
    
    def delete(self, name: str):
        try:
            res = self.db.collection.delete_one({'name': name})
            print(
                f'Materia deletada: {res.deleted_count} documento deletado')
            return res.deleted_count
        except Exception as e:
            print(f'Erro ao deletar motorista: {e}')
            return None

    def add_teacherDAO(self, name: str, teacher: Teacher):
        try:
            res = self.db.collection.update_one(
                {'name':name}, {'$push': {'teachers': teacher.to_dict()}})
            print(f'Professor(a) adicionado(a)!')
            return res
        except Exception as e:
            print(f'Erro ao adicionar professor(a): {e}')
            return None
    
    def add_studentDAO(self, name: str, student: Student):      
        try:
            res = self.db.collection.update_one(
                {'name': name}, {'$push': {'students': student.to_dict()}})
            print(f'Estudante adicionado(a)!')
            return res
        except Exception as e:
            print(f'Erro ao adicionar estudante: {e}')
            return None
        
    def update_note_student(self, matter_name: str, student_name: str, student_note):      
        try:
            # res = self.db.collection.update_one(
            #     {'name': matter_name}, {'students': {'name':student_name}, {'$set':{'note': student_note}}})
            res = self.db.collection.update_one(
                {'name': matter_name, 'students.name': student_name},
                {'$set': {'students.$.note': student_note}})
            print(f'Nota do estudante adicionado(a)!')
            return res
        except Exception as e:
            print(f'Erro ao adicionar estudante: {e}')
            return None
        
    def remove_teacher(self, matter_name: str, teacher_cpf: str):
        try:
            res = self.db.collection.update_one(
            {'name': matter_name}, {'$pull': {'teachers': {'id': teacher_cpf}}}
        )
            print('Professor(a) removido!')
            return res
        except Exception as e:
            print(f'Erro ao remover o(a) professor(a): {e}')
            return None

    def remove_student(self, matter_name: str, student_name: str):
        try:
            res = self.db.collection.update_one(
            {'name': matter_name}, {'$pull': {'students': {'id': student_name}}}
        )
            print('Estudante removido!')
            return res
        except Exception as e:
            print(f'Erro ao remover o estudante: {e}')
            return None  
    
    
