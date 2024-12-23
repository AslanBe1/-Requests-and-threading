import json
import requests
import psycopg2

url = 'https://dummyjson.com/products'

r = requests.get(url)


db_info = {
    'host':'localhost',
    'port':5432,
    'user':'postgres',
    'password':'123',
    'database':'najot_talim',
}

conn=psycopg2.connect(**db_info)
cur=conn.cursor()

all_posts = r.json().get('products',[])

for product in all_posts:
        cur.execute('''
        INSERT INTO get_json(
            title,
            description,
            category,
            price,
            discountPercentage,
            rating,
            stock,
            tags,
            brand,
            sku,
            weight,
            dimensions,
            warrantyInformation,
            shippingInformation,
            availabilityStatus,
            reviews,
            returnPolicy,
            minimumOrderQuantity,
            meta,
            images,
            thumbnail
        ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        ''', (
            product['title'],
            product['description'],
            product['category'],
            product['price'],
            product['discountPercentage'],
            product['rating'],
            product['stock'],
            json.dumps(product['tags']),
            product.get('brand',''),
            product['sku'],
            product['weight'],
            json.dumps(product['dimensions']),
            product['warrantyInformation'],
            product['shippingInformation'],
            product['availabilityStatus'],
            json.dumps(product['reviews']),
            product['returnPolicy'],
            product['minimumOrderQuantity'],
            json.dumps(product['meta']),
            json.dumps(product['images']),
            product['thumbnail'],
        ))


conn.commit()
cur.close()
conn.close()

print("Data successfully saved to PostgreSQL!")