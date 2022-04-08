import scrapy  
s="https://www.sitelike.org/similar/"
a=[]
with open("websites.txt",'r') as file:    
    for line in file:       
        for word in line.split():          
            a.append(s+word+"/")
class firstSpider(scrapy.Spider): 
    name='first'
    allowed_domains = ["sitelike.org"] 
   
    start_urls = a
    def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)
            
    def parse(self, response): 
        for sel in response.xpath('//ul/li'):
            link = sel.xpath('a/@href').extract()
        print(link)
        
