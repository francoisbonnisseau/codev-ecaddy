from Site import *


#test 1 : impossible d'accéder à la page
fnac = Site('fnac', 'https://www.fnac.com', 'https://www.fnac.com/search/quick/', '')
fnac.get_infos('ecouteurs')

# #test 2 : impossible de récupérer les informations : erreurs de sélecteurs
# alternate = Site('alternate', 'https://www.alternate.fr', 'https://www.alternate.fr/listing.xhtml?q=', {'products': '',
#                                                                                                         'name': '.product-name',
#                                                                                                         'brand': '.product-name > span',
#                                                                                                         'price': '.price',
#                                                                                                         'description': '.product-info',
#                                                                                                         'url_product': '.productBox.boxCounter',
#                                                                                                         'url_image': 'img.productPicture'})
# alternate.get_infos('ecouteurs')

# alternate = Site('alternate', 'https://www.alternate.fr', 'https://www.alternate.fr/listing.xhtml?q=', {'products': '.productBox.boxCounter',
#                                                                                                         'name': '',
#                                                                                                         'brand': '.product-name > span',
#                                                                                                         'price': '.price',
#                                                                                                         'description': '.product-info',
#                                                                                                         'url_product': '.productBox.boxCounter',
#                                                                                                         'url_image': 'img.productPicture'})
# alternate.get_infos('ecouteurs')

# alternate = Site('alternate', 'https://www.alternate.fr', 'https://www.alternate.fr/listing.xhtml?q=', {'products': '.productBox.boxCounter',
#                                                                                                         'name': '.product-name',
#                                                                                                         'brand': '',
#                                                                                                         'price': '.price',
#                                                                                                         'description': '.product-info',
#                                                                                                         'url_product': '.productBox.boxCounter',
#                                                                                                         'url_image': 'img.productPicture'})
# alternate.get_infos('ecouteurs')

# alternate = Site('alternate', 'https://www.alternate.fr', 'https://www.alternate.fr/listing.xhtml?q=', {'products': '.productBox.boxCounter',
#                                                                                                         'name': '.product-name',
#                                                                                                         'brand': '.product-name > span',
#                                                                                                         'price': '',
#                                                                                                         'description': '.product-info',
#                                                                                                         'url_product': '.productBox.boxCounter',
#                                                                                                         'url_image': 'img.productPicture'})
# alternate.get_infos('ecouteurs')

# alternate = Site('alternate', 'https://www.alternate.fr', 'https://www.alternate.fr/listing.xhtml?q=', {'products': '.productBox.boxCounter',
#                                                                                                         'name': '.product-name',
#                                                                                                         'brand': '.product-name > span',
#                                                                                                         'price': '.price',
#                                                                                                         'description': '',
#                                                                                                         'url_product': '.productBox.boxCounter',
#                                                                                                         'url_image': 'img.productPicture'})
# alternate.get_infos('ecouteurs')

# alternate = Site('alternate', 'https://www.alternate.fr', 'https://www.alternate.fr/listing.xhtml?q=', {'products': '.productBox.boxCounter',
#                                                                                                         'name': '.product-name',
#                                                                                                         'brand': '.product-name > span',
#                                                                                                         'price': '.price',
#                                                                                                         'description': '.product-info',
#                                                                                                         'url_product': '',
#                                                                                                         'url_image': 'img.productPicture'})
# alternate.get_infos('ecouteurs')

# alternate = Site('alternate', 'https://www.alternate.fr', 'https://www.alternate.fr/listing.xhtml?q=', {'products': '.productBox.boxCounter',
#                                                                                                         'name': '.product-name',
#                                                                                                         'brand': '.product-name > span',
#                                                                                                         'price': '.price',
#                                                                                                         'description': '.product-info',
#                                                                                                         'url_product': '',
#                                                                                                         'url_image': 'img.productPicture'})
# alternate.get_infos('ecouteurs')

# alternate = Site('alternate', 'https://www.alternate.fr', 'https://www.alternate.fr/listing.xhtml?q=', {'products': '.productBox.boxCounter',
#                                                                                                         'name': '.product-name',
#                                                                                                         'brand': '.product-name > span',
#                                                                                                         'price': '.price',
#                                                                                                         'description': '.product-info',
#                                                                                                         'url_product': '.productBox.boxCounter',
#                                                                                                         'url_image': ''})
# alternate.get_infos('ecouteurs')

# Define a list of test parameters
test_parameters = [
    ('alternate', 'https://www.alternate.fr', 'https://www.alternate.fr/listing.xhtml?q=', {
        'products': '.productBox.boxCounter',
        'name': '',
        'brand': '.product-name > span',
        'price': '.price',
        'description': '.product-info',
        'url_product': '.productBox.boxCounter',
        'url_image': 'img.productPicture'
    }),
    ('alternate', 'https://www.alternate.fr', 'https://www.alternate.fr/listing.xhtml?q=', {
        'products': '.productBox.boxCounter',
        'name': '.product-name',
        'brand': '',
        'price': '.price',
        'description': '.product-info',
        'url_product': '.productBox.boxCounter',
        'url_image': 'img.productPicture'
    }),
    ('alternate', 'https://www.alternate.fr', 'https://www.alternate.fr/listing.xhtml?q=', {
        'products': '.productBox.boxCounter',
        'name': '.product-name',
        'brand': '.product-name > span',
        'price': '',
        'description': '.product-info',
        'url_product': '.productBox.boxCounter',
        'url_image': 'img.productPicture'
    }),
    ('alternate', 'https://www.alternate.fr', 'https://www.alternate.fr/listing.xhtml?q=', {
        'products': '.productBox.boxCounter',
        'name': '.product-name',
        'brand': '.product-name > span',
        'price': '.price',
        'description': '',
        'url_product': '.productBox.boxCounter',
        'url_image': 'img.productPicture'
    }),
    ('alternate', 'https://www.alternate.fr', 'https://www.alternate.fr/listing.xhtml?q=', {
        'products': '.productBox.boxCounter',
        'name': '.product-name',
        'brand': '.product-name > span',
        'price': '.price',
        'description': '.product-info',
        'url_product': '',
        'url_image': 'img.productPicture'
    }),
    ('alternate', 'https://www.alternate.fr', 'https://www.alternate.fr/listing.xhtml?q=', {
        'products': '.productBox.boxCounter',
        'name': '.product-name',
        'brand': '.product-name > span',
        'price': '.price',
        'description': '.product-info',
        'url_product': '.productBox.boxCounter',
        'url_image': ''
    })
]

def run_test(site_name, base_url, search_url, selectors):
    try:
        site = Site(site_name, base_url, search_url, selectors)
        site.get_infos('ecouteurs')
    except Exception as e:
        print(f" {site_name}: {e}")
        return True

# Execute all tests
for params in test_parameters:
    run_test(*params)
