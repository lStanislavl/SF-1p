import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    # Установка неявного ожидания
    driver.implicitly_wait(10)
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')
    yield driver
    driver.quit()

def test_show_all_pets(driver):
    # Проверка явного ожидания
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'email')))
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('vasya@mail.com')
    # Явное ожидание поля пароля
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'pass')))
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('12345')
    # Явное ожидание кнопки входа
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    # Добавляем явные ожидания для элементов таблицы
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-deck .card')))
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-img-top')))
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-title')))
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-text')))

def test_my_pets_implicit(driver):
    """Тест с неявными ожиданиями для элементов карточек питомцев"""
    # Вход с использованием неявного ожидания
    driver.find_element(By.ID, 'email').send_keys('vasya@mail.com')
    driver.find_element(By.ID, 'pass').send_keys('12345')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверка заголовка
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    # Проверка элементов карточек с неявным ожиданием
    images = driver.find_elements(By.CSS_SELECTOR, '.card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-text')

    # Проверяем что элементы найдены (количество > 0)
    assert len(images) > 0
    assert len(names) > 0
    assert len(descriptions) > 0