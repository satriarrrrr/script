import sys

n = 10
if (len(sys.argv) > 1):
	n = int(sys.argv[1])

if n == 0:
	print('0')
elif n == 1:
	print('0 1')
else:
	kemarinlusa = 0
	kemarin = 1
	out = '0 1'
	for i in range(2,n+1):
		hariini = kemarin+kemarinlusa
		kemarinlusa = kemarin
		kemarin = hariini
		out = out+' %s'%str(hariini)
	print(out)