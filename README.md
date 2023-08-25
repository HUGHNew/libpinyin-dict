# libpinyin user-dict

libpinyin 自定义用户词典

- 通过 phrase-pinyin-data 项目提供大量数据
- 下载搜狗词库
- 支持用户自定义词典
- 支持英文词典(但似乎用不了)

submodules
- [phrase-pinyin-data](https://github.com/mozillazg/phrase-pinyin-data)

## 词典

数据来源为
- pypinyin项目原始数据 在submodule中 主要使用 `large_pinyin.txt`
- 搜狗词库: https://pinyin.sogou.com/dict/
- 用户自定义数据

自定义数据格式

```
# 注释 行首为 #
一个词
词 5
# word [count]
```

## 数据格式转换

参考 main.py

搜狗数据格式转换

```
docker run --rm -it -v /dict:/dict imewlconverter -i:scel /dict/cs.scel -os:linux -ct:pinyin -o:libpy /dict/cs.txt
```