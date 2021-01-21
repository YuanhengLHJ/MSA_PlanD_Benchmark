from h5py import Dataset, Group, File
from mmsdk import mmdatasdk
with File('CMU_MOSI_Opinion_Labels.csd','r') as f:
	for k in f.keys():
		if isinstance(f[k], Dataset):
			print(f[k].value)
		else:
			print(f[k].name)

file = File('CMU_MOSI_Opinion_Labels.csd')

def show(data):
    print('name ---', data.name)
    if 'value' in dir(data):
        # 有值的话直接打出
        # print(data.shape)

        print(data.value)
    else:
        # 是一个group的话则继续深入
        for k in data:
            show(data[k])


show(file)

            