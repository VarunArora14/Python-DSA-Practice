from curses.ascii import isalpha


class Spreadsheet:
    def __init__(self, rows: int):
        alphabets = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]
        self.mapper = {}
        for a in alphabets:
            self.mapper[a] = [0 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        alphabet = cell[0]
        rowNumber = int(cell[1:])
        self.mapper[alphabet][rowNumber] = value

    def resetCell(self, cell: str) -> None:
        alphabet = cell[0]
        rowNumber = int(cell[1:])
        self.mapper[alphabet][rowNumber] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        [first, second] = formula.split("+")
        val1, val2 = 0, 0
        if first[0].isalpha():
            alphabet = first[0]
            rowNumber = int(first[1:])
            val1 = self.mapper[alphabet][rowNumber]
        else:
            val1 = int(first)

        if second[0].isalpha():
            alphabet = second[0]
            rowNumber = int(second[1:])
            val2 = self.mapper[alphabet][rowNumber]
        else:
            val2 = int(second)

        print("val1", val1, "val2", val2)
        return val1 + val2


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
