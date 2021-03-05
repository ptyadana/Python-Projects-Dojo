# Starting a new scrapy project

In command line,
`scrapy startproject <project_name>` For example: `scrapy startproject article_crawler`

# File Structure

- scrapy.cfg: configuration files
- itesm.py: define the objects that we are scraping
- middlewares.py: contains various Scrapy hooks.
- Pipelines.py defined functions that create and filter items.
- settings.py: contains project settings.
- spiders directory: power house of Scrapy Project.

# Start Scraping

## Generate spider

- 1.go to name_scraper folder
- `scrapy genspider <scraper_name> <url>` example - `scrapy genspider ietf pythonscraping.com` or `scrapy genspider wikipedia en.wikipedia.org`
- 2.change url in `start_urls` and do necessary changes

## Run spider

- go to spider folder and run `scrapy runspider <spider_name>` Example: `scrapy runspider ietf.py`

---

# HTML selecting with Xpath

### directly go from root to that specific tag

/html/body/div/h1

instead use below,
//h1

//div/h1 => immediate child of div tags

//div//h1 => select h1 anywhere under div tag (not necessarily be immediate child)

### elements selected using attributes

//span[@class='title] => select span class which has class title.

//span[@class='title]/@id => select id of the span class which has title class.

//span[@class='title']/text() => select value of span class which has title class.

### getting info of meta data

//meta[@name='name_of_meta_data']/@content

### directly getting text without html tags

import w3libs.html
w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get())

---

## Scraping Articles

## Article Class

- we can define custom classes in `items.py`. For example, when we are crawling wiki, we are crawling articles and may want to store the records. For this case, we can define class to store information.

## Recording information directly to Class

When we save the information from crawler as file, there are 3 different ways.

- giving setting via command line
- adding settings in settings.py for Global settings
- adding settings directly in crawler or spider py class for local settings

### 1) Saving as CSV file / Json etc using command line

- `scrapy runspider <crawler_name.py> -o <file_name.csv> -t csv -s CLOSESPIDER_PAGECOUNT=10`
- For example: `scrapy runspider wikipedia.py -o articles.csv -t csv -s CLOSESPIDER_PAGECOUNT=10`
- we can change file extension and type as `json` instead of `csv` if we want to store in json format
  - `-o articles.csv`: write the output of the results into that file
  - `-t csv`: as extension csv
  - `-s CLOSESPIDER_PAGECOUNT=10`: spider will stop after crawling 10 pages by using setting `-s`

### Using FEED_URI and FEED_FORMAT

- `scrapy runspider wikipedia.py -s FEED_URI=articles.csv -s FEED_FORMAT=csv`
- it does the same thing as above command
- we can also put those information in settings.py file directly.

### 2) Using settings.py for all global settings

- as giving setting via command is not convinent, we can use **settings.py** instead to put all the configurations that we want.

### 3) Local settings for specific scraper or crawler

- we can also put those settings directly in crawler.py file as local settings. These settings will overwrite the global settings.
