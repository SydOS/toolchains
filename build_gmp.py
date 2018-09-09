import build

ver = "6.1.2"
url =  "https://ftp.gnu.org/gnu/gmp/gmp-" + ver + ".tar.bz2"

build.build(url=url, project="gmp")