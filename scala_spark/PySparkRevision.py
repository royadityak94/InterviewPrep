"""Quick Revision for Pyspark
Source (Dataframe API): https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PySpark_SQL_Cheat_Sheet_Python.pdf
Source (RDD): https://www.datacamp.com/cheat-sheet/pyspark-cheat-sheet-spark-in-python
"""

################################
#    Dataframe API             #
################################

# Initialize spark session
from pyspark import SparkSession
spark = SparkSession \
    .builder \
    .appName('Demo PySpark App') \
    .config("spark.some.config.option", "some-value")
    .getOrCreate()

# Creating DataFrame from RDDs
from pyspark.sql.types import *

sc = spark.sparkContext 
lines = sc.textFile('file.csv')
parts = lines.map(lambda l: l.split(','))
data_rdd = parts.map(lambda p: Row(name=p[0], age=int(p[1].strip())))
# Create Schema
schemaString = "name,age"
fields = [StructField(field, StringType(), True) for field in schemaString.split(',')]
df = spark.createDataFrame(data_rdd, fields)
df.show()

# Directly from data sources 
df = spark.read.json('xyz.json')
df = spark.read.load('xyz.json', format='json')
df = speark.read.load('xyz.parquet')
df = spark.read.text('xyz.txt')

# Inspecting Data 
df.dtypes # Col names, and their data types
df.show() # Contents of df
df.head(n) # First n rows 
df.first() # First row 
df.take(n) # first n rows 
df.schema # schema of df
df.describe().show() # Compute summary stats.
df.columns # columns of df
df.count() # total row count in df
df.distinct().count() # distinct row count in df
df.printSchema() # Print schema of df
df.explain() # print logical, physical plan

# Duplicate values 
df = df.dropDuplicates()

# Adding, Updating, Removing Columns
df = df.withColumn('city', df.address.city) \
    .withColumn('telePhoneNumber', explode(df.phoneNumber.number)) \
    .withColumn('telePhoneType', explode(df.phoneNumber.type))
# Update
df = df.withColumnRenamed('telePhoneNumber', 'phoneNumber')
# Drop
df = df.drop('address', 'phoneNumber')
df = df.drop(df.address).drop(df.phoneNumber)

# Queries 
from pyspark.sql import functions as F 

df.select('firstName').show()
df.select('col1', 'col2', 'col3').show()
df.select('firstName', 'age', 
    explode('phone').alias('contacts')).select('firstName', 'age', 'contacts.type')
df.select(df['firstName'], df['age']+1)

# Filter 
df.select(df['age'] > 24).show()
df.select('FirstName', F.when(df.age > 25, 1).otherwise(0))
df[df.firstName.isin('Abc', 'Def')].collect()

# Like Operator 
df.select('FirstName', df.lastName.like('Smith')) # df.lastName.startsWith('th')

# Substring
df.select(df.firstName.substr(1, 3).alias('subname')).collect()

# Between
df.select(df.age.between(10, 30)).show()


# Aggregations
df.groupby('age') \
    .count() \
    .show()

# Filter 
df.filter(df['age'] > 24)

# Sorting
df.sort(df.age.desc()).collect()
df.sort('age', ascending= False).collect()
df.orderBy(['age', 'city'], ascending=[0, 1]).collect()

# Missing and Replacing Values 
df.na.fill(50)
df.na.drop()
df.na.replace(10, 20)

# Repartitioning 
df.repartition(10).rdd.getNumPartitions()
df.coalesce(1).rdd.getNumPartitions()

# Temp views 
df.createGlobalTempView('view_name') #.createTempView(''), .createOrReplaceTempView(')

# Query View
df = spark.sql('SELECT * ...')

# Writing & Saving files 
df.select('col1', 'col2').write.save('xyz.parquet')
# .save('xyz.json', format='json')

# Spark Stop
spark.stop()

################################
#           RDD API            #
################################

# From Dataframe 
rdd1 = df.rdd # DF -> RDD
rdd.collect() # list with all RDD elements
# sample: .take(n), .first(), .top(n) -> n: # of elements to be returned
df.toJSON().first() # DF -> RDD of strings 
df.toPandas() # DF -> Pandas DF 

# SparkContext 
from pyspark import SparkContext 
sc = SparkContext(master = 'local[2]')

# Inspect Spark context 
sc.version # Spark Context Version
sc.pythonVer # Python Version
sc.master # Master URL to connect to
str(sc.sparkHome) # Spark path for worker nodes
str(sc.sparkUser()) # Displays Spark users running spark context 
sc.appName # Application Name
sc.applicationId # Application ID
sc.defaultParallelism # Default level of parallelism
sc.defaultMinPartitions # Minimum number of partitions for RDD

# Configurations 
from pyspark import SparkConf, SparkContext 
conf = (SparkConf()
        .setMaster('local')
        .setAppName('My App')
        .set('spark.executor.memory', '1g')
        )
sc = SparkContext(conf= conf)

# PySpark Shell 
./bin/spark-shell --master local[2]
./bin/pyspark --master local[4] --py-files code.py 
./bin/spark-submit /dir1/dir2/../pysparkfile.py

# Loading Data 
textFile = sc.textFile('/x/y/*.txt')
textFile = sc.wholeTextFiles('/x/y/')

# Data load via parallelized collections
rdd = sc.parallelize([('a', 1), ('b', 2)])
rdd = sc.parallelize(range(100))
rdd = sc.parallelize([ 
    ('a', ['x1', 'y1', 'z1']),
    ('b', ['x2', 'y2', 'z2']),
    ('c', ['x3', 'y3', 'z3']),
    ('d', ['x4', 'y4', 'z4']), 
])

# Retrieving RDD information 
rdd.getNumPartitions() # Lists num of partitions
rdd.count() # Count of RDD instances
rdd.countByKey() # Count RDD instance by key
rdd.countByValue() # Count RDD instance by value
rdd.collectAsMap() # Return (key, value) pairs as a dictionary
rdd.sum() # Sum of RDD elements
sc.parallelize([]).isEmpty() # Checks whether RDD is empty

rdd.max(), rdd.min(), rdd.mean(), rdd.stddev(), rdd.variance() # Basically: rdd.stats() # Statistics 
rdd.histogram(n) # Compute histograms by n bins 
rdd.stats() #(count, mean, stdev, max & min)


# Sampling and Filtering
rdd.sample(False, 0.15, 81).collect() # Sample from RDD (witReplacement, fraction, seed)
rdd.filter(lambda x: 'a' in x) # Filter RDD elemens
rdd.distinct().collect() # Distinct RDD values
rdd.keys().collect() # (key, value) RDD's key

# Iterating 
rdd.foreach(lambda pair: print(pair))

# Reduction (reduceByKey, reduce)
rdd.reduceByKey(lambda x, y: x+y) # Merge rdd values for each key
rdd.reduce(lambda a, b: a+b) # Merge all rdd values 

# Grouping 
rdd.groupBy(lambda x: x%2) \
    .mapValues(list) \
    .collect()

rdd.groupByKey() \
    .mapValues(list) \
    .collect()

# Applying Functions 
# Sample Input rdd = [('a', 7), ('b', 2)]
# Applying a function to each RDD element
rdd.map(lambda x: x + (x[1], x[0])).collect() # [('a', 7, 7, 'a'), ('b', 2, 2, 'b')]
# Applying a function to each RDD element and flattending the result 
rdd.flatMap(lambda x: x + (x[1], x[0])) # ['a', 7, 7, 'a', 'b', 2, 2, 'b']
# Applying flatMap to each rdd (k, v) without changing the keys
# I/p: [("a", ["x", "y", "z"]), ("b", ["p", "r"])]
rdd.flatMapValues(lambda x: x) # [('a', 'x'), ('a', 'y'), ('a', 'z'), ('b', 'p'), ('b', 'r')]

# Aggregating Functions
seqOp = (lambda x, y: (x[0] + y, x[1] + 1))
combOp = (lambda x, y: (x[0] + y[0], x[1] + y[1]))
# Aggregate RDD for each partition and then the results
rdd.aggregate((0, 0), seqOp, combOp)
# Aggregate values for each RDD keys
rdd.aggregateByKey((0, 0), seqOp, combOp).collect()
# Aggregate element for each partition, then the results 
rdd.fold(0, add)

# Merge values for each keys
rdd.foldByKey(0, add)




# Mathematical Operations
rdd.substract(rdd_2) # each rdd value from 'rdd' not in 'rdd2'
rdd.substractByKey(rdd2) # return (key, value) pair from rdd which do not match on key in rdd2
rdd.cartesian(rdd2) # Cartesian product of rdd and rdd2 

# Sorting 
rdd.sortBy(lambda x: x[1]).collect()
rdd.sortByKey().collect() # Sort (key, value ) RDD by key 

# Repartitioning 
rdd.repartition(4)
rdd.coalesce(1)


# Saving 
rdd.saveAsTextFile('xyz.txt')
rdd.saveAsHadoopFile('hdfs://namenodehost/parent/child', 'org.apache.hadoop.mapred.TextOutputFormat')

# Stopping
sc.stop()