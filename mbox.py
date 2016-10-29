fout = open('mbox.txt', 'r')
count = 0
for line in fout:
    print(line)
    count += 1
print(count)
fout.close()
