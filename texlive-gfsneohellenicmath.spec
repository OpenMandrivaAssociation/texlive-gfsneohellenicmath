%global tl_name gfsneohellenicmath
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02
Release:	%{tl_revision}.1
Summary:	A math font in the Neo-Hellenic style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/gfsneohellenicmath
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsneohellenicmath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsneohellenicmath.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The GFSNeohellenic font, a historic font first designed by Victor
Scholderer, and digitized by George Matthiopoulos of the Greek Font
Society (GFS), now has native support for Mathematics. The project was
commissioned to GFS by the Department of Mathematics of the University
of the Aegean, Samos, Greece. The Math Table was constructed by the
Mathematics Professor A. Tsolomitis. A useful application is in beamer
documents since this is a Sans Math font. The GFSNeohellenic fontfamily
supports many languages (including Greek), and it is distributed (both
text and math) under the OFL license.

