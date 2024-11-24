# ETL Project 

to-do:
- add table of contents
- add "Lessons Learned" section 
- add additional documentation of data assets (DAGs, ERDs, data dictionary, key audience for assets, etc.)
- add "Executive Summary" section for different personas (C-Suite, Middle Management, direct stakeholders, possible other end-users
- add "Limitations and Considerations" (things that can be improved + things to add)
- add "So What?" section that explores why builing out well-designed ETL pipelines are important
  

# Project Description

ETL project that uses three Python scripts to make requests to the Mockaroo API so that data can be programmatically generated and downloaded as .csv files. These data files, located in *_data folders, will later be ingested into MySQL Workbench and transformed using dbt.

# Project Goal

To develop and showcase an end-to-end data pipeline that handles data generation/sourcing, storage, transformation and downstream use cases (BI reporting needs).

# Project Tasks

The tasks of this learning project are:

1) Use an API and Python scripts to automatically generate several csv files based on user input.
2) Use dbt Seeds to bring data files into a local database that can be observed through MySQL Workbench.
3) Use dbt to create transformed tables based on Bronze-Silver-Gold architecture pattern.
4) Use dbt features like macros and tests to ensure that data quality checks catch errors/issues before downstream applications.
5) (planned) Use an orchestrator tool (like Dagster) to automate the previous four tasks. 
7) Use Tableau to create reporting dashboards that show period-over-period changes of metrics like A, B, C which are essential for X, Y, Z business functions.

# Tools 

- Mockaroo API
- Python 
- MySQL
- dbt
- ChatGPT 
