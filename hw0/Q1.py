import sys

def parse(file):
    with open(file,"r") as fr:
        txt=fr.read()

    txt=txt.strip('\n')
    txt=txt.strip('\t')
    wordlist=txt.split(' ')

    d={}
    n=0
    l=[]

    for word in wordlist:
        if word in d:
            l[d[word]][2]+=1
        else:
            d[word]=n
            l.append([word,n,1])
            n+=1

   # for data in l:
   #     print("%s %d %d"%(data[0],data[1],data[2]))
    with open('./Q1.txt','w') as fw:
        for data in l:
            fw.write("%s %d %d\n"%(data[0],data[1],data[2]))


if __name__ == "__main__":
    parse(sys.argv[1])
