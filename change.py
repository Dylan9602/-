
# DICOM文件轉換為NII NII.GZ NRRD格式
import SimpleITK as sitk
import nibabel as nib
import cv2
import numpy as np

import shutil
import os

#dicom即資料夾存儲的dcm尾碼文件轉為nii或nii.gz或nrrd格式
#dicom資料夾目錄  niipath:要保存的檔案名
#修改niipath文件的尾碼名為.nii .nii.gz .nrrd實現三種格式的保存

def dcm2niigz(dcmpath, niipath):
    reader = sitk.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(dcmpath)
    reader.SetFileNames(dicom_names)
    image2 = reader.Execute() 

    image_array = sitk.GetArrayFromImage(image2)
    origin = image2.GetOrigin()
    spacing = image2.GetSpacing()
    direction = image2.GetDirection()
    image3 = sitk.GetImageFromArray(image_array)
    
    image3.SetSpacing(spacing)
    image3.SetDirection(direction)
    image3.SetOrigin(origin)
    
    sitk.WriteImage(image3, niipath)  

oripath = r'C:\Users\QDUMIAO\Desktop\dicom'  #dicom資料夾
savepath1 = r'C:\Users\QDUMIAO\Desktop\ori.nii'  #轉換為nii
savepath2 = r'C:\Users\QDUMIAO\Desktop\ori.nii.gz'  #轉換為nii.gz
savepath3 = r'C:\Users\QDUMIAO\Desktop\ori.nii.nrrd'  #轉換為nrrd

dcm2niigz(oripath,savepath1)
dcm2niigz(oripath,savepath2)
dcm2niigz(oripath,savepath3)
