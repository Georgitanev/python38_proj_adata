# python38_proj_adata
 Scrapy scraper
 
 It uses python 3.8 
 Install requirements with:
 ```
 pip install -r requirements.txt
 ```

#### In installation folder
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
When I generate parties_dictionary_new.json and json_schema_with_email.json file, I move them in https://github.com/Georgitanev/python38_proj_adata/tree/main/src/parliamentbg/parliamentbg/spiders
folder.

It saves urls with additional information for all deputats.

#### Note: There are .xml files but # xml on /3013 not working properly. So use .xlsx files to get info.

#### It download .xlsx files with information.

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

##### To run under linux (manual or crontab) use this .sh script:

https://github.com/Georgitanev/python38_proj_adata/blob/main/crawl.sh

### Django rest API

django rest api plus serialisation and parameter endpoints

Added swagger documentations with these endpoints:

```
http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/
```

It saves urls with additional information for all deputats.
To run the scraper type:

```
cd MyApi
python manage.py runserver
```

##### after running it you can find rest api endpoints in local address:
``` 
http://127.0.0.1:8000/
```

#### Django rest api with serialisation and get method endpoints:

##### Get requests only
##### No Authentication required - Allow Any 
##### All records in json format - limit 10 records per page


```
first-app/list/
```
##### Search option for:
```
"pp"  - party short name - example '?search=GERP'
"dob" - date of birth short - example '?search=19721025' 
```
```
first-app/list2/?mp=21          - id = '21'
first-app/list2/?pp=GERP        - party short name 'GERP'
first-app/list2/?dob=19760217   - short date of birth '19760217'
```
##### Search by name:
```
first-app/search/?search=ИВА
```


