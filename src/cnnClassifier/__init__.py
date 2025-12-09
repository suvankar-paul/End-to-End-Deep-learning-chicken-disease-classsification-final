import os
import sys
import logging
from datetime import datetime

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Directory for logs
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Get count of existing log files for numbering
existing_logs = [f for f in os.listdir(log_dir) if f.endswith(".log")]
log_count = len(existing_logs) + 1

# Create filename as required -> date-time-running_log{n}.log
date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"{date_time}-running_log_{log_count}.log"
log_filepath = os.path.join(log_dir, log_filename)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")
