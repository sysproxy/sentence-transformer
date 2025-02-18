import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')
RELEASE_DIR = os.path.join(BASE_DIR, 'release')

MODEL_NAME = 'distiluse-base-multilingual-cased-v2'
MODEL_PATH = os.path.join(RESOURCES_DIR, MODEL_NAME)
