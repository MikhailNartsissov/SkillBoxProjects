source_file = open('numbers.txt', 'r', encoding='utf-8')
total = 0
for i_line in source_file:
    total += int(i_line)
source_file.close()
output_file = open('answer.txt', 'a', encoding='utf-8')
output_file.write(str(total) + '\n')
output_file.close()
