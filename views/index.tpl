<!DOCTYPE html>
<html>
<head>
    <title>Поиск информации на сайтах</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            transition: background-color 0.3s, color 0.3s;
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
            align-items: flex-end; 
            gap: 10px; 
        }

        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            background-color: #fff;
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

        body.dark-mode {
            background-color: #333;
            color: #fff;
        }

        body.dark-mode h1 {
            color: #fff; 
        }

        body.dark-mode input[type="text"] {
            background-color: #444;
            border: 1px solid #666;
            color: #fff;
        }

        body.dark-mode input[type="submit"] {
            background-color: #666;
            color: #fff;
        }

        .theme-toggle {
            position: absolute;
            top: 20px;
            right: 20px;
            cursor: pointer;
            font-size: 24px;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="theme-toggle" onclick="toggleDarkMode()">
        <i class="fas fa-lightbulb"></i>
    </div>

    <div>
        <h1>Поиск информации на сайтах</h1>
        <form action="/add_website" method="post">
            <label for="url">Введите URL сайта:</label>
            <input type="text" id="url" name="url" required>
            <div class="button-container">
                <input type="submit" value="Добавить сайт">
            </div>
        </form>
        <table>
        <tr>
        <td>
        <form action="/clear_database" method="post">
            <div class="button-container">
                <input type="submit" value="Очистить базу данных">
            </div>
        </form>
        </td>
        <td>
        <form action="/view_websites">
            <div class="button-container">
                <input type="submit" value="Просмотреть базу данных">
            </div>
        </form>    
        </td>
        <form action="/search" method="post">
            <label for="keywords">Введите ключевые слова для поиска (через запятую):</label>
            <input type="text" id="keywords" name="keywords" required>
            <td><div class="button-container">
                <input type="submit" value="Найти (Google)">
            </div></td>
            <td><div class="button-container">
                <input type="submit" value="Найти (Yandex)">
            </div></td>
        </form>
        </tr>
        </table>
    </div>

    <script>
        function toggleDarkMode() {
            const body = document.body;
            body.classList.toggle('dark-mode');
            
            const isDark = body.classList.contains('dark-mode');
            localStorage.setItem('isDark', isDark);
        }

        const savedIsDark = localStorage.getItem('isDark');
        if (savedIsDark === 'true') {
            toggleDarkMode(); 
        }
    </script>
</body>
</html>
 