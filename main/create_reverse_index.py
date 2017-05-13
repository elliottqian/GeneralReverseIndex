# -*- coding: utf-8 -*-

"""
要考虑缺失值
"""

import codecs


def main(file_path="/home/qianwei/Code/CMB/GeneralReverseIndex/reverse_index/test_info",
         split_symbol=" ",
         index_path="/home/qianwei/Code/CMB/GeneralReverseIndex/reverse_index"):
    info_f = codecs.open(file_path, encoding="utf-8")
    for line in info_f:
        line = line.strip()  # 去掉换行符
        lines = line.split(split_symbol)  # 按照符号分割
        rename_lines = rename_properties(lines)  # 属性重命名
        process_one_record(rename_lines, index_path)  # 建立倒排索引文件

    info_f.close()


def process_one_record(record, index_path):
    """
    为每一行文件做倒排索引文件, 自增的
    :param record: 一条记录
    :param index_path: 倒排索引的目录
    :return: 
    """
    user_id = record[0]
    for property_ in record[1:]:
        index_file = codecs.open(index_path + "/" + property_, mode="wb", encoding="utf-8")  # ab是继续写, wb是重新写
        index_file.write(user_id + "\n")
        index_file.close()


def rename_properties(lines):
    """
    属性重命名,防止属性重名
    :type lines: list
    :param lines: 
    :return:
    """
    new_lines = []
    new_lines.append(lines[0])
    i = 1
    for property_ in lines[1:]:
        new_lines.append(property_ + "_" + str(i))
        i += 1
    return new_lines


if __name__ == "__main__":
    main()
    pass
