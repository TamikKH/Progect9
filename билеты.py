#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    routes = []
    while True:
        print("1. Добавить маршрут")
        print("2. Найти маршруты по пункту")
        print("3. Выйти")
        choice = input("Выберите действие (1/2/3): ")
        if choice == "1":
            start = input("Введите начальный пункт маршрута: ")
            end = input("Введите конечный пункт маршрута: ")
            number = int(input("Введите номер маршрута: "))
            route = {"start": start, "end": end, "number": number}
            routes.append(route)
#            routes.sort(key=lambda x: x["number"])
            print("Маршрут добавлен.")
        elif choice == "2":
            location = input("Введите название пункта маршрута: ")
            found_routes = []
            for route in routes:
                if route["start"] == location or route["end"] == location:
                    found_routes.append(route)
            if found_routes:
                print("Найденные маршруты:")
                for route in found_routes:
                    print(f"Маршрут {route['number']}: {route['start']} - {route['end']}")
            else:
                print("Маршруты не найдены.")
        elif choice == "3":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
