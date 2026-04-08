import builtins as _builtins
import typing
import pulumi_azure_native.aad as __aad
import pulumi_azure_native.aadiam as __aadiam
import pulumi_azure_native.addons as __addons
import pulumi_azure_native.advisor as __advisor
import pulumi_azure_native.agfoodplatform as __agfoodplatform
import pulumi_azure_native.agricultureplatform as __agricultureplatform
import pulumi_azure_native.alertsmanagement as __alertsmanagement
import pulumi_azure_native.analysisservices as __analysisservices
import pulumi_azure_native.apicenter as __apicenter
import pulumi_azure_native.apimanagement as __apimanagement
import pulumi_azure_native.app as __app
import pulumi_azure_native.appcomplianceautomation as __appcomplianceautomation
import pulumi_azure_native.appconfiguration as __appconfiguration
import pulumi_azure_native.applicationinsights as __applicationinsights
import pulumi_azure_native.appplatform as __appplatform
import pulumi_azure_native.attestation as __attestation
import pulumi_azure_native.authorization as __authorization
import pulumi_azure_native.automanage as __automanage
import pulumi_azure_native.automation as __automation
import pulumi_azure_native.avs as __avs
import pulumi_azure_native.awsconnector as __awsconnector
import pulumi_azure_native.azureactivedirectory as __azureactivedirectory
import pulumi_azure_native.azurearcdata as __azurearcdata
import pulumi_azure_native.azuredata as __azuredata
import pulumi_azure_native.azuredatatransfer as __azuredatatransfer
import pulumi_azure_native.azurefleet as __azurefleet
import pulumi_azure_native.azurelargeinstance as __azurelargeinstance
import pulumi_azure_native.azureplaywrightservice as __azureplaywrightservice
import pulumi_azure_native.azuresphere as __azuresphere
import pulumi_azure_native.azurestack as __azurestack
import pulumi_azure_native.azurestackhci as __azurestackhci
import pulumi_azure_native.baremetalinfrastructure as __baremetalinfrastructure
import pulumi_azure_native.batch as __batch
import pulumi_azure_native.billing as __billing
import pulumi_azure_native.billingbenefits as __billingbenefits
import pulumi_azure_native.blueprint as __blueprint
import pulumi_azure_native.botservice as __botservice
import pulumi_azure_native.cdn as __cdn
import pulumi_azure_native.certificateregistration as __certificateregistration
import pulumi_azure_native.changeanalysis as __changeanalysis
import pulumi_azure_native.chaos as __chaos
import pulumi_azure_native.cloudhealth as __cloudhealth
import pulumi_azure_native.cloudngfw as __cloudngfw
import pulumi_azure_native.codesigning as __codesigning
import pulumi_azure_native.cognitiveservices as __cognitiveservices
import pulumi_azure_native.communication as __communication
import pulumi_azure_native.community as __community
import pulumi_azure_native.compute as __compute
import pulumi_azure_native.computebulkactions as __computebulkactions
import pulumi_azure_native.computelimit as __computelimit
import pulumi_azure_native.computeschedule as __computeschedule
import pulumi_azure_native.confidentialledger as __confidentialledger
import pulumi_azure_native.config as __config
import pulumi_azure_native.confluent as __confluent
import pulumi_azure_native.connectedcache as __connectedcache
import pulumi_azure_native.connectedvmwarevsphere as __connectedvmwarevsphere
import pulumi_azure_native.consumption as __consumption
import pulumi_azure_native.containerinstance as __containerinstance
import pulumi_azure_native.containerregistry as __containerregistry
import pulumi_azure_native.containerservice as __containerservice
import pulumi_azure_native.containerstorage as __containerstorage
import pulumi_azure_native.contoso as __contoso
import pulumi_azure_native.cosmosdb as __cosmosdb
import pulumi_azure_native.costmanagement as __costmanagement
import pulumi_azure_native.customerinsights as __customerinsights
import pulumi_azure_native.customproviders as __customproviders
import pulumi_azure_native.dashboard as __dashboard
import pulumi_azure_native.databasefleetmanager as __databasefleetmanager
import pulumi_azure_native.databasewatcher as __databasewatcher
import pulumi_azure_native.databox as __databox
import pulumi_azure_native.databoxedge as __databoxedge
import pulumi_azure_native.databricks as __databricks
import pulumi_azure_native.datacatalog as __datacatalog
import pulumi_azure_native.datadog as __datadog
import pulumi_azure_native.datafactory as __datafactory
import pulumi_azure_native.datalakeanalytics as __datalakeanalytics
import pulumi_azure_native.datalakestore as __datalakestore
import pulumi_azure_native.datamigration as __datamigration
import pulumi_azure_native.dataprotection as __dataprotection
import pulumi_azure_native.datareplication as __datareplication
import pulumi_azure_native.datashare as __datashare
import pulumi_azure_native.dbformariadb as __dbformariadb
import pulumi_azure_native.dbformysql as __dbformysql
import pulumi_azure_native.dbforpostgresql as __dbforpostgresql
import pulumi_azure_native.delegatednetwork as __delegatednetwork
import pulumi_azure_native.dependencymap as __dependencymap
import pulumi_azure_native.desktopvirtualization as __desktopvirtualization
import pulumi_azure_native.devcenter as __devcenter
import pulumi_azure_native.devhub as __devhub
import pulumi_azure_native.deviceprovisioningservices as __deviceprovisioningservices
import pulumi_azure_native.deviceregistry as __deviceregistry
import pulumi_azure_native.deviceupdate as __deviceupdate
import pulumi_azure_native.devopsinfrastructure as __devopsinfrastructure
import pulumi_azure_native.devspaces as __devspaces
import pulumi_azure_native.devtestlab as __devtestlab
import pulumi_azure_native.digitaltwins as __digitaltwins
import pulumi_azure_native.discovery as __discovery
import pulumi_azure_native.dns as __dns
import pulumi_azure_native.dnsresolver as __dnsresolver
import pulumi_azure_native.domainregistration as __domainregistration
import pulumi_azure_native.durabletask as __durabletask
import pulumi_azure_native.dynamics365fraudprotection as __dynamics365fraudprotection
import pulumi_azure_native.easm as __easm
import pulumi_azure_native.edge as __edge
import pulumi_azure_native.edgemarketplace as __edgemarketplace
import pulumi_azure_native.edgeorder as __edgeorder
import pulumi_azure_native.education as __education
import pulumi_azure_native.elastic as __elastic
import pulumi_azure_native.elasticsan as __elasticsan
import pulumi_azure_native.engagementfabric as __engagementfabric
import pulumi_azure_native.enterpriseknowledgegraph as __enterpriseknowledgegraph
import pulumi_azure_native.eventgrid as __eventgrid
import pulumi_azure_native.eventhub as __eventhub
import pulumi_azure_native.extendedlocation as __extendedlocation
import pulumi_azure_native.fabric as __fabric
import pulumi_azure_native.features as __features
import pulumi_azure_native.fileshares as __fileshares
import pulumi_azure_native.fluidrelay as __fluidrelay
import pulumi_azure_native.frontdoor as __frontdoor
import pulumi_azure_native.graphservices as __graphservices
import pulumi_azure_native.guestconfiguration as __guestconfiguration
import pulumi_azure_native.hardwaresecuritymodules as __hardwaresecuritymodules
import pulumi_azure_native.hdinsight as __hdinsight
import pulumi_azure_native.healthbot as __healthbot
import pulumi_azure_native.healthcareapis as __healthcareapis
import pulumi_azure_native.healthdataaiservices as __healthdataaiservices
import pulumi_azure_native.hybridcloud as __hybridcloud
import pulumi_azure_native.hybridcompute as __hybridcompute
import pulumi_azure_native.hybridconnectivity as __hybridconnectivity
import pulumi_azure_native.hybridcontainerservice as __hybridcontainerservice
import pulumi_azure_native.hybridnetwork as __hybridnetwork
import pulumi_azure_native.impact as __impact
import pulumi_azure_native.importexport as __importexport
import pulumi_azure_native.integrationspaces as __integrationspaces
import pulumi_azure_native.intune as __intune
import pulumi_azure_native.iotcentral as __iotcentral
import pulumi_azure_native.iotfirmwaredefense as __iotfirmwaredefense
import pulumi_azure_native.iothub as __iothub
import pulumi_azure_native.iotoperations as __iotoperations
import pulumi_azure_native.iotoperationsdataprocessor as __iotoperationsdataprocessor
import pulumi_azure_native.iotoperationsmq as __iotoperationsmq
import pulumi_azure_native.iotoperationsorchestrator as __iotoperationsorchestrator
import pulumi_azure_native.keyvault as __keyvault
import pulumi_azure_native.kubernetes as __kubernetes
import pulumi_azure_native.kubernetesconfiguration as __kubernetesconfiguration
import pulumi_azure_native.kubernetesruntime as __kubernetesruntime
import pulumi_azure_native.kusto as __kusto
import pulumi_azure_native.labservices as __labservices
import pulumi_azure_native.loadtestservice as __loadtestservice
import pulumi_azure_native.logic as __logic
import pulumi_azure_native.m365securityandcompliance as __m365securityandcompliance
import pulumi_azure_native.machinelearning as __machinelearning
import pulumi_azure_native.machinelearningservices as __machinelearningservices
import pulumi_azure_native.maintenance as __maintenance
import pulumi_azure_native.managedidentity as __managedidentity
import pulumi_azure_native.managednetwork as __managednetwork
import pulumi_azure_native.managednetworkfabric as __managednetworkfabric
import pulumi_azure_native.managedops as __managedops
import pulumi_azure_native.managedservices as __managedservices
import pulumi_azure_native.management as __management
import pulumi_azure_native.managementpartner as __managementpartner
import pulumi_azure_native.manufacturingplatform as __manufacturingplatform
import pulumi_azure_native.maps as __maps
import pulumi_azure_native.marketplace as __marketplace
import pulumi_azure_native.migrate as __migrate
import pulumi_azure_native.mission as __mission
import pulumi_azure_native.mongocluster as __mongocluster
import pulumi_azure_native.monitor as __monitor
import pulumi_azure_native.mysqldiscovery as __mysqldiscovery
import pulumi_azure_native.netapp as __netapp
import pulumi_azure_native.network as __network
import pulumi_azure_native.networkcloud as __networkcloud
import pulumi_azure_native.networkfunction as __networkfunction
import pulumi_azure_native.notificationhubs as __notificationhubs
import pulumi_azure_native.offazure as __offazure
import pulumi_azure_native.offazurespringboot as __offazurespringboot
import pulumi_azure_native.onlineexperimentation as __onlineexperimentation
import pulumi_azure_native.openenergyplatform as __openenergyplatform
import pulumi_azure_native.operationalinsights as __operationalinsights
import pulumi_azure_native.operationsmanagement as __operationsmanagement
import pulumi_azure_native.orbital as __orbital
import pulumi_azure_native.peering as __peering
import pulumi_azure_native.policyinsights as __policyinsights
import pulumi_azure_native.portal as __portal
import pulumi_azure_native.portalservices as __portalservices
import pulumi_azure_native.powerbi as __powerbi
import pulumi_azure_native.powerbidedicated as __powerbidedicated
import pulumi_azure_native.powerplatform as __powerplatform
import pulumi_azure_native.privatedns as __privatedns
import pulumi_azure_native.professionalservice as __professionalservice
import pulumi_azure_native.programmableconnectivity as __programmableconnectivity
import pulumi_azure_native.providerhub as __providerhub
import pulumi_azure_native.purview as __purview
import pulumi_azure_native.quantum as __quantum
import pulumi_azure_native.quota as __quota
import pulumi_azure_native.recommendationsservice as __recommendationsservice
import pulumi_azure_native.recoveryservices as __recoveryservices
import pulumi_azure_native.redhatopenshift as __redhatopenshift
import pulumi_azure_native.redis as __redis
import pulumi_azure_native.redisenterprise as __redisenterprise
import pulumi_azure_native.relationships as __relationships
import pulumi_azure_native.relay as __relay
import pulumi_azure_native.resourceconnector as __resourceconnector
import pulumi_azure_native.resourcegraph as __resourcegraph
import pulumi_azure_native.resourcehealth as __resourcehealth
import pulumi_azure_native.resources as __resources
import pulumi_azure_native.saas as __saas
import pulumi_azure_native.scheduler as __scheduler
import pulumi_azure_native.scom as __scom
import pulumi_azure_native.scvmm as __scvmm
import pulumi_azure_native.search as __search
import pulumi_azure_native.secretsynccontroller as __secretsynccontroller
import pulumi_azure_native.security as __security
import pulumi_azure_native.securityandcompliance as __securityandcompliance
import pulumi_azure_native.securityinsights as __securityinsights
import pulumi_azure_native.serialconsole as __serialconsole
import pulumi_azure_native.servicebus as __servicebus
import pulumi_azure_native.servicefabric as __servicefabric
import pulumi_azure_native.servicefabricmesh as __servicefabricmesh
import pulumi_azure_native.servicelinker as __servicelinker
import pulumi_azure_native.servicenetworking as __servicenetworking
import pulumi_azure_native.signalrservice as __signalrservice
import pulumi_azure_native.softwareplan as __softwareplan
import pulumi_azure_native.solutions as __solutions
import pulumi_azure_native.sovereign as __sovereign
import pulumi_azure_native.sql as __sql
import pulumi_azure_native.sqlvirtualmachine as __sqlvirtualmachine
import pulumi_azure_native.standbypool as __standbypool
import pulumi_azure_native.storage as __storage
import pulumi_azure_native.storageactions as __storageactions
import pulumi_azure_native.storagecache as __storagecache
import pulumi_azure_native.storagediscovery as __storagediscovery
import pulumi_azure_native.storagemover as __storagemover
import pulumi_azure_native.storagepool as __storagepool
import pulumi_azure_native.storagesync as __storagesync
import pulumi_azure_native.streamanalytics as __streamanalytics
import pulumi_azure_native.subscription as __subscription
import pulumi_azure_native.synapse as __synapse
import pulumi_azure_native.syntex as __syntex
import pulumi_azure_native.testbase as __testbase
import pulumi_azure_native.timeseriesinsights as __timeseriesinsights
import pulumi_azure_native.trafficmanager as __trafficmanager
import pulumi_azure_native.verifiedid as __verifiedid
import pulumi_azure_native.videoindexer as __videoindexer
import pulumi_azure_native.virtualmachineimages as __virtualmachineimages
import pulumi_azure_native.vmwarecloudsimple as __vmwarecloudsimple
import pulumi_azure_native.voiceservices as __voiceservices
import pulumi_azure_native.web as __web
import pulumi_azure_native.webpubsub as __webpubsub
import pulumi_azure_native.weightsandbiases as __weightsandbiases
import pulumi_azure_native.widget as __widget
import pulumi_azure_native.windowsesu as __windowsesu
import pulumi_azure_native.windowsiot as __windowsiot
import pulumi_azure_native.workloads as __workloads
from . import _utilities
from .provider import *

if typing.TYPE_CHECKING:
    aad = __aad
    aadiam = __aadiam
    addons = __addons
    advisor = __advisor
    agfoodplatform = __agfoodplatform
    agricultureplatform = __agricultureplatform
    alertsmanagement = __alertsmanagement
    analysisservices = __analysisservices
    apicenter = __apicenter
    apimanagement = __apimanagement
    app = __app
    appcomplianceautomation = __appcomplianceautomation
    appconfiguration = __appconfiguration
    applicationinsights = __applicationinsights
    appplatform = __appplatform
    attestation = __attestation
    authorization = __authorization
    automanage = __automanage
    automation = __automation
    avs = __avs
    awsconnector = __awsconnector
    azureactivedirectory = __azureactivedirectory
    azurearcdata = __azurearcdata
    azuredata = __azuredata
    azuredatatransfer = __azuredatatransfer
    azurefleet = __azurefleet
    azurelargeinstance = __azurelargeinstance
    azureplaywrightservice = __azureplaywrightservice
    azuresphere = __azuresphere
    azurestack = __azurestack
    azurestackhci = __azurestackhci
    baremetalinfrastructure = __baremetalinfrastructure
    batch = __batch
    billing = __billing
    billingbenefits = __billingbenefits
    blueprint = __blueprint
    botservice = __botservice
    cdn = __cdn
    certificateregistration = __certificateregistration
    changeanalysis = __changeanalysis
    chaos = __chaos
    cloudhealth = __cloudhealth
    cloudngfw = __cloudngfw
    codesigning = __codesigning
    cognitiveservices = __cognitiveservices
    communication = __communication
    community = __community
    compute = __compute
    computebulkactions = __computebulkactions
    computelimit = __computelimit
    computeschedule = __computeschedule
    confidentialledger = __confidentialledger
    config = __config
    confluent = __confluent
    connectedcache = __connectedcache
    connectedvmwarevsphere = __connectedvmwarevsphere
    consumption = __consumption
    containerinstance = __containerinstance
    containerregistry = __containerregistry
    containerservice = __containerservice
    containerstorage = __containerstorage
    contoso = __contoso
    cosmosdb = __cosmosdb
    costmanagement = __costmanagement
    customerinsights = __customerinsights
    customproviders = __customproviders
    dashboard = __dashboard
    databasefleetmanager = __databasefleetmanager
    databasewatcher = __databasewatcher
    databox = __databox
    databoxedge = __databoxedge
    databricks = __databricks
    datacatalog = __datacatalog
    datadog = __datadog
    datafactory = __datafactory
    datalakeanalytics = __datalakeanalytics
    datalakestore = __datalakestore
    datamigration = __datamigration
    dataprotection = __dataprotection
    datareplication = __datareplication
    datashare = __datashare
    dbformariadb = __dbformariadb
    dbformysql = __dbformysql
    dbforpostgresql = __dbforpostgresql
    delegatednetwork = __delegatednetwork
    dependencymap = __dependencymap
    desktopvirtualization = __desktopvirtualization
    devcenter = __devcenter
    devhub = __devhub
    deviceprovisioningservices = __deviceprovisioningservices
    deviceregistry = __deviceregistry
    deviceupdate = __deviceupdate
    devopsinfrastructure = __devopsinfrastructure
    devspaces = __devspaces
    devtestlab = __devtestlab
    digitaltwins = __digitaltwins
    discovery = __discovery
    dns = __dns
    dnsresolver = __dnsresolver
    domainregistration = __domainregistration
    durabletask = __durabletask
    dynamics365fraudprotection = __dynamics365fraudprotection
    easm = __easm
    edge = __edge
    edgemarketplace = __edgemarketplace
    edgeorder = __edgeorder
    education = __education
    elastic = __elastic
    elasticsan = __elasticsan
    engagementfabric = __engagementfabric
    enterpriseknowledgegraph = __enterpriseknowledgegraph
    eventgrid = __eventgrid
    eventhub = __eventhub
    extendedlocation = __extendedlocation
    fabric = __fabric
    features = __features
    fileshares = __fileshares
    fluidrelay = __fluidrelay
    frontdoor = __frontdoor
    graphservices = __graphservices
    guestconfiguration = __guestconfiguration
    hardwaresecuritymodules = __hardwaresecuritymodules
    hdinsight = __hdinsight
    healthbot = __healthbot
    healthcareapis = __healthcareapis
    healthdataaiservices = __healthdataaiservices
    hybridcloud = __hybridcloud
    hybridcompute = __hybridcompute
    hybridconnectivity = __hybridconnectivity
    hybridcontainerservice = __hybridcontainerservice
    hybridnetwork = __hybridnetwork
    impact = __impact
    importexport = __importexport
    integrationspaces = __integrationspaces
    intune = __intune
    iotcentral = __iotcentral
    iotfirmwaredefense = __iotfirmwaredefense
    iothub = __iothub
    iotoperations = __iotoperations
    iotoperationsdataprocessor = __iotoperationsdataprocessor
    iotoperationsmq = __iotoperationsmq
    iotoperationsorchestrator = __iotoperationsorchestrator
    keyvault = __keyvault
    kubernetes = __kubernetes
    kubernetesconfiguration = __kubernetesconfiguration
    kubernetesruntime = __kubernetesruntime
    kusto = __kusto
    labservices = __labservices
    loadtestservice = __loadtestservice
    logic = __logic
    m365securityandcompliance = __m365securityandcompliance
    machinelearning = __machinelearning
    machinelearningservices = __machinelearningservices
    maintenance = __maintenance
    managedidentity = __managedidentity
    managednetwork = __managednetwork
    managednetworkfabric = __managednetworkfabric
    managedops = __managedops
    managedservices = __managedservices
    management = __management
    managementpartner = __managementpartner
    manufacturingplatform = __manufacturingplatform
    maps = __maps
    marketplace = __marketplace
    migrate = __migrate
    mission = __mission
    mongocluster = __mongocluster
    monitor = __monitor
    mysqldiscovery = __mysqldiscovery
    netapp = __netapp
    network = __network
    networkcloud = __networkcloud
    networkfunction = __networkfunction
    notificationhubs = __notificationhubs
    offazure = __offazure
    offazurespringboot = __offazurespringboot
    onlineexperimentation = __onlineexperimentation
    openenergyplatform = __openenergyplatform
    operationalinsights = __operationalinsights
    operationsmanagement = __operationsmanagement
    orbital = __orbital
    peering = __peering
    policyinsights = __policyinsights
    portal = __portal
    portalservices = __portalservices
    powerbi = __powerbi
    powerbidedicated = __powerbidedicated
    powerplatform = __powerplatform
    privatedns = __privatedns
    professionalservice = __professionalservice
    programmableconnectivity = __programmableconnectivity
    providerhub = __providerhub
    purview = __purview
    quantum = __quantum
    quota = __quota
    recommendationsservice = __recommendationsservice
    recoveryservices = __recoveryservices
    redhatopenshift = __redhatopenshift
    redis = __redis
    redisenterprise = __redisenterprise
    relationships = __relationships
    relay = __relay
    resourceconnector = __resourceconnector
    resourcegraph = __resourcegraph
    resourcehealth = __resourcehealth
    resources = __resources
    saas = __saas
    scheduler = __scheduler
    scom = __scom
    scvmm = __scvmm
    search = __search
    secretsynccontroller = __secretsynccontroller
    security = __security
    securityandcompliance = __securityandcompliance
    securityinsights = __securityinsights
    serialconsole = __serialconsole
    servicebus = __servicebus
    servicefabric = __servicefabric
    servicefabricmesh = __servicefabricmesh
    servicelinker = __servicelinker
    servicenetworking = __servicenetworking
    signalrservice = __signalrservice
    softwareplan = __softwareplan
    solutions = __solutions
    sovereign = __sovereign
    sql = __sql
    sqlvirtualmachine = __sqlvirtualmachine
    standbypool = __standbypool
    storage = __storage
    storageactions = __storageactions
    storagecache = __storagecache
    storagediscovery = __storagediscovery
    storagemover = __storagemover
    storagepool = __storagepool
    storagesync = __storagesync
    streamanalytics = __streamanalytics
    subscription = __subscription
    synapse = __synapse
    syntex = __syntex
    testbase = __testbase
    timeseriesinsights = __timeseriesinsights
    trafficmanager = __trafficmanager
    verifiedid = __verifiedid
    videoindexer = __videoindexer
    virtualmachineimages = __virtualmachineimages
    vmwarecloudsimple = __vmwarecloudsimple
    voiceservices = __voiceservices
    web = __web
    webpubsub = __webpubsub
    weightsandbiases = __weightsandbiases
    widget = __widget
    windowsesu = __windowsesu
    windowsiot = __windowsiot
    workloads = __workloads
else: ...
