import os
import urllib.request as request
import zipfile
from src.textSummarizer.logging import logger
from src.textSummarizer.entity import DataIngestionConfig
import shutil

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file   
            )
            logger.info(f"file is downloaded")

        else:
            logger.info(f"file already exists")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        try:
            shutil.unpack_archive(self.config.local_data_file, unzip_path)
            logger.info(f"Unzipped dataset to: {unzip_path}")
        except Exception as e:
            logger.error(f"Failed to unzip: {e}")
            raise e             
