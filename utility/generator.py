from configuration.config import config
from configuration.config import SCALE
import shutil
import os


class Generator:
    """
    This class is responsible for generating both queries and data for specified scale.
    """

    def __init__(self):
        """
        Returns an instance of Generator class
        """
        self.tpcds_dir = config['tpcds_dir']
        self.project_path = config['project_path']

    def generate_data(self):
        """
        Generate data according to specified scale
        :return: void
        """
        shutil.rmtree(f'{self.project_path}/dependencies/data')  # clear data directory
        os.system(f"mkdir {self.project_path}/dependencies/data")  # make data directory
        os.chdir(f'{self.tpcds_dir}/tools/')  # position to tool directory
        command = f"./dsdgen -dir {self.project_path}/dependencies/data -scale {SCALE}"

        print(f"Executing command => {command} .....")
        os.system(command)  # execute command for generating queries
        os.chdir(f'{self.project_path}')  # return back to project directory
