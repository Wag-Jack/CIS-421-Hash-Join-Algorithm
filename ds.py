class RelationTable:
    def __init__(self, name, ts, var_char):
        self.table = list()
        self.table_name = name
        self.tuple_size = ts
        self.variable_identifier = var_char
        
    def add(self, tuple):
        if len(tuple) == self.tuple_size:
            self.table.append(tuple)

    def get_table(self):
        return self.table

    #Size based on number of tuples to conserve memory
    def get_table_size(self):
        return len(self.table)
    
    def get_identifier(self):
        return self.variable_identifier
    
    def print_table(self):
        print(f'{self.table_name}:\n|',end='')
        table_size = len(self.table)
        largest_digit_num = len(self.variable_identifier) + int(self.tuple_size / 10) + 1
        for i in self.table:
            for j in i:
                digits = len(str(j)) - 2
                if digits > largest_digit_num:
                    largest_digit_num = digits
        
        i = 1
        while i <= table_size:
            print(f'{' ' * (largest_digit_num - 2)}{self.variable_identifier}{i}|',end='')
            i += 1
        print()

        for i in self.table:
            print('|',end='')
            for j in i:
                print(f'{' ' * (largest_digit_num - len(str(j)))}{j}|',end='')
            print()


class HashTable:
    def __init__(self, size=3):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return key % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [value]
        else:
            self.table[index].append(value)

    def get_value(self, key):
        index = self._hash(key)
        value = self.table[index]
        return value if value is not None else None