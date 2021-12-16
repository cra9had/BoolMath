import re


class TruthTable:
    def __init__(self) -> None:
        self.table = []
        self.headers = []

    @staticmethod
    def get_rotated_matrix(matrix:list) -> list:
        """Rotate matrix to 90 degrees clckwise"""
        return list(list(x)[::-1] for x in zip(*matrix))

    @staticmethod
    def get_bin(number: int, length: int) -> str:
        """Returns bin number in format value:length.f"""
        number = bin(number)[2:]
        length_delta = len(number) - length
        if length_delta < 0:
            for _ in range(-length_delta):
                number = "0" + number
        elif length_delta > 0: 
            number = number[:-length_delta]
        return number

    def __repr__(self) -> str:
        str_table = " ".join(header for header in self.headers) + "\n"
        power = len(self.headers)
        for i in range(2**power):
            for j in range(power):
                str_table += self.table[j][i] + " "
            str_table += "\n"

        return str_table

    def solve_instance(self, instance: str):
        impl = re.findall(r"IMP\((.*?)\)", instance)

    def add_column(self, variable: str, values: list):
        self.headers.append(variable)
        self.table.append(values)

    def set_start_columns(self, variables:list) -> None:
        for variable in variables:
            self.headers.append(variable)
            self.table.append([])
        power = len(variables)
        for i in range(2**power):
            number = self.get_bin(i, power)
            for j in range(len(number)):
                self.table[j].append(number[j])


table = TruthTable()
table.set_start_columns(["A", "B", "C", "D"])
print(table)
instance = input(">>> ")
table.solve_instance(instance)
