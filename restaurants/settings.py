# Scrapy settings for restaurants project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'restaurants'

SPIDER_MODULES = ['restaurants.spiders']
NEWSPIDER_MODULE = 'restaurants.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'restaurants (+http://www.yourdomain.com)'
