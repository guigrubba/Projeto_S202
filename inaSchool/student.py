class Student:
    def __init__(self, register_number: int, name: str, curse: str):
        self.register_number = register_number
        self.name = name
        self.curse = curse
        
    def to_dict(self):
        return {
            "register_number": self.register_number,
            "name": self.name,
            "students": self.curse,
        }