import re
import os
from  lxml import etree
import xlsxwriter

def get_file(sht):
    item_count = 0
    for filename in os.listdir("Raw/Transcript/Segmented/"): #获取该文件夹下所有内容
        item_count += 1
        f = open("Raw/Transcript/Segmented/"+filename, "r")
        data = f.readlines()
        sentence_count = 0
        print("文件名：",filename)
        sht.write(item_count,0,str(filename)[:11])
        for sentence in data:
            print("正在写：",sentence)
            sentence_count += 1
            if(sentence_count<=10): 
                sht.write(item_count,sentence_count,sentence[8:])
            else:   
                sht.write(item_count,sentence_count,sentence[9:])
            
        f.close()



                
if __name__ == '__main__':
    text_file_name = "text_xls.xls"
    xlstext = xlsxwriter.Workbook("text.xls")
    sht = xlstext.add_worksheet("text.xls")
    get_file(sht)
    xlstext.close()
