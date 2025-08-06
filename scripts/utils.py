import logging
import os
from datetime import datetime

def setup_logger(name):
    os.makedirs("logs", exist_ok=True)
    log_file = os.path.join("logs", f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(name)
