import pandas as pd
import os
import logging
# Setup logging
log_filename = "result/loading.log"
os.makedirs("result", exist_ok=True)
logging.basicConfig(
    filename=log_filename, level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)