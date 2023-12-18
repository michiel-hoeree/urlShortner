def create_supplier(delay_factor, price_factor):
    def place_order(expected_delivery_time,price_estimate):
        deliveryTime = expected_delivery_time*delay_factor
        price = price_estimate * price_factor
        print(f"geschatte levertijd: {deliveryTime} dagen")
        print(f"geschatte kostprijs: {price} euro")
    return place_order

if __name__ == '__main__':
    get_offer_from_bol = create_supplier(0.8,1.1)
    get_offer_from_amazon = create_supplier(1.2,0.9)
    get_offer_from_aliexpress = create_supplier(1.5,0.75)
    
    get_offer_from_bol(100,100)
    get_offer_from_amazon(100,100)
    get_offer_from_aliexpress(100,100)