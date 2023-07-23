import os, sys, argparse

class CustomHelpParser(argparse.ArgumentParser):

    def error(self, message):
        self.print_help()
        custom_help += "\n For instance, utilize the command below to search for domains that are younger than 30 days, have 10 or more IP addresses, and a TTL of 1000 seconds or less.\n"
        custom_help += ' "python3 Domain-Analyzer.py -i /domains.txt -d 30 -p 10 -t 1000" \n'
        print(custom_help)
        self.exit(1)

def get_args():

    msg = "Domain Analyzer tool, to get information about domains listed in a file domain per line. The purpose of this tool is to aid in the detection of potential suspicious domains that may be used for evasive activities, such as newly created domains, DGA domains, and fast-flux domains."
    
    # Initialize parser
    parser = CustomHelpParser(description = msg)

    # Adding optional argument
    parser.add_argument("-i",
            "--input",
            required = True,
            help = "input txt file path that contains domains (domain per line).\n")
    parser.add_argument(
            "-d",
            "--days",
            type = int,
            default = 30,
            help = "number of days to check for newly created domains (default: 30 days).\n")
    parser.add_argument(
            "-p",
            "--ips",
            type = int,
            default = 10,
            help = "number of IPs to check for potential fast-flux (default: 10 IPs).\n")
    parser.add_argument(
            "-t",
            "--ttl",
            type = int,
            default = 1000,
            help = "TTL in seconds to check for potential fast-flux (default: 1000 secs).\n")
    parser.add_argument(
            "-q",
            "--quiet",
            action = "store_true",
            help = "quit the verbose mode.\n")

    # Read arguments from command line
    args = parser.parse_args()

    ext = os.path.splitext(args.input)[-1].lower()
    if args.input and ext != ".txt":
        print("Invalid input file.\n" + "File type must be .txt")
        exit()

    if args.days < 0 or args.ips < 0 or args.ttl < 0:
        print("Invalid arguments.\n" + "Value must be greater than 0 (or equal 0 at least).")
        exit()


    return args