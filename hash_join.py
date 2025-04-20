from ds import RelationTable, HashTable
import re

#Build method for Hash Join algorithm
def build(table, column):
    #Initialize build table as a HashTable object
    buildTable = HashTable()

    #Get the column to create build table from based on smaller table's column condition
    index = int(re.search(r'\d+', column).group()) - 1

    #Insert each tuple into hash table
    for row in table.get_table():
        key = row[index]
        buildTable.insert(key, row)

    #Return build table
    return buildTable

#Probe method for Hash Join algorithm
def probe(initialBuild, probe, build, j1, j2):
    #Get the identifiers for the resultant table
    resultant_size = initialBuild.get_tuple_size() + probe.get_tuple_size()
    resultant_identifier = initialBuild.get_identifier() + probe.get_identifier()

    #Get the name for the resultant table after probing
    resultant_name = initialBuild.get_table_name() + probe.get_table_name()
    char_identifier = re.findall(r'[a-zA-Z]', resultant_name)
    resultant_name = re.sub(char_identifier[0], '', resultant_name)
    resultant_name = char_identifier[0] + resultant_name
    
    #Create resultant RelationTable object
    resultant = RelationTable(resultant_name, resultant_size, resultant_identifier)
    
    #Get the selected column index for the probe table
    right_index = int(re.search(r'\d+', j2).group()) - 1

    #Go through each row of probe table to find join condition from build table
    for row in probe.get_table():
        
        #Determine if the current probe table column value is a key in the hash table
        key = row[right_index]
        if build.get_value(key) is not None:

            #Get the selected column index for the build table and find its bucket
            left_index = int(re.search(r'\d+', j1).group()) - 1
            buildRef = build.get_value(key)

            #Go through each tuple in the bucket
            for t in buildRef:
                insertRelation = list()
                
                #Combine the tuples from both tables if the build table's value matches the bucket's key
                if t[left_index] == key:    
                    for i in t: #initial buildTable
                        insertRelation.append(i)
                
                    for i in row: #probeTable
                        insertRelation.append(i)
                
                #Ensure we are not adding an empty tuple
                if len(insertRelation) > 0:
                    resultant.add(tuple(insertRelation))

    #Return the resulting table
    return resultant

#Hash Join algortihm's driver function
def hash_join(R1, R2):
    #Get the size of both tables
    r1 = R1[0].get_table_size()
    r2 = R2[0].get_table_size()

    #Build table will be the table with less tuples
    if r1 <= r2:
        buildTable = build(R1[0], R1[1])
        return probe(R1[0], R2[0], buildTable, R1[1], R2[1])
    else:
        buildTable = build(R2[0], R2[1])
        return probe(R2[0], R1[0], buildTable, R2[1], R1[1])