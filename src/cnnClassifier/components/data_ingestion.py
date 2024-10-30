"""os: Provides functions to interact with the operating system, such as checking for files and creating directories.
urllib.request as request: Allows us to make HTTP requests, particularly used here for downloading files from a URL.
zipfile: A module to handle ZIP file operations, like extracting ZIP files.
logger: Assumed to be a logging utility from the cnnClassifier package, which helps log information
             about the file download and extraction processes.
get_size: A utility function for calculating the file size, likely to log the size of existing files.
DataIngestionConfig: A configuration class that contains settings such as the data source URL, local file path,
                    and directory for extracted files.
Path: A part of pathlib for easier path manipulations (e.g., creating Path objects instead of using raw strings for paths)."""
import os
import urllib.request as request
import shutil
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

"""This class, DataIngestion, is designed to handle two main tasks: downloading a data file and extracting it if it’s a ZIP file.
__init__: The constructor takes a DataIngestionConfig object, which holds the necessary configuration for data ingestion 
                                                                            (e.g., URLs, file paths, and directories). 

The self.config variable is used to store this configuration for access in other methods."""

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config




    """Checks for File Existence: If the file specified by self.config.local_data_file does not already exist,
        it proceeds to download it. This prevents re-downloading the file if it's already present locally.
        Downloads the File: Uses request.urlretrieve to download the file from self.config.source_URL and 
                                          saves it to the location specified by self.config.local_data_file.
        filename: The path where the file is saved.
        headers: HTTP headers of the downloaded file.
        Logging: Logs the download details if the file was downloaded successfully, or logs the existing file's size if it already exists.
        Exception Handling: Logs an error if the download fails and returns False."""
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

# Copy the downloaded file to the new path (unzip path)
        self.save_to_unzip_path()


    """Create Directory if Needed: Ensures that the directory for unzipped files (self.config.unzip_dir) exists, creating it if necessary.
        Extract ZIP File: Opens the downloaded file (self.config.local_data_file) as a ZIP archive using zipfile.
                                               ZipFile and extracts its contents into unzip_path.
        Logging: Logs the completion of the extraction with the location of extracted files.
        Exception Handling: If the file is not a valid ZIP file (e.g., it's corrupted or an incorrect format), it logs an error and returns False."""

    # def extract_zip_file(self):
    #     """
    #     zip_file_path: str
    #     Extracts the zip file into the data directory
    #     Function returns None
    #     """
    #     unzip_path = self.config.unzip_dir
    #     os.makedirs(unzip_path, exist_ok=True)
    #     with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
    #         zip_ref.extractall(unzip_path)
        

    def save_to_unzip_path(self):
        """
        Saves the downloaded file to the specified unzip path.
        """
        # Ensure the unzip directory exists
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        # Define the destination path
        destination_path = os.path.join(unzip_path, os.path.basename(self.config.local_data_file))
        
        # Copy the file if it doesn't already exist at the destination
        if not os.path.exists(destination_path):
            shutil.copy(self.config.local_data_file, destination_path)
            logger.info(f"File copied to {destination_path}")
        else:
            logger.info(f"File already exists at {destination_path}, skipping copy.")