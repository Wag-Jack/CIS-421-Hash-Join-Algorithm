#Imports
import csv
import os
import re

#Class to define relation tables
class RelationTable:
    #Initializer
    def __init__(self, name, ts, var_char):
        self.table = list()
        self.table_name = name
        self.tuple_size = ts
        self.variable_identifier = var_char
        
    #Add to RelationTable if tuple is allowed size
    def add(self, tuple):
        if len(tuple) == self.tuple_size:
            self.table.append(tuple)

    #Getter method for the table itself
    def get_table(self):
        return self.table

    #Getter method for the table's name
    def get_table_name(self):
        return self.table_name

    #Return table size (amount of tuples stored)
    def get_table_size(self):
        return len(self.table)
    
    #Get table's variable identifier
    def get_identifier(self):
        return self.variable_identifier
    
    #Print out the table with correct column spacing
    def print_table(self):
        if self.get_table_size() != 0:
            print(f'{self.table_name}:\n|',end='')
            largest_digit_num = len(self.variable_identifier) + int(self.tuple_size / 10) + 1
            for i in self.table:
                for j in i:
                    digits = len(str(j)) - len(self.variable_identifier) + 1
                    if digits > largest_digit_num:
                        largest_digit_num = digits
        
            i = 1
            while i <= self.tuple_size:
                print(f'{' ' * (largest_digit_num - len(self.variable_identifier + str(i)))}{self.variable_identifier}{i}|',end='')
                i += 1
            print()

            for i in self.table:
                print('|',end='')
                for j in i:
                    print(f'{' ' * (largest_digit_num - len(str(j)))}{j}|',end='')
                print()
        else:
            print(f'Table {self.table_name} is empty.')

#Class to define hash tables
class HashTable:
    #Initializer
    def __init__(self, size=3):
        self.size = size
        self.table = [None] * size

    #Hash function method
    def _hash(self, key):
        return key % self.size
    
    #Method to insert entry into hash table
    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [value]
        else:
            self.table[index].append(value)

    #Method to get a tuple from the hash table
    def get_value(self, key):
        index = self._hash(key)
        value = self.table[index]
        return value if value is not None else None
    
#Function to make RelationTable object from CSV files in data directory
def makeRelationTable(filepath):
    with open(filepath, 'r') as data:
        #CSV reader object
        reader = csv.DictReader(data)
        
        #Finding identifiers for the table based on CSV file
        table_name = os.path.splitext(os.path.basename(filepath))[0]
        table_size = int(re.search(r'\d+', reader.fieldnames[-1]).group())
        id =  re.search(r'[a-z]', reader.fieldnames[-1]).group()

        #Create RelationTable object with identifiers
        R = RelationTable(table_name, table_size, id)

        for row in reader:
            #Add each tuple from file into RelationTable
            R.add(tuple(int(i) for i in row.values()))

        return R