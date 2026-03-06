# we can not compare np.nan===np.nan
import numpy as np

arr=np.array([1,2,np.nan,4,6])
print(np.isnan(arr))

# removing nan values 
cleaned_aray=np.nan_to_num(arr,nan=100)
print(cleaned_aray)

# handle infinite values 
arr2=np.array([1,2,np.inf,4,-np.inf,6])
print(np.isinf(arr2))
# removing inf values 
cleaned_arr=np.nan_to_num(arr2,posinf=100,neginf=-100)
print(cleaned_arr)