from src.utils import load_json, sort_data, clear_data, list_class, JSON_FILE


def main():
    data = load_json(JSON_FILE)
    cleared_data = clear_data(data)
    sorted_data = sort_data(cleared_data)
    list_operations = list_class(sorted_data)
    for item in list_operations[:5]:
        print(item)


if __name__ == '__main__':
    main()
