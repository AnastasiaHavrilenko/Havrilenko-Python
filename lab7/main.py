def print_dictionaary(dictionary):    #Функція друку усіх значень словника
  print("Значення словника:")
  for country, info in dictionary.items():
      print(f"{country}: {info}")

def add(dictionary, country, area, population, region):  #Функція додавання значення до словника
  dictionary[country] = {"Площа": area, "Населення": population, "Частина світу": region}
  print(f"{country} додано до словника.")

def remove(dictionary, country):    #Функція видалення значення зі словника
  if country in dictionary:
      del dictionary[country]
      print(f"{country} видалено зі словника.")
  else:
      print(f"{country} не знайдено у словнику.")

def main():
  n = 10  # Кількість країн
  countries_dictionary = {}

  countries_dictionary["Україна"] = {"Площа": 603550, "Населення": 44009214, "Частина світу": "Європа"}
  countries_dictionary["Ефіопія"] = {"Площа": 1112000, "Населення": 120337672, "Частина світу": "Африка"}
  countries_dictionary["Китай"] = {"Площа": 9596961, "Населення": 1409517397, "Частина світу": "Азія"}
  

  while True:
      print("\nМеню:")
      print("1. Вивести значення словника")
      print("2. Додати новий запис до словника")
      print("3. Видалити запис зі словника")
      print("4. Перевірити країни в Африці або Азії")
      print("5. Вийти з програми")
      choice = input("Виберіть опцію (1/2/3/4/5): ")

      if choice == "1":
        print_dictionaary(countries_dictionary) 
      elif choice == "2":
          country = input("Введіть назву країни: ")
          area = float(input("Введіть площу: "))
          population = int(input("Введіть населення: "))
          region = input("Введіть частину світу: ")
          add(countries_dictionary, country, area, population, region)
      elif choice == "3":
          country = input("Введіть назву країни для видалення: ")
          remove(countries_dictionary, country)
      elif choice == "4":
          print("Країни в Африці або Азії:")
          for country, info in countries_dictionary.items():
              if info["Частина світу"] in ["Африка", "Азія"]:
                  print(country)
      elif choice == "5":
          break
      else:
          print("Некоректний вибір. Спробуйте ще раз.")
main()
