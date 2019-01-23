export GMP_VER=6.1.2
export MPFR_VER=4.0.1
export MPC_VER=1.1.0
export ISL_VER=0.20
export CLOOG_VER=0.20.0
export BINUTILS_VER=2.31.1
export GCC_VER=7.4.0

export ISL_BASE=http://isl.gforge.inria.fr
export CLOOG_BASE=https://github.com/periscop/cloog/releases/download
export GNU_BASE=https://ftp.gnu.org/gnu

export TOOLPATH=/opt/SydOS-toolchains/
export TOOLBASEPATH=/opt/SydOS-toolchain-base/
export PATH=$TOOLPATH:$PATH

set -e
rm -rf build-* isl* cloog* gmp* mpfr* mpc* binutils* gcc* syods-toolchain-*.tar.gz
sudo rm -rf $TOOLPATH $TOOLBASEPATH

#-------------------------------------------------------------------------------
# Toolchain Depenancies
#-------------------------------------------------------------------------------

wget $GNU_BASE/gmp/gmp-$GMP_VER.tar.xz
tar -xf gmp-$GMP_VER.tar.xz
mkdir build-gmp
cd build-gmp
../gmp-$GMP_VER/configure --prefix=$TOOLBASEPATH
make -j4
sudo make install
cd ..

wget $GNU_BASE/mpfr/mpfr-$MPFR_VER.tar.xz
tar -xf mpfr-$MPFR_VER.tar.xz
mkdir build-mpfr
cd build-mpfr
../mpfr-$MPFR_VER/configure --prefix=$TOOLBASEPATH --with-gmp=$TOOLBASEPATH
make -j4
sudo make install
cd ..

wget $GNU_BASE/mpc/mpc-$MPC_VER.tar.gz
tar -xf mpc-$MPC_VER.tar.gz
mkdir build-mpc
cd build-mpc
../mpc-$MPC_VER/configure --prefix=$TOOLBASEPATH --with-gmp=$TOOLBASEPATH --with-mpfr=$TOOLBASEPATH
make -j4
sudo make install
cd ..

wget $ISL_BASE/isl-$ISL_VER.tar.gz
tar -xf isl-$ISL_VER.tar.gz
mkdir build-isl
cd build-isl
../isl-$ISL_VER/configure --prefix=$TOOLBASEPATH --with-gmp-prefix=$TOOLBASEPATH
make -j4
sudo make install
cd ..

wget $CLOOG_BASE/cloog-$CLOOG_VER/cloog-$CLOOG_VER.tar.gz
tar -xf cloog-$CLOOG_VER.tar.gz
mkdir build-cloog
cd build-cloog
../cloog-$CLOOG_VER/configure --prefix=$TOOLBASEPATH --with-gmp-prefix=$TOOLBASEPATH --with-isl-prefix=$TOOLBASEPATH
make -j4
sudo make install
cd ..

tar -zcvf sydos-toolchain-base.tar.gz $TOOLBASEPATH

#-------------------------------------------------------------------------------
# GCC & Binutils
#-------------------------------------------------------------------------------

wget $GNU_BASE/binutils/binutils-$BINUTILS_VER.tar.gz
wget $GNU_BASE/gcc/gcc-$GCC_VER/gcc-$GCC_VER.tar.gz

function gcc_binutils {
	tar -xf binutils-$BINUTILS_VER.tar.gz
	mkdir build-binutils
	cd build-binutils
	../binutils-$BINUTILS_VER/configure --with-isl=$TOOLBASEPATH --with-cloog=$TOOLBASEPATH --prefix=$TOOLPATH --with-sysroot --disable-nls --disable-werror --target=$1
	make -j4
	sudo make install
	cd ..

	tar -xf gcc-$GCC_VER.tar.gz
	mkdir build-gcc
	cd build-gcc
	../gcc-$GCC_VER/configure --with-isl=$TOOLBASEPATH --with-cloog=$TOOLBASEPATH --with-gmp=$TOOLBASEPATH --with-mpfr=$TOOLBASEPATH --with-mpc=$TOOLBASEPATH --prefix=$TOOLPATH --disable-nls --enable-languages=c,c++ --without-headers --target=$1
	make all-gcc -j4
	make all-target-libgcc -j4
	sudo make install-gcc
	sudo make install-target-libgcc
	cd ..

	tar -zcvf sydos-toolchain-$1.tar.gz $TOOLPATH
	sudo rm -rf $TOOLPATH
	rm -rf build-gcc build-binutils gcc-$GCC_VER binutils-$BINUTILS_VER
}

gcc_binutils x86_64-elf
gcc_binutils i786-elf
gcc_binutils i686-elf
gcc_binutils i586-elf
gcc_binutils i486-elf
gcc_binutils i386-elf