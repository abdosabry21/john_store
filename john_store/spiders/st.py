import scrapy


class StSpider(scrapy.Spider):
    name = "st"
    allowed_domains = ["gopher1.extrkt.com"]
    start_urls = ["https://gopher1.extrkt.com"]

    def parse(self, response):
        product_url=response.xpath('//ul[@class="products columns-4"]/li/a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]/@href')
        for url in product_url:
            yield scrapy.Request(url=url.get(),method="GET",callback=self.product_parse)
        
        
        
        for i in range(2, 13):
            ur = f'https://gopher1.extrkt.com/?paged={i}'
            print(
                "##############################################################################")
            print(ur)
            yield response.follow(ur, callback=self.parse)
        
        
        
        
        
        
        
        
        
        
        
        
    def product_parse(self , response):
        type_of_product=response.xpath('//nav[@class="woocommerce-breadcrumb"]/a/text()').getall()
        # print(type_of_product)
        f_type_of_product='/'.join(type_of_product)
        # print(f_type_of_product)
        
        
        title=response.xpath('//h1/text()').get()
        price='£'+ response.xpath('(//bdi/text())[1]').get()
        
        # print(title)
        # print(price)
        
        
        
        
        short_description=response.xpath('//div[@class="woocommerce-product-details__short-description"]/p/text()').get()
        # print(short_description)
        
        size=response.xpath('(//td[@class="woocommerce-product-attributes-item__value"])[1]/p/text()').get()
        Color=response.xpath('(//td[@class="woocommerce-product-attributes-item__value"])[2]/p/text()').get()
        # print(size)
        # print(Color)
        
        
        SKU=response.xpath('//span[@class="sku_wrapper"]/span/text()').get()
        # print(SKU)
        
        
        
        Category=response.xpath('//span[@class="posted_in"]/a/text()').get()
        
        # print(Category)
        
        Description=response.xpath('//div[@class="woocommerce-Tabs-panel woocommerce-Tabs-panel--description panel entry-content wc-tab"]/p/text()').getall()
        
        # print(Description)
        f_Description="\n".join(Description)
        print(f_Description)
        
        
        yield {
            "title":title,
            "price":price,
            "size":size,
            "Color":Color,
            "SKU":SKU,
            "Category":Category,
            "short description":short_description,
            "Description":f_Description,
            "path":f_type_of_product,
        }
        
        