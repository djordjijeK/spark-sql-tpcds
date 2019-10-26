from configuration.config import PROJECT_PATH
from configuration.config import SCALE
from configuration.config import config
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
        self.project_path = PROJECT_PATH

    def generate_data(self):
        """
        Generate data according to specified scale
        :return: void
        """
        print("============================================================================")
        if os.path.exists(f'{self.project_path}/dependencies/data'):
            shutil.rmtree(f'{self.project_path}/dependencies/data')  # clear data directory
        os.system(f"mkdir {self.project_path}/dependencies/data")  # make data directory
        os.chdir(f'{self.tpcds_dir}/tools/')  # position to tool directory
        command = f"./dsdgen -dir {self.project_path}/dependencies/data -scale {SCALE}"

        print(f"Executing command => {command} .....")
        os.system(command)  # execute command for generating data
        os.chdir(f'{self.project_path}')  # return back to project directory
        print("======================== DATA GENERATED SUCCESSFULLY =======================")

    def generate_queries(self):
        """
        Generate queries according to specified scale
        :return: void
        """
        print("============================================================================")
        if os.path.exists(f'{self.project_path}/dependencies/queries'):
            shutil.rmtree(f'{self.project_path}/dependencies/queries')  # clear data directory
        os.system(f"mkdir {self.project_path}/dependencies/queries")  # make data directory
        os.chdir(f'{self.tpcds_dir}/tools/')  # position to tool directory
        command = f"./dsqgen -directory ../query_templates/ " \
                  f" -output_dir {self.project_path}/dependencies/queries " \
                  f" -scale {SCALE} " \
                  f" -dialect netezza " \
                  f" -input ../query_templates/templates.lst "

        print(f"Executing command => {command} .....")
        os.system(command)  # execute command for generating queries
        os.chdir(f'{self.project_path}')  # return back to project directory
        print("====================== QUERIES GENERATED SUCCESSFULLY ======================")
