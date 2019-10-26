from bootstrap.bootstraper import App
from utility.generator import Generator
from utility.query_analyzer import QueryAnalyzer

generator = Generator()  # Generator of data and queries
generator.generate_data()
generator.generate_queries()

application = App()  # Boostrap TPC-DS banchmark
application.create_database()  # Set up new database
application.preprocess_queries()  # Preprocess queries before running

query_analzer = QueryAnalyzer(application.spark)  # Get an instance of query analyzer
query_analzer.run_benchmark()  # Finally run a banchmark
