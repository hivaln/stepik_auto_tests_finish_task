from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)  # Инициализация страницы товара
    page.open()  # Открываем страницу товара
    page.add_to_basket()  # Добавляем товар в корзину
    page.solve_quiz_and_get_code()  # Решаем задачу и получаем код
    page.should_be_success_message()  # Проверяем, что товар добавлен
    page.should_be_correct_product_name()  # Проверяем, что название товара в сообщении совпадает
    page.should_be_correct_basket_price()  # Проверяем, что цена корзины совпадает с ценой товара
