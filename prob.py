#-*- coding : utf-8 -*-
#/usr/bin/python

import sys
reload(sys)
sys.setdefaultencoding("utf-8")



class Prob:

    def __init__(self, filename):

        print "Begin Loading..."
        sys.stdout.flush()
        self.load(filename)

    def printto(self, args):
        self.output = self.output + str(args)

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
                    self.data[word][sense] = [float(item) for item in words[1:]]

    def search(self, word):
        if word not in self.data:
            return "\"\""
        data_items = self.data[word]
        self.output = ""
        with open("./templates/data.tsv", "w") as fout:
            self.printto("date")
            result = data_items.keys()
            for result_item in result:
                self.printto("\t")
                self.printto(result_item)
                l = len(data_items[result_item])
            for i in range(l):
                self.printto("\n")
                self.printto(50+i)
                for result_item in result:
                    self.printto("\t")
                    self.printto(data_items[result_item][i])
        return "\""+self.output +"\""

if __name__=="__main__":
    s = Prob("./../Data/rmrb.prob")
    while True:
        word = raw_input("Please input a word :  ")
        if word == "EXIT":
            break
        print s.search(word)

