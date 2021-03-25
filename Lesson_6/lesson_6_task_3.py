class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} - {self.position}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


my_worker = Position('Dmitriy', 'Litvionov', 'junior', 60000, 10000)
print(my_worker.get_full_name())
print(my_worker.get_total_income())