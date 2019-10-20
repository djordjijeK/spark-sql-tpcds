import subprocess

SCALE = 1   # specified scale of data and queries
queries_path = '../dependencies/queries'  # path to the generated integrated queries

config = dict(

    # determine project directory
    project_path=subprocess.check_output('dirname $PWD', shell=True).decode("UTF-8").replace('\n', ''),

    # path to the tpcds tool that generates data and queries
    tpcds_dir="/home/georggie/Downloads/tpcds-kit",

    # database name
    dbname=f'spark_tpcds_scale_{SCALE}',

    data_path='./dependencies/data',

    tables_path='./dependencies/ddl/individual',

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

    queries_path=queries_path,

    integrated_queries_file_name='query_0.sql',

    individual_queries_path=f"{queries_path}/individual"
)
