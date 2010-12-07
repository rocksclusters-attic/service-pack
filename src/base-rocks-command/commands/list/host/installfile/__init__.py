#
# $Id: __init__.py,v 1.1 2010/12/07 23:52:22 bruno Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 5.4 (Maverick)
# 
# Copyright (c) 2000 - 2010 The Regents of the University of California.
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
# $Log: __init__.py,v $
# Revision 1.1  2010/12/07 23:52:22  bruno
# the start of SP 5.4.1
#
# Revision 1.6  2010/09/07 23:52:55  bruno
# star power for gb
#
# Revision 1.5  2009/05/01 19:06:58  mjk
# chimi con queso
#
# Revision 1.4  2009/01/05 23:46:59  bruno
# can now build a compute node
#
# Revision 1.3  2008/10/18 00:55:50  mjk
# copyright 5.1
#
# Revision 1.2  2008/03/06 23:41:37  mjk
# copyright storm on
#
# Revision 1.1  2007/12/10 21:28:34  bruno
# the base roll now contains several elements from the HPC roll, thus
# making the HPC roll optional.
#
# this also includes changes to help build and configure VMs for V.
#
#

import os
import sys
import rocks
import string
import rocks.gen
import rocks.commands
import xml.dom.ext
import xml.dom.ext.reader.Sax2

class ProfileNodeFilter(rocks.gen.NodeFilter):
	def acceptNode(self, node):
		if node.nodeName == 'profile':
			return self.FILTER_ACCEPT
		if node.nodeName == 'section':
			return self.FILTER_ACCEPT

		return self.FILTER_SKIP


class Command(rocks.commands.Command):
	"""
	Process an XML-based installation file and output an OS-specific
	installation file (e.g., a kickstart or jumpstart file).

	<param type='string' name='section'>
	Which section within the XML installation file to process (e.g.,
	"kickstart", "begin", etc.).
	</param>

	<example cmd='list host installfile section="kickstart"'>
	Output a RedHat-compliant kickstart file.
	</example>
	"""

	def getChildText(self, node):
		text = ''
		for child in node.childNodes:
			if child.nodeType == child.TEXT_NODE:
				text += child.nodeValue
			if child.nodeType == child.CDATA_SECTION_NODE:
				text += child.nodeValue
		return string.strip(text)


	def run(self, params, args):
		section, = self.fillParams( [('section', None)] )

		if not section:
			rocks.commands.Abort("Must supply section")

		self.xml_doc = xml.dom.ext.reader.Sax2.FromXmlStream(sys.stdin)
		self.xml_filter = ProfileNodeFilter({})
		self.xml_tree = self.xml_doc.createTreeWalker(self.xml_doc,
			self.xml_filter.SHOW_ELEMENT, self.xml_filter, 0)

		node = self.xml_tree.nextNode()
		done = 0
		text = ''
		while node and done == 0:
			if node.nodeName == 'section':
				attr = node.attributes
				section_name = \
					attr.getNamedItem((None, 'name')).value

				if section_name == section:
					text = self.getChildText(node)
					done = 1

			node = self.xml_tree.nextNode()

		self.beginOutput()
		self.addOutput(None, text)
		self.endOutput(padChar='')
