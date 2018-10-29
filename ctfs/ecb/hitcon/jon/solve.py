file = "temp_file.txt"
f = open(file,'r')
all_data = []
for line in f.readlines():
    d = line.split("\x00")
    dic = {'title': d[0],'ref':d[1][3:],'url':d[2]}
    if(dic['title']=='down'):
        continue
    all_data.append(dic)

#IT'S probably the title
for data in all_data:
    split_size = 8
    title_len = len(data['title'])
    ref_2 = len(data['ref'])/2
    num_split = len(data['ref'])/(16)
    url_len = len(data['url'])
    print('title: '+str(title_len) + '  ref/2: ' + str(ref_2)+'  num_splits: '+str(num_split)+ '  num_theosplits: ' + str(title_len/split_size)+'  IDK: '+str(url_len/split_size))
    assert title_len < ref_2