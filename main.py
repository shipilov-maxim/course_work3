from src.utils import sort_data
from src.utils import JSON_FILE
from src.utils import load_json
from src.utils import list_class
from src.utils import clear_data



def main():
    data = load_json(JSON_FILE)
    cleared_data = clear_data(data)
    sorted_data = sort_data(cleared_data)
    list_operations = list_class(sorted_data)
    for item in list_operations[:5]:
        print(item)

if __name__ == '__main__':
    main()