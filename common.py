from pypinyin import lazy_pinyin
from pypinyin.contrib.tone_convert import to_normal
import requests

from sogo_dict import SOGO_DOMAIN, SOGO_LIST, SOGO_NIKE_LIST

PINYIN_SEP = '\''
LIB_STR_FORMAT = lambda word, pinyin, count: f"{word} {pinyin} {count}\n"

def get_sogo_dict():
    for idx, _ in enumerate(SOGO_LIST):
        get_sogo_dict_by_index(idx)

def get_sogo_dict_by_index(index:int):
    payload = SOGO_LIST[index]
    name = SOGO_NIKE_LIST[index]+".scel"
    resp = requests.get(SOGO_DOMAIN, payload)
    resp.status_code
    with open(name, "wb") as oput:
        oput.write(resp.content)

def convert_data_base(file:str, user_define:bool, output:str):
    # no existing check for input file
    with open(file) as iput:
        content = iput.read().splitlines()

    output_dict = []
    for line in content:
        oline = convert_user_define_data(line) if user_define else convert_module_data(line)
        if not oline: continue
        output_dict.append(oline)

    # simple write without makedir
    with open(output, "w") as oput:
        oput.writelines(output_dict)

def convert_module_data(line:str, count:int=5) -> str:
    """
    format large_pinyin.txt to libpinyin
    㐖毒, [xie du] -> 㐖毒 xie'du 5
    """
    # remove comments
    comment_idx = line.find('#')
    if comment_idx == 0 or len(line) == 0:
        return None # comment line
    elif comment_idx != -1:
        line = line[:comment_idx]

    # refactor
    parts = line.split()
    word = parts[0][:-1]
    pys = PINYIN_SEP.join([
        to_normal(p)
        for p in parts[1:]
    ])
    return LIB_STR_FORMAT(word, pys, count)

def convert_user_define_data(line:str, count:int=5) -> str:
    """
    Rust -> rust # no work for double pinyin
    一眼丁真 -> 一眼丁真
    """
    if len(line) == 0 or line[0] == '#': return None
    words = line.strip().split()
    if len(words) > 1: # its count must be 2
        count = int(words[-1])
    word = words[0]
    if ord(word[0]) < 255: # Chinese word or English word
        pinyin = word.lower()
    else:
        pinyin = PINYIN_SEP.join(lazy_pinyin(word))
    return LIB_STR_FORMAT(word, pinyin, count)

