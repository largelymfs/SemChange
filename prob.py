#-*- coding : utf-8 -*-
#/usr/bin/python

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import copy


class Prob:

    def __init__(self, filename):

        print "Begin Loading..."
        sys.stdout.flush()
        self.load(filename)

    def printto(self, args):
        self.output = self.output + str(args)


    def smooth_data(self, l,smooth=3):
        result = []
        for id in xrange(len(l)):
            start = max(0, id - smooth)
            finish = min(len(l)-1, id+smooth)
            res = 0.0
            for tmp in xrange(start, finish+1):
                res +=l[tmp]
            res = res * (1./ float(finish - start + 1))
            result.append(res)
        return result

    def smooth(self, smooth = 1):
        for word in self.data.keys():
            for sense in self.data[word]:
                self.data[word][sense] = self.smooth_data(self.data[word][sense])

    def load(self, filename):
        self.data = {}
        with open(filename) as fin:
            while True:
                line = fin.readline()
                if not line:
                    break

                words = line.strip().split()
                word = words[0]
                self.data[word] = {}
                sense_number = int(words[1])
                for _ in range(sense_number):
                    words = fin.readline().strip().split()
                    sense = int(words[0])
                    self.data[word][sense] = {}
                    self.data[word][sense] = [float(item) * 100 for item in words[1:]]

    def search(self, word, smooth = 3):
        if word not in self.data:
            return "\"\""
        data_items = copy.deepcopy(self.data[word])
        print data_items
        for key in data_items.keys():
            data_items[key] = self.smooth_data(data_items[key], smooth)
        print data_items

        self.output = ""
        with open("./templates/data.tsv", "w") as fout:
            self.printto("date")
            result = data_items.keys()
            for result_item in result:
                self.printto("\\t")
                self.printto(result_item)
                l = len(data_items[result_item])
            for i in range(l):
                self.printto("\\n")
                self.printto(1950+i)
                for result_item in result:
                    self.printto("\\t")
                    self.printto(data_items[result_item][i])
        return "\""+self.output +"\""

if __name__=="__main__":
    s = Prob("./../NewData/rmrb.prob.all")
    while True:
        word = raw_input("Please input a word :  ")
        if word == "EXIT":
            break
        print s.search(word)

