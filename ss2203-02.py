
import numpy as np
import matplotlib.pyplot as plt
import FileOutput


def main():

    #ファイルの読み込み
    mhd_path = 'ChestCT/ChestCT.mhd'
    raw_path = 'ChestCT/ChestCT.raw'

    #mhdファイルの読み込み
    with open(mhd_path, "r", encoding="utf-8") as f:
        for line in f:
            if "DimSize" in line:           #x,y,zのサイズを読み込む
                dim_size = line.split()

    height = int(dim_size[2])
    width = int(dim_size[3])
    depth = int(dim_size[4])
    
    #rawファイルの読み込み
    raw = open(raw_path, 'rb')
    img = np.fromfile(raw, dtype = np.uint16, count = depth * height * width)
    img = img.reshape((depth, height, width))
    raw.close() 

    #閾値処理
    thresh = 100
    maxval = 255
    after_image = (img < thresh) * maxval

    # モルフォロジー処理
    eroded_sheet = np.empty((depth, height, width))
    for sheet in range(depth):
        dim2 = after_image[sheet, ...]
        pad_dim2 = np.pad(dim2, 1, 'edge')
        areas = np.lib.stride_tricks.as_strided(pad_dim2, dim2.shape + (3, 3), pad_dim2.strides * 2)
        eroded_dim2 = np.min(areas, axis=(2, 3))
        eroded_sheet[sheet, ...] = eroded_dim2
    FileOutput.write_raw(eroded_sheet,"output.raw",np.uint8)

    
if __name__=="__main__":
    main()
