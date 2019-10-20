from utility.query_analyzer import QueryAnalyzer
from utility.generator import Generator
from boostrap.bootstraper import App

generator = Generator()  # Generator of data and queries
generator.generate_data()
generator.generate_queries()

application = App()  # Boostrap TPC-DS banchmark
application.create_database()  # Set up new database in order to run benchmark on it
application.create_queries()  # Generate queries to be run on database

query_analzer = QueryAnalyzer(application.spark)
results = query_analzer.run_benchmark()
# results = query_analzer.analyze_query(66)