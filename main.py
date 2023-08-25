import os

from common import convert_data_base, get_sogo_dict

if __name__ == "__main__":
    if not os.path.exists("output"):
        os.mkdir("output")
    convert_data_base("./phrase-pinyin-data/large_pinyin.txt", False, "output/large.txt")
    convert_data_base("./user-defined.txt", True, "output/user.txt")
    get_sogo_dict()
    # TODO: imeconverter
