from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}


def get_infos(product_name):
    root = "https://boulanger.com"
    url = f"https://www.boulanger.com/resultats?tr={product_name}"
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    
    products = soup.select('.product-list__item')
    data_list = []
    data = {} #? forme {'Nom','Marque,'Prix','Description','Url','Url_image'}
    
    if products:
        for product in products:
            name = product.select_one('.product-list__product-label')
            if name:
                name = name.get_text(strip=True)
                
            brand = product.select_one('.product-list__product-label > strong')
            if brand:
                brand = brand.get_text(strip=True)
                
            price = product.select_one('.price__amount')
            if price:
                price = price.get_text(strip=True)
                
            description = product.select_one('.keypoints')
            if description:
                description = description.get_text(strip=True)
                
            url_product = product.select_one('.product-list__product-image-link')
            if url_product:
                url_product = root + url_product.get('href')
                
            url_image = product.select_one('img.product-list__product-image')
            if url_image:
                url_image = url_image.get('src')
            
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
                print("problem")
    
    return data_list
               
          
            
if __name__ == "__main__":
    product = "ordinateur"
    data = get_infos(product_name=product)
    print(data)
    
    
    
    
