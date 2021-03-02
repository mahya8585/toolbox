from pathlib import Path
import re

# 作業ファイル群
source_file = Path.cwd().joinpath('source.txt')
result_file = Path.cwd().joinpath('result.txt')

results = []
with open(source_file, 'r', encoding='utf8') as source_txt:
    for row in source_txt:
        remove_text = re.sub('^(管理者|事業者)は、', '', row)
        change_prefix = re.sub('^', 'ドキュメントが定めるところにより、', remove_text)
        change_suffix_1 = re.sub('する。$', 'しています。', change_prefix)
        change_suffix_2 = re.sub('ける。$', 'けています。', change_suffix_1)
        change_suffix_3 = re.sub('しない。$', 'していません。', change_suffix_2)
        change_suffix_4 = re.sub('う。$', 'っています。', change_suffix_3)
        change_suffix_last = re.sub('める。$', 'めています。', change_suffix_4)
        results.append(change_suffix_last)

with open(result_file, mode='w', encoding='utf8') as fr:
    fr.writelines(results)
