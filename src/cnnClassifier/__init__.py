'''os: This module is used for interacting with the operating system, such as file handling and directory management.
sys: This module provides access to system-specific parameters and functions.
 Here, it will be used to send logs to the console (stdout).
logging: This module is the built-in Python module for creating log messages.
 It's very useful for debugging and tracking execution.
'''
import os
import sys
import logging



'''This string specifies the format of the log messages. The placeholders will be replaced with actual log information:
%(asctime)s: The time when the log message was created.
%(levelname)s: The log level (INFO, DEBUG, WARNING, ERROR, etc.).
%(module)s: The name of the module (the file where the log is coming from).
%(message)s: The actual log message.
'''
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
 



"""log_dir = "logs": Defines the name of the directory where log files will be stored.
log_filepath: Creates the full path for the log file, combining the directory log_dir and the file name "running_logs.log".
os.makedirs(log_dir, exist_ok=True): Ensures the directory logs is created.
 If it already exists, the exist_ok=True prevents any error.
 """
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)



"""level=logging.INFO: Sets the logging level to INFO, 
which means it will capture all log messages with level INFO or higher (i.e., INFO, WARNING, ERROR, CRITICAL).
format=logging_str: Uses the custom log format string (logging_str) defined earlier.
handlers=[...]: Defines where the logs will be output:
logging.FileHandler(log_filepath): This handler writes log messages to the file located at log_filepath (logs/running_logs.log).
logging.StreamHandler(sys.stdout): This handler prints log messages to the console (stdout).
"""
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)



"""logging.getLogger("phishingdomainLogger"): Creates or retrieves a logger named "phishingdomainLogger". 
This logger is used to generate log messages. 
Having a named logger allows you to manage and organize logs for different parts of a large program.
"""
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