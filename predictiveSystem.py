# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
loaded_model=pickle.load(open('C:/Users/Sanjana/OneDrive/Desktop/Kiran_python/machineLearning/trained_model.sav','rb'))
input_data=(4,110,92,0,0,37.6,0.191,30)
input_numpy_array=np.asarray(input_data,dtype='float')
#reshape is done because our model knows 786 rows but we are giving 1 row
input_reshape=input_numpy_array.reshape(1,-1)

value=loaded_model.predict(input_reshape)
print(value)
if value[0]==0:
  print("IT is a diabetic person")
else:
  print("It is not a diabetic person")