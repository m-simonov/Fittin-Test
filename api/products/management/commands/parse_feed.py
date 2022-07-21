import xml.etree.ElementTree as ET
from os.path import dirname, join

from django.core.management import BaseCommand
from products.models import Category, Offer, OfferPicture, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        tree = ET.parse(join(dirname(__file__), 'feed/test_catalog.xml'))
        root = tree.getroot()

        categories = []
        for category in root.iter('category'):
            category_title = category.text
            category_id = int(category.attrib.get('id'))
            category_parent_id = category.attrib.get('parentId', None)
            if category_parent_id:
                category_parent_id = int(category_parent_id)

            categories.append({
                'id': category_id,
                'title': category_title,
                'parent_id': category_parent_id
            })
        categories.sort(key=lambda x: x['id'])

        categories_models = {}
        for category in categories:
            category_id = category.get('id')
            categories_models[category_id] = Category(
                pk=category_id,
                title=category.get('title'),
                parent_category=categories_models.get(
                    category.get('parent_id', None), None)
            )
        try:
            Category.objects.bulk_create([*categories_models.values()])
        except:
            Category.objects.bulk_update(
                [*categories_models.values()], ['title', 'parent_category'])

        products = {}
        models = []
        for offer in root.iter('offer'):
            model = offer.find('model').text
            name = offer.find('name').text
            if model not in models:
                product_obj = Product(
                    name=name[:-3],
                    percent=offer.find('percent').text,
                    vat=offer.find('vat').text,
                    model=offer.find('model').text,
                    vendor_code=offer.find('vendorCode').text,
                    description=offer.find('description').text,
                    price=offer.find('price').text,
                    price_begin=offer.find('price_begin').text,
                )
                product_obj.save()
                categories = Category.objects.filter(
                    id__in=[int(i.text) for i in offer.findall('categoryId')])
                product_obj.category.set(categories)
                product_obj.save()
                products[model] = product_obj
                models.append(model)

            offer_params = {}
            for param in offer.findall('param'):
                offer_params[param.attrib['name']] = param.text
            offer_obj = Offer(
                barcode=offer.find('barcode').text,
                name=name,
                available=bool(offer.get('available')),
                params=offer_params
            )
            product_obj = products[model]
            product_obj.offers.add(offer_obj, bulk=False)
            offer_obj.save()

            pictures = []
            for picture in offer.findall('picture'):
                pictures.append(OfferPicture(
                    offer=offer_obj, picture_url=picture.text))
            offer_obj.pictures.add(*pictures, bulk=False)
