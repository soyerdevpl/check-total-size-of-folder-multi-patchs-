import os

# Ścieżka do katalogu, w którym znajduje się skrypt
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ścieżka do pliku tekstowego z listą folderów
folder_list_path = os.path.join(script_dir, "foldery.txt")

# Funkcja do obliczania rozmiaru folderu
def get_folder_size(folder):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    return total_size

# Wczytaj ścieżki folderów z pliku tekstowego
with open(folder_list_path, 'r', encoding='utf-8') as file:
    folders = file.readlines()

# Zmienna do przechowywania całkowitego rozmiaru
total_size = 0

# Iteracja przez każdy folder i obliczanie jego rozmiaru
for folder in folders:
    folder = folder.strip()
    if os.path.exists(folder):
        folder_size = get_folder_size(folder)
        total_size += folder_size
    else:
        print(f"Folder nie istnieje: {folder}")

# Konwersja rozmiaru na GB i wyświetlenie wyniku
total_size_gb = round(total_size / (1024 ** 3), 2)
print(f"Całkowity rozmiar folderów: {total_size_gb} GB")
