# nii nii.gz nrrd原始影像轉jpg
import SimpleITK as sitk
import nibabel as nib
import cv2
import numpy as np

import shutil
import os

#轉換為jpg圖像時,調整窗位窗寬
def window_transform(img, windowWidth, windowCenter):
    minWindow = float(windowCenter) - 0.5*float(windowWidth)
    img = (img - minWindow) / float(windowWidth)
    img[img < 0] = 0
    img[img > 1] = 1
    img = (img * 255).astype('float32')
    return img

#nii nii.gz nrrd的原始影像檔轉換為jpg
#file_path應該是nii nii.gz nrrd文件  to_path應該是一個資料夾
def Niigz2jpg(file_path,to_path,cwckON,cwckcenter,cwckwidth):
    
    n1 = nib.load(file_path)
    n1 = n1.get_fdata()
    
    if(cwckON):
        n1 = window_transform(n1,cwckwidth,cwckcenter)

    if(os.path.exists(to_path)):#若已存在資料夾
        shutil.rmtree(to_path)#則刪除資料夾
    os.mkdir(to_path)#重新創建資料夾
    
    
    for i in range(n1.shape[2]):
        out_path = to_path + '\\' + str(i) + ".jpg"
        nt=cv2.flip(np.rot90(n1[:,:,i],3),1)
        nt = nt.astype('float32')
        cv2.imwrite(out_path,nt)

