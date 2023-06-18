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

    def add_teacherDAO(self, name:)       
