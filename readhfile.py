from h5py import Dataset, Group, File
from mmsdk import mmdatasdk
import xlsxwriter
import datetime



file = File('CMU_MOSI_Opinion_Labels.csd','r')
shtl = 0

def iterRead(sht,data,layer_count,layer_name,item_name=''):

    print("层数：",layer_count,"name---",data.name)
    if layer_count <10:
        if 'value' in dir(data):
            print("正在解析叶子节点")
            if layer_name=='features':
                print("这是feature of ",item_name)
                global shtl 
                shtl += 1 
                sign = 0
                sht.write(shtl,0,item_name)
                for per_value in data.value:
                    sign += 1
                    if per_value <-2:               
                        sht.write(shtl,sign,-3)
                    elif per_value <-1:
                        sht.write(shtl,sign,-2)
                    elif per_value <0:
                        sht.write(shtl,sign,-1)
                    elif per_value <= 0 and 0 <= per_value:
                        sht.write(shtl,sign,0)
                    elif per_value <=1:
                        sht.write(shtl,sign,1)
                    elif per_value <=2:
                        sht.write(shtl,sign,2)
                    else: 
                        sht.write(shtl,sign,3)

        else:
            for layer in data:
                if layer_count == 3 : iterRead(sht,data[layer],layer_count+1,layer,layer_name)
                else : iterRead(sht,data[layer],layer_count+1,layer)
                


                


#label_file = 
def show(data):
    if 'value' in dir(data):
        # 有值的话直接打出
        print("叶子节点，",data.shape)

        #print("上部分",data.value)
    else:
        # 是一个group的话则继续深入
        for k in data:
            
            show(data[k])



if __name__ == '__main__':
    shtl = 0
    label_file_name = "label_2.xls"
    xlsresult = xlsxwriter.Workbook(label_file_name)
    sht = xlsresult.add_worksheet(label_file_name)

    sht.write(0, 0, '编号')
    for i in range(1,30):
        sht.write(0, i, i)
    iterRead(sht,file,0,'root','')
    xlsresult.close()




'''with File('CMU_MOSI_Opinion_Labels.csd','r') as f:
	for k in f.keys():
		if isinstance(f[k], Dataset):
			print(f[k].value)
		else:
			print(f[k].name)'''

            