class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'Full name of worker: {self.name} {self.surname}'

    def get_total_income(self):
        return f"Total income of worker: {self._income['wage'] + self._income['bonus']}"


position_1 = Position('Peter', 'Cult', 'Junior Engineer', {'wage': 70000, 'bonus': 20000})

print(position_1.get_full_name())
print(position_1.get_total_income())
