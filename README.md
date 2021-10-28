# ETL with Airflow
## Introduction
This repository contains the code for an [ETL pipeline](https://www.snowflake.com/guides/etl-pipeline) for [OpenStack](https://www.openstack.org/) Logs from [Zenodo](https://zenodo.org/record/3227177) written as a DAG in [Apache Airflow](https://airflow.apache.org/) in Python.

![](https://img.shields.io/badge/mysql-8.0.27-brightgreen)
![](https://img.shields.io/badge/airflow-2.2.0-yellow)

## *DAG?*
* DAGs or Directed Acyclic Graphs is how Airflow collects Tasks together, organized with dependencies and relationships to say how they should run.
* Tasks are the basic building blocks which handle some particular operation like downloading data, checking if files exists, loading the data etc.

Here is the DAG for the code in this repository.

![](https://github.com/DebangshuB/ETL-with-Airflow/blob/main/Images/DAG.jpg)

* It's a very simple DAG (literally a straight list) consisting of the following tasks :-
  * __download__ :- Download the tar.gz file from the download link.
  * __check_file__ :- Check for the existence of the tar.gx file in the file system.
  * __unzip__ :- Unzips the files.
  * __transform__ :- Parses the required data and saves it as a csv file.
  * __load__ :- Creates a .sql file which would load the data into my local [MySQL Server](https://www.mysql.com/).
  * __create_mysql_table__ :- Creates the MySQL table if it doesn't exist.
  * __insert_into_table__ :- Execute the .sql file created in the load step to load the file into the database.
  * __clear__ :- Clears all the extra files created.
  * __success_email__ :- Sends an email to specified email on success.
  * An email is send in case of a faliure aswell.
  * Can be configured to run at any regular interval.

##  Visualizations
Here are some visualizations I was able to make based on the data I mined.


| ![](https://github.com/DebangshuB/ETL-with-Airflow/blob/main/Images/statuscode.jpg) | ![](https://github.com/DebangshuB/ETL-with-Airflow/blob/main/Images/type.jpg) | ![](https://github.com/DebangshuB/ETL-with-Airflow/blob/main/Images/methods.jpg) |
|:--:| :--: | :--: |
| *Status Codes returned* | *Type* | *Methods Used* |


| ![](https://github.com/DebangshuB/ETL-with-Airflow/blob/main/Images/length.jpg) | ![](https://github.com/DebangshuB/ETL-with-Airflow/blob/main/Images/time_taken.jpg)| 
|:--:| :--: |
| *Length Of Message* | *Time Taken* | 

| ![](https://github.com/DebangshuB/ETL-with-Airflow/blob/main/Images/apicalloverdays.jpg) | ![](https://github.com/DebangshuB/ETL-with-Airflow/blob/main/Images/sumcalls.jpg)| 
|:--:| :--: |
| *Number of API Calls over days* | *Number of Calls over Hour Of Day* | 
