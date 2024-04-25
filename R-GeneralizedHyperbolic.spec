#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: e661f3a
#
Name     : R-GeneralizedHyperbolic
Version  : 0.8.6
Release  : 54
URL      : https://cran.r-project.org/src/contrib/GeneralizedHyperbolic_0.8-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/GeneralizedHyperbolic_0.8-6.tar.gz
Summary  : The Generalized Hyperbolic Distribution
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-DistributionUtils
BuildRequires : R-DistributionUtils
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Density, distribution and quantile functions and random number generation
  are provided for the hyperbolic distribution, the generalized hyperbolic
        distribution, the generalized inverse Gaussian distribution and
        the skew-Laplace distribution. Additional functionality is
        provided for the hyperbolic distribution, normal inverse
	Gaussian distribution and generalized inverse Gaussian distribution,
	including fitting of these distributions to data. Linear models with
        hyperbolic errors may be fitted using hyperblmFit.

%prep
%setup -q -n GeneralizedHyperbolic
pushd ..
cp -a GeneralizedHyperbolic buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701116497

%install
export SOURCE_DATE_EPOCH=1701116497
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/GeneralizedHyperbolic/DESCRIPTION
/usr/lib64/R/library/GeneralizedHyperbolic/INDEX
/usr/lib64/R/library/GeneralizedHyperbolic/Meta/Rd.rds
/usr/lib64/R/library/GeneralizedHyperbolic/Meta/data.rds
/usr/lib64/R/library/GeneralizedHyperbolic/Meta/features.rds
/usr/lib64/R/library/GeneralizedHyperbolic/Meta/hsearch.rds
/usr/lib64/R/library/GeneralizedHyperbolic/Meta/links.rds
/usr/lib64/R/library/GeneralizedHyperbolic/Meta/nsInfo.rds
/usr/lib64/R/library/GeneralizedHyperbolic/Meta/package.rds
/usr/lib64/R/library/GeneralizedHyperbolic/NAMESPACE
/usr/lib64/R/library/GeneralizedHyperbolic/R/GeneralizedHyperbolic
/usr/lib64/R/library/GeneralizedHyperbolic/R/GeneralizedHyperbolic.rdb
/usr/lib64/R/library/GeneralizedHyperbolic/R/GeneralizedHyperbolic.rdx
/usr/lib64/R/library/GeneralizedHyperbolic/R/sysdata.rdb
/usr/lib64/R/library/GeneralizedHyperbolic/R/sysdata.rdx
/usr/lib64/R/library/GeneralizedHyperbolic/data/ArkansasRiver.rda
/usr/lib64/R/library/GeneralizedHyperbolic/data/SandP500.rda
/usr/lib64/R/library/GeneralizedHyperbolic/data/ghypParam.rda
/usr/lib64/R/library/GeneralizedHyperbolic/data/gigParam.rda
/usr/lib64/R/library/GeneralizedHyperbolic/data/hyperbParam.rda
/usr/lib64/R/library/GeneralizedHyperbolic/data/mamquam.rda
/usr/lib64/R/library/GeneralizedHyperbolic/data/nervePulse.rda
/usr/lib64/R/library/GeneralizedHyperbolic/data/nigParam.rda
/usr/lib64/R/library/GeneralizedHyperbolic/data/resistors.rda
/usr/lib64/R/library/GeneralizedHyperbolic/data/traffic.rda
/usr/lib64/R/library/GeneralizedHyperbolic/help/AnIndex
/usr/lib64/R/library/GeneralizedHyperbolic/help/GeneralizedHyperbolic.rdb
/usr/lib64/R/library/GeneralizedHyperbolic/help/GeneralizedHyperbolic.rdx
/usr/lib64/R/library/GeneralizedHyperbolic/help/aliases.rds
/usr/lib64/R/library/GeneralizedHyperbolic/help/paths.rds
/usr/lib64/R/library/GeneralizedHyperbolic/html/00Index.html
/usr/lib64/R/library/GeneralizedHyperbolic/html/R.css
/usr/lib64/R/library/GeneralizedHyperbolic/hyperbWSqTable.R
/usr/lib64/R/library/GeneralizedHyperbolic/tests/doRUnit.R
/usr/lib64/R/library/GeneralizedHyperbolic/tests/ghypInversionTests.R
/usr/lib64/R/library/GeneralizedHyperbolic/tests/problemData.R
/usr/lib64/R/library/GeneralizedHyperbolic/tests/runghypMoments.R
/usr/lib64/R/library/GeneralizedHyperbolic/tests/test.qgig.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/Makefile
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runTests.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.dghyp.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.dgig.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.ghypChangePars.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.ghypMom.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.ghypScale.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.ghypStandPars.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.gigFit.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.pgig.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.qghyp.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.qgig.R
