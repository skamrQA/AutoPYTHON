from smartphone import Smartphone

phone1 = Smartphone("9R", "OnePlus", "+79115468799")
phone2 = Smartphone("13x", "Xiaomi", "+79009874544")
phone3 = Smartphone("14Pro", "Apple", "+79521235555")

catalog = [phone1, phone2, phone3]

for i in catalog:
    i.say_phone()