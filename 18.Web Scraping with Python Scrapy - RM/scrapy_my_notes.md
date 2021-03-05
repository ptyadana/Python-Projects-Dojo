# Starting a new scrapy project

In command line,
`scrapy startproject <project_name>`

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
- `scrapy genspider <scraper_name> <url>` example - `scrapy genspider ietf pythonscraping.com`
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
