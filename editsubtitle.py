# Or you can use this one
# sudo pip install pysrt
# srt -i shift 2s500ms movie.srt
# srt split 58m26s movie.srt
# srt -i rate 23.9 25 movie.srt
import sys

class Time(object):
	"""docstring for Time"""
	def __init__(self, arg):
		super(Time, self).__init__()
		temp = arg.split(":")
		self.hour = int(temp[0])
		self.minute = int(temp[1])
		temp = temp[2].split(",")
		self.second = int(temp[0])
		self.milisecond = int(temp[1])

	def add(self,time):
		tempMS = self.milisecond + time.milisecond
		self.milisecond = int(tempMS % 1000)
		tempS = self.second + time.second + int(tempMS / 1000)
		self.second = int(tempS % 60)
		tempM = self.minute + time.minute + int(tempS / 60)
		self.minute = int(tempM % 60)
		self.hour = self.hour + time.hour + int(tempM / 60)

	def sub(self,time):
		if self.milisecond >= time.milisecond:
			self.milisecond = self.milisecond - time.milisecond
		else:
			self.milisecond = self.milisecond + 1000 - time.milisecond
			self.second = self.second - 1
		if self.second >= time.second:
			self.second = self.second - time.second
		else:
			self.second = self.second + 60 - time.second
			self.minute = self.minute - 1
		if self.minute >= time.minute:
			self.minute = self.minute - time.minute
		else:
			self.minute = self.minute + 60 - time.minute
			self.hour = self.hour - 1
		self.hour = self.hour - time.hour

	def toString(self):
		strtime = {}
		strtime['h'] = '%s'%self.hour if self.hour/10 >= 1 else '0%s'%self.hour
		strtime['m'] = '%s'%self.minute if self.minute/10 >= 1 else '0%s'%self.minute
		strtime['s'] = '%s'%self.second if self.second/10 >= 1 else '0%s'%self.second
		strtime['ms'] = '%s'%self.milisecond if self.milisecond/100 >= 1 else '0%s'%self.milisecond if self.milisecond/100 >= 0.1 else '00%s'%self.milisecond
		return "%(h)s:%(m)s:%(s)s,%(ms)s"%strtime	

infile = open(sys.argv[1], 'r')
time = Time(sys.argv[3])

lines = infile.readlines()
for i in range(0,len(lines)):
	if lines[i][12:17] == ' --> ':
		timeStr = lines[i].split(' --> ')
		timeStart = Time(timeStr[0])
		timeEnd = Time(timeStr[1])
		if sys.argv[2] == 'add':
			timeStart.add(time)
			timeEnd.add(time)
		elif sys.argv[2] == 'sub':
			timeStart.sub(time)
			timeEnd.sub(time)
		else:
			sys.exit()
		times = {'start':timeStart.toString(),'end':timeEnd.toString()}
		lines[i] = "%(start)s --> %(end)s\n"%times
infile.close()
outfile = open(sys.argv[1], 'w')
outfile.writelines(lines)
outfile.close()