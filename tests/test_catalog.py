from app.rag.catalog import CatalogRetriever
def test_catalog():
    r=CatalogRetriever().search('noise cancelling headphones'); assert r[0]['sku']=='AX-100'
