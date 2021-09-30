# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Добавьте в папку с кодом файл wine.xlsx c колонками: 
<table>
  <tr>
    <th>Категории</th>
    <th>Название</th>
    <th>Сорт</th>
    <th>Картинка</th>
    <th>Акция</th>
    
  </tr>
  <tr>
    <td> Категория1</td>
    <td>Название1.75</td>
    <td>Сорт1</td>
    <td>Картинка1</td>
    <td>Акция1</td>
  </tr>
  <tr>
    <td>Категория1</td>
    <td>Название1.25</td>
    <td>Сорт1</td>
    <td>Картинка1</td>
    <td>Акция1</td>
  </tr>
</table>
или используйте шаблон из текущего репозитория.
- Установите необходимые пакеты:
```bash
$pip install -r requirements.txt
```
- Запустите сайт командой
```bash
$python3 main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
