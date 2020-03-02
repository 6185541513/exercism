
class Matrix:
    def __init__(self, matrix_string):
        # create rows
        self.rows = [[int(elem) for elem in row] for row in [rows_unformatted.split() for rows_unformatted in matrix_string.splitlines()]]

        # create columns
        self.columns = []
        number_of_columns = len(self.rows[0])  # ugly but "works"..
        for i in range(number_of_columns):  # 'i' keeps track of which index to use from each row to build the column
            column = []
            for row in self.rows:
                column.append(row[i])
            self.columns.append(column)

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]
