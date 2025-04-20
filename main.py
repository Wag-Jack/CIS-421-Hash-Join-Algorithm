from ds import makeRelationTable
from hash_join import hash_join
import os

#Main driver function for hash join algorithm
if __name__ == "__main__":
    #Directory hosting CSV files for relation data
    data_dir = './data'

    #Make RelationTable objects based on CSV file contents
    R = list()
    for file in os.listdir(data_dir):
        path = os.path.join(data_dir, file)
        R.append(makeRelationTable(path))

    #Print both created relation tables
    R[0].print_table()
    R[1].print_table()

    #Determine hash join conditions
    join0 = input('Choose what column you\'re joining from R1: ')
    join1 = input('Choose what column you\'re joining from R2: ')

    R1 = (R[0], join0)
    R2 = (R[1], join1)

    #Run hash join algorihtm
    hashJoinedTable = hash_join(R1, R2)

    #Print resulting tables
    hashJoinedTable.print_table()