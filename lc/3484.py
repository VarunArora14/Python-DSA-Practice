from curses.ascii import isalpha


# Better version
class Spreadsheet:
    def __init__(self, rows: int):
        self.mapper = {}

    def setCell(self, cell: str, value: int) -> None:
        self.mapper[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.mapper:
            self.mapper[cell] = 0

    def getValue(self, formula: str) -> int:
        [first, second] = formula[1:].split("+")
        val1, val2 = 0, 0
        if first[0].isalpha():
            val1 = self.mapper.get(first, 0)
        else:
            val1 = int(first)

        if second[0].isalpha():
            val2 = self.mapper.get(second, 0)
        else:
            val2 = int(second)

        # print("val1", val1, "val2", val2)
        return val1 + val2


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
