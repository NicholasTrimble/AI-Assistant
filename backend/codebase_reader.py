import os

def read_codebase(path):

    code = ""

    for root,dirs,files in os.walk(path):

        for file in files:

            if file.endswith((".js",".ts",".py",".html",".css")):

                with open(os.path.join(root,file),"r",errors="ignore") as f:
                    code += f.read()

    return code[:20000]