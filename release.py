import os
import pickle

from sentence_transformers import SentenceTransformer

import constants

model = SentenceTransformer(constants.MODEL_PATH, device='cpu')

with open(os.path.join(constants.RELEASE_DIR, 'model.pkl'), 'wb') as f:
    pickle.dump(model, f)
