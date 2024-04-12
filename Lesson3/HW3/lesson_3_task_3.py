from address import Address
from mailing import Mailing


address_one = Address("100110", "Мирный", "Ленинингратский пр-к", "21/1", "28")
address_two = Address("100110", "Мирный", "Ленинингратский пр-к", "21", "5")

mail = Mailing(address_one, address_two, 215550, "12345")

print(f"Отправление {mail.track} из {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apart} в {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apart}. Стоимость {mail.cost} рублей.")