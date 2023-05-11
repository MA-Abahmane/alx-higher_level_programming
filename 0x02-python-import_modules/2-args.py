#!/usr/bin/python3

def main_calc():

    if (argc > 1):
        if (argc == 2):
            print("{0} argument:".format(1))
        else:
            print("{0} arguments:".format(argc - 1))

        i = 1
        while (i < argc):
            argument = argv[i]
            print("{0}: {1}".format(i, argument))

        i += 1
    else:
        print("{0} arguments.".format(0))


# if file not run as main; do not run.
if __name__ == '__main__':
    import sys

    argc = len(sys.argv)
    argv = sys.argv

    main_calc(argc, argv)
