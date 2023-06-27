class Teacher:
    def __init__(self, name: str, cpf: str):
        self.name = name
        self.cpf = cpf

    def to_dict(self):
        return {
            "cpf": self.cpf,
            "name": self.name
        }