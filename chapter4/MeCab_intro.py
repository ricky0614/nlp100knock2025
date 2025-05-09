!apt-get -y install mecab libmecab-dev mecab-ipadic-utf8
!pip install --force-reinstall mecab-python3
!cp /etc/mecabrc /usr/local/etc/

# IPA辞書を利用する
# 茶筌出力にしたいときはunidic-liteを利用する
