import get_args
import sys, os

args = get_args.parse()

if args.type == "1":
    print(sys.version_info)
elif args.type == "2":
    os.mkdir(args.name)
else:

    print(os.listdir(os.pardir))