#!/bin/sh
bash start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /BigData_Q2_1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /BigData_Q2_1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /BigData_Q2_1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal /BigData_Q2_1/shot_logs.csv /BigData_Q2_1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file /BigData_Q2_1/mapper.py -mapper /BigData_Q2_1/mapper.py \
-file /BigData_Q2_1/reducer.py -reducer /BigData_Q2_1/reducer.py \
-input /BigData_Q2_1/input/* -output /BigData_Q2_1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /BigData_Q2_1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /BigData_Q2_1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /BigData_Q2_1/output/
bash stop.sh

