# Тестовое задание  


1) Используя фреймворк django создать веб-сервис
2) Создать две модели:
Organization, поля: name:str, description:str, 
Shop, поля: organization_id(Foreign key), 
name:str, 
description:str, 
address:str, 
index:int, 
is_deleted:bool
3) С помощью библиотеки djangorestframework создать метод GET /api/organizations/, который будет возвращать список существующих организаций со всеми полями и вложенными магазинами, у которых is_deleted = False. Пример ответа метода:
{
	"name": "str",
	"description": "str",
	"shops": [
		{
			"name": "str",
			"description": "str",
			"address": "str",
			"index": int
		(
	]
}
4) Создать метод PUT /api/shops/{id}/ - обновление сущности магазина
5) Создать метод GET /organizations/{id}/shops_file/ который будет возвращать файл с расширением xlsx(или csv, не важно), где будут колонки с названием полей магазинов, а строки - это привязанные к данной организации магазины. Пример:
	id, name
	1, test_shop
	2, test_shop2
6) Задокументировать api методы с помощью drf spectacular.
7) Добавить jwt авторизацию к апи методам с помощью библиотеки djangorestframework-simplejwt
8) Настроить в проекте whitenoise (проверить что статика отдаются при запуске не встроенным сервером а gunicorn)
ModuleNotFoundError: No module named 'fcntl' так как только на линуксе доступно, а у меня винда
9) Описать зависимости с помощью poetry
10) С помощью библиотеки django4-background-tasks создать фоновую задачу, которая будет отправлять письмо на почту. Создание задачи сделать в методе PUT /api/shop/{id}/
11) Добавить логирование в api методы.
12) Вывести модель Organization в административную панель, поля: name, description. C помощью inlines добавить магазины, связанные с организацией.
13) Переопределить любой template в административной панели. Подключить css и js. Поменять цвет кнопок и распечатать любой текст в консоли.
14) Создать middleware, который при каждом вызове любого api метода пишет в логи сообщение с названием метода
15) Написать Dockerfile, который будет собирать docker-образ сервиса
