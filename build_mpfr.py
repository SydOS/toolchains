import build

import build_gmp

ver = "4.0.1"
url =  "https://ftp.gnu.org/gnu/mpfr/mpfr-" + ver + ".tar.bz2"

build.build(url=url, project="mpfr", configargs="--with-gmp=" + build.installpath)