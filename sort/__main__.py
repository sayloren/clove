# this file is only called when the package is called from the command
# line
import argparse
from .run import run_graphing

def main():
	quick_lists,bubble_lists = run_graphing(100,10,1000)

if __name__ == "__main__":
	main()
