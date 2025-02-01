import logging
import os
from datetime import datetime

file_name = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)
LOG_FILEPATH = os.path.join(log_path, file_name)

logging.basicConfig(level=logging.INFO,
                    filename=file_name,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s "
                    )
