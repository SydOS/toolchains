import build

import build_gmp
import build_isl

ver = "0.18.4"
url =  "https://www.bastoul.net/cloog/pages/download/cloog-" + ver + ".tar.gz"

build.build(url=url, project="cloog", configargs="--with-gmp-prefix=" + build.installpath + " --with-isl-prefix=" + build.installpath)