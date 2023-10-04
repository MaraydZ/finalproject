<!DOCTYPE html>
<html>
<head>
    <title>Результаты поиска</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
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
    </style>
</head>
<body>
    <h1>Результаты поиска</h1>
    <table>
        <tr>
            <th>Сайт</th>
            <th>Ключевые слова</th>
        </tr>
        % for url, counts in results:
            <tr>
                <td>{{url}}</td>
                <td>
                    % for keyword, count in counts.items():
                        {{keyword}}: {{count}} вхождений<br>
                    % end
                </td>
            </tr>
        % end
    </table>
</body>
</html>
