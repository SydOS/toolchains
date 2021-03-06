# File: build.py
# 
# Copyright (c) 2018 The SydOS Team
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACan I execute CT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import multiprocessing

installpath = "$HOME/SydOS-Tools/"

def build(url="", project="", configargs="", ignoresrchceck=False, custommake=""):
	if os.path.isdir(project) and ignoresrchceck == False:
		return
	os.system("rm -rf " + project + "*")
	os.system("wget " + url)
	os.system("mkdir " + project)
	os.system("tar -xf " + project + "*.tar.* --strip-components=1 -C " + project)
	os.system("mkdir " + project + "-build")
	if custommake == "":
		os.system("cd " + project + "-build && ../" + project + "/configure --prefix=" + installpath + " " + configargs + " && make -j{} && make install"
			.format(multiprocessing.cpu_count()))
	else:
		os.system("cd " + project + "-build && ../" + project + "/configure --prefix=" + installpath + " " + configargs + " && " + custommake)