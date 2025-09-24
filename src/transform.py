from datetime import datetime
from src.extract import extract_custumers, extract_orders, extract_products, extract_categories
from src import ROOT_DIR, processed_path
import pandas as pd



def transform_costumer():
    df = extract_custumers()

    df['cap'] = df['cap'].astype(str).str.zfill(5)
    #df['cap'] = df['cap'].astype(str).apply(lambda value: '00' + value if len(value) == 3 else value)
    #df['cap'] = df['cap'].astype(str).apply(lambda value: '0' + value if len(value) == 4 else value)

    df = df.drop_duplicates()
    df.reset_index(inplace=True)
    df.drop(columns='index', inplace=True)

    df['region'] = df['region'].replace(['Friuli Venezia Giulia', 'Emilia Romagna', 'Trentino Alto Adige'],
                                        ['Friuli-Venezia Giulia', 'Emilia-Romagna', 'Trentino-Alto Adige'],
                                        regex=True)

    temp = "costumers_list"
    cur_date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = temp + "_" + cur_date_time + ".csv"
    df.to_csv(ROOT_DIR / processed_path / file_name, encoding="utf-8", sep=",", index_label="id")



def transform_orders():
    df = extract_orders()

    #df['order_delivered_customer_date'].fillna('0000-00-00 00:00:00', inplace = True)

    df['order_estimated_delivery_date'] = df['order_estimated_delivery_date'].replace(' 00:00:00',
                                        '',
                                        regex=True)

    df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])
    df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

    temp = "orders_list"
    cur_date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = temp + "_" + cur_date_time + ".csv"
    df.to_csv(ROOT_DIR / processed_path / file_name, encoding="utf-8", sep=",", index_label="id")



def transform_products():
    df = extract_products()

    df.fillna({'product_name_length':0,'product_description_length':0, 'product_photos_qty':0}, inplace=True)

    df.fillna({'category' : 'miscellaneous'}, inplace=True)

    df_columns = ['product_name_length','product_description_length','product_photos_qty']
    for i in df_columns:
        df[i] = df[i].astype(int)

    temp = "products_list"
    cur_date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = temp + "_" + cur_date_time + ".csv"
    df.to_csv(ROOT_DIR / processed_path / file_name, encoding="utf-8", sep=",", index_label="id")



def transform_categories():
    df = extract_categories()

    df.rename(columns={'product_category_name_english':'product_english','product_category_name_italian':'product_italian'}, inplace=True)

    df['product_english'] = df['product_english'].replace('fashio_female_clothing','fashion_female_clothing', regex=True)

    new_category = pd.DataFrame([{'product_english':'miscellaneous','product_italian':'generale'}])
    df = pd.concat([df,new_category], ignore_index=True)

    def categorize(item):
        if item in [ 'mobili_decorazione', 'mobili_ufficio']:
            return 'mobili'
        elif item in ['letto_bagno_tavola', 'climatizzazione']:
            return 'articoli per la casa'
        elif item in ['moda_borse_accessori', 'moda_abbigliamento_donna', 'moda_calzature', 'moda_abbigliamento_uomo']:
            return 'moda'
        elif item in ['negozio_animali']:
            return 'animali'
        elif item in ['telefonia', 'informatica_accessori', 'elettronica', 'telefonia_fissa', 'audio']:
            return 'elettronica'
        elif item in ['salute_bellezza', 'profumeria', 'pannolini_igiene']:
            return 'salute e bellezza'
        elif item in ['libri_interesse_generale','libri_tecnici']:
            return 'libri'
        elif item in [ 'articoli_cool', 'orologi_regali']:
            return 'idee regalo'
        elif item in ['industria_commercio_affari']:
            return 'prodotti industriali'
        elif item in ['attrezzi_da_giardino']:
            return 'giardinaggio'
        elif item in ['neonati']:
            return 'articoli per l\'infanzia'
        else:
            return 'generale'

    df['category'] = df['product_italian'].apply(categorize)

    df = df.drop_duplicates()
    df.reset_index(inplace=True)
    df.drop(columns='index', inplace=True)
    #df.rename(columns={'product_category_name_english':'category'}, inplace=True)

    temp = "categories_list"
    cur_date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = temp + "_" + cur_date_time + ".csv"
    df.to_csv(ROOT_DIR / processed_path / file_name, encoding="utf-8", sep=",", index_label="id")





if __name__ == "__main__":
    print(transform_products())