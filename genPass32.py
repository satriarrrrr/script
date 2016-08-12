import string
import random

random = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
f1=open('./donotopen', 'w+')
print >>f1, random