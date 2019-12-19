# FIND the BUG
# a test example by Thomas Willach 12/10/2019
# written and tested in Windows 10, Pycharm IDE, using python 2.4.1
# tested in Linux Ubuntu 14.4 LTS, IDLE using python 2.7.6


# REQUIREMENTS
# Environment settings
# Python (2.x), Ideally as a single module.
# Only modules from the standard python library.

# Dependencies must be documented at the appropriate location.
# Testing in a Linux environment, but should be platform independent.
# executable with different Python versions 2.4 to 2.7
# Enclosed 2 ASCII files bug.txt and landscape.txt.
# it should be possible to specify both files
# tested with another more complex landscape as well.

# The problem Find the bug
# You program shall search a text file for bugs and print the number
# of their occurrence.
# The contents of this file is a lot simpler than the file that we will
# be testing the completed program. Each occurrence of the character
# pattern as specified in bug.txt is counted,
# except for the whitespaces contained therein.

# Results
# Aside from solving the problem as described above we expect that your
# code is meaningfully documented, easy to maintain, expand, and reusable
# Your solution path shall demonstrate your skills and
# how you tackle complex problems.
# Using solely a Brute Force  or Fire and Forget solution of the problem
# will not be considered # enough.
# solve with well-balanced mix of technical skill, aesthetics and pragmatism
# Notice
# Please consider when implementing your solution,
# that during the course of the hiring process you
# will be expected to expand your program with
# additional functionalities.


import re, os

# findthebug functions
def get_list_of_filelines(filename):
    # load textfile linewise to a list object
    lines = open(filename).readlines()
    open(filename).close()
    return lines

def get_list_of_regexlines(list_of_lines):
    # convert controlcharacters ' [](){}|?+-^$' from
    # bug definition ascii file to a regular expression format
    list_of_regexlines = []
    i = 0
    for line in list_of_lines:
        reline = ''
        for sign in line:
            if sign in '[](){}|?+-^$':
                sign = '\\' + sign
            elif sign ==' ':
                # whitespace characters should not counted
                sign = '.'
            elif sign =='\n':
                # linespace characters should not counted
                sign = ''
            reline = reline + sign
        list_of_regexlines.append([])
        list_of_regexlines[i] = reline
        i+=1
    return list_of_regexlines


def get_list_size(list):
    # number and lenght of a list object
    file_dim=[]
    for i in range(0, len(list)):
        file_dim.append([i, len(list[i])])
    return file_dim


def get_linewise_matches(searchtext_list, content_lines):
    # load searchtext file (bug) linewise to a list object

    # searchtext_list example data from 'bug.txt':
    # ['\\|.\\|', '###O', '\\|.\\|']

    # content_lines example data from 'landscape.txt':
    # ['                                       \n',
    #  '    | |\n',
    #  '    ###O\n',
    #  '    | |           | |\n',
    #  '                  ###O\n',
    #  '                  | |              | |\n',
    #  '                                   ###O\n',
    #  '                                   | |']
    content_dim = get_list_size(content_lines)
    bug_dim = get_list_size(searchtext_list)
    partmatches = []
    for contentline_no in range(0, len(content_dim)):
        for bug_line_no in range(0, len(bug_dim)):
            bugline = searchtext_list[bug_line_no]
            pattern = re.compile(bugline)
            matches = pattern.finditer(content_lines[contentline_no])
            for match in matches:
                partmatches.append([bug_line_no, contentline_no, \
                    match.start(), match.end(), match.group(), bugline])
    # matches of each bugline
    return partmatches


def get_occurance_report(searchtext_list, partmatches):
    # find complete bug occurance from linewise partmatches
    # for each element in partmatches check out near coordinates
    # if searchtext_list matches complete
    # with near content_text coordinates equal to line in searchtext_list

    # partmatches example date from 'bug.txt' and 'landscape.txt':
    #          [bug_line_no, contentline_no, match.start(),
    #          match.end(), match.group(), bugline]
    #  0 o1    [0, 1, 4, 7, '| |', '\\|.\\|']
    #  1       [2, 1, 4, 7, '| |', '\\|.\\|']
    #  2 o1    [1, 2, 4, 8, '###O', '###O']
    #  3       [0, 3, 4, 7, '| |', '\\|.\\|']
    #  4 o2    [0, 3, 18, 21, '| |', '\\|.\\|']
    #  5 o1    [2, 3, 4, 7, '| |', '\\|.\\|']
    #  6       [2, 3, 18, 21, '| |', '\\|.\\|']
    #  7 o2    [1, 4, 18, 22, '###O', '###O']
    #  8       [0, 5, 18, 21, '| |', '\\|.\\|']
    #  9 o3    [0, 5, 35, 38, '| |', '\\|.\\|']
    # 10 o2    [2, 5, 18, 21, '| |', '\\|.\\|']
    # 11       [2, 5, 35, 38, '| |', '\\|.\\|']
    # 12 o3    [1, 6, 35, 39, '###O', '###O']
    # 13       [0, 7, 35, 38, '| |', '\\|.\\|']
    # 14 o3    [2, 7, 35, 38, '| |', '\\|.\\|'

    occurance = 0
    occurance_report = [0]
    finding_report = []
    for element in range(0, len(partmatches) - 1):
        if partmatches[element][0] == 0:
            finding = 1
            for matchline in range(element + 1, len(partmatches)):
                if partmatches[matchline][0] == \
                        partmatches[element][0] + finding and \
                partmatches[matchline][1] == \
                            partmatches[element][1] + finding and \
                partmatches[matchline][2] == \
                                partmatches[element][2]:
                            if finding == 1:
                                finding_report.append(\
                                    "finding = " + str(finding)\
                                    + ": "+ str(partmatches[element]))
                            finding += 1
                            finding_report.append(\
                                    "finding = " + str(finding) + ": "\
                                    + str(partmatches[matchline]))
                            if finding == len(searchtext_list):
                                occurance += 1
                                occurance_report.append(\
                                    ["line_no " + str(partmatches[element][1]+1) + \
                                    " at position " + str(partmatches[element][2]+1)])
                                finding_report.append("occurance= " + str(occurance))
    occurance_report[0] = occurance
    # print(str(occurance_report))
    # print(str(finding_report))
    return occurance_report

    # example: occurance_report =
    # [3, ['line_no 2 at position 5'],
    # ['line_no 4 at position 19'],
    # ['line_no 6 at position 36']]

    # example: finding_report =
    # ["finding = 1: [0, 1, 4, 7, '| |', '\\\\|.\\\\|']",
    # "finding = 2: [1, 2, 4, 8, '###O', '###O']",
    # "finding = 3: [2, 3, 4, 7, '| |', '\\\\|.\\\\|']",
    # 'occurance= 1',
    # "finding = 1: [0, 3, 18, 21, '| |', '\\\\|.\\\\|']",
    # "finding = 2: [1, 4, 18, 22, '###O', '###O']",
    # "finding = 3: [2, 5, 18, 21, '| |', '\\\\|.\\\\|']",
    # 'occurance= 2',
    # "finding = 1: [0, 5, 35, 38, '| |', '\\\\|.\\\\|']",
    # "finding = 2: [1, 6, 35, 39, '###O', '###O']",
    # "finding = 3: [2, 7, 35, 38, '| |', '\\\\|.\\\\|']",
    # 'occurance= 3']


def get_occurance_number(searchtext_list, partmatches):
    return get_occurance_report(searchtext_list, partmatches)[0]


def get_occurance_positions(searchtext_list, partmatches):
    return get_occurance_report(searchtext_list, partmatches)[1:]


if __name__ == '__main__':
    # FIND the BUG
    # a test example by Thomas Willach 12/10/2019
    print("FIND the BUG\na test example by Thomas Willach 12/10/2019\
    \n\nYour work directory is: " + os.getcwd()) + "\n"

    # prompt for work directory (or enter default)
    newdir = raw_input("Please enter new work directory (or enter default):")\
    or os.getcwd()

    # set work directory
    os.chdir(newdir)

    # prompt for filenames (or enter default)
    bug_filename = raw_input(\
    "\nPlease enter filename\n\tbug textfile (or enter default): ")\
    or 'bug.txt'

    content_text = raw_input("\n\tcontent textfile (or enter default): ")\
    or 'landscape.txt'
    print("\nfilenames are \n\t" + bug_filename + "\n\t" + content_text +"\n" )

    # load searchtext file ('bug.txt') to a list object
    # and close all open file
    bug_lines = get_list_of_filelines(bug_filename)
    # bug_lines example data from 'bug.txt':
    # ['| |\n', '###O\n', '| |\n']

    # create searchable regular expression from bug_lines
    # for each occurence of the character pattern,
    # except whitespace between pattern characters
    searchtext_list = get_list_of_regexlines(bug_lines)
    # searchtext_list exampe date aus  'bug.txt':
    # ['\\|.\\|', '###O', '\\|.\\|']

    # content_text as list object
    content_lines = get_list_of_filelines(content_text)

    # search for matches of lines from searchtext_list in content_lines
    # partmatches as a list object
    partmatches = get_linewise_matches(searchtext_list, content_lines)

    # find complete bug occurance from linewise partmatches
    # for each element in partmatches check near content coordinates
    occurance_number = get_occurance_number(searchtext_list, partmatches)
    print("findthebug.py has found \n\t" + str(occurance_number)+ " occurances of '" \
                                           + str(bug_filename) + "' in '" + str(content_text) + "'")
    # result for example data:
    # findthebug.py has found 3 occurances of 'bug.txt' in 'landscape.txt'

    # start positions of 'bug.txt' in 'landscape.txt'
    occurance_positions = get_occurance_positions(searchtext_list, partmatches)
    print("\nstart positions in")
    for pos in occurance_positions:
        print("\t" + str(pos[0]))

    # start positions in
    # line 3 at position 4
    # line 5 at position 18
    # line 7 at position 35





