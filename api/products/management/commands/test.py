import os
from os.path import dirname, join
import xml.etree.ElementTree as ET

tree = ET.parse(join(dirname(__file__), 'test_catalog.xml'))
root = tree.getroot()

# categories = []
# for category in root.iter('category'):
#     category_title = category.text
#     category_id = int(category.attrib.get('id'))
#     category_parent_id = category.attrib.get('parentId')
#     if category_parent_id:
#         category_parent_id = int(category_parent_id)
    
#     cat = {'id': category_id, 'title': category_title, 'parent_id': category_parent_id}
    
#     categories.append(cat)

# categories.sort(key=lambda x: x['id'])
# print(categories)

# for offer in root[0].findall('offer'):
#     offer_id = offer.get('id')
#     print(offer)

for offer in root.iter('offer'):
    offer_id = offer.get('id')
    offer_name = offer.find('name').text
    offer_price = offer.find('price').text
    offer_price_begin = offer.find('price_begin').text
    offer_percent = offer.find('percent').text
    offer_category_id = offer.find('categoryId').text
    offer_pictures = [pictures_url.text for pictures_url in offer.findall('picture')]
    offer_vat = offer.find('vat').text
    offer_model = offer.find('model').text
    offer_vendor_code = offer.find('vendorCode').text
    offer_description = offer.find('description').text
    offer_barcode = offer.find('barcode').text
    offer_params = {}
    for param in offer.findall('param'):
        offer_params[param.attrib['name']] = param.text
    

    # print(offer, offer.get('id'), offer.find('name').text)
    # print(offer_pictures)

    # for param in offer.findall('param'):
    #     print(param.attrib, param.text)




