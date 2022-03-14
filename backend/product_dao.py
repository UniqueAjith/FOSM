from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM food_ordering.products"
    cursor.execute(query)
    response=[]
    for (product_id,name,quanity,price_per_quanity) in cursor:
        response.append({'product_id':product_id,'name':name,'quanity':quanity,'price_per_quanity':price_per_quanity})
    return response

def insert_new_product(connection,product):
    cursor = connection.cursor()
    query = "INSERT INTO products (name,quanity,price_per_quanity) VALUES (%s,%s,%s)"
    data = (product['name'],product['quanity'],product['price_per_quanity'])
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid

def delete_product(connection,product_id):
    cursor = connection.cursor()
    query = "DELETE FROM products WHERE product_id ="+str(product_id)
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))