# Pyspark-read-data-from-AWS-S3
Simple pyspark code to connect to AWS and read a  csv file from S3 bucket

To connect to AWS services, for example AWS S3 we need to add 3 jars into our spark.
You can find them attached to this repo.

All you need to do is copy those jars into your spark folder.
The location will be like:  
"spark-3.0.1-bin-hadoop2.7/jars". Paste the jars under this location.
Set the aws secret key and id and configure Spark session accordingly using sc._jsc.hadoopConfiguration().set().

Once you are done setting up the environment just go ahead and read any csv or parquet file from your S3 bucket.
for example: 

sdf = spark.read.option("header", "true").csv("s3n://your_bucket_path/test.csv")
