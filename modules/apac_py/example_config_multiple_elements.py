#~ For instructions on how configure the mip see twiki page
#~ http://www.vpac.org/twiki/bin/view/APACgrid/ConfigureAPACInfoServiceProvider. When referred to 
#~ a twiki page in this document, that is the page that is meant

#~ The configuration is divided in to X main segments

#~ Package 
	#~ Site
	#~ Cluster (M)
		#~ Computing element (M)
			#~ VOView (M)
		#~ Subcluster (M)
			#~ Processor 
			#~ Memory
			#~ Operating system
	#~ Storage Element (M)
		#~ Area (M)
		#~ Protocol (M)


#~ The items with a (M) next to them can be multiple instances in a single configuration. 
#~ For example there maybe 3 subcluster in a single cluster, or many VOViews in a computing element

#~ Below is the minimum configuration options possible. If your site does have multiple instances of the 
#~ items above fileX which contains ready made duplicates of each element may be useful to you. 

###############


# package name : this name must be the same as in pkgs in source.pl
# there is only one package per configuration file
package = config['default'] = Package()
# this name will be used to create another configuration file, in this case default.pl.  This config file will be referred to as package.pl in the rest of these comments. See twiki page for more details.


###############


# SITE INFORMATION
# There can only be one site in a configuration
# this is the name defined in site line in package.pl
site = package.Site['TEST'] = Site()
 
site.Name = 'ExampleSite'
site.Description = 'An example site'
site.OtherInfo = ['some info', 'other info']
site.Web = 'http://example.apac.site'

site.Sponsor = [ 'sponsor 1', 'sponsor 2' ]
site.Location = 'Town, Country'
site.Latitude = '0'
site.Longitude = '0'

# if you set Contact the you don't need to set the others
site.Contact = 'mailto:support@example.apac.site'
#site.SysAdminContact = 'mailto:admin@example.apac.site'
#site.SecurityContact = 'mailto:security@example.apac.site'
#site.UserSupportContact = 'mailto:support@example.apac.site'


###############

# CLUSTER
# this name is defined in cluster line in package.pl
cluster = package.Cluster['cluster1'] = Cluster()
 
cluster.Name = 'clusterhostname'
cluster.WNTmpDir = '/working/tmp/dir'
cluster.TmpDir = '/std/tmp/dir'

####

# COMPUTING ELEMENT
# this name is defined in computing element of package.pl
computeElement = package.ComputingElement['compute1'] = ComputingElement()

#computeElement.nodePropertyFilter = 'property'
computeElement.Name = 'queue_name'
computeElement.Status = 'Production'
computeElement.JobManager = 'jobmanager-pbs'
computeElement.HostName = 'ng2.example.apac.site'
computeElement.GateKeeperPort = 8443
computeElement.ContactString = 'ng2.hostname/jobmanager-pbs'
computeElement.DefaultSE = 'ngdata.example.apac.site'
computeElement.ApplicationDir = 'UNAVAILABLE'
computeElement.DataDir = cluster.TmpDir
computeElement.LRMSType = 'Torque' # Torque|PBSPro|OpenPBS (note: ANUPBS is considered as OpenPBS)

computeElement.qstat = '/usr/bin/qstat'
computeElement.pbsnodes = '/usr/bin/pbsnodes'

# this information can be retrieved from your LRMS (if defined)
#computeElement.MaxTotalJobs = 9999999
#computeElement.MaxRunningJobs = 9999999
#computeElement.MaxCPUTime = 9999999
#computeElement.MaxWallClockTime = 9999999
#computeElement.MaxTotalJobsPerUser = 9999999

# you can define these if you want, but it's not advised
#computeElement.LRMSVersion = '2.1.4'
#computeElement.Priority = 1
#computeElement.FreeCPUs = 1
#computeElement.TotalCPUs = 1
        
#computeElement.WaitingJobs = 0
#computeElement.RunningJobs = 0
#computeElement.TotalJobs = 0
#computeElement.FreeJobSlots = 0

#computeElement.ACL = [ '/VO3', '/VO4' ]


# VOVIEW
# this name is defined must be unique for each voview in the computing element. It is not refered to anywhere else
voview = computeElement.views['view1'] = VOView()

# the RealUser is used in working out the job information for the VOView, ie WaitingJobs, TotalCPUs, etc
# it should be retrieved from GUMS in the future
voview.RealUser = 'grid-admin'
voview.DefaultSE = 'ngdata.example.apac.site'
voview.DataDir = '/path/to/area1'
voview.ACL = [ '/VO1', '/VO2' ]
# /VOVIEW


#~ # SECOND VOVIEW
#~ # to define another voiewi for the computing element uncomment these lines and fill in the text
#~ # this name is defined must be unique for each voview. It is not refered to anywhere else
#~ voview = computeElement.views['view1'] = VOView()

#~ # the RealUser is used in working out the job information for the VOView, ie WaitingJobs, TotalCPUs, etc
#~ # it should be retrieved from GUMS in the future
#~ voview.RealUser = 'grid-admin'
#~ voview.DefaultSE = 'ngdata.example.apac.site'
#~ voview.DataDir = '/path/to/area1'
#~ voview.ACL = [ '/VO1', '/VO2' ]
#~ # /SECOND VOVIEW

# /COMPUTING ELEMENT




#~ # SECOND COMPUTING ELEMENT 
#~ # to define another computing element uncomment these lines and fill in the text
#~ # this name is defined in computing element of package.pl
#~ computeElement = package.ComputingElement['compute1'] = ComputingElement()

#~ #computeElement.nodePropertyFilter = 'property'
#~ computeElement.Name = 'queue_name'
#~ computeElement.Status = 'Production'
#~ computeElement.JobManager = 'jobmanager-pbs'
#~ computeElement.HostName = 'ng2.example.apac.site'
#~ computeElement.GateKeeperPort = 8443
#~ computeElement.ContactString = 'ng2.hostname/jobmanager-pbs'
#~ computeElement.DefaultSE = 'ngdata.example.apac.site'
#~ computeElement.ApplicationDir = 'UNAVAILABLE'
#~ computeElement.DataDir = cluster.TmpDir
#~ computeElement.LRMSType = 'Torque' # Torque|PBSPro|OpenPBS (note: ANUPBS is considered as OpenPBS)

#~ computeElement.qstat = '/usr/bin/qstat'
#~ computeElement.pbsnodes = '/usr/bin/pbsnodes'

#~ # this information can be retrieved from your LRMS (if defined)
#~ #computeElement.MaxTotalJobs = 9999999
#~ #computeElement.MaxRunningJobs = 9999999
#~ #computeElement.MaxCPUTime = 9999999
#~ #computeElement.MaxWallClockTime = 9999999
#~ #computeElement.MaxTotalJobsPerUser = 9999999

#~ # you can define these if you want, but it's not advised
#~ #computeElement.LRMSVersion = '2.1.4'
#~ #computeElement.Priority = 1
#~ #computeElement.FreeCPUs = 1
#~ #computeElement.TotalCPUs = 1
        
#~ #computeElement.WaitingJobs = 0
#~ #computeElement.RunningJobs = 0
#~ #computeElement.TotalJobs = 0
#~ #computeElement.FreeJobSlots = 0

#~ #computeElement.ACL = [ '/VO3', '/VO4' ]


#~ # VOVIEW
#~ # this name is defined must be unique for each voview in the computing element. It is not refered to anywhere else
#~ voview = computeElement.views['view1'] = VOView()

#~ # the RealUser is used in working out the job information for the VOView, ie WaitingJobs, TotalCPUs, etc
#~ # it should be retrieved from GUMS in the future
#~ voview.RealUser = 'grid-admin'
#~ voview.DefaultSE = 'ngdata.example.apac.site'
#~ voview.DataDir = '/path/to/area1'
#~ voview.ACL = [ '/VO1', '/VO2' ]
#~ # /VOVIEW


#~ # SECOND VOVIEW
#~ # to define another voiewi for the computing element uncomment these lines and fill in the text
#~ # this name is defined must be unique for each voview. It is not refered to anywhere else
#~ voview = computeElement.views['view1'] = VOView()

#~ # the RealUser is used in working out the job information for the VOView, ie WaitingJobs, TotalCPUs, etc
#~ # it should be retrieved from GUMS in the future
#~ voview.RealUser = 'grid-admin'
#~ voview.DefaultSE = 'ngdata.example.apac.site'
#~ voview.DataDir = '/path/to/area1'
#~ voview.ACL = [ '/VO1', '/VO2' ]
#~ # /SECOND VOVIEW

#~ #/SECOND COMPUTING ELEMENT 

####

# SUBCLUSTER
# this name is defined in the subcluser line in package.pl 
subcluster = package.SubCluster['sub1'] = SubCluster()
 
subcluster.InboundIP = False
subcluster.OutboundIP = True
subcluster.PlatformType = ''
subcluster.SMPSize = 1

subcluster.PhysicalCPUs = 128
subcluster.LogicalCPUs = 128
subcluster.WNTmpDir = cluster.WNTmpDir
subcluster.TmpDir = cluster.TmpDir


# PROCESSOR
# each subcluster has one cpu reference
subcluster.Processor = Processor()
subcluster.Processor.File = '/proc/cpuinfo'
# if you want to override any values, just uncomment
#subcluster.Processor.Model = 'prossy model'
#subcluster.Processor.Vendor = 'prossy vendor'
#subcluster.Processor.ClockSpeed = 10000
#subcluster.Processor.InstructionSet = 'fpu tsc msr pae mce cx8 apic mtrr mca'

# MAIN MEMORY
# each subcluster has one memory reference
subcluster.MainMemory = MainMemory()
subcluster.MainMemory.File = '/proc/meminfo'
# uncomment to override
#subcluster.MainMemory.RAMSize = 1024
#subcluster.MainMemory.VirtualSize = 3072

# OPERATING SYSTEM
# each subcluster has one OS reference
subcluster.OperatingSystem = OperatingSystem()
subcluster.OperatingSystem.File = '/usr/bin/lsb_release'
#subcluster.OperatingSystem.Name = 'OS of your choice'
#subcluster.OperatingSystem.Release = 'hopefully recent'
#subcluster.OperatingSystem.Version = '1.0.0'
# /SUBCLUSTER




#~ # SECOND SUBCLUSTER
#~ # to define another subcluster uncomment these lines and fill in the text
#~ # this name is defined in the subcluser line in package.pl 
#~ subcluster = package.SubCluster['sub1'] = SubCluster()
 
#~ subcluster.InboundIP = False
#~ subcluster.OutboundIP = True
#~ subcluster.PlatformType = ''
#~ subcluster.SMPSize = 1

#~ subcluster.PhysicalCPUs = 128
#~ subcluster.LogicalCPUs = 128
#~ subcluster.WNTmpDir = cluster.WNTmpDir
#~ subcluster.TmpDir = cluster.TmpDir


#~ # PROCESSOR
#~ # each subcluster has one cpu reference
#~ subcluster.Processor = Processor()
#~ subcluster.Processor.File = '/proc/cpuinfo'
#~ # if you want to override any values, just uncomment
#~ #subcluster.Processor.Model = 'prossy model'
#~ #subcluster.Processor.Vendor = 'prossy vendor'
#~ #subcluster.Processor.ClockSpeed = 10000
#~ #subcluster.Processor.InstructionSet = 'fpu tsc msr pae mce cx8 apic mtrr mca'

#~ # MAIN MEMORY
#~ # each subcluster has one memory reference
#~ subcluster.MainMemory = MainMemory()
#~ subcluster.MainMemory.File = '/proc/meminfo'
#~ # uncomment to override
#~ #subcluster.MainMemory.RAMSize = 1024
#~ #subcluster.MainMemory.VirtualSize = 3072

#~ # OPERATING SYSTEM
#~ # each subcluster has one OS reference
#~ subcluster.OperatingSystem = OperatingSystem()
#~ subcluster.OperatingSystem.File = '/usr/bin/lsb_release'
#~ #subcluster.OperatingSystem.Name = 'OS of your choice'
#~ #subcluster.OperatingSystem.Release = 'hopefully recent'
#~ #subcluster.OperatingSystem.Version = '1.0.0'
#~ # /SECOND SUBCLUSTER
# /CLUSTER

#~ # SECOND CLUSTER
#~ # to define another cluster, uncomment these line and fill them in
#~ # this name is defined in cluster line in package.pl
#~ cluster = package.Cluster['cluster1'] = Cluster()
 
#~ cluster.Name = 'clusterhostname'
#~ cluster.WNTmpDir = '/working/tmp/dir'
#~ cluster.TmpDir = '/std/tmp/dir'

#~ ####

#~ # COMPUTING ELEMENT
#~ # this name is defined in computing element of package.pl
#~ computeElement = package.ComputingElement['compute1'] = ComputingElement()

#~ #computeElement.nodePropertyFilter = 'property'
#~ computeElement.Name = 'queue_name'
#~ computeElement.Status = 'Production'
#~ computeElement.JobManager = 'jobmanager-pbs'
#~ computeElement.HostName = 'ng2.example.apac.site'
#~ computeElement.GateKeeperPort = 8443
#~ computeElement.ContactString = 'ng2.hostname/jobmanager-pbs'
#~ computeElement.DefaultSE = 'ngdata.example.apac.site'
#~ computeElement.ApplicationDir = 'UNAVAILABLE'
#~ computeElement.DataDir = cluster.TmpDir
#~ computeElement.LRMSType = 'Torque' # Torque|PBSPro|OpenPBS (note: ANUPBS is considered as OpenPBS)

#~ computeElement.qstat = '/usr/bin/qstat'
#~ computeElement.pbsnodes = '/usr/bin/pbsnodes'

#~ # this information can be retrieved from your LRMS (if defined)
#~ #computeElement.MaxTotalJobs = 9999999
#~ #computeElement.MaxRunningJobs = 9999999
#~ #computeElement.MaxCPUTime = 9999999
#~ #computeElement.MaxWallClockTime = 9999999
#~ #computeElement.MaxTotalJobsPerUser = 9999999

#~ # you can define these if you want, but it's not advised
#~ #computeElement.LRMSVersion = '2.1.4'
#~ #computeElement.Priority = 1
#~ #computeElement.FreeCPUs = 1
#~ #computeElement.TotalCPUs = 1
        
#~ #computeElement.WaitingJobs = 0
#~ #computeElement.RunningJobs = 0
#~ #computeElement.TotalJobs = 0
#~ #computeElement.FreeJobSlots = 0

#~ #computeElement.ACL = [ '/VO3', '/VO4' ]


#~ # VOVIEW
#~ # this name is defined must be unique for each voview in the computing element. It is not refered to anywhere else
#~ voview = computeElement.views['view1'] = VOView()

#~ # the RealUser is used in working out the job information for the VOView, ie WaitingJobs, TotalCPUs, etc
#~ # it should be retrieved from GUMS in the future
#~ voview.RealUser = 'grid-admin'
#~ voview.DefaultSE = 'ngdata.example.apac.site'
#~ voview.DataDir = '/path/to/area1'
#~ voview.ACL = [ '/VO1', '/VO2' ]
#~ # /VOVIEW


#~ # SECOND VOVIEW
#~ # to define another voiewi for the computing element uncomment these lines and fill in the text
#~ # this name is defined must be unique for each voview. It is not refered to anywhere else
#~ voview = computeElement.views['view1'] = VOView()

#~ # the RealUser is used in working out the job information for the VOView, ie WaitingJobs, TotalCPUs, etc
#~ # it should be retrieved from GUMS in the future
#~ voview.RealUser = 'grid-admin'
#~ voview.DefaultSE = 'ngdata.example.apac.site'
#~ voview.DataDir = '/path/to/area1'
#~ voview.ACL = [ '/VO1', '/VO2' ]
#~ # /SECOND VOVIEW

#~ # /COMPUTING ELEMENT




#~ # SECOND COMPUTING ELEMENT 
#~ # to define another computing element uncomment these lines and fill in the text
#~ # this name is defined in computing element of package.pl
#~ computeElement = package.ComputingElement['compute1'] = ComputingElement()

#~ #computeElement.nodePropertyFilter = 'property'
#~ computeElement.Name = 'queue_name'
#~ computeElement.Status = 'Production'
#~ computeElement.JobManager = 'jobmanager-pbs'
#~ computeElement.HostName = 'ng2.example.apac.site'
#~ computeElement.GateKeeperPort = 8443
#~ computeElement.ContactString = 'ng2.hostname/jobmanager-pbs'
#~ computeElement.DefaultSE = 'ngdata.example.apac.site'
#~ computeElement.ApplicationDir = 'UNAVAILABLE'
#~ computeElement.DataDir = cluster.TmpDir
#~ computeElement.LRMSType = 'Torque' # Torque|PBSPro|ANUPBS

#~ computeElement.qstat = '/usr/bin/qstat'
#~ computeElement.pbsnodes = '/usr/bin/pbsnodes'

#~ # this information can be retrieved from your LRMS (if defined)
#~ #computeElement.MaxTotalJobs = 9999999
#~ #computeElement.MaxRunningJobs = 9999999
#~ #computeElement.MaxCPUTime = 9999999
#~ #computeElement.MaxWallClockTime = 9999999
#~ #computeElement.MaxTotalJobsPerUser = 9999999

#~ # you can define these if you want, but it's not advised
#~ #computeElement.LRMSVersion = '2.1.4'
#~ #computeElement.Priority = 1
#~ #computeElement.FreeCPUs = 1
#~ #computeElement.TotalCPUs = 1
        
#~ #computeElement.WaitingJobs = 0
#~ #computeElement.RunningJobs = 0
#~ #computeElement.TotalJobs = 0
#~ #computeElement.FreeJobSlots = 0

#~ #computeElement.ACL = [ '/VO3', '/VO4' ]


#~ # VOVIEW
#~ # this name is defined must be unique for each voview in the computing element. It is not refered to anywhere else
#~ voview = computeElement.views['view1'] = VOView()

#~ # the RealUser is used in working out the job information for the VOView, ie WaitingJobs, TotalCPUs, etc
#~ # it should be retrieved from GUMS in the future
#~ voview.RealUser = 'grid-admin'
#~ voview.DefaultSE = 'ngdata.example.apac.site'
#~ voview.DataDir = '/path/to/area1'
#~ voview.ACL = [ '/VO1', '/VO2' ]
#~ # /VOVIEW


#~ # SECOND VOVIEW
#~ # to define another voiewi for the computing element uncomment these lines and fill in the text
#~ # this name is defined must be unique for each voview. It is not refered to anywhere else
#~ voview = computeElement.views['view1'] = VOView()

#~ # the RealUser is used in working out the job information for the VOView, ie WaitingJobs, TotalCPUs, etc
#~ # it should be retrieved from GUMS in the future
#~ voview.RealUser = 'grid-admin'
#~ voview.DefaultSE = 'ngdata.example.apac.site'
#~ voview.DataDir = '/path/to/area1'
#~ voview.ACL = [ '/VO1', '/VO2' ]
#~ # /SECOND VOVIEW

#~ #/SECOND COMPUTING ELEMENT 

#~ ####

#~ # SUBCLUSTER
#~ # this name is defined in the subcluser line in package.pl 
#~ subcluster = package.SubCluster['sub1'] = SubCluster()
 
#~ subcluster.InboundIP = False
#~ subcluster.OutboundIP = True
#~ subcluster.PlatformType = ''
#~ subcluster.SMPSize = 1

#~ subcluster.PhysicalCPUs = 128
#~ subcluster.LogicalCPUs = 128
#~ subcluster.WNTmpDir = cluster.WNTmpDir
#~ subcluster.TmpDir = cluster.TmpDir


#~ # PROCESSOR
#~ # each subcluster has one cpu reference
#~ subcluster.Processor = Processor()
#~ subcluster.Processor.File = '/proc/cpuinfo'
#~ # if you want to override any values, just uncomment
#~ #subcluster.Processor.Model = 'prossy model'
#~ #subcluster.Processor.Vendor = 'prossy vendor'
#~ #subcluster.Processor.ClockSpeed = 10000
#~ #subcluster.Processor.InstructionSet = 'fpu tsc msr pae mce cx8 apic mtrr mca'

#~ # MAIN MEMORY
#~ # each subcluster has one memory reference
#~ subcluster.MainMemory = MainMemory()
#~ subcluster.MainMemory.File = '/proc/meminfo'
#~ # uncomment to override
#~ #subcluster.MainMemory.RAMSize = 1024
#~ #subcluster.MainMemory.VirtualSize = 3072

#~ # OPERATING SYSTEM
#~ # each subcluster has one OS reference
#~ subcluster.OperatingSystem = OperatingSystem()
#~ subcluster.OperatingSystem.File = '/usr/bin/lsb_release'
#~ #subcluster.OperatingSystem.Name = 'OS of your choice'
#~ #subcluster.OperatingSystem.Release = 'hopefully recent'
#~ #subcluster.OperatingSystem.Version = '1.0.0'
#~ # /SUBCLUSTER




#~ # SECOND SUBCLUSTER
#~ # to define another subcluster uncomment these lines and fill in the text
#~ # this name is defined in the subcluser line in package.pl 
#~ subcluster = package.SubCluster['sub1'] = SubCluster()
 
#~ subcluster.InboundIP = False
#~ subcluster.OutboundIP = True
#~ subcluster.PlatformType = ''
#~ subcluster.SMPSize = 1

#~ subcluster.PhysicalCPUs = 128
#~ subcluster.LogicalCPUs = 128
#~ subcluster.WNTmpDir = cluster.WNTmpDir
#~ subcluster.TmpDir = cluster.TmpDir


#~ # PROCESSOR
#~ # each subcluster has one cpu reference
#~ subcluster.Processor = Processor()
#~ subcluster.Processor.File = '/proc/cpuinfo'
#~ # if you want to override any values, just uncomment
#~ #subcluster.Processor.Model = 'prossy model'
#~ #subcluster.Processor.Vendor = 'prossy vendor'
#~ #subcluster.Processor.ClockSpeed = 10000
#~ #subcluster.Processor.InstructionSet = 'fpu tsc msr pae mce cx8 apic mtrr mca'

#~ # MAIN MEMORY
#~ # each subcluster has one memory reference
#~ subcluster.MainMemory = MainMemory()
#~ subcluster.MainMemory.File = '/proc/meminfo'
#~ # uncomment to override
#~ #subcluster.MainMemory.RAMSize = 1024
#~ #subcluster.MainMemory.VirtualSize = 3072

#~ # OPERATING SYSTEM
#~ # each subcluster has one OS reference
#~ subcluster.OperatingSystem = OperatingSystem()
#~ subcluster.OperatingSystem.File = '/usr/bin/lsb_release'
#~ #subcluster.OperatingSystem.Name = 'OS of your choice'
#~ #subcluster.OperatingSystem.Release = 'hopefully recent'
#~ #subcluster.OperatingSystem.Version = '1.0.0'
#~ # /SECOND SUBCLUSTER

#~ # /SECOND CLUSTER

###############

# STORAGE ELEMENT
# this name is defined in the storage element line package.pl
storageElement = package.StorageElement['storage1'] = StorageElement()
 
# STORAGE ELEMENT AREA
# this name must be unique for each storage area in the storage element. It is not reference anywhere else.
area = storageElement.areas['area1'] = StorageArea()
 
area.Path = '/path/to/area1'
area.Type = 'volatile'
area.ACL = [ '/VO1', '/VO2' ]
# /STORAGE ELEMENT AREA


# SECOND STORAGE ELEMENT AREA
# this name must be unique for each storage area in the storage element. It is not reference anywhere else.
area = storageElement.areas['area2'] = StorageArea()
 
area.Path = '/path/to/area2'
area.Type = 'volatile'
area.ACL = [ '/VO3', '/VO4' ]
# /SECOND STORAGE ELEMENT AREA


# STORAGE ELEMENT PROTOCOL
# this name must be unique for each protocol in the storage element. It is not reference anywhere else.
accessProtocol = storageElement.access_protocols['prot1'] = AccessProtocol()

accessProtocol.Type = 'gsiftp'
accessProtocol.Version = '1.0.0'
accessProtocol.Endpoint = 'gsiftp://ngdata.example.apac.site:2811'
accessProtocol.Capability = [ 'file transfer', 'other capability' ]
# /STORAGE ELEMENT PROTOCOL

#~ # SECOND STORAGE ELEMENT PROTOCOL
#~ # to define another protocal uncomment these lines and fill in the text
#~ # this name must be unique for each protocol in the storage element. It is not reference anywhere else.
#~ accessProtocol = storageElement.access_protocols['prot1'] = AccessProtocol()

#~ accessProtocol.Type = 'gsiftp'
#~ accessProtocol.Version = '1.0.0'
#~ accessProtocol.Endpoint = 'gsiftp://ngdata.example.apac.site:2811'
#~ accessProtocol.Capability = [ 'file transfer', 'other capability' ]
#~ # /SECOND STORAGE ELEMENT PROTOCOL

# /STORAGE ELEMENT



#~ # SECOND STORAGE ELEMENT
#~ # to define another storage element uncomment these lines and fill in the text 
#~ # this name is defined in the storage element line package.pl
#~ storageElement = package.StorageElement['storage1'] = StorageElement()
 
#~ # STORAGE ELEMENT AREA
#~ # this name must be unique for each storage area in the storage element. It is not reference anywhere else.
#~ area = storageElement.areas['area1'] = StorageArea()
 
#~ area.Path = '/path/to/area1'
#~ area.Type = 'volatile'
#~ area.ACL = [ '/VO1', '/VO2' ]
#~ # /STORAGE ELEMENT AREA


#~ # SECOND STORAGE ELEMENT AREA
#~ # this name must be unique for each storage area in the storage element. It is not reference anywhere else.
#~ area = storageElement.areas['area2'] = StorageArea()
 
#~ area.Path = '/path/to/area2'
#~ area.Type = 'volatile'
#~ area.ACL = [ '/VO3', '/VO4' ]
#~ # /SECOND STORAGE ELEMENT AREA


#~ # STORAGE ELEMENT PROTOCOL
#~ # this name must be unique for each protocol in the storage element. It is not reference anywhere else.
#~ accessProtocol = storageElement.access_protocols['prot1'] = AccessProtocol()

#~ accessProtocol.Type = 'gsiftp'
#~ accessProtocol.Version = '1.0.0'
#~ accessProtocol.Endpoint = 'gsiftp://ngdata.example.apac.site:2811'
#~ accessProtocol.Capability = [ 'file transfer', 'other capability' ]
#~ # /STORAGE ELEMENT PROTOCOL

#~ # SECOND STORAGE ELEMENT PROTOCOL
#~ # to define another protocal uncomment these lines and fill in the text
#~ # this name must be unique for each protocol in the storage element. It is not reference anywhere else.
#~ accessProtocol = storageElement.access_protocols['prot1'] = AccessProtocol()

#~ accessProtocol.Type = 'gsiftp'
#~ accessProtocol.Version = '1.0.0'
#~ accessProtocol.Endpoint = 'gsiftp://ngdata.example.apac.site:2811'
#~ accessProtocol.Capability = [ 'file transfer', 'other capability' ]
#~ # /SECOND STORAGE ELEMENT PROTOCOL

#~ # /SECOND STORAGE ELEMENT


