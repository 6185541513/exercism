import math


class Matrix:
    def __init__(self, matrix_string):
        # create rows
        rows_string = [[int(elem) for elem in row] for row in [rows_unformatted.split() for rows_unformatted in matrix_string.splitlines()]]

        for elem in rows_string:
            print("!!!!!!!!!!!"+str(elem))

        # create columns
        number_of_columns = len(rows_string[0])
        columns_string = []
        for i in range(number_of_columns):
            column = []
            for row in rows_string:
                column.append(row[i])
            columns_string.append(column)

        # string -> int
        self.rows = list(map(int, rows_string))
        self.columns = list(map(int, columns_string))

    def row(self, index):
        return self.rows[index]

    def column(self, index):
        return self.columns[index]
