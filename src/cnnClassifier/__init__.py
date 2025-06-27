
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
 
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)


logger = logging.getLogger("phishingdomainLogger")




"""Summary:
This code sets up a logging system that writes log messages both to a file (logs/running_logs.log) and to the console.
The log messages include timestamps, severity levels, module names, and actual log content.
By using the logger (logger), you can now log information, warnings, or errors from various parts of your application. 
Here's an example of how to use the logger:

logger.info("This is an info message.")
logger.error("This is an error message.")
Benefits:
Tracking: This helps keep track of what's happening during the execution of the code.
Debugging: Logs can be very useful when debugging issues or understanding program flow.
Error Reporting: By saving logs, you can look back at issues that happened in the past."""