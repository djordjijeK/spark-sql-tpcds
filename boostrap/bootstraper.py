from boostrap.query_parser import QueryParser
from configuration.config import config
from pyspark.sql import SparkSession
import shutil


class App:
    def __init__(self):
        self.spark = SparkSession.builder.getOrCreate()  # Get spark instance
        self.spark.conf.set("spark.sql.crossJoin.enabled", "True")  # Enable cartesian product
        self.spark.sparkContext.setLogLevel("ERROR")

    def create_database(self):
        self.spark.sql(f"DROP DATABASE IF EXISTS {config['dbname']} CASCADE")  # drop database in cascade mode (tables -> db)
        self.spark.sql(f"CREATE DATABASE {config['dbname']}")  # create database from zero
        self.spark.sql(f"USE {config['dbname']}")  # get database context
        print(f"Successfully created database **{config['dbname']}**")
        self.import_tables()  # finally import tables

    def import_tables(self):
        shutil.rmtree('./spark-warehouse')  # drop database storage
        for table in config['tables']:
            self.create_table(table)

    def create_table(self, table_name):
        print(f'Creating table: **{table_name}**')
        self.spark.sql(f'DROP TABLE IF EXISTS {table_name}')
        file, content = self.spark.sparkContext.wholeTextFiles(f"{config['tables_path']}/{table_name}.sql").collect()[0]
        sqlStatements = content.replace('\n', ' ') \
            .replace("${TPCDS_GENDATA_DIR}", config['data_path']) \
            .replace("csv", "org.apache.spark.sql.execution.datasources.csv.CSVFileFormat").split(';')
        for sqlStatement in sqlStatements:
            if not sqlStatement == '' and not sqlStatement == ' ':
                self.spark.sql(sqlStatement)

    def preprocess_queries(self):
        QueryParser(config['integrated_queries_file_name']) # Call QueryParser in order to properly generate queries
