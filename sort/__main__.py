# this file is only called when the package is called from the command
# line with python -m sort <other flags>
import argparse
from .run import run_graphing

def get_args():
	parser = argparse.ArgumentParser(description="Description")
	parser.add_argument("-t","--total",type=int,default="100",help='total number of lists to have')
	parser.add_argument("-a","--max",type=int,default="10",help='max value to have in a list')
	parser.add_argument("-e","--element",type=int,default="1000",help='the range of numbers from which to draw the random number of elements per list')
	return parser.parse_args()

def main():
	args = get_args()
	quick_lists,bubble_lists,bubble_latex,quick_latex = run_graphing(args.total,args.max,args.element)
	return bubble_latex,quick_latex

if __name__ == "__main__":
	main()
