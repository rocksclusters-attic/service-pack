include ../../sp-version.mk

ROLL			= service-pack
NAME    		= roll-$(ROLL)-usersguide
VERSION			= $(SP_VERSION)
RELEASE 		= 0

RPM.ARCH		= noarch

SUMMARY_COMPATIBLE	= $(VERSION)
SUMMARY_MAINTAINER	= Rocks Group
SUMMARY_ARCHITECTURE	= i386, x86_64

ROLL_REQUIRES		= base kernel os
ROLL_CONFLICTS		=

