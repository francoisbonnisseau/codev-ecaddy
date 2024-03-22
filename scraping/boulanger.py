from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}


def get_infos_boulanger(product_name):
    root = "https://boulanger.com"
    url = f"https://www.boulanger.com/resultats?tr={product_name}"
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    
    products = soup.select('.product-list__item')
    data_list = []
    data = {} #? forme {'Nom','Marque,'Prix','Description','Url','Url_image'}
    
    if products:
        for product in products:
            name = product.select_one('.product-list__product-label').text
            brand = product.select_one('.product-list__product-label > strong').text
            price = product.select_one('.price__amount').text
            description = product.select_one('.keypoints').text
            url_product = root + product.select_one('.product-list__product-image-link').get('href')
            url_image = product.select_one('product-list__product-image').get('src')
            
            try:
                data = {
                    'Nom' : name,
                    'Marque' : brand,
                    'Prix' : price,
                    'Description' :description,
                    'Url' : url_product,
                    'Url_image' : url_image
                }
                
                data_list.append(data)
                
            except:
                #if a variable is not defined
                #! raise an error
            
            
            
    
    
    
