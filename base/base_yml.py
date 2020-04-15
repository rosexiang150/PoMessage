import yaml

# 定义一个方法，专门读取.yaml文件，并把yaml文件返回
def yml_data_with_file(file_name):

    # with open('./data/search_data.yaml', 'r') as f:
    with open('./data/' " + file_name + " '.yaml', 'r') as f:
        return yaml.load(f)