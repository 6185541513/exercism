
class Matrix:
    def __init__(self, matrix_string):
        # create rows
        self.rows = [[int(elem) for elem in row] for row in [rows_unformatted.split() for rows_unformatted in matrix_string.splitlines()]]

        # create columns
        self.columns = []
        self.columns = []
        for i in range(len(self.rows)):  # i = length of columns
            column = []
            for j in range(len(self.rows[i])):  # j = number of columns
                column.append()
        self.columns.append(column)

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]
