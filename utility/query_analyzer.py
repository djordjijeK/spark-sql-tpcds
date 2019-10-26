from configuration.config import config
from configuration.config import PROJECT_PATH
import time


class QueryAnalyzer:

    def __init__(self, spark_instance):
        """
            Returns an instance of the query analyzer
            :param spark_instance
        """
        self.spark_instance = spark_instance
        [
            self.spark_instance.read.parquet(f"{PROJECT_PATH}/spark-warehouse/{config['dbname']}.db/{table}/").createTempView(table)
            for table in config['tables']
        ]

    def run_benchmark(self):
        results = {}
        for i in range(0, 99):
            results[i] = self.analyze_query(i)
            print(f"Query {i} successfully executed")

        file = open(f"{config['queries_path']}/results.txt", 'w')
        file.write(str(results))
        file.close()

    def analyze_query(self, query_number):
        try:
            query = open(f"{config['individual_queries_path']}/query_{query_number}.sql").read()
            subqueries = query.split(';')
            time_elapsed = 0
            for index, subquery in enumerate(subqueries):
                if not subquery == ' ' and not subquery == '':
                    start = time.time()
                    self.spark_instance.sql(subquery).collect()
                    time_elapsed += time.time() - start
        except Exception as exception:
            print(f"Woops! Problem with query {query_number} \n" + str(exception))
            return query_number, None

        return time_elapsed
