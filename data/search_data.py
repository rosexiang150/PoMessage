import yaml

def main():
    data = {'search_data': ['hello', '123', '456', '789']}
    with open('./search_data.yaml', 'w') as f:
        yaml.dump(data, f, encoding='utf-8', allow_unicode='True')

if __name__ == '__main__':
    main()