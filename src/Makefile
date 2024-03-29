# $Id: Makefile,v 1.30 2013/02/13 19:47:30 clem Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		       version 6.1.1 (Sand Boa)
# 
# Copyright (c) 2000 - 2014 The Regents of the University of California.
# All rights reserved.	
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
# notice unmodified and in its entirety, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided 
# with the distribution.
# 
# 3. All advertising and press materials, printed or electronic, mentioning
# features or use of this software must display the following acknowledgement: 
# 
# 	"This product includes software developed by the Rocks(r)
# 	Cluster Group at the San Diego Supercomputer Center at the
# 	University of California, San Diego and its contributors."
# 
# 4. Except as permitted for the purposes of acknowledgment in paragraph 3,
# neither the name or logo of this software nor the names of its
# authors may be used to endorse or promote products derived from this
# software without specific prior written permission.  The name of the
# software includes the following terms, and any derivatives thereof:
# "Rocks", "Rocks Clusters", and "Avalanche Installer".  For licensing of 
# the associated name, interested parties should contact Technology 
# Transfer & Intellectual Property Services, University of California, 
# San Diego, 9500 Gilman Drive, Mail Code 0910, La Jolla, CA 92093-0910, 
# Ph: (858) 534-5815, FAX: (858) 534-7345, E-MAIL:invent@ucsd.edu
# 
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# @Copyright@
#
#

INCLUDEPACKAGE = base/src/command/ base/src/devel base/src/developersguide base/src/foundation-git \
                 base/src/foundation-mysql base/src/foundation-python-extras base/src/usersguide \
		 base/src/java ganglia/src/rocks-command ganglia/src/usersguide \
                 perl/src/cpan perl/src/cpan-support \
                 bio/src/libxslt bio/src/bioperl-support bio/src/bioperl-ext bio/src/bioperl

BASEPATH = ../../


ROCKSROOT.ABSOLUTE = $(shell cd $(ROCKSROOT); pwd)
ARCH.BIN = $(ROCKSROOT.ABSOLUTE)/bin/arch
ARCH = $(shell $(ARCH.BIN))

ifeq ($(strip $(ARCH)), x86_64)
INCLUDEPACKAGE += kvm/src/rocks-command kvm/src/usersguide
endif

default:	rpm

rpm::
	for i in $(INCLUDEPACKAGE) ; do \
		cd $(BASEPATH)$$i; \
		ROLLNAME=`awk  '{if ( /ROLLNAME/ ) print $3}' ../../version.mk `  $(MAKE) $@ || exit 2 ; \
		PkgName=`grep ^NAME version.mk | awk '{print $$3}'|sed 's/$$(ROLL)/*/'`; \
		if [ "$$PkgName" ] ; then \
			cp $(BASEPATH)RPMS/*/$$PkgName*rpm ../../../service-pack/RPMS/$(ARCH) || exit 2; \
		fi; \
		cd -; \
	done
	#special case for the perl cpan-support packages
	cp $(BASEPATH)/perl/RPMS/*/opt-perl-*.rpm ../RPMS/$(ARCH) || exit 2;
	cp $(BASEPATH)/bio/RPMS/*/opt-perl-*.rpm ../RPMS/$(ARCH) || exit 2;
	cp $(BASEPATH)/base/RPMS/$(ARCH)/jdk-*.rpm ../RPMS/$(ARCH) || exit 2;
	cd usersguide; make rpm


copyright clean::
	for i in $(INCLUDEPACKAGE) ; do \
		cd $(BASEPATH)$$i; \
		$(MAKE) $@ || exit 2 ; \
		cd -; \
	done


