#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-GeneralizedHyperbolic
Version  : 0.8.1
Release  : 2
URL      : https://cran.r-project.org/src/contrib/GeneralizedHyperbolic_0.8-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/GeneralizedHyperbolic_0.8-1.tar.gz
Summary  : The Generalized Hyperbolic Distribution
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-DistributionUtils
Requires: R-RUnit
BuildRequires : R-DistributionUtils
BuildRequires : R-RUnit
BuildRequires : clr-R-helpers

%description
related distributions. Density, distribution and quantile
        functions and random number generation are provided for the
        hyperbolic distribution, the generalized hyperbolic
        distribution, the generalized inverse Gaussian distribution and
        the skew-Laplace distribution. Additional functionality is
        provided for the hyperbolic distribution, normal inverse
        Gaussian distribution and generalized inverse Gaussian
        distribution, including fitting of these distributions to data.
        Linear models with hyperbolic errors may be fitted using
        hyperblmFit.

%prep
%setup -q -c -n GeneralizedHyperbolic

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521202905

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521202905
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library GeneralizedHyperbolic
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library GeneralizedHyperbolic
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library GeneralizedHyperbolic
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library GeneralizedHyperbolic|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/GeneralizedHyperbolic/NEWS
/usr/lib64/R/library/GeneralizedHyperbolic/R/GeneralizedHyperbolic
/usr/lib64/R/library/GeneralizedHyperbolic/R/GeneralizedHyperbolic.rdb
/usr/lib64/R/library/GeneralizedHyperbolic/R/GeneralizedHyperbolic.rdx
/usr/lib64/R/library/GeneralizedHyperbolic/data/ArkansasRiver.rda
/usr/lib64/R/library/GeneralizedHyperbolic/data/SandP500.rda
/usr/lib64/R/library/GeneralizedHyperbolic/data/ghypParam.rda
/usr/lib64/R/library/GeneralizedHyperbolic/data/gigParam.rda
/usr/lib64/R/library/GeneralizedHyperbolic/data/hyperbParam.rda
/usr/lib64/R/library/GeneralizedHyperbolic/data/hyperbWSqTable.rda
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
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/Makefile
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/report.html
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/report.txt
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/reportSummary.txt
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runTests.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.dhyperb.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.ghypChangePars.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.ghypMom.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.ghypScale.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.ghypStandPars.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.gigFit.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.pgig.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.qghyp.R
/usr/lib64/R/library/GeneralizedHyperbolic/unitTests/runit.qgig.R