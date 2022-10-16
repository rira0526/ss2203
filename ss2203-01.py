import os
import pydicom
import dicom
import matplotlib.pyplot as plt

#dicomファイルのリストの取得
path = "HeadCtSample_2022"
file_name= []
InstanceNumber = []
file_count = 0
for _file_name in os.listdir(path):
    file_name.append(path + '/' + _file_name)
    ds = pydicom.read_file(file_name[file_count])
    InstanceNumber.append(ds.InstanceNumber)
    file_count += 1 
print(InstanceNumber)
print(file_count)

# ds = pydicom.read_file(files[0])
# root_dir = './HeadCtSample_2022'
# dcms = []
# for d, s, fl in os.walk(root_dir):
#     for fn in fl:
#         if ".dcm" in fn.lower():
#             dcms.append(os.path.join(d, fn))
# ref_dicom = dicom.read_file(dcms[0])
# d_array = np.zeros((ref_dicom.Rows, ref_dicom.Columns, len(dcms)), dtype=ref_dicom.pixel_array.dtype)
# for dcm in dcms:
#     d = dicom.read_file(dcm)
#     d_array[:, :, dcms.index(dcm)] = d.pixel_array

# path_list = glob.glob(ChestCT + '\*')
# print(path_list)

# name_list = []
#     for i in path_list:
#         file = os.path.basename(i)          
#         name, ext = os.path.splitext(file)  
#         name_list.append(name)              
#     return path_list, name_list
# _data=pd.DataFrame()


# for file, name in zip(path_list,name_list):
#     tmp=pd.read_csv(file)
#     _data=pd.concat([_data,tmp],sort=True)


# import pydicom
# path = pydicom.data.get_testdata_file('1.2.276.0.7230010.3.1.4.296485376.1.1521714580.2081598.dcm')
# dataset = pydicom.filereader.dcmread(path)
# print(type(dataset))

# import matplotlib.pyplot as plt
# import numpy as numpy
# import pydicom

# dcm_data =  pydicom.dcmread('1.2.276.0.7230010.3.1.4.296485376.1.1521714580.2081598.dcm')
# img = dcm_data.pixel_array
# plt.imshow(img, cmap = "gray", vmax = 100, vmin = 0)
# plt.show()