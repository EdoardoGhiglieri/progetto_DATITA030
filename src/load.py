import os
from dotenv import load_dotenv
import psycopg

load_dotenv()
host = os.getenv("dbhost")
db = os.getenv("dbname")
port = os.getenv("dbport")
user = os.getenv("dbuser")
password = os.getenv("dbpw")



def load_costumers():

    with psycopg.connect(host=host,
                        dbname=db,
                        user=user,
                        password=password,
                        port=port) as conn:
        with conn.cursor() as cur:
            sql = """
            CREATE TABLE IF NOT EXISTS costumers
            (
                costumer_id character varying(32) PRIMARY KEY,
                region character varying,
                city character varying,
                cap character varying(5)
            );"""

            cur.execute(sql)
        conn.commit()

def load_sellers():

    with psycopg.connect(host=host,
                        dbname=db,
                        user=user,
                        password=password,
                        port=port) as conn:
        with conn.cursor() as cur:
            sql = """
            CREATE TABLE IF NOT EXISTS sellers
            (
                seller_id character varying(32) PRIMARY KEY,
                region character varying
            );"""

            cur.execute(sql)
        conn.commit()

def load_categories():

    with psycopg.connect(host=host,
                        dbname=db,
                        user=user,
                        password=password,
                        port=port) as conn:
        with conn.cursor() as cur:
            sql = """
            CREATE TABLE IF NOT EXISTS categories
            (
                category character varying PRIMARY KEY,
                category_ita character varying
            );"""

            cur.execute(sql)
        conn.commit()

def load_products():

    with psycopg.connect(host=host,
                        dbname=db,
                        user=user,
                        password=password,
                        port=port) as conn:
        with conn.cursor() as cur:
            sql = """
            CREATE TABLE IF NOT EXISTS products
            (
                product_id character varying(32) PRIMARY KEY,
                category character varying ,
                product_name_length integer,
                product_description_length integer,
                product_photos_qty integer
            );"""

            cur.execute(sql)
        conn.commit()

def load_items():

    with psycopg.connect(host=host,
                        dbname=db,
                        user=user,
                        password=password,
                        port=port) as conn:
        with conn.cursor() as cur:
            sql = """
            CREATE TABLE IF NOT EXISTS items
            (
            order_id character varying(32),
            order_item character varying,
            product_id character varying(32),
            seller_id character varying(32),
            price integer,
            freight integer
            );"""

            cur.execute(sql)
        conn.commit()

def load_orders():

    with psycopg.connect(host=host,
                        dbname=db,
                        user=user,
                        password=password,
                        port=port) as conn:
        with conn.cursor() as cur:
            sql = """
            CREATE TABLE IF NOT EXISTS orders
            (
                order_id character varying(32) PRIMARY KEY,
                customer_id character varying(32) UNIQUE,
                order_status character varying,
                order_purchase_timestamp timestamp without time zone,
                order_delivered_customer_date timestamp without time zone,
                order_estimated_delivery_date date
            );"""

            cur.execute(sql)
        conn.commit()


if __name__ == "__main__":
    load_items()
    load_costumers()
    load_categories()
    load_sellers()
    load_orders()
    load_products()


