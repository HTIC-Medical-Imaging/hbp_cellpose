import os
os.makedirs('weights',exist_ok=True)
# print(os.environ.get('CELLPOSE_LOCAL_MODELS_PATH'))
os.environ['CELLPOSE_LOCAL_MODELS_PATH']=os.getcwd()+'/weights'

from cellpose.models import Cellpose

if __name__=="__main__":

    model = Cellpose(gpu=True, model_type='cyto')
