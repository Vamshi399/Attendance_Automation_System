import mysql.connector
from DBConnection import DBConnection
from openpyxl import Workbook
wb = Workbook()
SQL = 'SELECT dt,rollno,name,sts from  attendance'
database = DBConnection.getConnection()
cur = database.cursor()
cur.execute(SQL)
results = cur.fetchall()
ws = wb.create_sheet(0)
ws.title = "Attendance"
ws.append(cur.column_names)

for row in results:
        ws.append(row)

workbook_name = "Reports"
wb.save(workbook_name + ".xlsx")