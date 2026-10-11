import numpy as np
def detect_outliers_zscore(values,threshold=2.0):
    a=np.array(values)
    mean=np.mean(a)
    std=np.std(a)
    z=np.abs((a-mean)/std)
    return a[z>threshold].tolist()
metrics=[10.0,12.0,12.0,13.0,12.0,11.0,14.0,100.0,12.0]
print(detect_outliers_zscore(metrics))