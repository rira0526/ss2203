import numpy as np
#mhdファイルの作成
def WriteMhd(dcm_np_array, zdistance, pixel_spacing):       #引数は、numpy配列と、解像度
    with open('dcm.mhd', 'w') as f:
        datalist = ['ObjectType = Image\n']
        datalist.extend(['NDims = ', str(dcm_np_array.ndim), '\n'])
        datalist.extend(['DimSize = ', str(dcm_np_array.shape[0]), ' ', str(dcm_np_array.shape[1]), ' ', str(dcm_np_array.shape[2]), '\n'])
        datalist.extend(['ElementType = MET_SHORT', '\n'])
        datalist.extend(['ElementSpacing = ',str(pixel_spacing[0]), ' ', str(pixel_spacing[1]), ' ', str(zdistance), '\n'])
        datalist.extend(['ElementByteOrderMSB = False', '\n'])
        datalist.extend(['ElementDataFile = test.raw', '\n'])
        f.writelines(datalist)

#rawファイルへの書き出し
def WriteRaw(dcm_np_array,output_file_name,e_type):     #引数は、numpy配列と、出力ファイル名と、型
    f = open(output_file_name, 'wb')
    f.write(dcm_np_array.astype(e_type))            
    f.close()