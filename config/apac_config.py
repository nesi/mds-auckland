
#~ For instructions on how configure the mip see twiki page
#~ http://www.vpac.org/twiki/bin/view/APACgrid/ConfigureAPACInfoServiceProvider. When referred to 
#~ a twiki page in this document, it means this page

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

# This name will be used as the name of another configuration file, in this case the file would be called default.pl.  
# This config file will be referred to as package.pl in the rest of these comments. See twiki page for more details.


###############


# SITE INFORMATION
# There can only be one site in a configuration
# this is the name defined in site line in package.pl
# see twiki page for further details on this section
site = package.Site['auckland.ac.nz'] = Site()
 
site.Name = 'Auckland'
site.Description = 'Auckland''s BeSTGRID'
site.OtherInfo = ['', '']
site.Web = 'http://www.bestgrid.org'

site.Sponsor = [ 'ITS'] 
site.Location = 'Auckland, New Zealand' 
site.Latitude = '-36.853' 
site.Longitude = '174.768'

# if you set Contact the you don't need to set the others
site.Contact = 'mailto:a.kharuk@auckland.ac.nz'
#site.SysAdminContact = 'mailto:admin@example.apac.site'
#site.SecurityContact = 'mailto:security@example.apac.site'
#site.UserSupportContact = 'mailto:support@example.apac.site'


###############

# old cluster. Should probably be removed

cluster = package.Cluster['hpc-bestgrid.auckland.ac.nz'] = Cluster()
 
cluster.Name = 'hpc-bestgrid.auckland.ac.nz'
cluster.WNTmpDir = '/tmp'
cluster.TmpDir = '/home/grid-bestgrid'




# ngdata is  gridftp server for user permanent data

ngdataStorageElement = package.StorageElement['ngdata.ceres.auckland.ac.nz'] = StorageElement()
ngdataLocalArea = ngdataStorageElement.areas['ngdata.arcs.bestgrid.uoa.localusers'] = StorageArea();
ngdataLocalArea.Path = '${GLOBUS_USER_HOME}';
ngdataLocalArea.VirtualPath =  '${GLOBUS_USER_HOME}'
ngdataLocalArea.Type = 'volatile';
ngdataLocalArea.ACL = ['/ARCS/BeSTGRID/UoA/LocalUsers'];

ngdataAccess = ngdataStorageElement.access_protocols['ngdataAccessProtocol'] = AccessProtocol();
ngdataAccess.Type = "gsiftp"
ngdataAccess.Version = "2.3"
ngdataAccess.Endpoint = "gsiftp://ngdata.ceres.auckland.ac.nz:2811"
ngdataAccess.Capability = ['file transfer', 'other capability']

# new cluster


package = config['er171'] = Package()

cluster = package.Cluster['er171.ceres.auckland.ac.nz'] = Cluster()
 
cluster.Name = 'er171.ceres.auckland.ac.nz'
cluster.WNTmpDir = '/tmp'
cluster.TmpDir = '/home/grid-bestgrid'

er171GoldCE = package.ComputingElement['ng2.auckland.ac.nz-gold'] = ComputingElement()
er171GoldCE.Name = 'gold@er171.ceres.auckland.ac.nz'
er171GoldCE.Status = 'Production'
er171GoldCE.JobManager = 'PBS'
er171GoldCE.HostName = 'ng2.auckland.ac.nz'
er171GoldCE.GateKeeperPort = 8443
er171GoldCE.ContactString = 'https://ng2.auckland.ac.nz:8443/wsrf/services/ManagedJobFactoryService'
er171GoldCE.DefaultSE = 'ng2.auckland.ac.nz'
er171GoldCE.ApplicationDir = '/share/apps'
er171GoldCE.DataDir = '/home/grid-vs'
er171GoldCE.LRMSType = 'Torque' # Torque|PBSPro|ANUPBS

er171GoldCE.qstat = '/usr/local/bin/qstat2'
er171GoldCE.pbsnodes = '/usr/local/bin/pbsnodes'
er171GoldCE.ACL = [ '/ARCS/BeSTGRID/Drug_discovery/Local']

goldView = er171GoldCE.views['er171.arcs.bestgrid.drug_discovery.local'] = VOView()

goldView.DefaultSE = 'ng2.auckland.ac.nz'
goldView.DataDir = '.[label=BeSTGRID home;user_subdir=False]'
goldView.ACL = [ '/ARCS/BeSTGRID/Drug_discovery/Local' ]



er171CE = package.ComputingElement['ng2.auckland.ac.nz-er171CE'] = ComputingElement()
er171CE.Name = 'route@er171.ceres.auckland.ac.nz'
er171CE.Status = 'Production'
er171CE.JobManager = 'PBS'
er171CE.HostName = 'ng2.auckland.ac.nz'
er171CE.GateKeeperPort = 8443
er171CE.ContactString = 'https://ng2.auckland.ac.nz:8443/wsrf/services/ManagedJobFactoryService'
er171CE.DefaultSE = 'ng2.auckland.ac.nz'
er171CE.ApplicationDir = '/share/apps'
er171CE.DataDir = cluster.TmpDir
er171CE.LRMSType = 'Torque' # Torque|PBSPro|ANUPBS

er171CE.qstat = '/usr/local/bin/qstat2'
er171CE.pbsnodes = '/usr/local/bin/pbsnodes'
er171CE.ACL = [ '/ARCS/NGAdmin', '/ARCS/BeSTGRID/UoA/BioInfo', '/ARCS/BeSTGRID', '/ARCS/BeSTGRID/UoA/SSRG1',
                        '/ARCS/BeSTGRID/UoA/Brownings','/ARCS/BeSTGRID/Drug_discovery', '/ARCS/BeSTGRID/UoA/LocalUsers', 'ARCS/BeSTGRID/Local']

er171BeSTGRIDView = er171CE.views['er171.arcs.bestgrid'] = VOView()

er171BeSTGRIDView.RealUser = 'grid-bestgrid'
er171BeSTGRIDView.DefaultSE = 'ng2.auckland.ac.nz'
er171BeSTGRIDView.DataDir = '/home/grid-bestgrid'
er171BeSTGRIDView.ACL = [ '/ARCS/BeSTGRID' ]

er171BeSTGRIDLocalView = er171CE.views['er171.arcs.bestgrid.local'] = VOView()

#er171BeSTGRIDLocalView.RealUser = 'grid-bestgrid'
er171BeSTGRIDLocalView.DefaultSE = 'ng2.auckland.ac.nz'
er171BeSTGRIDLocalView.DataDir = '.[label=BeSTGRID home;user_subdir=False]'
er171BeSTGRIDLocalView.ACL = [ '/ARCS/BeSTGRID/Local' ]

er171BrowningsView = er171CE.views['er171.arcs.bestgrid.uoa.brownings'] = VOView()

er171BrowningsView.RealUser = 'grid-browning'
er171BrowningsView.DefaultSE = 'ng2.auckland.ac.nz'
er171BrowningsView.DataDir = '/home/grid-browning'
er171BrowningsView.ACL = ['/ARCS/BeSTGRID/UoA/Brownings']

er171BioInfoView = er171CE.views['er171.arcs.bestgrid.uoa.bioinfo'] = VOView()
er171BioInfoView.DefaultSE = 'ng2.auckland.ac.nz'
er171BioInfoView.DataDir = '/home/grid-bio'
er171BioInfoView.ACL = ['/ARCS/BeSTGRID/UoA/BioInfo']

er171DataLocalView = er171CE.views['view7'] = VOView()
er171DataLocalView.DefaultSE = 'ngdata.ceres.auckland.ac.nz'
er171DataLocalView.ACL = ['/ARCS/BeSTGRID/UoA/LocalUsers']

er171DrugView = er171CE.views['er171.arcs.bestgrid.drug_discovery'] = VOView()
er171DrugView.RealUser = 'grid-vs'
er171DrugView.DataDir = '/home/grid-vs[label=Drug discovery home;user_subdir=False]'
er171DrugView.DefaultSE = 'ng2.auckland.ac.nz'
er171DrugView.ACL = ['/ARCS/BeSTGRID/Drug_discovery']

subcluster = package.SubCluster['ng2.auckland.ac.nz-hpc2'] = SubCluster()
 
subcluster.InboundIP = False
subcluster.OutboundIP = True
subcluster.PlatformType = ''
subcluster.SMPSize = 1

subcluster.PhysicalCPUs = 88
subcluster.LogicalCPUs = 88
subcluster.WNTmpDir = cluster.WNTmpDir
subcluster.TmpDir = cluster.TmpDir


# PROCESSOR
# each subcluster has one cpu reference
# see twiki page for further details on this section
subcluster.Processor = Processor()
subcluster.Processor.File = '/proc/cpuinfo'
# if you want to override any values, just uncomment
#subcluster.Processor.Model = 'Intel Xeon 3000'
#subcluster.Processor.Vendor = 'Intel'
#subcluster.Processor.ClockSpeed = 3000
#subcluster.Processor.InstructionSet = 'fpu tsc msr pae mce cx8 apic mtrr mca'

# MAIN MEMORY
# each subcluster has one memory reference
# see twiki page for further details on this section
subcluster.MainMemory = MainMemory()
subcluster.MainMemory.File = '/proc/meminfo'
# uncomment to override
#subcluster.MainMemory.RAMSize = 1024
#subcluster.MainMemory.VirtualSize = 3072

# OPERATING SYSTEM
# each subcluster has one OS reference
# see twiki page for further details on this section
subcluster.OperatingSystem = OperatingSystem()
subcluster.OperatingSystem.File = '/usr/bin/lsb_release'
subcluster.OperatingSystem.Name = 'CentOS'
subcluster.OperatingSystem.Release = '5'

ng2StorageElement = package.StorageElement['ng2.auckland.ac.nz'] = StorageElement()
 
# STORAGE ELEMENT AREA
# this name must be unique for each storage area in the storage element. It is not reference anywhere else.
# see twiki page for further details on this section

ng2LocalArea = ng2StorageElement.areas['ng2.arcs.bestgrid.uoa.localusers'] = StorageArea();
ng2LocalArea.Path = '${GLOBUS_USER_HOME}';
ng2LocalArea.VirtualPath =  '${GLOBUS_USER_HOME}'
ng2LocalArea.Type = 'volatile';
ng2LocalArea.ACL = ['/ARCS/BeSTGRID/UoA/LocalUsers'];

ng2BeSTGRIDArea = ng2StorageElement.areas['ng2.arcs.bestgrid'] = StorageArea()
 
ng2BeSTGRIDArea.Path = '/home/grid-bestgrid'
ng2BeSTGRIDArea.Type = 'volatile'
ng2BeSTGRIDArea.ACL = [ '/ARCS/BeSTGRID' ]

ng2BeSTGRIDArea = ng2StorageElement.areas['ng2.arcs.bestgrid.local'] = StorageArea()
 
ng2BeSTGRIDArea.Path = '.[label=BeSTGRID home;user_subdir=False]'
ng2BeSTGRIDArea.Type = 'volatile'
ng2BeSTGRIDArea.ACL = [ '/ARCS/BeSTGRID/Local' ]
# /STORAGE ELEMENT AREA

# STORAGE ELEMENT AREA
# this name must be unique for each storage area in the storage element. It is not reference anywhere else.
# see twiki page for further details on this section
ng2BioInfoArea = ng2StorageElement.areas['ng2.arcs.bestgrid.uoa.bioinfo'] = StorageArea()
 
ng2BioInfoArea.Path = '/home/LocalUsers'
ng2BioInfoArea.Type = 'volatile'
ng2BioInfoArea.ACL = [ '/ARCS/BeSTGRID/UoA/BioInfo' ]

ng2BrowningsArea = ng2StorageElement.areas['ng2.arcs.bestgrid.uoa.brownings'] = StorageArea()
 
ng2BrowningsArea.Path = '/home/grid-browning'
ng2BrowningsArea.Type = 'volatile'
ng2BrowningsArea.ACL = [ '/ARCS/BeSTGRID/UoA/Brownings' ]


ng2DrugArea = ng2StorageElement.areas['ng2.arcs.bestgrid.drug_discovery'] = StorageArea()
 
ng2DrugArea.Path = '/home/grid-vs[label=Drug discovery home;user_subdir=False]'
ng2DrugArea.Type = 'volatile'
ng2DrugArea.ACL = [ '/ARCS/BeSTGRID/Drug_discovery' ]


# /STORAGE ELEMENT AREA

# STORAGE ELEMENT PROTOCOL
# this name must be unique for each protocol in the storage element. It is not reference anywhere else.
# see twiki page for further details on this section
accessProtocol = ng2StorageElement.access_protocols['protocol'] = AccessProtocol()

accessProtocol.Type = 'gsiftp'
accessProtocol.Version = '2.3'
accessProtocol.Endpoint = 'gsiftp://ng2.auckland.ac.nz:2811'
accessProtocol.Capability = [ 'file transfer', 'other capability' ]


####
