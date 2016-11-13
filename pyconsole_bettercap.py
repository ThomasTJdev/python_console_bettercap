#!/usr/bin/python
#
# Just a simple python3 front for Bettercap
# POC for implementation in KatanaFramework
#
# MIT - (c) 2016 ThomasTJ (TTJ)
#


# LIBRARIES
import subprocess           # For invoking to xterm
import shlex                # Parsing command for invoking to xterm
import os                   # Running bettercap
import sys                  # Exiting
import shutil               # Check if bettercap is installed
import signal               # Capture Ctrl+c
import helpers as help      # Helpers for gateway and interface
from time import sleep      # Just counting down before launch
# END LIBRARIES

# VARIABLES
global sop                            # Main class for all options
global bettercappath
battercappath = "/usr/bin/bettercap"  # Change accordingly
# END VARIABLES


# COLORFUL
class bc:
    BRED        = '\033[41m'  # BACKGROUND RED
    BGREEN      = '\033[42m'  # BACKGROUND GREEN
    BYELLOW     = '\033[43m'  # BACKGROUND YELLOW
    HEADER      = '\033[95m'  # LIGHT MAGENTA
    OKBLUE      = '\033[94m'  # LIGHT BLUE
    OKGREEN     = '\033[92m'  # LIGHT GREEN
    WARNING     = '\033[93m'  # LIGHT YELLOW
    FAIL        = '\033[91m'  # LIGHT RED
    ENDC        = '\033[0m'   # WHITE ENDC
    BOLD        = '\033[1m'   # BOLD
    UNDERLINE   = '\033[4m'   # UNDERLINE
    ITALIC      = '\x1B[3m'   # ITALIC
# END COLORFUL


# OPTIONS
class options():
    Author              = "Thomas TJ (TTJ)"
    Version             = "1.0"
    Description         = "Python console for Bettercap"
    CodeName            = "pyconsole_bettercap"
    DateCreation        = "13/11/2016"
    LastModification    = "13/11/2016"
    License             = "MIT"


    def __init__(self, interface, gateway, sniffer, proxy, target, invoke):
        self.interface = interface
        self.gateway = gateway
        self.sniffer = sniffer
        self.proxy = proxy
        self.target = target
        self.invoke = invoke
        self.show_all()


    def dd(self):
        print(options.interface)


    def show_opt(self):
        print(
            ""
            + "\n\t" + bc.OKBLUE + ("%-*s %-*s %-*s %s" % (12, "OPTION", 6, "RQ", 14, "VALUE", "DESCRIPTION")) + bc.ENDC
            + "\n\t" + ("%-*s %-*s %-*s %s" % (12, "------", 6, "--", 14, "-----", "-----------"))
            + "\n\t" + ("%-*s %-*s %-*s %s" % (12, "interface:", 6, "y", 14, self.interface, "Interfaces " + help.get_interfaces("all")))
            + "\n\t" + ("%-*s %-*s %-*s %s" % (12, "gateway:", 6, "y", 14, self.gateway, "Gateway, e.g. 192.168.1.1"))
            + "\n\t" + ("%-*s %-*s %-*s %s" % (12, "sniffer:", 6, "n", 14, self.sniffer, "Activate sniffer - why not? (y/n)"))
            + "\n\t" + ("%-*s %-*s %-*s %s" % (12, "proxy:", 6, "n", 14, self.proxy, "Downgrade HTTPS to HTTP for sniffing (y/n)"))
            + "\n\t" + ("%-*s %-*s %-*s %s" % (12, "target:", 6, "n", 14, self.target, "Target IPs. Separate with ',' or subnet xx\\24"))
            + "\n\t" + ("%-*s %-*s %-*s %s" % (12, "invoke:", 6, "n", 14, self.invoke, "Open sniffing in new xterm (y/n)"))

            + "\n"
            )


    def show_all(self):
        print(
            ""
            + "\n" + "\tArthur:\t\t" + self.Author
            + "\n" + "\tVersion:\t" + self.Version
            + "\n" + "\tDescription:\t" + self.Description
            + "\n" + "\tCodename:\t" + self.CodeName
            + "\n" + "\tLicense:\t" + self.License
            + "\n" + "\tDatecreation:\t" + self.DateCreation
            + "\n" + "\tLastmodified:\t" + self.LastModification
            + "\n\n"
            + "\n\t" + bc.OKBLUE + "COMMANDS:" + bc.ENDC
            + "\n\t" + "---------"
            + "\n\t" + ("%-*s -> %s" % (6, "run", "Run the script"))
            + "\n\t" + ("%-*s -> %s" % (6, "sop", "Show options"))
            + "\n\t" + ("%-*s -> %s" % (6, "sfop", "Show all info"))
            + "\n\t" + ("%-*s -> %s" % (6, "exit", "Exit"))
            + "\n"
            )
        self.show_opt()
# END OPTIONS


# RUN BETTERCAP
def run_bc():
    i = getattr(sop, 'interface')
    if i:
        opt_com = '--interface ' + i + ' '

    g = getattr(sop, 'gateway')
    if g:
        opt_com = opt_com + '--gateway ' + g + ' '

    s = getattr(sop, 'sniffer')
    if s.lower() == 'y':
        opt_com += '--sniffer' + ' '

    p = getattr(sop, 'proxy')
    if p.lower() == 'y':
        opt_com += '--proxy' + ' '

    t = getattr(sop, 'target')
    if t:
        opt_com += '--target ' + t + ' '

    command = (battercappath + ' ' + opt_com)

    print(
        "\n"
        + "\t" + "Loading     : Bettercap"
        + "\n\t" + "Command     : " + command
        + "\n\t" + "Stop        : Ctrl + C (and wait)"
        + "\n\t" + "Starting in : 3 seconds"
        + "\n\t"
        )
    n = 3
    while n > 0:
        print("\t" + str(n) + "..  ")
        n = n-1
        sleep(1)
    print("\n\n")

    if getattr(sop, 'invoke') == "y":
        scommand = "xterm -T Invoke[Bettercap] -bg black -e " + command
        args = shlex.split(scommand)
        subprocess.Popen(args)
    else:
        os.system(command)
    print("\n\n")
# END BETTERCAP


# CONSOLE
def console():
    value = input("  " + bc.FAIL + "mdw" + bc.ENDC + "@" + bc.FAIL + "bettercap:" + bc.ENDC + " ")
    userinput = value.split()
    if 'sop' in userinput[:1]:
        sop.show_opt()
    elif 'sfop' in userinput[:1]:
        sop.show_all()
    elif 'exit' in userinput[:1]:
        sys.exit()
    elif 'run' in userinput[:1]:
        run_bc()
    elif 'set' in userinput[:1]:
        uservalue = str(userinput[2:3]).strip('[]\'')
        if not hasattr(sop, str(userinput[1:2]).strip('[]\'')):
            print(bc.WARNING + "\n    Error, no options for: " + str(userinput[1:2]).strip('[]\'') + "\n" + bc.ENDC)

        elif 'interface' in userinput[1:2]:
            setattr(sop, 'interface', uservalue)
            print("\n    interface\t> " + uservalue + "\n")

        elif 'gateway' in userinput[1:2]:
            setattr(sop, 'gateway', uservalue)
            print("\n    gateway\t> " + uservalue + "\n")

        elif 'target' in userinput[1:2]:
            setattr(sop, 'taget', uservalue)
            print("\n    taget\t> " + uservalue + "\n")

        elif 'invoke' in userinput[1:2]:
            if uservalue.lower() not in ('y', 'n'):
                print(bc.WARNING + "\n    Error, only 'n' and 'y' allowed for option: " + str(userinput[1:2]).strip('[]\'') + "\n" + bc.ENDC)
            else:
                setattr(sop, 'invoke', uservalue)
                print("\n    invoke\t> " + uservalue + "\n")

        elif 'sniffer' in userinput[1:2]:
            if uservalue.lower() not in ('y', 'n'):
                print(bc.WARNING + "\n    Error, only 'n' and 'y' allowed for option: " + str(userinput[1:2]).strip('[]\'') + "\n" + bc.ENDC)
            else:
                setattr(sop, 'sniffer', uservalue)
                print("\n    sniffer\t> " + uservalue + "\n")

        elif 'proxy' in userinput[1:2]:
            if uservalue.lower() not in ('y', 'n'):
                print(bc.WARNING + "\n    Error, only 'n' and 'y' allowed for option: " + str(userinput[1:2]).strip('[]\'') + "\n" + bc.ENDC)
            else:
                setattr(sop, 'proxy', uservalue)
                print("\n    proxy\t> " + uservalue + "\n")

    else:
        print(bc.WARNING + "\n    error\t> " + str(userinput[:1]) + "\n" + bc.ENDC)
    # Always return to console:
    console()
# END console


# Capture Ctrl+c and exit
def sigint_handler(signum, frame):
    print("  Exiting")
    sys.exit()
signal.signal(signal.SIGINT, sigint_handler)    # Capture Ctrl+c and exit
# End capture

# STARTER
def __init__():
    if os.getuid() != 0:
        print("r00tness is needed due to packet sniffing!")
        print("Run the script again as root/sudo")
        sys.exit()
    if shutil.which('bettercap') is None:
        print("Bettercap as executable!")
        print("Manual edit this scripts Bettercap path or install Bettercap")
        print("Exiting")
        sys.exit()
    global sop
    sop = options(help.get_interfaces("single"), help.get_gateway(), "y", "y", "", "")
    console()

__init__()
