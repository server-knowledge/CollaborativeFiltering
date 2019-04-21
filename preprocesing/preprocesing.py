# -- coding: utf-8 --
import random
from data.csv_handler import create_csv, append_csv

# 设置一些参数

# 歌曲数量
SONG_COUNT = 100
# 用户数量
USER_COUNT = 5
# 每首歌听过的最大次数
MAX_LICENSED_COUNT = 20


def get_index(count_temp):
    index_list_temp = []
    count = 0
    while count < count_temp:
        index = random.randint(1, USER_COUNT)
        if index != count_temp:
            count += 1
            index_list_temp.append(index)
    return index_list_temp


def main():
    csv_head = []
    for item in range(USER_COUNT):
        csv_head.append('user' + str(item))
    create_csv(csv_head)
    result_list = []
    for item in range(SONG_COUNT):
        listened_count = random.randint(0, USER_COUNT)
        result = [0 for _ in range(USER_COUNT + 1)]
        result[0] = 'song' + str(item + 1)
        if listened_count != 0:
            index_list = get_index(listened_count)
            for index in index_list:
                result[index] = random.randint(1, MAX_LICENSED_COUNT)
        result_list.append(result)
    print(result_list)
    append_csv(result_list)


if __name__ == '__main__':
    main()
