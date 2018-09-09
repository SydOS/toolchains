import os

installpath = "$HOME/SydOS.framework/"

def build(url="", project="", configargs="", ignoresrchceck=False, custommake=""):
	if os.path.isdir(project) and ignoresrchceck == False:
		return
	os.system("rm -rf " + project + "*")
	os.system("wget " + url)
	os.system("mkdir " + project)
	os.system("tar -xf " + project + "*.tar.* --strip-components=1 -C " + project)
	os.system("mkdir " + project + "-build")
	if custommake == "":
		os.system("cd " + project + "-build && ../" + project + "/configure --prefix=" + installpath + " " + configargs + " && make && make install")
	else:
		os.system("cd " + project + "-build && ../" + project + "/configure --prefix=" + installpath + " " + configargs + " && " + custommake)