import os
from datetime import datetime
import pprint as pp
import shutil

thisdir = os.path.dirname(os.path.abspath(__file__)) + "\\"

def make_list_of_ext_paths(search_here, ext):
    outlist = []
    for root, _, files in os.walk(search_here, topdown=False):
        for name in files:
            filepath = os.path.join(root, name)
            if filepath.endswith(ext):
                outlist.append(filepath)
    return outlist

def copy_filepaths_here(copy_here, filepath_list):
    filepath_list = [[x, "_".join(x.split("\\")[-2:])] for x in filepath_list]
    #sample1 = filepath_list[0]
    #pp.pprint(sample1)
    if not os.path.exists(copy_here):
        os.makedirs(copy_here)
    for filepath in filepath_list:
        shutil.copyfile(filepath[0], os.path.join(copy_here, filepath[1]))

if __name__ == "__main__":
    start_time = datetime.now()
    pdflist = make_list_of_ext_paths(r"D:\Git\UVA_MSDS_Content\STAT_6021_Linear_Models", ".pdf")
    copy_filepaths_here(r"D:\Git\UVA_MSDS_Content\STAT_6021_Linear_Models\PDFs", pdflist)
    #pp.pprint(pdflist)
    print("--- %s seconds ---" % (datetime.now() - start_time))