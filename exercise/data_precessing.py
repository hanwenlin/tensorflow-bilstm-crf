import os,sys
BASE_DIR = os.path.dirname(os.path.abspath('__file__'))
sys.path.append(BASE_DIR)

train_path = os.path.join(os.path.join(os.path.join(BASE_DIR, 'data'),'msra'), 'train.txt')
wordtag_path = os.path.join(os.path.join(os.path.join(BASE_DIR, 'data'),'msra'), 'wordtag.txt')

def wordtag(trainfile, wordtagfile):
    tags = set()
    with open(wordtagfile, 'w', encoding='utf-8') as f1:
        with open(trainfile, 'r', encoding='utf-8') as f:
            for line in f:
                items = line.strip().split()
                for item in items:
                    ners, tag = item.split('/')
                    tags.add(tag)
                    if tag=='o':
                        for i in ners:
                            # if i:
                            f1.write(i + '/o'+' ')
                    else:
                        if len(ners)>=2:
                            nerB, nerM, nerE = ners[0], ners[1:-1], ners[-1]
                            f1.write(nerB+'/B_'+tag+' ')
                            for i in nerM:
                                if i:
                                    f1.write(i+'/M_'+tag+' ')
                            f1.write(nerE + '/E_' + tag + ' ')
                        else:
                            f1.write(ners + '/B_' + tag + ' ')
                f1.write('\n')

    return tags

if not os.path.exists(wordtag_path):
    wordtag(train_path, wordtag_path)
else:
    input_data = open(wordtag_path, 'r', encoding='utf-8')



datas = list()
labels = list()
linedata=list()
linelabel=list()
tag2id = {'' :0,
'B_ns' :1,
'B_nr' :2,
'B_nt' :3,
'M_nt' :4,
'M_nr' :5,
'M_ns' :6,
'E_nt' :7,
'E_nr' :8,
'E_ns' :9,
'o': 10}

id2tag = {0:'' ,
1:'B_ns' ,
2:'B_nr' ,
3:'B_nt' ,
4:'M_nt' ,
5:'M_nr' ,
6:'M_ns' ,
7:'E_nt' ,
8:'E_nr' ,
9:'E_ns' ,
10: 'o'}



