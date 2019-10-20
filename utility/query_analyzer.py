from configuration.config import config
import time


class QueryAnalyzer:

    def __init__(self, spark_instance):
        """
            Returns an instance of the query analyzer
            :param spark_instance
        """
        self.spark_instance = spark_instance
        [
            self.spark_instance.read.parquet(f"../spark-warehouse/{config['dbname']}.db/{table}/").createTempView(table)
            for table in config['tables']
        ]

    def run_benchmark(self):
        results = {}
        for i in range(90, 99):
            results[i] = self.analyze_query(i)
            print(f"Done {i}")

        return results

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
