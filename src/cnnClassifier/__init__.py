import os
import sys
import logging

# 1. Logging ka format set kar rahe hain
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# 2. Logs ke liye directory aur file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)  # Folder banayega agar nahi hai

# 3. Logging configuration setup
logging.basicConfig(
    level=logging.INFO,            # Sirf INFO level aur usse upar ke logs dikhayega
    format=logging_str,             # Upar defined format use karega
    handlers=[
        logging.FileHandler(log_filepath),  # File me log save karega
        logging.StreamHandler(sys.stdout)   # Console me bhi log dikhayega
    ]
)

# 4. Logger object banate hain jisko project me import karke use kar sakte ho
logger = logging.getLogger("cnnClassifierLogger")
