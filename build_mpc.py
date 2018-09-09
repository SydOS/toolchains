import build

import build_gmp
import build_mpfr

ver = "1.1.0"
url =  "https://ftp.gnu.org/gnu/mpc/mpc-" + ver + ".tar.gz"

build.build(url=url, project="mpc", configargs="--with-gmp=" + build.installpath + " --with-mpfr=" + build.installpath)