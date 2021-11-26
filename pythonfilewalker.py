def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

def super_underliner(input, rang_draw=0, offset=2, underline_char="-"):
    print(input)
    if rang_draw==0:
        rang_draw=range(len(input)+offset)
    elif type(rang_draw) == str: 
        rang_draw=range(len(rang_draw)+offset)
    else:
        rang_draw=range(rang_draw)  
    for i in rang_draw:
        print(underline_char, end="")
    print("")

def listfiles(dirpath, namefilter, fullpath):
    print (dirpath)
    os.chdir(dirpath)
    directory=os.getcwd()
    #super_underliner(directory, directory, 2, "_")
    content_ammount=0
    filtered_content_ammount=[""]
    #f=open(directory+'filepaths.txt', 'w')
   # filter_resoult=open(directory+'filter-resoult.txt', 'w')
    if namefilter!="":
        namefilter=namefilter.split()
        print (namefilter)
        for i in namefilter:
                   filtered_content_ammount.append(0)

    for root, dirs, files in os.walk("."):
        for name in files:
            myfiles=os.path.join(directory,root[2:], name)
           # f.write(myfiles+"\n")
            if namefilter!="":
                count=0
                for i in namefilter:
                    count+=1
                    if i in myfiles:
                        try:
                            print(myfiles)
                            #filter_resoult.write(myfiles+"\n") 
                            filtered_content_ammount[count]+=1
                        except Exception: pass
            else:
                try:
                    print(myfiles)
                except Exception: pass
            content_ammount+=1
    super_underliner("\n\nOS walk started on:"+directory, directory, 20, "-")
    print("Os walk checked:",content_ammount,"individual files")
    if namefilter!="":
        print("\nNumber of files filtered by criteria:")
        count=0
        for a in filtered_content_ammount:
            if count !=0: print (namefilter[count-1],"=",a)
            count+=1



install_and_import('argparse')
install_and_import('os')
install_and_import('string')


parser = argparse.ArgumentParser(description='LS command with caviats')
parser.add_argument("-t", metavar="text", help="Printsome text man")
parser.add_argument("-d", metavar="Directory", help="Starting directory")
parser.add_argument("-f", metavar="filter", help="Filter Files by string")
parser.add_argument("-F",  nargs='?', const='', metavar="Fullpath", help="Display full path of a file")

args = parser.parse_args()
t = args.t

x= args.d or "./"
y= args.f or ""
fullpath=0
listfiles(x,y,fullpath)

