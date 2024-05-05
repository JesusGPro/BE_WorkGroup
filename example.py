import sqlite3

table_name = 'BE_table_followupbe'
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()
query = cursor.execute(f"SELECT * FROM {table_name}").fetchall()
connection.close()

kg_m3 =[]
for value in query:
    if value[2]=='ADIT 3N' or value[2]=='ADIT 3':
        kg_m3.append(round(value[15] / 119.44, 2))
    else:
        kg_m3.append(round(value[15] / 169.33, 2))

records =[]
for i in range(len(query)):
    records.append([query[i][0], query[i][1], query[i][2], query[i][3], query[i][4], query[i][5], query[i][6], query[i][7], query[i][8],
               query[i][9], query[i][10], query[i][11], query[i][12], query[i][15], kg_m3[i], query[i][16]])
    

print(records[0],records[1])
