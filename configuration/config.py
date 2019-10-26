import subprocess

SCALE = 1  # scale for data and queries
PROJECT_PATH = subprocess.check_output('pwd', shell=True).decode("UTF-8").replace('\n', '')  # project path on the file system

config = dict(

    # path to the tpcds tool that generates data and queries
    tpcds_dir="/home/georggie/Downloads/tpcds-kit",

    # database name
    dbname=f'spark_tpcds_scale_{SCALE}',

    # path to the generated data
    data_path=f'{PROJECT_PATH}/dependencies/data',

    # path to the ddl for tables
    tables_path=f'{PROJECT_PATH}/dependencies/ddl/individual',

    # all db tables
    tables=[
        "call_center",
        "catalog_sales",
        "customer_demographics",
        "income_band",
        "promotion",
        "store",
        "time_dim",
        "web_returns",
        "catalog_page",
        "customer",
        "date_dim",
        "inventory",
        "reason",
        "store_returns",
        "warehouse",
        "web_sales",
        "catalog_returns",
        "customer_address",
        "household_demographics",
        "item",
        "ship_mode",
        "store_sales",
        "web_page",
        "web_site"
    ],

    # path to the integrated queries
    queries_path=f'{PROJECT_PATH}/dependencies/queries',

    integrated_queries_file_name='query_0.sql',

    # path to the individual queries
    individual_queries_path=f'{PROJECT_PATH}/dependencies/queries/individual'
)
