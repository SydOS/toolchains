import build

import build_isl
import build_cloog
import build_mpc

ver = "8.2.0"
url =  "https://ftp.gnu.org/gnu/gcc/gcc-" + ver + "/gcc-" + ver + ".tar.gz"

def do_build(target=""):
	build.build(url=url, project="gcc", configargs="--with-isl={} --with-cloog={} --with-gmp={} --with-mpfr={} --with-mpc={} --disable-nls --enable-languages=c,c++ --without-headers --target={}".format(build.installpath, build.installpath, build.installpath, build.installpath, build.installpath, target), ignoresrchceck=True, custommake="make all-gcc && make all-target-libgcc && make install-gcc && make install-target-libgcc")