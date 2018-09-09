import build

import build_gmp

ver = "0.19"
url =  "http://isl.gforge.inria.fr/isl-" + ver + ".tar.gz"

build.build(url=url, project="isl", configargs="--with-gmp-prefix=" + build.installpath)