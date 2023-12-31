# libpinyin user-dict

输入法的安装参考[这里](https://hughnew.github.io/RDLog/post/2023-08/quickstart-pinyin-installation/)

libpinyin 自定义用户词典

- 通过 phrase-pinyin-data 项目提供大量数据
- 下载搜狗词库
- 支持用户自定义词典
- 支持英文词典(但似乎用不了)

submodules
- [phrase-pinyin-data](https://github.com/mozillazg/phrase-pinyin-data)

## 使用


```bash
# 下载所需工具
pip install -r requirements.txt
docker pull mritd/imewlconverter:latest
git submodule update --init

# 执行命令
# 按序执行
# 1. 创建 ouput 文件夹
# 2. 转换 large_pinyin
# 3. 转换 user-defined 如果存在的话
# 4. 获取搜狗词典 相关配置在 sogo_dict.py 中
# 5. 转换搜狗词典
python3 main.py
```

然后在设置中添加转换后的词典

![ibus-pref](user-data.png)

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
docker run --rm -it -v /dict:/dict mritd/imewlconverter -i:scel /dict/cs.scel -os:linux -ct:pinyin -o:libpy /dict/cs.txt
```

也可以使用 [Dockerfile](https://github.com/studyzy/imewlconverter/blob/master/Dockerfile) 自己构建镜像