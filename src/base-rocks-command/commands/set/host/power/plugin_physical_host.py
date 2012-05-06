# $Id: plugin_physical_host.py,v 1.4 2012/05/06 05:49:39 phil Exp $
# 
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 5.5 (Mamba)
# 		         version 6.0 (Mamba)
# 
# Copyright (c) 2000 - 2012 The Regents of the University of California.
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
# $Log: plugin_physical_host.py,v $
# Revision 1.4  2012/05/06 05:49:39  phil
# Copyright Storm for Mamba
#
# Revision 1.3  2011/07/23 02:31:31  phil
# Viper Copyright
#
# Revision 1.2  2010/12/08 00:13:26  bruno
# get the right commands
#
# Revision 1.3  2010/09/07 23:53:01  bruno
# star power for gb
#
# Revision 1.2  2010/07/14 19:39:39  bruno
# better
#
# Revision 1.1  2010/06/22 21:42:36  bruno
# power control and console access for VMs
#
#

import rocks.commands

class Plugin(rocks.commands.Plugin):

	def provides(self):
		return 'physical-host'

	def run(self, args):
		host = args[0]
		state = args[1]
		rsakey = args[2]

		#
		# determine if this is a physical host
		#
		physnode = 1

		rows = self.db.execute("""show tables like 'vm_nodes' """)

		if rows == 1:
			rows = self.db.execute("""select vn.id from
				vm_nodes vn, nodes n where vn.node = n.id and
				n.name = "%s" """ % (host))
			if rows == 1:
				physnode = 0

		if physnode:
			#
			# write IPMI commands here
			#
			pass

