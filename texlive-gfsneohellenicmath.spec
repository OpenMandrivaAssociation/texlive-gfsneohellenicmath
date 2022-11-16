Name:		texlive-gfsneohellenicmath
Version:	63928
Release:	1
Summary:	A math font in the Neo-Hellenic style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gfsneohellenicmath
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsneohellenicmath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsneohellenicmath.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The GFSNeohellenic font, a historic font first designed by
Victor Scholderer, and digitized by George Matthiopoulos of the
Greek Font Society (GFS), now has native support for
Mathematics. The project was commissioned to GFS by the
Department of Mathematics of the University of the Aegean,
Samos, Greece. The Math Table was constructed by the
Mathematics Professor A. Tsolomitis. A useful application is in
beamer documents since this is a Sans Math font. The
GFSNeohellenic fontfamily supports many languages (including
Greek), and it is distributed (both text and math) under the
OFL license.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/gfsneohellenicmath
%{_texmfdistdir}/fonts/opentype/public/gfsneohellenicmath
%doc %{_texmfdistdir}/doc/fonts/gfsneohellenicmath

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
