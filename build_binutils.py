import build

import build_isl
import build_cloog
import build_mpc

ver = "2.31.1"
url =  "https://ftp.gnu.org/gnu/binutils/binutils-" + ver + ".tar.gz"

def do_build(target=""):
	build.build(url=url, project="binutils", configargs="--with-isl={} --with-cloog={} --with-sysroot --disable-nls --disable-werror --target={}".format(build.installpath, build.installpath, target), ignoresrchceck=True)