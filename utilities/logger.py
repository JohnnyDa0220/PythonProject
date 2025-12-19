import os
import logging
from datetime import datetime
from utilities.config_reader import get_properties


class Log:
    @staticmethod
    def capture_logger():
        folder = get_properties('PATH', 'logger_path')
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%H%M%S_%d-%m-%Y")
        file_name = f"log_{timestamp}.log"
        path = os.path.join(folder, file_name)
        logging.basicConfig(
            filename=path,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filemode='a',
            force=True

        )
        return logging.getLogger()
