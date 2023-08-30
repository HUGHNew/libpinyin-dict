IME_CONFIG = {
    "image": "mritd/imewlconverter", # pull from hub.docker.com
    "os": "linux",
    "ifmt": "scel",
    "ofmt": "libpy", # convert to libpinyin
}
docker_cmd = lambda i,o: \
    "docker run --rm -it -v $(pwd):/dict {image} -i:{ifmt} /dict/{i} -os:{os} -ct:pinyin -o:{ofmt} /dict/{o}".format_map(
        {"i":i , "o":o , **IME_CONFIG}
    )