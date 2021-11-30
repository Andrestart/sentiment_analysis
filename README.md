# Sentiment analysis project

The objective of this project is making an API that filters a previously created database in SQL. This database has been downloaded from Kaggle and then, it has been cleaned and prepared for inserting the data to create a database in SQL. You can see below the schema I made in SQL.

![](https://github.com/Andrestart/sentiment_analysis/blob/main/schema.PNG)

After creating the database, I have created the API that filters that database. This way, we can get only what a character says and also their sentiment analysis, that provides how positive and how subjective the speech is, ranging from -1 to 1.

[Click here to see the API documentation.](https://github.com/Andrestart/sentiment_analysis/blob/main/infoapi.md)

In order to do that, I have followed these steps:
* Getting the dataset where I got the dialogues from([click here to download it](https://www.kaggle.com/xvivancos/star-wars-movie-scripts)).
* Cleaning and processing the dataset. You can find follow the cleaning process in the jupyter notebook inside "notebooks" folder in the file "1_cleaning_dataset.ipynb".  You can get the cleaned dataset in the "cleandf.csv" file, in "tables" folder.
* Creating a schema and a database in SQL that follows my files' structure. You can find the database creation script in the file "swtables" in "tables" folder.
* Inserting the values in the database. You can see how these values are inserted in "notebooks/2_sql_insert.ipynb", which takes its functions from "tools/sql_tools_insert_db".
* Creating the API in "main .py", getting the functions from "tools.sql_tools_insert_api".

I have used the following libraries(click on them to see their documentation):
* [pandas](https://pandas.pydata.org/docs/)
* [SQL alchemy](https://docs.sqlalchemy.org/en/14/)
* [sys](https://docs.python.org/3/library/sys.html)
* [textblob](https://textblob.readthedocs.io/en/dev/)
* [markdown.extensions.fenced_code](https://python-markdown.github.io/extensions/fenced_code_blocks/)
* [flask](https://flask.palletsprojects.com/en/2.0.x/)
* [os](https://docs.python.org/3/library/os.html)