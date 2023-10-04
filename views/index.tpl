<!DOCTYPE html>
<html>
<head>
    <title>Поиск информации на сайтах</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        h1 {
            color: #333;
        }

        label {
            font-weight: bold;
        }

        .button-container {
            display: flex;
            justify-content: space-between; 
            gap: 10px; 
        }

        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        input[type="submit"] {
            background-color: #333;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #555;
        }
    </style>
</head>
<body>
    <h1>Поиск информации на сайтах</h1>
    <form action="/add_website" method="post">
        <label for="url">Введите URL сайта:</label>
        <input type="text" id="url" name="url" required>
        <div class="button-container">
            <input type="submit" value="Добавить сайт">
        </div>
    </form>
    <form action="/clear_database" method="post">
        <div class="button-container">
            <input type="submit" value="Очистить базу данных">
        </div>
    </form>
    <form action="/view_websites">
        <div class="button-container">
            <input type="submit" value="Просмотреть базу данных">
        </div>
    </form>    
    <form action="/search" method="post">
        <label for="keywords">Введите ключевые слова для поиска (через запятую):</label>
        <input type="text" id="keywords" name="keywords" required>
        <input type="submit" value="Найти">
    </form>
</body>
</html>
