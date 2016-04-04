Name:           perl-URI
Version:        1.60
Release:        1
License:        GPL-2.0+ or Artistic
Summary:        A Perl module implementing URI parsing and manipulation
Url:            http://search.cpan.org/dist/URI/
Group:          Development/Libraries
Source0:        URI-%{version}.tar.gz
Source1001: 	perl-URI.manifest
BuildRequires:  perl
BuildRequires:  perl(MIME::Base64)
BuildArch:      noarch

%description
This module implements the URI class. Objects of this class represent
"Uniform Resource Identifier references" as specified in RFC 2396 (and
updated by RFC 2732).

%prep
%setup -q -n URI-%{version}
cp %{SOURCE1001} .
chmod 644 uri-test

%build
export CFLAGS+=" -fvisibility=hidden"
  export CXXFLAGS+=" -fvisibility=hidden"
  
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
