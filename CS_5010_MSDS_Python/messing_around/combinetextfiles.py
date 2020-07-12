import itertools 
import glob

folder = r"D:\Git\UVA_MSDS_Content\CS 5010 MSDS Python\\"
filename_pattern = r"pyScript*.py"
filelist = glob.glob(folder + filename_pattern)

with open(folder + 'pyScript_mod1_combined.py', 'w') as outfile:
    for fname in filelist:
        outfile.write('\n\n\n##'+('-'*10)+fname+'\n')
        with open(fname) as infile:
            outfile.write(infile.read())

    # for line in itertools.chain.from_iterable(itertools.imap(open, filnames)):
    #     outfile.write(line)
