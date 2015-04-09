import numpy as np
import sys

def convert2np(raw_string):
    return np.array([float(item) for item in raw_string.split()])

class MSWord2Vec:
    def __init__(self, vector_fn, cluster_fn):
        print "load vectors..."
        sys.stdout.flush()
        self.load_vectors(vector_fn)
        print "load cluster..."
        sys.stdout.flush()
        self.load_vectors(cluster_fn)
        print "ok"
        sys.stdout.flush()


    def load_vectors(self, filename):
        self.sense_vectors = {}
        self.global_vectors = {}
        with open(filename) as fin:
            vocab_size, layer_size = fin.readline().strip().split()
            vocab_size = int(vocab_size)
            layer_size = int(layer_size)
            for _ in range(vocab_size):
                words = fin.readline().strip().split()
                word = words[0]
                sense_number = int(words[1])
                self.global_vectors[word] = np.array([float(item) for item in words[2:]])
                self.sense_vectors[word] = []
                for _ in range(sense_number):
                    self.sense_vectors[word].append(convert2np(fin.readline().strip()))


    def load_cluster(self, filename):
        self.cluster = {}
        with open(filename) as fin:
            vocab_size, layer_size = fin.readline().strip().split()
            vocab_size = int(vocab_size)
            layer_size = int(layer_size)
            for _ in range(vocab_size):
                word, sense_number = fin.readline().strip().split()
                sense_number = int(sense_number)
                self.cluster[word] = []
                for _ in range(sense_number):
                    self.cluster[word].append(convert2np(fin.readline().strip()))



