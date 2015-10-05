from lxml import html
import requests
import time

class AppCrawler:
	
	def __init__(self, starting_url, depth):
		self.starting_url = starting_url
    self.depth = depth
		self.current_depth = 0
    self.depth_links = []
	  self.apps = []
 
	def crawl(self):
    app =  self.get_data_from_link(self.starting_url)
    self.apps.append(app)
    self.dpeth_links.append(app.links)

    while self.current_depth < self.depth:
      current_links = []
      
      for link in self.depth_links[self.current_depth]:
        current_app = self.get_app_from_links(link)
        current_links.extend(current_app.links)
        self.apps.append(current_app)
        time.sleep(3)

      self.current_depth += 1
      self.depth_links.append(current_links)

		return
  
  def get_data_from_link(self, link):
    start_page = requests.get(link)
    tree = html.fromstring(start_page.text)
    
    thing = tree.xpath('//h1[@class="classname"]/text()')[0]
    thing2 = tree.xpath('//div[@class="classname"]/h2/text()')[0]
    thing3 = tree.xpath('//li[@class="classname"]/text()')[0]
    links = tree.xpath('//div[@class="center-div-classname"]//*/a[@class="divname"]/@href')

    app = App(thing, thing2, thing3, links)
    
    return app

class App:

  def __init__(self, thing, thing1, thing2, links):
    self.thing = thing
    self.thing1 = thing1
    self.thing2 = thing2
    self.links = links
    
  def __str__(self):
    return("Thing: " + self.thing.encode('UTF-8') +
    "\r\nThing1: " + self.thing1.encode('UTF-8') +
    "\r\nThing2: " + self.thing2.encode('UTF-8') + "\r\n"

crawler = AppCrawler('www.website.com', 0)
crawler.crawl()

for app in crawler.apps:
  print app
