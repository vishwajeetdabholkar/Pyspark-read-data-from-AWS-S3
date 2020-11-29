#set Aws seceret id and key
aws_id = 'your_id'
aws_key = 'your_key'

# configure hadoop with s3 creds
sc._jsc.hadoopConfiguration().set("fs.s3n.awsAccessKeyId", aws_id)
sc._jsc.hadoopConfiguration().set("fs.s3n.awsSecretAccessKey", aws_key)

sdf = spark.read.option("header", "true").csv("s3n://path_to_your_bucket_or_folder/test.csv")

sdf.show()
