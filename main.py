from offer.offer import Offer as Bot

try:
    bot = Bot()
    bot.land_first_page()
    bot.select_offer_field("cybersécurité")
    bot.select_offer_place("ile de")
    bot.apply_filtration()
    bot.report_offers()
except Exception as e:
    raise