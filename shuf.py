#!/usr/bin/python

import random, sys
import string
import argparse

def main():

    #shuffles input by outputting a random permutation of its input lines."""

    parser = argparse.ArgumentParser(description="Python implementation of GNU's shuf")

    parser.add_argument("file", nargs="?", type=argparse.FileType('r'), help="Input file to shuffle")
    parser.add_argument("-e", "--echo", nargs='*', help="treat each ARG as an input line")
    parser.add_argument("-i", "--input-range", nargs="?", help="treat each number LO through HI as an input line")
    parser.add_argument("-n count", "--head-count", help="output at most COUNT lines")
    parser.add_argument("-r", "--repeat", action='store_true', help="output lines can be repeated")

    args=parser.parse_args()
    
    if args.file:
        file_contents = []
        for line in args.file:
            if line[-1] == "\n":
                file_contents.append(line.rstrip("\n"))
            else:
                file_contents.append(line)
            random.shuffle(file_contents)
        file_lines = len(file_contents)
        if args.head_count:
            count = int(args.head_count)
            if args.repeat:
                for x in range(count):
                    print(file_contents[random.randrange(0, file_lines)])
            else:
                reps = file_lines if file_lines < count else count 
                for item in file_contents[:reps]:
                    print(item, end="\n")
        else:
            if args.repeat:
                while 0 == 0:
                    print(file_contents[random.randrange(0, file_lines)])
            for item in file_contents:
                print(item, end="\n")
    
    if args.echo:
        random.shuffle(args.echo)
        echo_lines = len(args.echo)
        if args.head_count:
            count = int(args.head_count)
            reps = echo_lines if echo_lines < count else count
            if args.repeat:
                for x in range(count):
                    print(file_contents[random.randrange(0, echo_lines)])
            else:
                for item in args.echo[:reps]:
                    print(item)
        else:
            if args.repeat:
                while 0 == 0:
                    print(args.echo[random.randrange(0, echo_lines)])
            else:
                for item in args.echo:
                    print(item)

    if args.input_range:
        lo, hi = map(int, args.input_range.split('-'))
        if lo > hi:
            print(f"shuf: invalid input range: ‘{lo}-{hi}'")
        else:
            lo_hi_list = list(range(lo, hi+1))
            random.shuffle(lo_hi_list)
            if args.head_count:
                count = int(args.head_count)
                reps = min(count, len(lo_hi_list))
                for x in range(reps):
                    print(lo_hi_list[x])
            else:
                for item in lo_hi_list:
                    print(item)

# FIX TO DISPlAY ERROR MESSAGES

        
if __name__ == "__main__":
    main()
