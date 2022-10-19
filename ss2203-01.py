import os
import pydicom
import matplotlib.pyplot as plt
import argparse
import numpy as np
from PIL import Image
import FileOutput

def main():
    #dicomファイルのリストの取得
    parser = argparse.ArgumentParser()      #コマンド入力でフォルダ名を取得
    parser.add_argument('folder_name')
    args = parser.parse_args()
    path = args.folder_name
    file_name= []
    instance_number = []
    file_count = 0
    for _file_name in os.listdir(path):     #フォルダ内のファイル名を取得し、パスを加える
        file_name.append(path + '/' + _file_name)
        ds = pydicom.read_file(file_name[file_count])
        instance_number.append(int(ds.InstanceNumber))      #インスタンスナンバーを取得する
        file_count += 1 
    order_file_name = []

    #ファイル名を、インスタンスナンバーの昇順に並べ替える
    for index in range(file_count):
        for order in instance_number:
            if order - 1== index:
                order_file_name.append(file_name[instance_number.index(index + 1)])
                ds = pydicom.read_file(order_file_name[index])
            
    dcm_array = []
    ds0 = pydicom.read_file(order_file_name[0])
    ds1 = pydicom.read_file(order_file_name[1])

    rescale_intercept = ds0.RescaleIntercept
    rescale_slope = ds1.RescaleSlope

    pixel_spacing = ds0.PixelSpacing        #解像度
    zdistance = int(ds0.ImagePositionPatient[2]) - int(ds1.ImagePositionPatient[2])     #z方向の解像度

    #3次元画像データの作成
    for dcm in order_file_name:
        ds = pydicom.read_file(dcm)
        dcm_array.append(ds.pixel_array) 
            
    dcm_np_array = np.array(dcm_array)              #配列をnumpy配列に変換する
    if ds0.Modality == 'CT':                        #モダリティがCTの場合に、numpy配列を書き換える
        dcm_np_array = dcm_np_array * rescale_intercept + rescale_slope

    FileOutput.WriteMhd(dcm_np_array, zdistance, pixel_spacing)
    FileOutput.WriteRaw(dcm_np_array,'dcm.raw',np.int16)

if __name__=="__main__":
    main()

