<!DOCTYPE html>
<html>
<head>
    <title>Результаты поиска</title>
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

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        th, td {
            border: 1px solid #ccc;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #333;
            color: #fff;
        }

        /* Стили для темной темы */
        body.dark-mode {
            background-color: #333;
            color: #fff;
        }

        body.dark-mode h1 {
            color: #fff; 
        }

        body.dark-mode th, body.dark-mode td {
            border-color: #666;
        }

        body.dark-mode th {
            background-color: #444;
        }

        body.dark-mode a {
            color: #0099cc;
        }
    </style>
</head>
<body>
    <div class="theme-toggle" onclick="toggleDarkMode()">
        <i class="fas fa-lightbulb"></i>
    </div>

    <h1>Результаты поиска</h1>
    <table>
        <tr>
            <th>Ссылка</th>
            <th>Баллы</th>
        </tr>
        % for url, score in results:
        <tr>
            <td><a href="{{url}}" target="_blank">{{url}}</a></td>
            <td>{{score}}</td>
        </tr>
        % end
    </table>

    <script>
        // Функция для переключения темы
        function toggleDarkMode() {
            const body = document.body;
            body.classList.toggle('dark-mode');
        }

        // Проверяем сохраненное значение и устанавливаем режим
        const savedIsDark = localStorage.getItem('isDark');
        if (savedIsDark === 'true') {
            toggleDarkMode(); // Включаем темный режим, если в файле сохранено true
        }
    </script>
</body>
</html>
