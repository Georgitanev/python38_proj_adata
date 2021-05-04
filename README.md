# python38_proj_adata
 Scrapy scraper
 
 It uses python 3.8 
 Install requirements with:
 ```
 pip install -r requirements.txt
 ```
It saves urls with additional information for all deputats.
To run the scraper type:
```
cd src
```
```
cd parliamentbg
```
#### This Project creates a database.db file and table in it with columns for inserting all data.
##### With this command it downloading all records for all persons In Database
```
scrapy crawl parliament_all
```
##### With this command it downloading all records for all persons In Database and in json file
```
scrapy crawl parliament_all -O test_crawler.json
```

#### Usage of dict_to_json.py
This file generating json files:
With long and short names of parties, to use them like dictionary when spyder running
```
parties_dictionary_new.json
```
Json schema for data validation and strict e-mail validation
```
json_schema_with_email.json
```
When I generate them, I move them in https://github.com/Georgitanev/python38_proj_adata/tree/main/src/parliamentbg/parliamentbg/spiders
folder.
