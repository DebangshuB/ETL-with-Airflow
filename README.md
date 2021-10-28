# ETL with Airflow
## Introduction
Apache Airflow is an open-source workflow management platform. 

This repository contains the code for an [ETL pipeline](https://www.snowflake.com/guides/etl-pipeline) for [OpenStack Logs](https://zenodo.org/record/3227177) written as a DAG in Airflow.

## *DAG?*
DAGs or Directed Acyclic Graphs is how Airflow collects Tasks together, organized with dependencies and relationships to say how they should run.

Tasks are the basic building blocks which handle some particular operation like downloading data, checking if files exists, loading the data etc.
