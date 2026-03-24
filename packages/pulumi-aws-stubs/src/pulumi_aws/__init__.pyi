

import builtins as _builtins
import typing
import pulumi_aws.accessanalyzer as __accessanalyzer
import pulumi_aws.account as __account
import pulumi_aws.acm as __acm
import pulumi_aws.acmpca as __acmpca
import pulumi_aws.alb as __alb
import pulumi_aws.amp as __amp
import pulumi_aws.amplify as __amplify
import pulumi_aws.apigateway as __apigateway
import pulumi_aws.apigatewayv2 as __apigatewayv2
import pulumi_aws.appautoscaling as __appautoscaling
import pulumi_aws.appconfig as __appconfig
import pulumi_aws.appfabric as __appfabric
import pulumi_aws.appflow as __appflow
import pulumi_aws.appintegrations as __appintegrations
import pulumi_aws.applicationinsights as __applicationinsights
import pulumi_aws.applicationloadbalancing as __applicationloadbalancing
import pulumi_aws.appmesh as __appmesh
import pulumi_aws.apprunner as __apprunner
import pulumi_aws.appstream as __appstream
import pulumi_aws.appsync as __appsync
import pulumi_aws.arcregionswitch as __arcregionswitch
import pulumi_aws.athena as __athena
import pulumi_aws.auditmanager as __auditmanager
import pulumi_aws.autoscaling as __autoscaling
import pulumi_aws.autoscalingplans as __autoscalingplans
import pulumi_aws.backup as __backup
import pulumi_aws.batch as __batch
import pulumi_aws.bcmdata as __bcmdata
import pulumi_aws.bedrock as __bedrock
import pulumi_aws.bedrockfoundation as __bedrockfoundation
import pulumi_aws.bedrockmodel as __bedrockmodel
import pulumi_aws.billing as __billing
import pulumi_aws.budgets as __budgets
import pulumi_aws.cfg as __cfg
import pulumi_aws.chatbot as __chatbot
import pulumi_aws.chime as __chime
import pulumi_aws.chimesdkmediapipelines as __chimesdkmediapipelines
import pulumi_aws.cleanrooms as __cleanrooms
import pulumi_aws.cloud9 as __cloud9
import pulumi_aws.cloudcontrol as __cloudcontrol
import pulumi_aws.cloudformation as __cloudformation
import pulumi_aws.cloudfront as __cloudfront
import pulumi_aws.cloudhsmv2 as __cloudhsmv2
import pulumi_aws.cloudsearch as __cloudsearch
import pulumi_aws.cloudtrail as __cloudtrail
import pulumi_aws.cloudwatch as __cloudwatch
import pulumi_aws.codeartifact as __codeartifact
import pulumi_aws.codebuild as __codebuild
import pulumi_aws.codecatalyst as __codecatalyst
import pulumi_aws.codecommit as __codecommit
import pulumi_aws.codeconnections as __codeconnections
import pulumi_aws.codedeploy as __codedeploy
import pulumi_aws.codeguruprofiler as __codeguruprofiler
import pulumi_aws.codegurureviewer as __codegurureviewer
import pulumi_aws.codepipeline as __codepipeline
import pulumi_aws.codestarconnections as __codestarconnections
import pulumi_aws.codestarnotifications as __codestarnotifications
import pulumi_aws.cognito as __cognito
import pulumi_aws.comprehend as __comprehend
import pulumi_aws.computeoptimizer as __computeoptimizer
import pulumi_aws.config as __config
import pulumi_aws.connect as __connect
import pulumi_aws.controltower as __controltower
import pulumi_aws.costexplorer as __costexplorer
import pulumi_aws.costoptimizationhub as __costoptimizationhub
import pulumi_aws.cur as __cur
import pulumi_aws.customerprofiles as __customerprofiles
import pulumi_aws.dataexchange as __dataexchange
import pulumi_aws.datapipeline as __datapipeline
import pulumi_aws.datasync as __datasync
import pulumi_aws.datazone as __datazone
import pulumi_aws.dax as __dax
import pulumi_aws.detective as __detective
import pulumi_aws.devicefarm as __devicefarm
import pulumi_aws.devopsguru as __devopsguru
import pulumi_aws.directconnect as __directconnect
import pulumi_aws.directoryservice as __directoryservice
import pulumi_aws.dlm as __dlm
import pulumi_aws.dms as __dms
import pulumi_aws.docdb as __docdb
import pulumi_aws.drs as __drs
import pulumi_aws.dsql as __dsql
import pulumi_aws.dynamodb as __dynamodb
import pulumi_aws.ebs as __ebs
import pulumi_aws.ec2 as __ec2
import pulumi_aws.ec2clientvpn as __ec2clientvpn
import pulumi_aws.ec2transitgateway as __ec2transitgateway
import pulumi_aws.ecr as __ecr
import pulumi_aws.ecrpublic as __ecrpublic
import pulumi_aws.ecs as __ecs
import pulumi_aws.efs as __efs
import pulumi_aws.eks as __eks
import pulumi_aws.elasticache as __elasticache
import pulumi_aws.elasticbeanstalk as __elasticbeanstalk
import pulumi_aws.elasticsearch as __elasticsearch
import pulumi_aws.elastictranscoder as __elastictranscoder
import pulumi_aws.elb as __elb
import pulumi_aws.emr as __emr
import pulumi_aws.emrcontainers as __emrcontainers
import pulumi_aws.emrserverless as __emrserverless
import pulumi_aws.evidently as __evidently
import pulumi_aws.finspace as __finspace
import pulumi_aws.fis as __fis
import pulumi_aws.fms as __fms
import pulumi_aws.fsx as __fsx
import pulumi_aws.gamelift as __gamelift
import pulumi_aws.glacier as __glacier
import pulumi_aws.globalaccelerator as __globalaccelerator
import pulumi_aws.glue as __glue
import pulumi_aws.grafana as __grafana
import pulumi_aws.guardduty as __guardduty
import pulumi_aws.iam as __iam
import pulumi_aws.identitystore as __identitystore
import pulumi_aws.imagebuilder as __imagebuilder
import pulumi_aws.inspector as __inspector
import pulumi_aws.inspector2 as __inspector2
import pulumi_aws.invoicing as __invoicing
import pulumi_aws.iot as __iot
import pulumi_aws.ivs as __ivs
import pulumi_aws.ivschat as __ivschat
import pulumi_aws.kendra as __kendra
import pulumi_aws.keyspaces as __keyspaces
import pulumi_aws.kinesis as __kinesis
import pulumi_aws.kinesisanalyticsv2 as __kinesisanalyticsv2
import pulumi_aws.kms as __kms
import pulumi_aws.lakeformation as __lakeformation
import pulumi_aws.lambda_ as __lambda_
import pulumi_aws.lb as __lb
import pulumi_aws.lex as __lex
import pulumi_aws.licensemanager as __licensemanager
import pulumi_aws.lightsail as __lightsail
import pulumi_aws.location as __location
import pulumi_aws.m2 as __m2
import pulumi_aws.macie as __macie
import pulumi_aws.macie2 as __macie2
import pulumi_aws.mediaconvert as __mediaconvert
import pulumi_aws.medialive as __medialive
import pulumi_aws.mediapackage as __mediapackage
import pulumi_aws.mediapackagev2 as __mediapackagev2
import pulumi_aws.mediastore as __mediastore
import pulumi_aws.memorydb as __memorydb
import pulumi_aws.mq as __mq
import pulumi_aws.msk as __msk
import pulumi_aws.mskconnect as __mskconnect
import pulumi_aws.mwaa as __mwaa
import pulumi_aws.neptune as __neptune
import pulumi_aws.neptunegraph as __neptunegraph
import pulumi_aws.networkfirewall as __networkfirewall
import pulumi_aws.networkflowmonitor as __networkflowmonitor
import pulumi_aws.networkmanager as __networkmanager
import pulumi_aws.networkmonitor as __networkmonitor
import pulumi_aws.notifications as __notifications
import pulumi_aws.oam as __oam
import pulumi_aws.observabilityadmin as __observabilityadmin
import pulumi_aws.odb as __odb
import pulumi_aws.opensearch as __opensearch
import pulumi_aws.opensearchingest as __opensearchingest
import pulumi_aws.organizations as __organizations
import pulumi_aws.outposts as __outposts
import pulumi_aws.paymentcryptography as __paymentcryptography
import pulumi_aws.pinpoint as __pinpoint
import pulumi_aws.pipes as __pipes
import pulumi_aws.polly as __polly
import pulumi_aws.pricing as __pricing
import pulumi_aws.qbusiness as __qbusiness
import pulumi_aws.qldb as __qldb
import pulumi_aws.quicksight as __quicksight
import pulumi_aws.ram as __ram
import pulumi_aws.rbin as __rbin
import pulumi_aws.rds as __rds
import pulumi_aws.redshift as __redshift
import pulumi_aws.redshiftdata as __redshiftdata
import pulumi_aws.redshiftserverless as __redshiftserverless
import pulumi_aws.rekognition as __rekognition
import pulumi_aws.resiliencehub as __resiliencehub
import pulumi_aws.resourceexplorer as __resourceexplorer
import pulumi_aws.resourcegroups as __resourcegroups
import pulumi_aws.resourcegroupstaggingapi as __resourcegroupstaggingapi
import pulumi_aws.rolesanywhere as __rolesanywhere
import pulumi_aws.route53 as __route53
import pulumi_aws.route53domains as __route53domains
import pulumi_aws.route53recoverycontrol as __route53recoverycontrol
import pulumi_aws.route53recoveryreadiness as __route53recoveryreadiness
import pulumi_aws.rum as __rum
import pulumi_aws.s3 as __s3
import pulumi_aws.s3control as __s3control
import pulumi_aws.s3outposts as __s3outposts
import pulumi_aws.s3tables as __s3tables
import pulumi_aws.sagemaker as __sagemaker
import pulumi_aws.savingsplans as __savingsplans
import pulumi_aws.scheduler as __scheduler
import pulumi_aws.schemas as __schemas
import pulumi_aws.secretsmanager as __secretsmanager
import pulumi_aws.securityhub as __securityhub
import pulumi_aws.securitylake as __securitylake
import pulumi_aws.serverlessrepository as __serverlessrepository
import pulumi_aws.servicecatalog as __servicecatalog
import pulumi_aws.servicediscovery as __servicediscovery
import pulumi_aws.servicequotas as __servicequotas
import pulumi_aws.ses as __ses
import pulumi_aws.sesv2 as __sesv2
import pulumi_aws.sfn as __sfn
import pulumi_aws.shield as __shield
import pulumi_aws.signer as __signer
import pulumi_aws.sns as __sns
import pulumi_aws.sqs as __sqs
import pulumi_aws.ssm as __ssm
import pulumi_aws.ssmcontacts as __ssmcontacts
import pulumi_aws.ssmincidents as __ssmincidents
import pulumi_aws.ssoadmin as __ssoadmin
import pulumi_aws.storagegateway as __storagegateway
import pulumi_aws.swf as __swf
import pulumi_aws.synthetics as __synthetics
import pulumi_aws.timestreaminfluxdb as __timestreaminfluxdb
import pulumi_aws.timestreamquery as __timestreamquery
import pulumi_aws.timestreamwrite as __timestreamwrite
import pulumi_aws.transcribe as __transcribe
import pulumi_aws.transfer as __transfer
import pulumi_aws.verifiedaccess as __verifiedaccess
import pulumi_aws.verifiedpermissions as __verifiedpermissions
import pulumi_aws.vpc as __vpc
import pulumi_aws.vpclattice as __vpclattice
import pulumi_aws.vpn as __vpn
import pulumi_aws.waf as __waf
import pulumi_aws.wafregional as __wafregional
import pulumi_aws.wafv2 as __wafv2
import pulumi_aws.workspaces as __workspaces
import pulumi_aws.workspacesweb as __workspacesweb
import pulumi_aws.xray as __xray
from . import _utilities, outputs
from ._enums import *
from .get_arn import *
from .get_availability_zone import *
from .get_availability_zones import *
from .get_billing_service_account import *
from .get_caller_identity import *
from .get_default_tags import *
from .get_ip_ranges import *
from .get_partition import *
from .get_region import *
from .get_regions import *
from .get_service import *
from .get_service_principal import *
from .provider import *
from ._inputs import *

if typing.TYPE_CHECKING:
    accessanalyzer = __accessanalyzer
    account = __account
    acm = __acm
    acmpca = __acmpca
    alb = __alb
    amp = __amp
    amplify = __amplify
    apigateway = __apigateway
    apigatewayv2 = __apigatewayv2
    appautoscaling = __appautoscaling
    appconfig = __appconfig
    appfabric = __appfabric
    appflow = __appflow
    appintegrations = __appintegrations
    applicationinsights = __applicationinsights
    applicationloadbalancing = __applicationloadbalancing
    appmesh = __appmesh
    apprunner = __apprunner
    appstream = __appstream
    appsync = __appsync
    arcregionswitch = __arcregionswitch
    athena = __athena
    auditmanager = __auditmanager
    autoscaling = __autoscaling
    autoscalingplans = __autoscalingplans
    backup = __backup
    batch = __batch
    bcmdata = __bcmdata
    bedrock = __bedrock
    bedrockfoundation = __bedrockfoundation
    bedrockmodel = __bedrockmodel
    billing = __billing
    budgets = __budgets
    cfg = __cfg
    chatbot = __chatbot
    chime = __chime
    chimesdkmediapipelines = __chimesdkmediapipelines
    cleanrooms = __cleanrooms
    cloud9 = __cloud9
    cloudcontrol = __cloudcontrol
    cloudformation = __cloudformation
    cloudfront = __cloudfront
    cloudhsmv2 = __cloudhsmv2
    cloudsearch = __cloudsearch
    cloudtrail = __cloudtrail
    cloudwatch = __cloudwatch
    codeartifact = __codeartifact
    codebuild = __codebuild
    codecatalyst = __codecatalyst
    codecommit = __codecommit
    codeconnections = __codeconnections
    codedeploy = __codedeploy
    codeguruprofiler = __codeguruprofiler
    codegurureviewer = __codegurureviewer
    codepipeline = __codepipeline
    codestarconnections = __codestarconnections
    codestarnotifications = __codestarnotifications
    cognito = __cognito
    comprehend = __comprehend
    computeoptimizer = __computeoptimizer
    config = __config
    connect = __connect
    controltower = __controltower
    costexplorer = __costexplorer
    costoptimizationhub = __costoptimizationhub
    cur = __cur
    customerprofiles = __customerprofiles
    dataexchange = __dataexchange
    datapipeline = __datapipeline
    datasync = __datasync
    datazone = __datazone
    dax = __dax
    detective = __detective
    devicefarm = __devicefarm
    devopsguru = __devopsguru
    directconnect = __directconnect
    directoryservice = __directoryservice
    dlm = __dlm
    dms = __dms
    docdb = __docdb
    drs = __drs
    dsql = __dsql
    dynamodb = __dynamodb
    ebs = __ebs
    ec2 = __ec2
    ec2clientvpn = __ec2clientvpn
    ec2transitgateway = __ec2transitgateway
    ecr = __ecr
    ecrpublic = __ecrpublic
    ecs = __ecs
    efs = __efs
    eks = __eks
    elasticache = __elasticache
    elasticbeanstalk = __elasticbeanstalk
    elasticsearch = __elasticsearch
    elastictranscoder = __elastictranscoder
    elb = __elb
    emr = __emr
    emrcontainers = __emrcontainers
    emrserverless = __emrserverless
    evidently = __evidently
    finspace = __finspace
    fis = __fis
    fms = __fms
    fsx = __fsx
    gamelift = __gamelift
    glacier = __glacier
    globalaccelerator = __globalaccelerator
    glue = __glue
    grafana = __grafana
    guardduty = __guardduty
    iam = __iam
    identitystore = __identitystore
    imagebuilder = __imagebuilder
    inspector = __inspector
    inspector2 = __inspector2
    invoicing = __invoicing
    iot = __iot
    ivs = __ivs
    ivschat = __ivschat
    kendra = __kendra
    keyspaces = __keyspaces
    kinesis = __kinesis
    kinesisanalyticsv2 = __kinesisanalyticsv2
    kms = __kms
    lakeformation = __lakeformation
    lambda_ = __lambda_
    lb = __lb
    lex = __lex
    licensemanager = __licensemanager
    lightsail = __lightsail
    location = __location
    m2 = __m2
    macie = __macie
    macie2 = __macie2
    mediaconvert = __mediaconvert
    medialive = __medialive
    mediapackage = __mediapackage
    mediapackagev2 = __mediapackagev2
    mediastore = __mediastore
    memorydb = __memorydb
    mq = __mq
    msk = __msk
    mskconnect = __mskconnect
    mwaa = __mwaa
    neptune = __neptune
    neptunegraph = __neptunegraph
    networkfirewall = __networkfirewall
    networkflowmonitor = __networkflowmonitor
    networkmanager = __networkmanager
    networkmonitor = __networkmonitor
    notifications = __notifications
    oam = __oam
    observabilityadmin = __observabilityadmin
    odb = __odb
    opensearch = __opensearch
    opensearchingest = __opensearchingest
    organizations = __organizations
    outposts = __outposts
    paymentcryptography = __paymentcryptography
    pinpoint = __pinpoint
    pipes = __pipes
    polly = __polly
    pricing = __pricing
    qbusiness = __qbusiness
    qldb = __qldb
    quicksight = __quicksight
    ram = __ram
    rbin = __rbin
    rds = __rds
    redshift = __redshift
    redshiftdata = __redshiftdata
    redshiftserverless = __redshiftserverless
    rekognition = __rekognition
    resiliencehub = __resiliencehub
    resourceexplorer = __resourceexplorer
    resourcegroups = __resourcegroups
    resourcegroupstaggingapi = __resourcegroupstaggingapi
    rolesanywhere = __rolesanywhere
    route53 = __route53
    route53domains = __route53domains
    route53recoverycontrol = __route53recoverycontrol
    route53recoveryreadiness = __route53recoveryreadiness
    rum = __rum
    s3 = __s3
    s3control = __s3control
    s3outposts = __s3outposts
    s3tables = __s3tables
    sagemaker = __sagemaker
    savingsplans = __savingsplans
    scheduler = __scheduler
    schemas = __schemas
    secretsmanager = __secretsmanager
    securityhub = __securityhub
    securitylake = __securitylake
    serverlessrepository = __serverlessrepository
    servicecatalog = __servicecatalog
    servicediscovery = __servicediscovery
    servicequotas = __servicequotas
    ses = __ses
    sesv2 = __sesv2
    sfn = __sfn
    shield = __shield
    signer = __signer
    sns = __sns
    sqs = __sqs
    ssm = __ssm
    ssmcontacts = __ssmcontacts
    ssmincidents = __ssmincidents
    ssoadmin = __ssoadmin
    storagegateway = __storagegateway
    swf = __swf
    synthetics = __synthetics
    timestreaminfluxdb = __timestreaminfluxdb
    timestreamquery = __timestreamquery
    timestreamwrite = __timestreamwrite
    transcribe = __transcribe
    transfer = __transfer
    verifiedaccess = __verifiedaccess
    verifiedpermissions = __verifiedpermissions
    vpc = __vpc
    vpclattice = __vpclattice
    vpn = __vpn
    waf = __waf
    wafregional = __wafregional
    wafv2 = __wafv2
    workspaces = __workspaces
    workspacesweb = __workspacesweb
    xray = __xray
else:
    ...
