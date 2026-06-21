def get_cats_info(path):
    cats_list = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 3:
                    cat_dict = {
                        "id": data[0],
                        "name": data[1],
                        "age": data[2]
                    }
                    cats_list.append(cat_dict)
        return cats_list

    except FileNotFoundError:
        print("pass")
        return []
    except Exception as e:
        print(f"reading err{e}")
        return []

# cats_info = get_cats_info("cats_file.txt")
