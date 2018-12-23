
#practice using python on simple bioinformatics from:
#http://hplgit.github.io/bioinf-py/doc/pub/html/main_bioinf.html#basic-bioinformatics-examples-in-python

#different ways to count a certain letter in a DNA string
#========================================================

#list iteration
def count_v1(dna, base):
    dna = list(dna)
    i = 0
    for j in dna:
        if j == base:
            i+=1
    #print('%s appears %d times in %s' % (base, i, dna))
    return i


#string iteration
def count_v2(dna, base):
    i = 0
    for j in dna:
        if j  == base:
            i+=1
    #print('%s appears %d times in %s' % (base, i, dna))
    return i

#index iteration
def count_v3(dna, base):
    i,j=0,0
    for j in range(len(dna)):
        if dna[j]==base:
            i+=1
    #print('%s appears %d times in %s' % (base, i, dna))
    return i

#summing a boolean list
def count_v4(dna, base):
    l = []
    for j in dna:
        l.append(1 if  j == base else 0)
    #print('%s appears %d times in %s' % (base, sum(l), dna))
    return sum(l)

#using a sum iterator
def count_v10(dna, base):
    j = sum(i == base for i in dna)
    #print('%s appears %d times in %s' % (base, j, dna))
    return j

#using built in function
def count_v11(base, dna):
    j =  dna.count(base)
    #print('%s appears %d times in %s' % (base, j, dna))
    return j

#creating a better test string
import random
def make_string():
    alphabet = list('ATGC')
    N = 1000000
    dna = [random.choice(alphabet) for i in range(N)]
    dna = ''.join(dna)
    return dna

#test time difference
import time
dna = make_string()
functions = [count_v1, count_v2, count_v3, count_v4,count_v10, count_v11]
timings = []
for function in functions:
    t0 = time.clock()
    function(dna, 'A')
    t1 = time.clock()
    total= t1-t0
    timings.append(total)

for i in timings:
    print(i)

#observed outputs
#0.19746844213647144
#0.16197521319677557
#0.255670933945011
#0.5176204377166383
#0.3684054868654012
#3.063250655954697e-05

#clearly the built in function is the fastest