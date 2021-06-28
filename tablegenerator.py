import glob
import os

prefix="<table style=\"table-layout:fixed;width:100%;\"><tbody>\n"
content=""
for dirpath in sorted(glob.glob("sampleimg/*")):
    dirname=os.path.basename(dirpath)
    eachbody=""
    for filepath in glob.glob(os.path.join(dirpath,"*")):
        filepath = filepath.replace("\\", "/")
        filepath = "./" + filepath
        eachbody+="<td align=\"center\" style=\"word-wrap:break-word;\">\n"
        eachbody+="<img alt=\"{}の画像例\" src=\"{}\" title=\"{}の画像例\"/>\n".format(dirname,filepath,dirname)
        eachbody+="<br/>{}の画像例</td>\n".format(os.path.basename(dirname))
    eachcontent="<tr>\n"+eachbody+"</tr>"
    content+=eachcontent
postfix="</tbody>\n</table>\n"
print(prefix+content+postfix)
