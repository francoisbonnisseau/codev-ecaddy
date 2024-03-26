from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

def get_infos(product_name):
    url = f"https://www.materiel.net/recherche/{product_name}"
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    
    products = soup.select('.c-products-list__item')
    data_list = []
    data = {} #? forme {'Nom','Marque,'Prix','Description','Url','Url_image'}
    
    if products:
        for product in products:
            name = product.select_one('.c-product__title')
            if name:
                name = name.get_text(strip=True)
                
            brand = product.select_one('.c-product__title')
            if brand:
                brand = brand.get_text(strip=True).split(" ")[0]
                
            price = product.select_one('.o-product__price')
            if price:
                price = price.get_text(strip=True)
                
            description = product.select_one('.c-product__description')
            if description:
                description = description.get_text(strip=True)
                
            url_product = product.select_one('.c-product__link')
            if url_product:
                url_product = url_product.get('href')
                
            url_image = product.select_one('.c-product__thumb > a > img.img-fluid')
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
    product = "ecouteurs"
    data = get_infos(product_name=product)
    print(data)
    
    
    
    
