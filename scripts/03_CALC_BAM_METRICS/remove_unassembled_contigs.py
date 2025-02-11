#!//usr/bin/python
import sys

valid_chroms = list(map(str, range(1,23))) + ['X', 'Y', 'MT']
valid_chroms = set(valid_chroms)
sys.stdout.write(sys.stdin.readline())
for line in sys.stdin:
	toks = line.strip().split('\t')
	chrom = toks[0]
	if chrom.startswith("chr"):
		chrom = chrom[3:]
	if chrom == "chrom": 
		sys.stdout.write(line)
		continue
	if chrom not in valid_chroms:
		#as soon as we hit an unassembled contig, quit
		break 
	sys.stdout.write(line)
