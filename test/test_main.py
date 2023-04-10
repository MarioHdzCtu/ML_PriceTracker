import pytest
from mains import Item, StoreNotRegistered

test_link = "https://www.mercadolibre.com.mx/memoria-ram-fury-beast-ddr4-rgb-color-negro-8gb-1-kingston-kf432c16bba8/p/MLM18614782#reco_item_pos=0&reco_backend=machinalis-homes-pdp-boos&reco_backend_type=function&reco_client=home_navigation-recommendations&reco_id=83526d68-df60-489e-96f5-c3bcfd25ea8f&c_id=/home/navigation-recommendations/element&c_element_order=1&c_uid=73c3e898-cdb4-4ef5-8d20-d73370dcd963"


@pytest.mark.parametrize('link,store,name',[
('https://www.mercadolibre.com.mx/memoria-ram-fury-beast-ddr4-rgb-color-negro-8gb-1-kingston-kf432c16bba8/p/MLM18614782#reco_item_pos=0&reco_backend=machinalis-homes-pdp-boos&reco_backend_type=function&reco_client=home_navigation-recommendations&reco_id=83526d68-df60-489e-96f5-c3bcfd25ea8f&c_id=/home/navigation-recommendations/element&c_element_order=1&c_uid=73c3e898-cdb4-4ef5-8d20-d73370dcd963','ML','Memoria RAM Fury Beast DDR4 RGB color negro  8GB 1 Kingston KF432C16BBA/8'),
('https://articulo.mercadolibre.com.mx/MLM-1427771667-kit-de-actualizacion-gaming-ryzen-5-5600g-motherboard-a320-_JM?variation=174560950941#reco_item_pos=0&reco_backend=machinalis-p2p&reco_backend_type=function&reco_client=home_navigation-related-recommendations&reco_id=c5d913ed-3ac4-40d5-af8d-016f4bd66db4&c_id=/home/navigation-related-recommendations/element&c_element_order=1&c_uid=801c5107-10f9-48f9-8903-dbc1a216b8f0','ML','Kit De Actualizacion Gaming Ryzen 5 5600g + Motherboard A320')
])
def test_item_names(link:str,store:str,name:str):
    """Test thet the name of the product is retrieve correctly

    Args:
        link (str): Link of the product
        store (str): Name of the store to select the appropiate env variables
        name (str): Expected name result
    """
    item = Item(link,store)
    assert item.name == name

@pytest.mark.parametrize('link,store,price',[
    ('https://www.mercadolibre.com.mx/memoria-ram-fury-beast-ddr4-rgb-color-negro-8gb-1-kingston-kf432c16bba8/p/MLM18614782#reco_item_pos=0&reco_backend=machinalis-homes-pdp-boos&reco_backend_type=function&reco_client=home_navigation-recommendations&reco_id=83526d68-df60-489e-96f5-c3bcfd25ea8f&c_id=/home/navigation-recommendations/element&c_element_order=1&c_uid=73c3e898-cdb4-4ef5-8d20-d73370dcd963','ML',498),
    ('https://articulo.mercadolibre.com.mx/MLM-1427771667-kit-de-actualizacion-gaming-ryzen-5-5600g-motherboard-a320-_JM?variation=174560950941#reco_item_pos=0&reco_backend=machinalis-p2p&reco_backend_type=function&reco_client=home_navigation-related-recommendations&reco_id=c5d913ed-3ac4-40d5-af8d-016f4bd66db4&c_id=/home/navigation-related-recommendations/element&c_element_order=1&c_uid=801c5107-10f9-48f9-8903-dbc1a216b8f0','ML',3649)
])
def test_item_price(link:str,store:str,price:float):
    """Test thet the price of the product is retrieve correctly

    Args:
        link (str): Link of the product
        store (str): Name of the store to select the appropiate env variables
        price (float): Expected price result
    """
    item = Item(link,store)
    assert item.price == price