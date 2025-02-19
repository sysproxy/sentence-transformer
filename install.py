from sentence_transformers import SentenceTransformer

import constants

model = SentenceTransformer(f'sentence-transformers/{constants.MODEL_NAME}', device='cpu')
model.save(constants.MODEL_PATH)

print(f'Model saved to {constants.MODEL_PATH}')
