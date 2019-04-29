#coding:utf-8
import time
import xlsxwriter

class Loginfo(object):
    def __init__(self, path = '', mode = 'w'):
        fname = path + time.strftime('%y%m%d', time.gmtime())
        self.log = open(path + fname + '.txt', mode)
    
    def log_init(self, sheetname, *title):
        pass
    
    def log_write(self, msg):
        self.log.write(msg)
        
    def log_close(self):
        self.log.close()
        
#生成Excel测试报告
class Xlloginfo(object):
    #传一个目录名
    def __init__(self, path = '', mode = ''):
        #生成文件的名称
        fname = path + time.strftime('%y-%m-%d', time.gmtime())
        self.row = 0
        self.xl = xlsxwriter.Workbook(path+fname+'.xlsx')
        #将有错误的背景色变红色
        self.style = self.xl.add_format({'bg_color':'red'})
        
    def xl_write(self, *args):
        col = 0
        style = ''
        if 'error' in args:
            style = self.style
        for val in args:
            self.sheet.write_string(self.row, col, val, style)
            col += 1
        self.row += 1
    
    #初始化，数据表的名称及第一行的内容
    def log_init(self, sheetname, *title):
        self.sheet = self.xl.add_worksheet(sheetname)
        #列宽
        self.sheet.set_column('A:E', 30)
        self.xl_write(*title)
        
    def log_write(self, *args):
        self.xl_write(*args)
    def log_close(self):
        self.xl.close()
        
        
if __name__ == '__main__':
#     log = Loginfo()
#     log.log_write('test Loginfo 测试')
#     log.log_close()
    #测试
    xinfo = Xlloginfo()
    xinfo.log_init('test', 'uname', 'upwd', 'ucode', 'result', 'info')
    xinfo.log_write('123', '123', 'error', 'Error')
    xinfo.log_close()
