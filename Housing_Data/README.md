# Housing Data 

 I got historical data from 2010 to now but alot of houses 
are newer than 2010 so they don't have that data. I got about 850 houses on the market 
currently from Denver. The data frame has an attribute with the neighborhood so we should
group them by that and by year to get an idea of what is going on.

# ** ANY CSV FOR HOUSING IS IN DATA FOLDER**


# PLEASE DO NOT TOUCH DATA IN "ORIGINAL_DATA_NO_TOUCH"
Those are originals from initial web scrapping that took 4 hours to get because I 
had to do it slowly to avoid the CAPTCHA robot stuff. Those should serve as backups.

**scrapper.py** -  gets the initial data that we need, currently grabs 25 pages worth of data
so about 1000 houses in the denver are but some are duplicates so about 860 houses

**house_details** - iterates through houses and grabs historical data by opening a firefox web browser and 
pressing the table button for historical data. Has "time.sleep()" parameters sprinkled around 
to make it seem more "human" to avoid captcha. Firefox is runnning headless so you can comfortably
run in background 

**url_done.txt** - the urls for all the houses that I was able to get historical data from

**data.csv** - house data with historical zillow estimated prices 


