import re
import json

def parse_receipt(filename):
    print(f"=== ПАРСИНГ ЧЕКА ИЗ ФАЙЛА {filename} ===\n")
    try:
        # Открываем файл с чеком
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            
        # Шаблоны для поиска
        datetime_pattern = r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})"
        total_pattern = r"ИТОГО:\n([\d\s]+,\d{2})"
        payment_pattern = r"(Банковская карта|Наличные)"
        item_pattern = r"^\d+\.\n(.*?)\n\d+,\d{3}\s*x\s*([\d\s]+,\d{2})"

        # Поиск по тексту чека
        dt_match = re.search(datetime_pattern, text)
        total_match = re.search(total_pattern, text)
        payment_match = re.search(payment_pattern, text)
        items_found = re.findall(item_pattern, text, re.MULTILINE)

        # Сборка данных в словарь
        parsed_data = {
            "Date": dt_match.group(1) if dt_match else "Не найдено",
            "Time": dt_match.group(2) if dt_match else "Не найдено",
            "Payment_Method": payment_match.group(1) if payment_match else "Не найдено",
            "Total_Amount": total_match.group(1).replace(" ", "") if total_match else "Не найдено",
            "Products": []
        }

        for name, price in items_found:
            parsed_data["Products"].append({
                "Product_Name": name.strip(), 
                "Price": price.replace(" ", "")
            })

        # Вывод на экран
        print(json.dumps(parsed_data, indent=4, ensure_ascii=False))

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден в папке!")

# Запуск парсера
parse_receipt("raw.txt")
parse_receipt("raw.txt")
