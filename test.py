from common import convert_module_data, convert_user_define_data, convert_data_base, to_normal

if __name__ == "__main__":
    print(to_normal("ǚ"))
    mlines = [
        "# source: https://github.com/mozillazg/phrase-pinyin-data",
        "㐖毒: xié dú"
    ]
    ud = ["鲲鲲", "一眼丁真\n", "Rust"]
    for l in mlines:
        print(convert_module_data(l), end='')
    for l in ud:
        print(convert_user_define_data(l), end='')
    convert_data_base("demo/mt.txt", False, "demo/mt.o")
    # convert_data_base("demo/ud.txt", True, "demo/ud.o")
    convert_data_base("./user-defined.txt", True, "demo/ud.o")