## Generate-reports-using-Wikipedia-API-
This repo generates various reports about the updates being done on Wikipedia website by using the Wikipedia Streaming API. 

## How it works
reports function is called every one minute and prints the "Total number of Wikipedia Domains updated" and the sorted "Users who made changes to en.wikipedia.org".

bonusreportsfunction works similar to the reports function but in case of 1 minute it prints the the "Total number of Wikipedia Domains updated" and the sorted "Users who made changes to en.wikipedia.org" based on the data received in last 5 minutes. 

### Installation 

pip install sseclient

###  To Run the file

` python3 file.py`
