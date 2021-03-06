
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
er171GoldCE.GRAMVersion = '4.0.5'
er171GoldCE.LRMSType = 'Torque' # Torque|PBSPro|ANUPBS

er171GoldCE.qstat = '/usr/local/bin/qstat2'
er171GoldCE.pbsnodes = '/usr/local/bin/pbsnodes'
er171GoldCE.ACL = [ '/ARCS/BeSTGRID/Drug_discovery/Local']

goldView = er171GoldCE.views['er171.arcs.bestgrid.drug_discovery.local'] = VOView()

goldView.DefaultSE = 'ng2.auckland.ac.nz'
goldView.DataDir = '.[label=VS Job dir;user_subdir=False;hidden=True]'
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
er171CE.GRAMVersion = '4.0.5'
er171CE.LRMSType = 'Torque' # Torque|PBSPro|ANUPBS

er171CE.qstat = '/usr/local/bin/qstat2'
er171CE.pbsnodes = '/usr/local/bin/pbsnodes'
er171CE.ACL = [ '/ARCS/NGAdmin', '/ARCS/BeSTGRID', 
                        '/ARCS/BeSTGRID/Drug_discovery/Local', 
                        '/ARCS/BeSTGRID/UoA/CivEng',
                        '/ARCS/BeSTGRID/UoA/MechEng',
                        '/ARCS/BeSTGRID/Quantum_Optics',
                        '/ARCS/BeSTGRID/Workshop','/ARCS/BeSTGRID/UoA/LocalUsers', '/ARCS/BeSTGRID/Local',
                '/nz/uoa']

er171ORGView = er171CE.views['er171.nz.uoa'] = VOView()
er171ORGView.DataDir = '${GLOBUS_USER_HOME}'
er171ORGView.DefaultSE = 'ng2.auckland.ac.nz'
er171ORGView.ACL = [ '/nz/uoa' ]

er171BeSTGRIDView = er171CE.views['er171.arcs.bestgrid'] = VOView()

er171BeSTGRIDView.RealUser = 'grid-bestgrid'
er171BeSTGRIDView.DefaultSE = 'ng2.auckland.ac.nz'
er171BeSTGRIDView.DataDir = '/home/grid-bestgrid'
er171BeSTGRIDView.ACL = [ '/ARCS/BeSTGRID' ]

er171UoAView = er171CE.views['er171.arcs.bestgrid.uoa.localusers'] = VOView()
er171UoAView.DefaultSE = 'ng2.auckland.ac.nz'
er171UoAView.DataDir = '${GLOBUS_USER_HOME}'
er171UoAView.ACL = [ '/ARCS/BeSTGRID/UoA/LocalUsers' ]

er171OpticsView = er171CE.views['er171.arcs.bestgrid.quantum_optics'] = VOView()
er171OpticsView.DefaultSE = 'ng2.auckland.ac.nz'
er171OpticsView.DataDir = '${GLOBUS_USER_HOME}'
er171OpticsView.ACL = [ '/ARCS/BeSTGRID/Quantum_Optics' ]

er171MechView = er171CE.views['er171.arcs.bestgrid.mechEng'] = VOView()
er171MechView.DefaultSE = 'ng2.auckland.ac.nz'
er171MechView.DataDir = '${GLOBUS_USER_HOME}'
er171MechView.ACL = [ '/ARCS/BeSTGRID/UoA/MechEng' ]

er171WorkshopView = er171CE.views['er171.arcs.bestgrid.workshop'] = VOView()
er171WorkshopView.DefaultSE = 'ng2.auckland.ac.nz'
er171WorkshopView.DataDir  = '/home/grid-workshop'
er171WorkshopView.ACL  = ['/ARCS/BeSTGRID/Workshop']


er171CivEngView = er171CE.views['er171.arcs.bestgrid.uoa.civeng'] = VOView()

er171CivEngView.RealUser = 'grid-civil'
er171CivEngView.DefaultSE = 'ng2.auckland.ac.nz'
er171CivEngView.DataDir = '/home/grid-civil'
er171CivEngView.ACL = [ '/ARCS/BeSTGRID/UoA/CivEng' ]

er171NGAdminView = er171CE.views['er171.arcs.ngadmin'] = VOView()

er171NGAdminView.RealUser = 'grid-admin'
er171NGAdminView.DefaultSE = 'ng2.auckland.ac.nz'
er171NGAdminView.DataDir = '/home/grid-admin'
er171NGAdminView.ACL = [ '/ARCS/NGAdmin' ]

er171BeSTGRIDLocalView = er171CE.views['er171.arcs.bestgrid.local'] = VOView()

er171BeSTGRIDLocalView.DefaultSE = 'ng2.auckland.ac.nz'
er171BeSTGRIDLocalView.DataDir = '${GLOBUS_USER_HOME}'
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


er171DrugView = er171CE.views['er171.arcs.bestgrid.drug_discovery'] = VOView()
er171DrugView.RealUser = 'grid-vs'
er171DrugView.DataDir = '/home/grid-vs[label=Drug discovery home;user_subdir=False]'
er171DrugView.DefaultSE = 'ng2.auckland.ac.nz'
er171DrugView.ACL = ['/ARCS/BeSTGRID/Drug_discovery']

er171DrugAcsrcView = er171CE.views['er171.arcs.bestgrid.drug_discovery.acsrc'] = VOView()
er171DrugAcsrcView.RealUser = 'grid-acsrc'
er171DrugAcsrcView.DataDir = '/home/grid-acsrc[label=Acsrc home;user_subdir=False]'
er171DrugAcsrcView.DefaultSE = 'ng2.auckland.ac.nz'
er171DrugAcsrcView.ACL = ['/ARCS/BeSTGRID/Drug_discovery/ACSRC']

er171DrugSBSView = er171CE.views['er171.arcs.bestgrid.drug_discovery.sbs'] = VOView()
er171DrugSBSView.RealUser = 'grid-sbs'
er171DrugSBSView.DataDir = '/home/grid-sbs[label=SBS home;user_subdir=False]'
er171DrugSBSView.DefaultSE = 'ng2.auckland.ac.nz'
er171DrugSBSView.ACL = ['/ARCS/BeSTGRID/Drug_discovery/SBS-Structural_Biology']

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

ng2BeSTGRIDORGArea = ng2StorageElement.areas['ng2.nz.uoa'] = StorageArea();
ng2BeSTGRIDORGArea.Path = '${GLOBUS_USER_HOME}'
ng2BeSTGRIDORGArea.VirtualPath = '${GLOBUS_USER_HOME}'
ng2BeSTGRIDORGArea.Type = 'volatile'
ng2BeSTGRIDORGArea.ACL = [ '/nz/uoa' ]

ng2LocalArea = ng2StorageElement.areas['ng2.arcs.bestgrid.uoa.localusers'] = StorageArea();
ng2LocalArea.Path = '${GLOBUS_USER_HOME}';
ng2LocalArea.VirtualPath =  '${GLOBUS_USER_HOME}'
ng2LocalArea.Type = 'volatile';
ng2LocalArea.ACL = ['/ARCS/BeSTGRID/UoA/LocalUsers'];

ng2BeSTGRIDArea = ng2StorageElement.areas['ng2.arcs.bestgrid'] = StorageArea()
 
ng2BeSTGRIDArea.Path = '/home/grid-bestgrid'
ng2BeSTGRIDArea.Type = 'volatile'
ng2BeSTGRIDArea.ACL = [ '/ARCS/BeSTGRID' ]

ng2WorkshopArea = ng2StorageElement.areas['ng2.arcs.bestgrid.workshop'] = StorageArea()
ng2WorkshopArea.Path = '/home/grid-workshop'
ng2WorkshopArea.Type = 'volatile'
ng2WorkshopArea.ACL = ['/ARCS/BeSTGRID/Workshop']

ng2CivEngArea = ng2StorageElement.areas['ng2.arcs.bestgrid.uoa.civeng'] = StorageArea()
 
ng2CivEngArea.Path = '/home/grid-civil'
ng2CivEngArea.Type = 'volatile'
ng2CivEngArea.ACL = [ '/ARCS/BeSTGRID/UoA/CivEng' ]

ng2NGAdminArea = ng2StorageElement.areas['ng2.arcs.ngadmin'] = StorageArea()
 
ng2NGAdminArea.Path = '/home/grid-admin'
ng2NGAdminArea.Type = 'volatile'
ng2NGAdminArea.ACL = [ '/ARCS/NGAdmin' ]

ng2LocalBeSTGRIDArea = ng2StorageElement.areas['ng2.arcs.bestgrid.local'] = StorageArea()
 
ng2LocalBeSTGRIDArea.Path = '${GLOBUS_USER_HOME}';
ng2LocalBeSTGRIDArea.VirtualPath = '${GLOBUS_USER_HOME}';
ng2LocalBeSTGRIDArea.Type = 'volatile'
ng2LocalBeSTGRIDArea.ACL = [ '/ARCS/BeSTGRID/Local' ]


ng2BioInfoArea = ng2StorageElement.areas['ng2.arcs.bestgrid.uoa.bioinfo'] = StorageArea()
ng2BioInfoArea.Path = '/home/LocalUsers'
ng2BioInfoArea.Type = 'volatile'
ng2BioInfoArea.ACL = [ '/ARCS/BeSTGRID/UoA/BioInfo' ]

ng2BrowningsArea = ng2StorageElement.areas['ng2.arcs.bestgrid.uoa.brownings'] = StorageArea()
ng2BrowningsArea.Path = '/home/grid-browning'
ng2BrowningsArea.Type = 'volatile'
ng2BrowningsArea.ACL = [ '/ARCS/BeSTGRID/UoA/Brownings' ]

ng2QOArea = ng2StorageElement.areas['ng2.arcs.bestgrid.quantum_optics'] = StorageArea()
ng2QOArea.Type = 'volatile'
ng2QOArea.Path =  '.[label=Quantum Optics user home;user_subdir=False;hidden=True]'
ng2QOArea.ACL = [ '/ARCS/BeSTGRID/Quantum_Optics' ]

ng2MechArea = ng2StorageElement.areas['ng2.arcs.bestgrid.mechEng'] = StorageArea()
ng2MechArea.Type = 'volatile'
ng2MechArea.Path =  '.[label=Mechanical ENgineering user home;user_subdir=False;hidden=True]'
ng2MechArea.ACL = [ '/ARCS/BeSTGRID/UoA/MechEng' ]

"""
 Drug Discovery Project
"""

ng2DrugArea = ng2StorageElement.areas['ng2.arcs.bestgrid.drug_discovery'] = StorageArea()
ng2DrugArea.Path = '/home/grid-vs[label=Drug discovery resources;user_subdir=False]'
ng2DrugArea.Type = 'permanent'
ng2DrugArea.ACL = [ '/ARCS/BeSTGRID/Drug_discovery' ]

ng2DrugAcsrcArea = ng2StorageElement.areas['ng2.arcs.bestgrid.drug_discovery.acsrc'] = StorageArea()
ng2DrugAcsrcArea.Path = '/home/grid-acsrc[label=Acsrc  resources;user_subdir=False]'
ng2DrugAcsrcArea.Type = 'permanent'
ng2DrugAcsrcArea.ACL = [ '/ARCS/BeSTGRID/Drug_discovery/ACSRC' ]

ng2DrugSBSArea = ng2StorageElement.areas['ng2.arcs.bestgrid.drug_discovery.sbs'] = StorageArea()
ng2DrugSBSArea.Path = '/home/grid-sbs[label=SBS  resources;user_subdir=False]'
ng2DrugSBSArea.Type = 'permanent'
ng2DrugSBSArea.ACL = [ '/ARCS/BeSTGRID/Drug_discovery/SBS-Structural_Biology' ]


ng2DrugLocalArea = ng2StorageElement.areas['ng2.arcs.bestgrid.drug_discovery.local'] = StorageArea()
ng2DrugLocalArea.Path =  '.[label=Drug discovery user home;user_subdir=False;hidden=True]'
ng2DrugLocalArea.Type = 'permanent'
ng2DrugLocalArea.ACL = [ '/ARCS/BeSTGRID/Drug_discovery/Local' ]



# /STORAGE ELEMENT AREA

# STORAGE ELEMENT PROTOCOL
# this name must be unique for each protocol in the storage element. It is not reference anywhere else.
# see twiki page for further details on this section
accessProtocol = ng2StorageElement.access_protocols['protocol'] = AccessProtocol()
accessProtocol.Type = 'gsiftp'
accessProtocol.Version = '2.3'
accessProtocol.Endpoint = 'gsiftp://ng2.auckland.ac.nz:2811'
accessProtocol.Capability = [ 'file transfer', 'other capability' ]


#### data fabric mappings 

dfAucklandSE = package.StorageElement['df.auckland.ac.nz'] = StorageElement()

dfLocalArea = dfAucklandSE.areas['df-auckland.arcs.bestgrid.local'] = StorageArea()
dfLocalArea.Path = '${GLOBUS_USER_HOME}';
dfLocalArea.VirtualPath =  '${GLOBUS_USER_HOME}';
dfLocalArea.ACL = [ '/ARCS/BeSTGRID/Local','/nz/nesi' ];
dfLocalArea.Type = 'permanent';

dfaccess = dfAucklandSE.access_protocols['protocol'] = AccessProtocol()
dfaccess.Type = 'gsiftp'
dfaccess.Version = '2.3'
dfaccess.Endpoint = 'gsiftp://df.auckland.ac.nz:2811'
dfaccess.Capability = [ 'file transfer', 'other capability' ]
