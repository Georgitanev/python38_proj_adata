#!/bin/sh
# go to the spider directory
cd src/parliamentbg/

# getting working directory and print it
CWD="$(pwd)"
echo $CWD

# get date time for testing purposes
# datetime=$(date '+%m_%d_%Y_%H_%M_%S')
# run the spider
#scrapy crawl multi_subject_spider -a debug='True' &> "logs/log_${datetime}.txt"

/usr/local/bin/scrapy crawl parliament_all
