Name:		texlive-bondgraphs
Version:	36605
Release:	2
Summary:	Draws bond graphs in LaTeX, using PGF/TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bondgraphs
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bondgraphs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bondgraphs.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bondgraphs.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is used to draw bond graphs in LaTeX. It uses a
recent version (3.0+) of PGF and TikZ for the drawing, hence,
it is mainly a set of TikZ styles that makes the drawing of
bond graphs easier. Compared to the bondgraph package this
package relies more on TikZ styles and less on macros, to
generate the drawings. As such it can be more flexible than
his, but requires more TikZ knowledge of the user.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/bondgraphs
%{_texmfdistdir}/tex/latex/bondgraphs
%doc %{_texmfdistdir}/doc/latex/bondgraphs

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
