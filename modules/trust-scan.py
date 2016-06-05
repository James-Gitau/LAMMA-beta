# Project LAMMA
#
#                         __    _____ _____ _____ _____
#                        |  |  |  _  |     |     |  _  |
#                        |  |__|     | | | | | | |     |
#                        |_____|__|__|_|_|_|_|_|_|__|__|
#
#                                     (beta)
#
#
#    Plugin Name    :   trust_scan.py
#    Plugin ID      :   t-01
#    Plugin Purpose :   Invokes the scanning of trust stores and key stores
#
#
#    Plugin Author  :   @ahatti
#
#    Plugin Version :   0.0.1
#    Plugin Status  :   beta
#
################################################################################

# Include Section
import subprocess
import os
import os.path
import sys
import getopt
from sys import argv, stdout

# Plugin Informaiton

# Env Variable


# Plugin Mode

# Settings

# Report Findings



# --------------------------------------------------------------------------------
# Function      : usage
#
# Purpose       : Proivde a mini help on usage of this program
#
# Parameters    : None
#
# Returns       : None

def usage():
    print "\n\n    remote [-H] [-s] [-l] [-o] [-p] [-i] "
    print "\n    Purpose  : Scan a trust/key store at given Path with a specided script "
    print "\n               the results can be stored in a Repository for further comparision "
    print "\n"
    print "        -H [--help]      : prints this usage help"
    print "        -s [--script]    : scan the target with given script"
    print "        -l [--list]      : list all the plugins on a specified path"
    print "        -p [--path]      : path to stores which needs to be scanned"
    print " \n\n\n"

    sys.exit(2)


pass  # USAGE BLOCK






# --------------------------------------------------------------------------------
# Function      : list_all_trust_scripts()
#
# Purpose       : list all the scripts in the trust module
#
# Parameters    : path to be searched
#
# Returns       : None

def list_all_trust_scripts(path):

    prefix = get_path_prefix()

    indir =  prefix + path

    for root, dirs, filenames in sorted(os.walk(indir)):
        pos = indir.__len__()
        check_dir = root[pos:]
        if ( check_dir.find(".git") != -1):
            continue

        print "./" + root[pos:] + "/"

        for f in filenames:
            if f.endswith(".py"):
                if (f == "__init__.py"):
                    continue
                print "\t  ", f

    exit(0)


pass




# --------------------------------------------------------------------------------
# Function      : get_path_prefix
#
# Purpose       : based on from where the script is invoked, it returns the cwd
#
# Parameters    : None
#
# Returns       : relative cwd


def get_path_prefix() :
    indir = os.getcwd()

    if (indir.endswith("LAMMA")):
        prefix = "modules/trust-module/"

    if (indir.endswith("modules")):
        prefix = "trust-module/"

    indir = indir + "/" + prefix

    return prefix
pass




# -------------------------------------------------------------------------------
# Function  : main
#
# Purpose   : The main funciton of the script. Reads the configuration file for
#
# Params    : 1. argv     (list)    - list of command line arguments
#
# Returns   : None

def main(argv):
    # **** Lets process the arguments *********




    # Initialize the variables


    script_set = ""
    #report_path = "/home/evader/Desktop/PROJECTS/LAMMA/BETA/reports/"
    out_file = ""
    in_file = ""
    path = ""
    skip_scan = False
    cmd_string = "python "
    sink = stdout
    other_opt = ""

    # ---- Show the usage for too few arguments

    print "We are in Trust module"

    if len(argv) < 1:
        usage()
        sys.exit(2)
    pass  # if block

    # --- try block

    try:
        opts, args = getopt.getopt(argv, "H:s:l:p:i:r:",
                                   ["help=", "script=", "list", "path", "in", "repo"])


    except getopt.GetoptError:
        usage()
        sys.exit(2)
    pass  # TRY BLOCK

    # ---- Process the arguments passed to the script

    for opt, arg in opts:

        if opt in ("-H", "--help"):
            usage()

        elif opt in ("-s", "--script"):
            script_set = arg

        elif opt in ("-l", "--list"):
            list_scripts = True
            list_all_trust_scripts(arg)

        elif opt in ("-p", "--path"):
            path = arg

        #-- Option specified in the child scripts
        elif opt in ("-r", "--repo"):
            other_opt = other_opt + " " + opt + " " + arg + " "

        elif opt in ("-i", "--in"):
            other_opt = other_opt + " " + opt + " " + arg + " "


        pass  # IF BLOCK
    pass  # FOR BLOCK

    # ---- collect the values and check


    # --- Check the scripts to be executed : flag [-s]

    if (script_set == ""):
        print ("\n\n>> No script[s] specified")
        print ("\n\t pls specify choice of your scripts to be executed")
        print ("\n\t\t -s  [script_name]")
        skip_scan = True
    else :
        cmd_string = cmd_string + " " + os.getcwd()+ "/" +get_path_prefix() + script_set

    pass  # if Block



    # -- Check for the Host+Port or Infile

    if (path == ""):
        print "\n\n>> Specify the path of stroe to be scanned"
        skip_scan = True
    else :
        cmd_string = cmd_string + " -p" + " " + path
    pass  # -- If block

    cmd_string = cmd_string + " " + other_opt

    # -- We have enouh configuration parameters to continue

    # -- Show the configuration before starting the scan ----

    print ("\n\n[+] Starting %s plugin\n\n " %script_set )

    print "\n\n\t Now Executing:  ", (cmd_string), "\n"


    subprocess.call(cmd_string, shell="false")

    print "[+] Scaning complete...\n\n"


pass  # main

# -------------------------------------------------------------------------------
#
# Kick off the script

if __name__ == "__main__":
    main(sys.argv[1:])

pass  # IF BLOCK
