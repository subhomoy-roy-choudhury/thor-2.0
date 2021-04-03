from speech import *
import pandas as pd
import time 
import progressbar   #pip install progressbar
  


feature_list =['patient_id','patient_age','patient_gender','patient_bp','patient_hr']
param=[0 for j in range(5)]

'''
patient_id = param[0]
patient_age = param[1]
patient_gender = param[2]
patient_bp = param[3]
patient_hr= param[4] 
'''
def heart_disease_predict():
    widgets = [' [', 
         progressbar.Timer(format= 'elapsed time: %(elapsed)s'), 
         '] ', 
           progressbar.Bar('*'),' (', 
           progressbar.ETA(), ') ', 
          ] 
  
    # bar = progressbar.ProgressBar(max_value=4,  
    #                           widgets=widgets).start() 
    i=0
    with progressbar.ProgressBar(max_value=4,widgets=widgets) as bar:
        while(i<=4):
            if i==2:
                a=gender_input(feature_list[i])
                if (a!=None):
                    param[i]=a
                    i=i+1
            else:
                a=float_input(feature_list[i])
                if (a!=None):
                    param[i]=a
                    i=i+1
            bar.update(i-1) 
    print(param,type(param[1]))
    # unpickle Model
    
    model = pd.read_pickle(r'pretrained_models/new_model.pickle')
    # Prediction through parameters
    result = model.predict([[param[0],param[1],param[2],param[3],param[4]]])  # input must be 2D array
    print(result)
    if result=='Heart-Disease':
        talk("You have Heart Disease")
    else:
        talk("You don't have Heart Disease")
