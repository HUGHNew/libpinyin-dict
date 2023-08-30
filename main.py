import os

from common import convert_data_base, get_sogo_dict, get_sogo_dict_pair_list
from convert import docker_cmd

if __name__ == "__main__":
    if not os.path.exists("output"):
        os.mkdir("output")
    convert_data_base("./phrase-pinyin-data/large_pinyin.txt", False, "output/large.txt")
    if os.path.exists("./user-defined.txt"):
        convert_data_base("./user-defined.txt", True, "output/user.txt")
    get_sogo_dict()
    # imeconverter
    dict_pair = get_sogo_dict_pair_list()
    for i, o in dict_pair:
        cmd = docker_cmd(i, o)
        print(f"$ {cmd}")
        os.system(cmd)
        convert_data_base(o, False, "output"+o)
        os.remove(o)
