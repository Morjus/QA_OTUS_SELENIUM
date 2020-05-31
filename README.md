# QA_OTUS_SELENIUM
Repository selenium works

Поиск элементов на странице.
Цель: Нучиться использовать методы поиска элементов в selenium.
1. Написать тесты проверяющие наличие элементов на разных страницах приложения opencart.
2. Реализовать минимум пять тестов (одни тест = одна страница приложения)
3. Какие элементы проверять определить самостоятельно, но не меньше 5 для каждой страницы.

Покрыть нужно:

1. Главную /
2. Каталог /index.php?route=product/category&path=20
3. Карточку товара /index.php?route=product/product&path=57&product_id=49
4. Страницу логина /index.php?route=account/login
5. Страницу логина в админку /admin/

**Критерии оценки:** Использования различных типов локаторов и селекторов.
Рекомендуем сдать до: 11.05.2020 


# Ожидание элементов.
**Цель:** Научиться использовать ожидания и обработку исключений в тестах


1. К существующим тестам добавить явные ожидания элементов.
2. Добавить 2 тестовых сценария на раздел администратора
3. Добавить проверку логина и разлогина раздела.
4. Добавить проверку перехода к разделу с товарами, что появляется таблица с товарами.


**Критерии оценки:** Приложить скриншот того что тесты проходят.
Ссылку на пул-реквест к своему проекту.


# Работа с элементами.
**Цель:** Попрактиковаться в работе со свойствами элементов.


Для страницы Products реализовать тесты, которые проверяют:
1. Функциональность добавления.
2. Функциональность изменения.
3. Функциональность удаления продукта.


**Дополнительно:** Реализовать предусловие которое гарантирует наличие продукта в списке для тестов удаления и редактирования.
Рекомендуем сдать до: 18.05.2020


# PageObject.
**Цель:** Научиться реализовывать паттерн PageObject на практике.


В имеющемся проекте автоматизации приложения OpenCart на данный момент имеются описания селекторов страниц и небольшой пул автотестов.
Необходимо перевести код на паттерн PageObject. Добавить 5 новых тестов написанных в этой парадигме.
Выбор функциональности или сценариев остается на ваше усмотрение.


Критерии оценки: Тесты проекта выполнены в парадигме PageObject.
Рекомендуем сдать до: 21.05.2020