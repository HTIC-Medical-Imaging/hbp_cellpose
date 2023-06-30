import os
os.makedirs('weights',exist_ok=True)
print(os.environ.get('CELLPOSE_LOCAL_MODELS_PATH'))
os.environ['CELLPOSE_LOCAL_MODELS_PATH']=os.getcwd()+'/weights'

from cellpose.models import Cellpose
from cellpose.io import save_masks
import numpy as np
import pickle
import glob
from datetime import datetime
from tqdm import tqdm

class MmapReader:
    def __init__(self,mmappath):
        info_name = mmappath.replace('.dat','_info.pkl')
        info = pickle.load(open(info_name,'rb'))
        shp = info['shape']
        self.image_ptr = np.memmap(mmappath, dtype='uint8',mode='r',shape=shp)

if __name__=="__main__":

    model = Cellpose(gpu=True, model_type='cyto')

    datadir = '/data/special/jp2cache/'
    for img in tqdm(glob.glob(datadir+'/*_lossless.jp2')):
        arr = MmapReader(img)

        sub = arr.image_ptr[:16000,:16000,:]

        masks, flows, styles, diams = model.eval(sub, diameter=None, channels=[0,0])

        save_masks(sub,masks,flows,img,savedir='/data/output/cellposeoutput')