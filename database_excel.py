
import xlwt
import pymysql


_host = 'localhost'
_db = 'reportesmensajeros'
_user = 'root'
_password = ''
_table = 'category'
_excel_name = 'ReporteExcelDB'


conn = pymysql.connect(host=_host,user=_user,password=_password,db=_db,charset='utf8')
cursor = conn.cursor()
count = cursor.execute('select id,username,student_no from %s'%_table);
cursor.scroll(0,mode='absolute')
print('has %s line'%count);

ret = cursor.fetchall();
 

fields = cursor.description

excel = xlwt.Workbook()

sheet = excel.add_sheet(_excel_name,cell_overwrite_ok=True)

for k,v in enumerate(fields):
  sheet.write(0,k,v[0])

for key,value in enumerate(ret):
  for kk,vv in enumerate(value):
    sheet.write(key+1,kk,vv)
 
excel.save('./%s.xlsx'%_excel_name)

