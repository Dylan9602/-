首先常見的醫學影像格式有dicom nii nii.gz nrrd，將原始影像轉換為nii.gz格式，便於處理且存儲空間佔用更小。
接下來我們便可以使用change_jpg這隻程式函數將原始影像轉換為jpg圖像。
再來運用拉普拉斯可以增強圖像的細節，找到圖像的邊緣，讓圖像銳化。
