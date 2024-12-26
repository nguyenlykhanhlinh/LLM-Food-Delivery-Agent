import pandas as pd
from sqlalchemy.orm import Session

from database import SessionLocal
from data_models import Restaurant, Foods


# Hàm thêm nhà hàng vào cơ sở dữ liệu
def add_restaurant(db: Session, name: str, description: str, image: str):
    restaurant = Restaurant(name=name, description=description, image=image)
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant 


# Hàm thêm món ăn vào cơ sở dữ liệu
def add_food(
    db: Session, restaurant_id: int, name: str, description: str, image: str, price: int
):
    food = Foods(
        restaurant_id=restaurant_id,
        name=name,
        description=description,
        image=image,
        price=price,
    )
    db.add(food)
    db.commit()
    db.refresh(food)
    return food


def main():
    db = SessionLocal()

    # Sample data for restaurants
    restaurants = [
        {
<<<<<<< HEAD
            "name": "Nhà Hàng Chay Việt Co",
            "description": "Nhà hàng của chúng tôi chuyên cung cấp các món ăn Việt Nam, các món ăn nổi bật được yêu thích tại Việt Nam, mời bạn cùng gia đình và bạn bè thưởng thức một bữa tiệc Việt Nam đích thực.",
            "image": "/static/restaurants/CoVietnamese_Restaurant&Vegan.png",
        },
        {
            "name": "SushiLAB",
            "description": "Sushi tươi và các món ăn Nhật Bản",
            "image": "/static/restaurants/sushi_lab.png",
        },
        {
            "name": "Nhà Hàng The Eroica",
            "description": "Nhà hàng The Eroica dẫn dắt thực khách vào một hành trình ẩm thực đa tầng với thực đơn đa dạng các món ăn Á - Âu. Không gian fine-dining được thiết kế sang trọng, tinh tế và hài hòa đến từng chi tiết, hứa hẹn là điểm đến lý tưởng cho bất kỳ buổi hẹn đặc biệt nào: từ bữa tối lãng mạn cho các cặp đôi, buổi gặp mặt gia đình hoặc tiệc công ty. Bạn sẽ trải nghiệm dịch vụ ẩm thực hoàn hảo với nhiều món ăn ngon từ các đầu bếp tài năng của chúng tôi.",
            "image": "/static/restaurants/the_eroica_restaurant.png",
        },
        {
            "name": "Burger King Hàng Buồm",
            "description": "Burger cao cấp và khoai tây chiên",
            "image": "/static/restaurants/burger_king_hang_buom.png",
        },
        {
            "name": "Pizza Hub - Pizza Nướng Lò Củi & Đồ Nướng",
            "description": "Pizza nướng lò củi",
            "image": "/static/restaurants/pizza_hub_wood_fired_pizza_grills.png",
        },
        {
            "name": "Indian Spice",
            "description": "Các món cà ri và nướng truyền thống của Ấn Độ",
=======
            "name": "Italian Bistro",
            "description": "Authentic Italian cuisine",
            "image": "/static/restaurants/italian_bistro.png",
        },
        {
            "name": "Sushi House",
            "description": "Fresh sushi and Japanese dishes",
            "image": "/static/restaurants/sushi_house.png",
        },
        {
            "name": "Taco Fiesta",
            "description": "Mexican street food and tacos",
            "image": "/static/restaurants/taco_fiesta.png",
        },
        {
            "name": "Burger Joint",
            "description": "Gourmet burgers and fries",
            "image": "/static/restaurants/burger_joint.png",
        },
        {
            "name": "Pizza Palace",
            "description": "Wood-fired pizzas",
            "image": "/static/restaurants/pizza_palace.png",
        },
        {
            "name": "Indian Spice",
            "description": "Traditional Indian curries and tandoori",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/indian_spice.png",
        },
        {
            "name": "Thai Delight",
<<<<<<< HEAD
            "description": "Các món Thái ngon miệng và mì",
=======
            "description": "Flavorful Thai dishes and noodles",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/thai_delight.png",
        },
        {
            "name": "Chinese Wok",
<<<<<<< HEAD
            "description": "Ẩm thực Trung Hoa cổ điển và dim sum",
=======
            "description": "Classic Chinese cuisine and dim sum",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/chinese_wok.png",
        },
        {
            "name": "Mediterranean Grill",
<<<<<<< HEAD
            "description": "Hương vị Địa Trung Hải tươi ngon và kebab",
=======
            "description": "Fresh Mediterranean flavors and kebabs",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/mediterranean_grill.png",
        },
        {
            "name": "French Bistro",
<<<<<<< HEAD
            "description": "Ẩm thực Pháp tinh tế và bánh ngọt",
=======
            "description": "Elegant French dining and pastries",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/french_bistro.png",
        },
        {
            "name": "Steakhouse",
<<<<<<< HEAD
            "description": "Bít tết cao cấp và hải sản",
=======
            "description": "Premium steaks and seafood",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/steakhouse.png",
        },
        {
            "name": "Vegan Cafe",
<<<<<<< HEAD
            "description": "Các món chay và sinh tố",
=======
            "description": "Plant-based dishes and smoothies",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/vegan_cafe.png",
        },
        {
            "name": "Greek Taverna",
<<<<<<< HEAD
            "description": "Các món Hy Lạp cổ điển và hải sản",
=======
            "description": "Greek classics and seafood",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/greek_taverna.png",
        },
        {
            "name": "Southern Comfort",
<<<<<<< HEAD
            "description": "Các món ăn gia đình miền Nam",
=======
            "description": "Homestyle Southern cooking",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/southern_comfort.png",
        },
        {
            "name": "BBQ Shack",
<<<<<<< HEAD
            "description": "Thịt nướng và BBQ",
=======
            "description": "Smoked meats and barbecue",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/bbq_shack.png",
        },
        {
            "name": "Seafood Delight",
<<<<<<< HEAD
            "description": "Hải sản tươi ngon và các món cá",
=======
            "description": "Fresh seafood and fish dishes",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/seafood_delight.png",
        },
        {
            "name": "Veggie Heaven",
<<<<<<< HEAD
            "description": "Các món chay và thuần chay ngon miệng",
=======
            "description": "Delicious vegetarian and vegan dishes",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/veggie_heaven.png",
        },
        {
            "name": "Chicken Coop",
<<<<<<< HEAD
            "description": "Các món gà nướng và chiên",
=======
            "description": "Grilled and fried chicken dishes",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/chicken_coop.png",
        },
        {
            "name": "Pasta Paradise",
<<<<<<< HEAD
            "description": "Đa dạng các món mì Ý",
=======
            "description": "A variety of pasta dishes",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/pasta_paradise.png",
        },
        {
            "name": "Bakery Bliss",
<<<<<<< HEAD
            "description": "Bánh mì và bánh ngọt tươi ngon",
=======
            "description": "Freshly baked breads and pastries",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/bakery_bliss.png",
        },
        {
            "name": "Salad Bar",
<<<<<<< HEAD
            "description": "Các món salad ngon và lành mạnh",
=======
            "description": "Healthy and delicious salads",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/salad_bar.png",
        },
        {
            "name": "Ramen House",
<<<<<<< HEAD
            "description": "Mì ramen và các món Nhật",
=======
            "description": "Japanese ramen and noodle dishes",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/ramen_house.png",
        },
        {
            "name": "Ice Cream Shop",
<<<<<<< HEAD
            "description": "Đa dạng các hương vị kem và món tráng miệng",
=======
            "description": "Variety of ice cream flavors and desserts",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
            "image": "/static/restaurants/ice_cream_shop.png",
        },
        {
            "name": "Sandwich Shop",
<<<<<<< HEAD
            "description": "Bánh mì sandwich và cuộn tươi ngon",
            "image": "/static/restaurants/sandwich_shop.png",
        },
        {
            "name": "Pancake House",
            "description": "Các loại pancake ngọt và mặn",
            "image": "/static/restaurants/pancake_house.png",
        },
        {
            "name": "Bún Chả Tạ",
            "description": "Bún chả Tạ là món ăn Việt Nam gồm thịt nướng và bún",
            "image": "/static/restaurants/bun_cha_ta.png",
=======
            "description": "Freshly made sandwiches and wraps",
            "image": "/static/restaurants/sandwich_shop.png",
        },
        {
            "name": "Pancake House",
            "description": "Sweet and savory pancakes",
            "image": "/static/restaurants/pancake_house.png",
        },
        {
            "name": "Your New Restaurant",
            "description": "Your restaurant description",
            "image": "/static/restaurants/your_image.png",
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
        },
    ]


    # Sample data for foods
    foods = [
        # Nhà Hàng Chay Việt Co
        {
            "restaurant_id": 1,
<<<<<<< HEAD
            "name": "Nem rán",
            "description": "Nem rán hoặc nem cuốn với nhiều loại nhân như rau củ, thịt và bún.",
            "image": "/static/foods/fried_spring_rolls.png",
            "price": 70.000,
        },
        {
            "restaurant_id": 1,
            "name": "Phở bò/gà truyền thống",
            "description": "Món phở cổ điển Việt Nam với bún gạo, phục vụ cùng lựa chọn thịt bò hoặc gà.",
            "image": "/static/foods/traditional_noodle_soup_with_beef_chicken.png",
            "price": 70.000,
        },
        {
            "restaurant_id": 1,
            "name": "Bánh xèo đặc biệt",
            "description": "Bánh xèo Việt Nam làm từ bột gạo, nghệ, và nước cốt dừa, thường có nhân tôm, thịt heo và giá đỗ.",
            "image": "/static/foods/special_vietnamese_pancace_banh_xeo.png",
            "price": 100.000,
        },
        {
            "restaurant_id": 1,
            "name": "Bò hoặc heo cuốn lá lốt kèm bún tươi (6 cuốn)",
            "description": "Thịt nướng cuộn lá lốt, phục vụ cùng bún tươi và nước chấm.",
            "image": "/static/foods/beef_or_pork_rolled_with_betel_leaves_come_with_fresh_noodle_6pcs.png",
            "price": 100.000,
        },
        {
            "restaurant_id": 1,
            "name": "Gỏi hoa chuối tôm thịt",
            "description": "Gỏi hoa chuối tươi ngon với tôm, thịt gà và nước sốt chua ngọt.",
            "image": "/static/foods/banana_flower_salad_with_shrimp_chicken.png",
            "price": 110.000,
        },
        {
            "restaurant_id": 1,
            "name": "Bún chả Hà Nội truyền thống",
            "description": "Món ăn đặc trưng Hà Nội với thịt nướng, bún tươi, rau thơm và nước chấm.",
            "image": "/static/foods/hanoi_traditional_grilled_pork_with_rice_noodle_bun_cha.png",
            "price": 115.000,
        },
        {
            "restaurant_id": 1,
            "name": "Nem lụi nướng",
            "description": "Nem nướng từ thịt heo băm nhuyễn, nêm nếm với sả, phục vụ cùng rau sống và nước chấm.",
            "image": "/static/foods/fried_minced_pork_in_lemongrass_nem_lui.png",
            "price": 90.000,
        },
        {
            "restaurant_id": 1,
            "name": "Súp kem nấm và rau củ",
            "description": "Súp kem thơm ngon với nấm và rau củ.",
            "image": "/static/foods/vegetable_soup_with_cream_and_mushroom_soup.png",
            "price": 80.000,
=======
            "name": "Margherita Pizza",
            "description": "Classic pizza with tomato sauce, fresh mozzarella, and basil",
            "image": "/static/foods/margherita_pizza.png",
            "price": 12,
        },
        {
            "restaurant_id": 1,
            "name": "Spaghetti Carbonara",
            "description": "Creamy pasta with pancetta, egg, and Pecorino Romano cheese",
            "image": "/static/foods/spaghetti_carbonara.png",
            "price": 14,
        },
        {
            "restaurant_id": 1,
            "name": "Caprese Salad",
            "description": "Fresh salad with tomatoes, mozzarella, basil, and balsamic glaze",
            "image": "/static/foods/caprese_salad.png",
            "price": 10,
        },
        {
            "restaurant_id": 1,
            "name": "Tiramisu",
            "description": "Classic Italian dessert with coffee-soaked ladyfingers and mascarpone cream",
            "image": "/static/foods/tiramisu.png",
            "price": 8,
        },
        {
            "restaurant_id": 1,
            "name": "Risotto",
            "description": "Creamy risotto with mushrooms and Parmesan cheese",
            "image": "/static/foods/risotto.png",
            "price": 16,
        },
        {
            "restaurant_id": 1,
            "name": "Chianti",
            "description": "Italian red wine",
            "image": "/static/beverages/chianti.png",
            "price": 8,
        },
        {
            "restaurant_id": 1,
            "name": "Espresso",
            "description": "Strong Italian coffee",
            "image": "/static/beverages/espresso.png",
            "price": 3,
        },
        {
            "restaurant_id": 1,
            "name": "Limoncello",
            "description": "Italian lemon liqueur",
            "image": "/static/beverages/limoncello.png",
            "price": 7,
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
        },
        # SushiLAB
        {
            "restaurant_id": 2,
            "name": "California Roll",
<<<<<<< HEAD
            "description": "Cuộn sushi với thịt cua, bơ và dưa chuột.",
            "image": "/static/foods/california_roll.png",
            "price": 80.000,
=======
            "description": "Sushi roll with crab, avocado, and cucumber",
            "image": "/static/foods/california_roll.png",
            "price": 8,
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
        },
        {
            "restaurant_id": 2,
            "name": "Spicy Tuna Roll",
<<<<<<< HEAD
            "description": "Cuộn sushi với cá ngừ cay, sốt mayo và dưa chuột.",
            "image": "/static/foods/spicy_tuna_roll.png",
            "price": 90.000,
=======
            "description": "Sushi roll with spicy tuna, mayo, and cucumber",
            "image": "/static/foods/spicy_tuna_roll.png",
            "price": 9,
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
        },
        {
            "restaurant_id": 2,
            "name": "Salmon Nigiri",
<<<<<<< HEAD
            "description": "Sushi với một lát cá hồi tươi trên cơm sushi.",
            "image": "/static/foods/salmon_nigiri.png",
            "price": 70.000,
=======
            "description": "Sushi with a slice of fresh salmon on top of sushi rice",
            "image": "/static/foods/salmon_nigiri.png",
            "price": 7,
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
        },
        {
            "restaurant_id": 2,
            "name": "Shrimp Tempura Roll",
<<<<<<< HEAD
            "description": "Cuộn sushi với tôm chiên tempura, bơ và dưa chuột.",
            "image": "/static/foods/shrimp_tempura_roll.png",
            "price": 100.000,
        },
        {
            "restaurant_id": 2,
            "name": "Súp Miso",
            "description": "Súp Nhật Bản truyền thống với đậu phụ và rong biển.",
            "image": "/static/foods/miso_soup.png",
            "price": 40.000,
        },
        {
            "restaurant_id": 2,
            "name": "Rượu Sake",
            "description": "Rượu gạo Nhật Bản.",
            "image": "/static/beverages/sake.png",
            "price": 60.000,
        },
        {
            "restaurant_id": 2,
            "name": "Trà xanh Nhật",
            "description": "Trà xanh Nhật Bản nóng.",
            "image": "/static/beverages/green_tea.png",
            "price": 30.000,
        },
        {
            "restaurant_id": 2,
            "name": "Rượu Mận",
            "description": "Rượu ngọt Nhật Bản làm từ mận.",
            "image": "/static/beverages/plum_wine.png",
            "price": 70.000,
        },
        # Burger King Hàng Buồm
        {
            "restaurant_id": 4,
            "name": "Burger Phô Mai Truyền Thống",
            "description": "Burger thơm ngon với phô mai, xà lách, cà chua và hành.",
            "image": "/static/foods/classic_cheeseburger.png",
            "price": 100.000,
        },
        {
            "restaurant_id": 4,
            "name": "Burger Thịt Xông Khói",
            "description": "Burger hấp dẫn với thịt xông khói, phô mai, xà lách, cà chua và hành.",
            "image": "/static/foods/bacon_burger.png",
            "price": 120.000,
        },
        {
            "restaurant_id": 4,
            "name": "Burger Nấm Phô Mai Thụy Sĩ",
            "description": "Burger ngon miệng với phô mai Thụy Sĩ và nấm xào.",
            "image": "/static/foods/mushroom_swiss_burger.png",
            "price": 110.000,
        },
        {
            "restaurant_id": 4,
            "name": "Burger Chay",
            "description": "Burger chay lành mạnh với xà lách, cà chua và hành.",
            "image": "/static/foods/veggie_burger.png",
            "price": 100.000,
        },
        {
            "restaurant_id": 4,
            "name": "Khoai Tây Chiên",
            "description": "Khoai tây chiên vàng giòn kèm tương cà.",
            "image": "/static/foods/french_fries.png",
            "price": 40.000,
        },
        # Bun Cha Ta
        {
            "restaurant_id": 1,
            "name": "Bún Chả Tạ",
            "description": "Món Bún Chả Tạ với thịt nướng và bún, kèm nước chấm chua ngọt.",
            "image": "/static/foods/bun_cha_ta.png",
            "price": 100.000,
=======
            "description": "Sushi roll with tempura shrimp, avocado, and cucumber",
            "image": "/static/foods/shrimp_tempura_roll.png",
            "price": 10,
        },
        {
            "restaurant_id": 2,
            "name": "Miso Soup",
            "description": "Traditional Japanese soup with tofu and seaweed",
            "image": "/static/foods/miso_soup.png",
            "price": 4,
        },
        {
            "restaurant_id": 2,
            "name": "Sake",
            "description": "Japanese rice wine",
            "image": "/static/beverages/sake.png",
            "price": 6,
        },
        {
            "restaurant_id": 2,
            "name": "Green Tea",
            "description": "Hot Japanese green tea",
            "image": "/static/beverages/green_tea.png",
            "price": 3,
        },
        {
            "restaurant_id": 2,
            "name": "Plum Wine",
            "description": "Sweet Japanese wine made from plums",
            "image": "/static/beverages/plum_wine.png",
            "price": 7,
        },
        # Taco Fiesta
        {
            "restaurant_id": 3,
            "name": "Carne Asada Taco",
            "description": "Taco with grilled steak, onions, and cilantro",
            "image": "/static/foods/carne_asada_taco.png",
            "price": 3,
        },
        {
            "restaurant_id": 3,
            "name": "Carnitas Taco",
            "description": "Taco with slow-cooked pork, onions, and cilantro",
            "image": "/static/foods/carnitas_taco.png",
            "price": 3,
        },
        {
            "restaurant_id": 3,
            "name": "Chicken Taco",
            "description": "Taco with grilled chicken, onions, and cilantro",
            "image": "/static/foods/chicken_taco.png",
            "price": 3,
        },
        {
            "restaurant_id": 3,
            "name": "Fish Taco",
            "description": "Taco with battered fish, cabbage, and chipotle mayo",
            "image": "/static/foods/fish_taco.png",
            "price": 4,
        },
        {
            "restaurant_id": 3,
            "name": "Churros",
            "description": "Fried dough pastry with cinnamon sugar",
            "image": "/static/foods/churros.png",
            "price": 5,
        },
        {
            "restaurant_id": 3,
            "name": "Margarita",
            "description": "Classic Mexican cocktail with tequila, lime, and triple sec",
            "image": "/static/beverages/margarita.png",
            "price": 7,
        },
        {
            "restaurant_id": 3,
            "name": "Mexican Beer",
            "description": "Refreshing Mexican lager",
            "image": "/static/beverages/mexican_beer.png",
            "price": 5,
        },
        {
            "restaurant_id": 3,
            "name": "Horchata",
            "description": "Sweet Mexican drink made from rice",
            "image": "/static/beverages/horchata.png",
            "price": 4,
        },
        # Burger Joint
        {
            "restaurant_id": 4,
            "name": "Classic Cheeseburger",
            "description": "Juicy burger with cheese, lettuce, tomato, and onion",
            "image": "/static/foods/classic_cheeseburger.png",
            "price": 10,
        },
        {
            "restaurant_id": 4,
            "name": "Bacon Burger",
            "description": "Delicious burger with bacon, cheese, lettuce, tomato, and onion",
            "image": "/static/foods/bacon_burger.png",
            "price": 12,
        },
        {
            "restaurant_id": 4,
            "name": "Mushroom Swiss Burger",
            "description": "Tasty burger with Swiss cheese and sautéed mushrooms",
            "image": "/static/foods/mushroom_swiss_burger.png",
            "price": 11,
        },
        {
            "restaurant_id": 4,
            "name": "Veggie Burger",
            "description": "Healthy vegetarian burger with lettuce, tomato, and onion",
            "image": "/static/foods/veggie_burger.png",
            "price": 10,
        },
        {
            "restaurant_id": 4,
            "name": "French Fries",
            "description": "Crispy golden fries served with ketchup",
            "image": "/static/foods/french_fries.png",
            "price": 4,
        },
        {
            "restaurant_id": 4,
            "name": "Craft Beer",
            "description": "Local craft beer",
            "image": "/static/beverages/craft_beer.png",
            "price": 6,
        },
        {
            "restaurant_id": 4,
            "name": "Milkshake",
            "description": "Creamy milkshake with vanilla, chocolate, or strawberry",
            "image": "/static/beverages/milkshake.png",
            "price": 5,
        },
        {
            "restaurant_id": 4,
            "name": "Soda",
            "description": "Refreshing carbonated drink",
            "image": "/static/beverages/soda.png",
            "price": 3,
        },
        # Pizza Palace
        {
            "restaurant_id": 5,
            "name": "Pepperoni Pizza",
            "description": "Delicious pizza with tomato sauce, mozzarella, and pepperoni",
            "image": "/static/foods/pepperoni_pizza.png",
            "price": 12,
        },
        {
            "restaurant_id": 5,
            "name": "Veggie Pizza",
            "description": "Healthy pizza with tomato sauce, mozzarella, bell peppers, onions, and olives",
            "image": "/static/foods/veggie_pizza.png",
            "price": 14,
        },
        {
            "restaurant_id": 5,
            "name": "Meat Lovers Pizza",
            "description": "Hearty pizza with tomato sauce, mozzarella, pepperoni, sausage, and bacon",
            "image": "/static/foods/meat_lovers_pizza.png",
            "price": 16,
        },
        {
            "restaurant_id": 5,
            "name": "BBQ Chicken Pizza",
            "description": "Tasty pizza with BBQ sauce, mozzarella, chicken, red onion, and cilantro",
            "image": "/static/foods/bbq_chicken_pizza.png",
            "price": 15,
        },
        {
            "restaurant_id": 5,
            "name": "Hawaiian Pizza",
            "description": "Sweet and savory pizza with tomato sauce, mozzarella, ham, and pineapple",
            "image": "/static/foods/hawaiian_pizza.png",
            "price": 14,
        },
        {
            "restaurant_id": 5,
            "name": "Italian Soda",
            "description": "Refreshing soda with a choice of fruit syrup",
            "image": "/static/beverages/italian_soda.png",
            "price": 4,
        },
        {
            "restaurant_id": 5,
            "name": "Chianti",
            "description": "Italian red wine",
            "image": "/static/beverages/chianti.png",
            "price": 8,
        },
        {
            "restaurant_id": 5,
            "name": "Limoncello",
            "description": "Italian lemon liqueur",
            "image": "/static/beverages/limoncello.png",
            "price": 7,
        },
        # Indian Spice
        {
            "restaurant_id": 6,
            "name": "Chicken Tikka Masala",
            "description": "Grilled chicken in a creamy tomato sauce served with basmati rice",
            "image": "/static/foods/chicken_tikka_masala.png",
            "price": 14,
        },
        {
            "restaurant_id": 6,
            "name": "Lamb Curry",
            "description": "Tender lamb in a spiced curry sauce served with basmati rice",
            "image": "/static/foods/lamb_curry.png",
            "price": 16,
        },
        {
            "restaurant_id": 6,
            "name": "Saag Paneer",
            "description": "Indian cheese in a creamy spinach sauce served with naan bread",
            "image": "/static/foods/saag_paneer.png",
            "price": 12,
        },
        {
            "restaurant_id": 6,
            "name": "Vegetable Biryani",
            "description": "Aromatic rice dish with mixed vegetables and spices served with raita",
            "image": "/static/foods/vegetable_biryani.png",
            "price": 10,
        },
        {
            "restaurant_id": 6,
            "name": "Garlic Naan",
            "description": "Leavened bread with garlic and butter",
            "image": "/static/foods/garlic_naan.png",
            "price": 4,
        },
        {
            "restaurant_id": 6,
            "name": "Mango Lassi",
            "description": "Refreshing yogurt-based drink with mango",
            "image": "/static/beverages/mango_lassi.png",
            "price": 4,
        },
        {
            "restaurant_id": 6,
            "name": "Masala Chai",
            "description": "Spiced tea with milk",
            "image": "/static/beverages/masala_chai.png",
            "price": 3,
        },
        {
            "restaurant_id": 6,
            "name": "Kingfisher Beer",
            "description": "Indian lager beer",
            "image": "/static/beverages/kingfisher_beer.png",
            "price": 5,
        },
        # Thai Delight
        {
            "restaurant_id": 7,
            "name": "Pad Thai",
            "description": "Stir-fried rice noodles with shrimp, tofu, eggs, and peanuts",
            "image": "/static/foods/pad_thai.png",
            "price": 12,
        },
        {
            "restaurant_id": 7,
            "name": "Green Curry",
            "description": "Spicy green curry with chicken, eggplant, and basil served with jasmine rice",
            "image": "/static/foods/green_curry.png",
            "price": 14,
        },
        {
            "restaurant_id": 7,
            "name": "Tom Yum Soup",
            "description": "Hot and sour soup with shrimp, lemongrass, and mushrooms",
            "image": "/static/foods/tom_yum_soup.png",
            "price": 8,
        },
        {
            "restaurant_id": 7,
            "name": "Papaya Salad",
            "description": "Spicy salad with green papaya, tomatoes, and peanuts",
            "image": "/static/foods/papaya_salad.png",
            "price": 10,
        },
        {
            "restaurant_id": 7,
            "name": "Mango Sticky Rice",
            "description": "Sweet dessert with sticky rice, fresh mango, and coconut milk",
            "image": "/static/foods/mango_sticky_rice.png",
            "price": 6,
        },
        {
            "restaurant_id": 7,
            "name": "Thai Iced Tea",
            "description": "Sweet tea with milk",
            "image": "/static/beverages/thai_iced_tea.png",
            "price": 4,
        },
        {
            "restaurant_id": 7,
            "name": "Singha Beer",
            "description": "Thai lager beer",
            "image": "/static/beverages/singha_beer.png",
            "price": 5,
        },
        {
            "restaurant_id": 7,
            "name": "Lemongrass Juice",
            "description": "Refreshing juice with lemongrass",
            "image": "/static/beverages/lemongrass_juice.png",
            "price": 4,
        },
        # Chinese Wok
        {
            "restaurant_id": 8,
            "name": "Kung Pao Chicken",
            "description": "Stir-fried chicken with peanuts, vegetables, and chili peppers served with steamed rice",
            "image": "/static/foods/kung_pao_chicken.png",
            "price": 12,
        },
        {
            "restaurant_id": 8,
            "name": "Beef and Broccoli",
            "description": "Stir-fried beef with broccoli in a savory sauce served with steamed rice",
            "image": "/static/foods/beef_and_broccoli.png",
            "price": 14,
        },
        {
            "restaurant_id": 8,
            "name": "Sweet and Sour Pork",
            "description": "Battered pork with pineapple, bell peppers, and sweet and sour sauce served with steamed rice",
            "image": "/static/foods/sweet_and_sour_pork.png",
            "price": 12,
        },
        {
            "restaurant_id": 8,
            "name": "Vegetable Fried Rice",
            "description": "Fried rice with mixed vegetables and eggs",
            "image": "/static/foods/vegetable_fried_rice.png",
            "price": 10,
        },
        {
            "restaurant_id": 8,
            "name": "Spring Rolls",
            "description": "Crispy rolls filled with vegetables served with sweet and sour sauce",
            "image": "/static/foods/spring_rolls.png",
            "price": 6,
        },
        {
            "restaurant_id": 8,
            "name": "Tsingtao Beer",
            "description": "Chinese lager beer",
            "image": "/static/beverages/tsingtao_beer.png",
            "price": 5,
        },
        {
            "restaurant_id": 8,
            "name": "Jasmine Tea",
            "description": "Hot tea with jasmine flavor",
            "image": "/static/beverages/jasmine_tea.png",
            "price": 3,
        },
        {
            "restaurant_id": 8,
            "name": "Plum Juice",
            "description": "Sweet juice made from plums",
            "image": "/static/beverages/plum_juice.png",
            "price": 4,
        },
        # Mediterranean Grill
        {
            "restaurant_id": 9,
            "name": "Chicken Shawarma",
            "description": "Marinated chicken with garlic sauce and pickles wrapped in pita bread",
            "image": "/static/foods/chicken_shawarma.png",
            "price": 10,
        },
        {
            "restaurant_id": 9,
            "name": "Falafel",
            "description": "Deep-fried chickpea patties with tahini sauce and salad wrapped in pita bread",
            "image": "/static/foods/falafel.png",
            "price": 8,
        },
        {
            "restaurant_id": 9,
            "name": "Greek Salad",
            "description": "Fresh salad with tomatoes, cucumbers, olives, and feta cheese",
            "image": "/static/foods/greek_salad.png",
            "price": 10,
        },
        {
            "restaurant_id": 9,
            "name": "Hummus",
            "description": "Chickpea dip with olive oil and pita bread",
            "image": "/static/foods/hummus.png",
            "price": 6,
        },
        {
            "restaurant_id": 9,
            "name": "Baklava",
            "description": "Sweet pastry with layers of filo and chopped nuts",
            "image": "/static/foods/baklava.png",
            "price": 5,
        },
        {
            "restaurant_id": 9,
            "name": "Greek Wine",
            "description": "White or red Greek wine",
            "image": "/static/beverages/greek_wine.png",
            "price": 7,
        },
        {
            "restaurant_id": 9,
            "name": "Turkish Coffee",
            "description": "Strong coffee served in a small cup",
            "image": "/static/beverages/turkish_coffee.png",
            "price": 3,
        },
        {
            "restaurant_id": 9,
            "name": "Mint Lemonade",
            "description": "Refreshing lemonade with mint",
            "image": "/static/beverages/mint_lemonade.png",
            "price": 4,
        },
        # French Bistro
        {
            "restaurant_id": 10,
            "name": "Coq au Vin",
            "description": "Braised chicken with red wine, mushrooms, and onions served with mashed potatoes",
            "image": "/static/foods/coq_au_vin.png",
            "price": 18,
        },
        {
            "restaurant_id": 10,
            "name": "Beef Bourguignon",
            "description": "Slow-cooked beef with red wine, mushrooms, and carrots served with mashed potatoes",
            "image": "/static/foods/beef_bourguignon.png",
            "price": 20,
        },
        {
            "restaurant_id": 10,
            "name": "French Onion Soup",
            "description": "Caramelized onion soup with Gruyère cheese croutons",
            "image": "/static/foods/french_onion_soup.png",
            "price": 8,
        },
        {
            "restaurant_id": 10,
            "name": "Ratatouille",
            "description": "Stewed vegetables with tomato sauce and herbs served with crusty bread",
            "image": "/static/foods/ratatouille.png",
            "price": 12,
        },
        {
            "restaurant_id": 10,
            "name": "Crème Brûlée",
            "description": "Vanilla custard with caramelized sugar",
            "image": "/static/foods/creme_brulee.png",
            "price": 6,
        },
        {
            "restaurant_id": 10,
            "name": "French Wine",
            "description": "Red or white French wine",
            "image": "/static/beverages/french_wine.png",
            "price": 8,
        },
        {
            "restaurant_id": 10,
            "name": "Espresso",
            "description": "Strong French coffee",
            "image": "/static/beverages/espresso.png",
            "price": 3,
        },
        {
            "restaurant_id": 10,
            "name": "Lemonade",
            "description": "Refreshing lemonade",
            "image": "/static/beverages/lemonade.png",
            "price": 4,
        },
        # Steakhouse
        {
            "restaurant_id": 11,
            "name": "Ribeye Steak",
            "description": "Grilled ribeye steak with garlic herb butter served with mashed potatoes",
            "image": "/static/foods/ribeye_steak.png",
            "price": 28,
        },
        {
            "restaurant_id": 11,
            "name": "Filet Mignon",
            "description": "Tender filet mignon with red wine reduction served with mashed potatoes",
            "image": "/static/foods/filet_mignon.png",
            "price": 32,
        },
        {
            "restaurant_id": 11,
            "name": "Grilled Salmon",
            "description": "Grilled salmon with lemon herb sauce served with steamed vegetables",
            "image": "/static/foods/grilled_salmon.png",
            "price": 22,
        },
        {
            "restaurant_id": 11,
            "name": "Caesar Salad",
            "description": "Classic salad with romaine lettuce, croutons, and Parmesan cheese",
            "image": "/static/foods/caesar_salad.png",
            "price": 10,
        },
        {
            "restaurant_id": 11,
            "name": "Mashed Potatoes",
            "description": "Creamy mashed potatoes with butter",
            "image": "/static/foods/mashed_potatoes.png",
            "price": 6,
        },
        {
            "restaurant_id": 11,
            "name": "Cabernet Sauvignon",
            "description": "Full-bodied red wine",
            "image": "/static/beverages/cabernet_sauvignon.png",
            "price": 8,
        },
        {
            "restaurant_id": 11,
            "name": "Craft Beer",
            "description": "Local craft beer",
            "image": "/static/beverages/craft_beer.png",
            "price": 6,
        },
        {
            "restaurant_id": 11,
            "name": "Whiskey",
            "description": "Aged whiskey on the rocks",
            "image": "/static/beverages/whiskey.png",
            "price": 7,
        },
        # Vegan Cafe
        {
            "restaurant_id": 12,
            "name": "Vegan Burger",
            "description": "Plant-based burger with lettuce, tomato, and onion served with sweet potato fries",
            "image": "/static/foods/vegan_burger.png",
            "price": 12,
        },
        {
            "restaurant_id": 12,
            "name": "Quinoa Salad",
            "description": "Healthy salad with quinoa, mixed greens, and roasted vegetables",
            "image": "/static/foods/quinoa_salad.png",
            "price": 10,
        },
        {
            "restaurant_id": 12,
            "name": "Lentil Soup",
            "description": "Hearty soup with lentils and vegetables",
            "image": "/static/foods/lentil_soup.png",
            "price": 8,
        },
        {
            "restaurant_id": 12,
            "name": "Stuffed Bell Peppers",
            "description": "Bell peppers filled with quinoa, beans, and vegetables",
            "image": "/static/foods/stuffed_bell_peppers.png",
            "price": 14,
        },
        {
            "restaurant_id": 12,
            "name": "Fruit Smoothie",
            "description": "Blended smoothie with a choice of fruits and almond milk",
            "image": "/static/foods/fruit_smoothie.png",
            "price": 6,
        },
        {
            "restaurant_id": 12,
            "name": "Green Juice",
            "description": "Healthy juice with kale, spinach, and apple",
            "image": "/static/beverages/green_juice.png",
            "price": 5,
        },
        {
            "restaurant_id": 12,
            "name": "Herbal Tea",
            "description": "Hot tea with a choice of herbs",
            "image": "/static/beverages/herbal_tea.png",
            "price": 3,
        },
        {
            "restaurant_id": 12,
            "name": "Almond Milk Latte",
            "description": "Coffee with almond milk",
            "image": "/static/beverages/almond_milk_latte.png",
            "price": 4,
        },
        # Greek Taverna
        {
            "restaurant_id": 13,
            "name": "Gyro",
            "description": "Grilled meat with tzatziki sauce, tomatoes, and onions wrapped in pita bread",
            "image": "/static/foods/gyro.png",
            "price": 10,
        },
        {
            "restaurant_id": 13,
            "name": "Moussaka",
            "description": "Layered dish with eggplant, ground beef, and béchamel sauce",
            "image": "/static/foods/moussaka.png",
            "price": 14,
        },
        {
            "restaurant_id": 13,
            "name": "Spanakopita",
            "description": "Savory pastry with spinach and feta cheese",
            "image": "/static/foods/spanakopita.png",
            "price": 8,
        },
        {
            "restaurant_id": 13,
            "name": "Dolmades",
            "description": "Stuffed grape leaves with rice and herbs",
            "image": "/static/foods/dolmades.png",
            "price": 6,
        },
        {
            "restaurant_id": 13,
            "name": "Greek Yogurt",
            "description": "Thick yogurt with honey and walnuts",
            "image": "/static/foods/greek_yogurt.png",
            "price": 5,
        },
        {
            "restaurant_id": 13,
            "name": "Greek Wine",
            "description": "White or red Greek wine",
            "image": "/static/beverages/greek_wine.png",
            "price": 7,
        },
        {
            "restaurant_id": 13,
            "name": "Ouzo",
            "description": "Anise-flavored Greek liquor",
            "image": "/static/beverages/ouzo.png",
            "price": 6,
        },
        {
            "restaurant_id": 13,
            "name": "Greek Coffee",
            "description": "Strong coffee served in a small cup",
            "image": "/static/beverages/greek_coffee.png",
            "price": 3,
        },
        # Southern Comfort
        {
            "restaurant_id": 14,
            "name": "Fried Chicken",
            "description": "Crispy fried chicken served with mashed potatoes and gravy",
            "image": "/static/foods/fried_chicken.png",
            "price": 14,
        },
        {
            "restaurant_id": 14,
            "name": "Shrimp and Grits",
            "description": "Sautéed shrimp with creamy grits and bacon",
            "image": "/static/foods/shrimp_and_grits.png",
            "price": 16,
        },
        {
            "restaurant_id": 14,
            "name": "Chicken and Waffles",
            "description": "Fried chicken with fluffy waffles and maple syrup",
            "image": "/static/foods/chicken_and_waffles.png",
            "price": 14,
        },
        {
            "restaurant_id": 14,
            "name": "Biscuits and Gravy",
            "description": "Buttermilk biscuits with sausage gravy",
            "image": "/static/foods/biscuits_and_gravy.png",
            "price": 8,
        },
        {
            "restaurant_id": 14,
            "name": "Pecan Pie",
            "description": "Sweet pie with pecan filling",
            "image": "/static/foods/pecan_pie.png",
            "price": 6,
        },
        {
            "restaurant_id": 14,
            "name": "Sweet Tea",
            "description": "Refreshing iced tea with sugar",
            "image": "/static/beverages/sweet_tea.png",
            "price": 3,
        },
        {
            "restaurant_id": 14,
            "name": "Bourbon",
            "description": "Aged bourbon on the rocks",
            "image": "/static/beverages/bourbon.png",
            "price": 7,
        },
        {
            "restaurant_id": 14,
            "name": "Mint Julep",
            "description": "Classic cocktail with bourbon, mint, and sugar",
            "image": "/static/beverages/mint_julep.png",
            "price": 7,
        },
        # BBQ Shack
        {
            "restaurant_id": 15,
            "name": "Pulled Pork Sandwich",
            "description": "Slow-cooked pulled pork with BBQ sauce served with coleslaw",
            "image": "/static/foods/pulled_pork_sandwich.png",
            "price": 10,
        },
        {
            "restaurant_id": 15,
            "name": "Beef Brisket",
            "description": "Smoked beef brisket with BBQ sauce served with coleslaw",
            "image": "/static/foods/beef_brisket.png",
            "price": 14,
        },
        {
            "restaurant_id": 15,
            "name": "Baby Back Ribs",
            "description": "Tender pork ribs with BBQ sauce served with coleslaw",
            "image": "/static/foods/baby_back_ribs.png",
            "price": 16,
        },
        {
            "restaurant_id": 15,
            "name": "Mac and Cheese",
            "description": "Creamy macaroni and cheese",
            "image": "/static/foods/mac_and_cheese.png",
            "price": 6,
        },
        {
            "restaurant_id": 15,
            "name": "Cornbread",
            "description": "Sweet and moist cornbread",
            "image": "/static/foods/cornbread.png",
            "price": 4,
        },
        {
            "restaurant_id": 15,
            "name": "Craft Beer",
            "description": "Local craft beer",
            "image": "/static/beverages/craft_beer.png",
            "price": 6,
        },
        {
            "restaurant_id": 15,
            "name": "Sweet Tea",
            "description": "Refreshing iced tea with sugar",
            "image": "/static/beverages/sweet_tea.png",
            "price": 3,
        },
        {
            "restaurant_id": 15,
            "name": "Bourbon",
            "description": "Aged bourbon on the rocks",
            "image": "/static/beverages/bourbon.png",
            "price": 7,
        },
        # Seafood Delight
        {
            "restaurant_id": 16,
            "name": "Grilled Salmon",
            "description": "Grilled salmon with lemon herb sauce served with steamed vegetables",
            "image": "/static/foods/grilled_salmon.png",
            "price": 22,
        },
        {
            "restaurant_id": 16,
            "name": "Shrimp Scampi",
            "description": "Sautéed shrimp with garlic, white wine, and butter served with pasta",
            "image": "/static/foods/shrimp_scampi.png",
            "price": 20,
        },
        {
            "restaurant_id": 16,
            "name": "Clam Chowder",
            "description": "Creamy soup with clams, potatoes, and onions",
            "image": "/static/foods/clam_chowder.png",
            "price": 8,
        },
        {
            "restaurant_id": 16,
            "name": "Fish and Chips",
            "description": "Battered fish with crispy fries and tartar sauce",
            "image": "/static/foods/fish_and_chips.png",
            "price": 14,
        },
        {
            "restaurant_id": 16,
            "name": "Lobster Roll",
            "description": "Fresh lobster with mayo and celery on a toasted bun",
            "image": "/static/foods/lobster_roll.png",
            "price": 18,
        },
        {
            "restaurant_id": 16,
            "name": "White Wine",
            "description": "Refreshing white wine",
            "image": "/static/beverages/white_wine.png",
            "price": 7,
        },
        {
            "restaurant_id": 16,
            "name": "Craft Beer",
            "description": "Local craft beer",
            "image": "/static/beverages/craft_beer.png",
            "price": 6,
        },
        {
            "restaurant_id": 16,
            "name": "Iced Tea",
            "description": "Refreshing iced tea",
            "image": "/static/beverages/iced_tea.png",
            "price": 3,
        },
        # Veggie Heaven
        {
            "restaurant_id": 17,
            "name": "Veggie Burger",
            "description": "Plant-based burger with lettuce, tomato, and onion served with sweet potato fries",
            "image": "/static/foods/veggie_burger.png",
            "price": 12,
        },
        {
            "restaurant_id": 17,
            "name": "Quinoa Salad",
            "description": "Healthy salad with quinoa, mixed greens, and roasted vegetables",
            "image": "/static/foods/quinoa_salad.png",
            "price": 10,
        },
        {
            "restaurant_id": 17,
            "name": "Lentil Soup",
            "description": "Hearty soup with lentils and vegetables",
            "image": "/static/foods/lentil_soup.png",
            "price": 8,
        },
        {
            "restaurant_id": 17,
            "name": "Stuffed Bell Peppers",
            "description": "Bell peppers filled with quinoa, beans, and vegetables",
            "image": "/static/foods/stuffed_bell_peppers.png",
            "price": 14,
        },
        {
            "restaurant_id": 17,
            "name": "Vegan Chocolate Cake",
            "description": "Delicious chocolate cake made with plant-based ingredients",
            "image": "/static/foods/vegan_chocolate_cake.png",
            "price": 6,
        },
        {
            "restaurant_id": 17,
            "name": "Green Juice",
            "description": "Healthy juice with kale, spinach, and apple",
            "image": "/static/beverages/green_juice.png",
            "price": 5,
        },
        {
            "restaurant_id": 17,
            "name": "Herbal Tea",
            "description": "Hot tea with a choice of herbs",
            "image": "/static/beverages/herbal_tea.png",
            "price": 3,
        },
        {
            "restaurant_id": 17,
            "name": "Almond Milk Latte",
            "description": "Coffee with almond milk",
            "image": "/static/beverages/almond_milk_latte.png",
            "price": 4,
        },
        # Chicken Coop
        {
            "restaurant_id": 18,
            "name": "Fried Chicken",
            "description": "Crispy fried chicken served with mashed potatoes and gravy",
            "image": "/static/foods/fried_chicken.png",
            "price": 14,
        },
        {
            "restaurant_id": 18,
            "name": "Chicken and Waffles",
            "description": "Fried chicken with fluffy waffles and maple syrup",
            "image": "/static/foods/chicken_and_waffles.png",
            "price": 14,
        },
        {
            "restaurant_id": 18,
            "name": "Chicken Caesar Salad",
            "description": "Classic salad with romaine lettuce, croutons, Parmesan cheese, and grilled chicken",
            "image": "/static/foods/chicken_caesar_salad.png",
            "price": 12,
        },
        {
            "restaurant_id": 18,
            "name": "Chicken Noodle Soup",
            "description": "Hearty soup with chicken, noodles, and vegetables",
            "image": "/static/foods/chicken_noodle_soup.png",
            "price": 8,
        },
        {
            "restaurant_id": 18,
            "name": "Chicken Pot Pie",
            "description": "Comforting pie with chicken and vegetables in a creamy sauce",
            "image": "/static/foods/chicken_pot_pie.png",
            "price": 12,
        },
        {
            "restaurant_id": 18,
            "name": "Craft Beer",
            "description": "Local craft beer",
            "image": "/static/beverages/craft_beer.png",
            "price": 6,
        },
        {
            "restaurant_id": 18,
            "name": "Sweet Tea",
            "description": "Refreshing iced tea with sugar",
            "image": "/static/beverages/sweet_tea.png",
            "price": 3,
        },
        {
            "restaurant_id": 18,
            "name": "Lemonade",
            "description": "Refreshing lemonade",
            "image": "/static/beverages/lemonade.png",
            "price": 4,
        },
        # Pasta Paradise
        {
            "restaurant_id": 19,
            "name": "Spaghetti Carbonara",
            "description": "Creamy pasta with pancetta, egg, and Pecorino Romano cheese",
            "image": "/static/foods/spaghetti_carbonara.png",
            "price": 14,
        },
        {
            "restaurant_id": 19,
            "name": "Fettuccine Alfredo",
            "description": "Pasta with creamy Alfredo sauce and Parmesan cheese",
            "image": "/static/foods/fettuccine_alfredo.png",
            "price": 12,
        },
        {
            "restaurant_id": 19,
            "name": "Lasagna",
            "description": "Layered pasta with ground beef, tomato sauce, and cheese",
            "image": "/static/foods/lasagna.png",
            "price": 16,
        },
        {
            "restaurant_id": 19,
            "name": "Pesto Pasta",
            "description": "Pasta with basil pesto sauce and Parmesan cheese",
            "image": "/static/foods/pesto_pasta.png",
            "price": 12,
        },
        {
            "restaurant_id": 19,
            "name": "Tiramisu",
            "description": "Classic Italian dessert with coffee-soaked ladyfingers and mascarpone cream",
            "image": "/static/foods/tiramisu.png",
            "price": 8,
        },
        {
            "restaurant_id": 19,
            "name": "Chianti",
            "description": "Italianred wine",
            "image": "/static/beverages/chianti.png",
            "price": 8,
        },
        {
            "restaurant_id": 19,
            "name": "Espresso",
            "description": "Strong Italian coffee",
            "image": "/static/beverages/espresso.png",
            "price": 3,
        },
        {
            "restaurant_id": 19,
            "name": "Limoncello",
            "description": "Italian lemon liqueur",
            "image": "/static/beverages/limoncello.png",
            "price": 7,
        },
        # Bakery Bliss
        {
            "restaurant_id": 20,
            "name": "Croissant",
            "description": "Flaky and buttery French pastry",
            "image": "/static/foods/croissant.png",
            "price": 3,
        },
        {
            "restaurant_id": 20,
            "name": "Baguette",
            "description": "Crusty French bread",
            "image": "/static/foods/baguette.png",
            "price": 2,
        },
        {
            "restaurant_id": 20,
            "name": "Cinnamon Roll",
            "description": "Sweet roll with cinnamon and cream cheese frosting",
            "image": "/static/foods/cinnamon_roll.png",
            "price": 4,
        },
        {
            "restaurant_id": 20,
            "name": "Blueberry Muffin",
            "description": "Moist muffin with blueberries",
            "image": "/static/foods/blueberry_muffin.png",
            "price": 3,
        },
        {
            "restaurant_id": 20,
            "name": "Chocolate Chip Cookie",
            "description": "Sweet cookie with chocolate chips",
            "image": "/static/foods/chocolate_chip_cookie.png",
            "price": 2,
        },
        {
            "restaurant_id": 20,
            "name": "Coffee",
            "description": "Hot coffee with a choice of milk",
            "image": "/static/beverages/coffee.png",
            "price": 3,
        },
        {
            "restaurant_id": 20,
            "name": "Tea",
            "description": "Hot tea with a choice of flavors",
            "image": "/static/beverages/tea.png",
            "price": 3,
        },
        {
            "restaurant_id": 20,
            "name": "Hot Chocolate",
            "description": "Sweet hot chocolate with whipped cream",
            "image": "/static/beverages/hot_chocolate.png",
            "price": 4,
        },
        # Salad Bar
        {
            "restaurant_id": 21,
            "name": "Greek Salad",
            "description": "Fresh salad with tomatoes, cucumbers, olives, and feta cheese",
            "image": "/static/foods/greek_salad.png",
            "price": 10,
        },
        {
            "restaurant_id": 21,
            "name": "Caesar Salad",
            "description": "Classic salad with romaine lettuce, croutons, and Parmesan cheese",
            "image": "/static/foods/caesar_salad.png",
            "price": 8,
        },
        {
            "restaurant_id": 21,
            "name": "Cobb Salad",
            "description": "Hearty salad with chicken, bacon, avocado, eggs, and blue cheese",
            "image": "/static/foods/cobb_salad.png",
            "price": 12,
        },
        {
            "restaurant_id": 21,
            "name": "Spinach Salad",
            "description": "Healthy salad with spinach, strawberries, almonds, and goat cheese",
            "image": "/static/foods/spinach_salad.png",
            "price": 10,
        },
        {
            "restaurant_id": 21,
            "name": "Quinoa Salad",
            "description": "Healthy salad with quinoa, mixed greens, and roasted vegetables",
            "image": "/static/foods/quinoa_salad.png",
            "price": 10,
        },
        {
            "restaurant_id": 21,
            "name": "Green Juice",
            "description": "Healthy juice with kale, spinach, and apple",
            "image": "/static/beverages/green_juice.png",
            "price": 5,
        },
        {
            "restaurant_id": 21,
            "name": "Herbal Tea",
            "description": "Hot tea with a choice of herbs",
            "image": "/static/beverages/herbal_tea.png",
            "price": 3,
        },
        {
            "restaurant_id": 21,
            "name": "Fruit Smoothie",
            "description": "Blended smoothie with a choice of fruits and almond milk",
            "image": "/static/beverages/fruit_smoothie.png",
            "price": 6,
        },
        # Ramen House
        {
            "restaurant_id": 22,
            "name": "Tonkotsu Ramen",
            "description": "Ramen with pork bone broth, pork belly, and soft-boiled egg",
            "image": "/static/foods/tonkotsu_ramen.png",
            "price": 12,
        },
        {
            "restaurant_id": 22,
            "name": "Shoyu Ramen",
            "description": "Ramen with soy sauce broth, chicken, and soft-boiled egg",
            "image": "/static/foods/shoyu_ramen.png",
            "price": 11,
        },
        {
            "restaurant_id": 22,
            "name": "Miso Ramen",
            "description": "Ramen with miso broth, corn, and soft-boiled egg",
            "image": "/static/foods/miso_ramen.png",
            "price": 11,
        },
        {
            "restaurant_id": 22,
            "name": "Gyoza",
            "description": "Japanese dumplings with pork and vegetables",
            "image": "/static/foods/gyoza.png",
            "price": 6,
        },
        {
            "restaurant_id": 22,
            "name": "Takoyaki",
            "description": "Fried octopus balls with bonito flakes and mayo",
            "image": "/static/foods/takoyaki.png",
            "price": 6,
        },
        {
            "restaurant_id": 22,
            "name": "Sake",
            "description": "Japanese rice wine",
            "image": "/static/beverages/sake.png",
            "price": 6,
        },
        {
            "restaurant_id": 22,
            "name": "Green Tea",
            "description": "Hot Japanese green tea",
            "image": "/static/beverages/green_tea.png",
            "price": 3,
        },
        {
            "restaurant_id": 22,
            "name": "Plum Wine",
            "description": "Sweet Japanese wine made from plums",
            "image": "/static/beverages/plum_wine.png",
            "price": 7,
        },
        # Ice Cream Shop
        {
            "restaurant_id": 23,
            "name": "Vanilla Ice Cream",
            "description": "Creamy ice cream with vanilla flavor",
            "image": "/static/foods/vanilla_ice_cream.png",
            "price": 3,
        },
        {
            "restaurant_id": 23,
            "name": "Chocolate Ice Cream",
            "description": "Rich ice cream with chocolate flavor",
            "image": "/static/foods/chocolate_ice_cream.png",
            "price": 3,
        },
        {
            "restaurant_id": 23,
            "name": "Strawberry Ice Cream",
            "description": "Sweet ice cream with strawberry flavor",
            "image": "/static/foods/strawberry_ice_cream.png",
            "price": 3,
        },
        {
            "restaurant_id": 23,
            "name": "Mint Chocolate Chip Ice Cream",
            "description": "Refreshing ice cream with mint and chocolate chips",
            "image": "/static/foods/mint_chocolate_chip_ice_cream.png",
            "price": 4,
        },
        {
            "restaurant_id": 23,
            "name": "Cookie Dough Ice Cream",
            "description": "Delicious ice cream with chunks of cookie dough",
            "image": "/static/foods/cookie_dough_ice_cream.png",
            "price": 4,
        },
        {
            "restaurant_id": 23,
            "name": "Root Beer Float",
            "description": "Classic dessert with root beer and vanilla ice cream",
            "image": "/static/beverages/root_beer_float.png",
            "price": 5,
        },
        {
            "restaurant_id": 23,
            "name": "Milkshake",
            "description": "Creamy milkshake with vanilla, chocolate, or strawberry",
            "image": "/static/beverages/milkshake.png",
            "price": 5,
        },
        {
            "restaurant_id": 23,
            "name": "Iced Coffee",
            "description": "Refreshing iced coffee with a choice of milk",
            "image": "/static/beverages/iced_coffee.png",
            "price": 4,
        },
        # Sandwich Shop
        {
            "restaurant_id": 24,
            "name": "Turkey Sandwich",
            "description": "Sandwich with turkey, lettuce, tomato, and mayo",
            "image": "/static/foods/turkey_sandwich.png",
            "price": 8,
        },
        {
            "restaurant_id": 24,
            "name": "Ham Sandwich",
            "description": "Sandwich with ham, cheese, lettuce, and mustard",
            "image": "/static/foods/ham_sandwich.png",
            "price": 8,
        },
        {
            "restaurant_id": 24,
            "name": "Tuna Salad Sandwich",
            "description": "Sandwich with tuna salad and lettuce",
            "image": "/static/foods/tuna_salad_sandwich.png",
            "price": 8,
        },
        {
            "restaurant_id": 24,
            "name": "BLT Sandwich",
            "description": "Classic sandwich with bacon, lettuce, and tomato",
            "image": "/static/foods/blt_sandwich.png",
            "price": 8,
        },
        {
            "restaurant_id": 24,
            "name": "Grilled Cheese Sandwich",
            "description": "Comforting sandwich with melted cheese",
            "image": "/static/foods/grilled_cheese_sandwich.png",
            "price": 6,
        },
        {
            "restaurant_id": 24,
            "name": "Soda",
            "description": "Refreshing carbonated drink",
            "image": "/static/beverages/soda.png",
            "price": 3,
        },
        {
            "restaurant_id": 24,
            "name": "Iced Tea",
            "description": "Refreshing iced tea",
            "image": "/static/beverages/iced_tea.png",
            "price": 3,
        },
        {
            "restaurant_id": 24,
            "name": "Coffee",
            "description": "Hot coffee with a choice of milk",
            "image": "/static/beverages/coffee.png",
            "price": 3,
        },
        # Pancake House
        {
            "restaurant_id": 25,
            "name": "Buttermilk Pancakes",
            "description": "Fluffy pancakes served with butter and maple syrup",
            "image": "/static/foods/buttermilk_pancakes.png",
            "price": 8,
        },
        {
            "restaurant_id": 25,
            "name": "Blueberry Pancakes",
            "description": "Pancakes with blueberries served with butter and maple syrup",
            "image": "/static/foods/blueberry_pancakes.png",
            "price": 9,
        },
        {
            "restaurant_id": 25,
            "name": "Chocolate Chip Pancakes",
            "description": "Pancakes with chocolate chips served with butter and maple syrup",
            "image": "/static/foods/chocolate_chip_pancakes.png",
            "price": 9,
        },
        {
            "restaurant_id": 25,
            "name": "Bacon and Egg Pancakes",
            "description": "Pancakes with bacon and eggs served with butter and maple syrup",
            "image": "/static/foods/bacon_and_egg_pancakes.png",
            "price": 10,
        },
        {
            "restaurant_id": 25,
            "name": "Banana Nut Pancakes",
            "description": "Pancakes with bananas and nuts served with butter and maple syrup",
            "image": "/static/foods/banana_nut_pancakes.png",
            "price": 9,
        },
        {
            "restaurant_id": 25,
            "name": "Coffee",
            "description": "Hot coffee with a choice of milk",
            "image": "/static/beverages/coffee.png",
            "price": 3,
        },
        {
            "restaurant_id": 25,
            "name": "Orange Juice",
            "description": "Freshly squeezed orange juice",
            "image": "/static/beverages/orange_juice.png",
            "price": 4,
        },
        {
            "restaurant_id": 25,
            "name": "Milk",
            "description": "Cold milk",
            "image": "beverages/milk.png",
            "price": 2,
        },
        # Your New Food
        {
            "restaurant_id": 1,
            "name": "Your New Food",
            "description": "Your food description",
            "image": "/static/foods/your_food_image.png",
            "price": 15,
>>>>>>> 40731b41b3bfe5317ad9c6b9b89eb31a1ced9642
        },
    ]


    # Populate restaurants table
    for restaurant in restaurants:
        add_restaurant(
            db, restaurant["name"], restaurant["description"], restaurant["image"]
        )

    # Populate foods table
    for food in foods:
        add_food(
            db,
            food["restaurant_id"],
            food["name"],
            food["description"],
            food["image"],
            food["price"],
        )

    print("Data populated successfully!")


if __name__ == "__main__":
    main()
