'''PySpark Quick Notes
Sources:
1. https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PySpark_Cheat_Sheet_Python.pdf
'''
# Initializing Spark Context
from pyspark import SparkContext
sc = SparkContext(master='local[2]')
# stopping
sc.stop()
#  Saving
rdd.saveAsTextFile('rdd.txt')
rdd.saveAsHadoopFile('hdfs://../..', 'org.apache.hadoop.mapred.TextOutputFormat')

# Inspect SparkContext
sc.version # Version information
sc.pythonVer # Python Version
sc.master # master URL to connect to
str(sc.sparkHome) # Name of spark user running spark context
str(sc.sparkUser()) # application name
sc.appName
sc.applicationId
sc.defaultParallelism # default parallelism level
sc.defaultMinPartitions # default min. partitions for RDD

# Retrieving RDD Informations
rdd.getNumPartitions() # List total partitions
rdd.count() # count RDD instances
rdd.countByKey() # count RDD instances by key #  defaultdict(<type 'int'>,{'a':2,'b':1})
rdd.countByValue() # defaultdict(<type 'int'>,{('b',2):1,('a',2):1,('a',7):1})
rdd.sum() # sum of rdd elements
sc.parallelize(rdd).isEmpty() # check if RDD is empty

# Configuration
from pyspark import SparkConf, SparkContext
conf = (SparkConf()
        .setMaster('local')
        .setAppName('Test')
        .set('spark.executor.memory', '1g'))
sc = SparkContext(conf = conf)

# Data Load
rdd = sc.parallelize([('a', 7), ('a', 2)])
rdd = sc.parallelize(range(100))
rdd = sc.parallelize([("a", ['x', 'y', 'z']),
                       "b", ['p', 'r']
                    ])
# External Data: HDFS/S3/Others
textFile = sc.textFile('/my/directory/*.txt')
textFile2 = sc.wholeTextFiles('/my/directory/')

# Applying functions
rdd.map(lambda x: x + (x[1], x[0])).collect() # Applying function to each RDD element
rdd.flatMap(lambda x: x + (x[1], x[0])) #  Applying function to each RDD element, then flatten the result
rdd.collect() # collect all the values to single machine as a list
rdd.flatMapValues(lambda x: x).collect() # Applying flatMap to each key,value pair without changing keys

# Selecting Data
rdd.take(n) # take first n elements
rdd.first()
rdd.top(n) # take top n elements
rdd.sample(False, 0.15, 81).collect() # sampled subset of rdd, length = 0.15*n
# Filtering
rdd.filter(lambda x: 'a' in x).collect()
rdd.distinct().collect()
rdd.keys().collect() # Return (key, value) RDD keys
# Iteration
def g(x): print(x)
rdd.foreach(g)

# Repartitioning
rdd.repartition(4) # New RDD with 4 partitions
rdd.coalesce(1) # Decrease RDD partitions to 1

# Mathematical Operations
rdd.substract(rdd1).collect() # return each value in 'rdd' not contained in 'rdd1'
rdd.substractByKey(rdd1).collect() # return each (key, value) in rdd not matching with 'rdd1'
rdd.cartesian(rdd2).collect() # cartesian product of rdd & rdd2
rdd.sortBy(lambda x: x[1]).collect() # sort rdd by given function
rdd.sortByKey().collect() # sort (key, value) rdd by key

# Reshaping
rdd.reduceByKey(lamda x, y: x+y).collect() # merge rdd values by key: (k1: (v1, v2, ..), k2: (v3, v4, ..))
rdd.reduce(lambda x, y: x+y) # merge rdd values

# Grouping by
rdd.groupBy(lambda x: x % 2).mapValues(list).collect() # Return RDD of grouped values
rdd.groupByKey().mapValues(list).collect() # Group rdd by key

# Aggregation - Need more context //TODO:
'''
aggregate() lets you take an RDD and generate a single value that is of a different type than what was stored in the original RDD. Parameters:
zeroValue: The initialization value, for your result, in the desired format.
seqOp: The operation you want to apply to RDD records. Runs once for every record in a partition.
combOp: Defines how the resulted objects (one for every partition), gets combined.
'''
seqOp = (lambda x, y: (x[0] + y, x[1] + 1))
combOp = (lambda x, y: (x[0] + y[0], x[1]+y[1]))
rdd.aggregate((0, 0), seqOp, combOp)
rdd.aggregateByKey((0, 0), seqOp, combOp).collect() [('a', (9, 2)), ('b', (2, 1))]
rdd.fold(0, add) # 4950
rdd.foldByKey(0, add).collect() # [('a', 9), ('b', 2)]
rdd.KeyBy(lambda x: x+x).collect() # Tuple of RDD element


# Using Spark Shell
./bin/spark-shell --master local[2] # which master, the 'spark master' should connect to
./bin/pyspark --master local[4] --py-files code.py #commma separated list of py files added to runtime path
# Executing Spark Script
./bin/spark-submit path/to/file.py
