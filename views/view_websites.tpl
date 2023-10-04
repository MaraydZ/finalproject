<!DOCTYPE html>
<html>
<head>
    <title>Просмотр всех сайтов</title>
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
    <h1>Все добавленные сайты:</h1>
    <ul>
        % for website in websites:
        <li>{{ website[1] }}</li>
        % end
    </ul>
    <a href="/">Вернуться на главную страницу</a>
</body>
</html>
