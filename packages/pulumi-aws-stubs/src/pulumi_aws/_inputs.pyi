import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ProviderAssumeRoleArgs",
    "ProviderAssumeRoleArgsDict",
    "ProviderAssumeRoleWithWebIdentityArgs",
    "ProviderAssumeRoleWithWebIdentityArgsDict",
    "ProviderDefaultTagsArgs",
    "ProviderDefaultTagsArgsDict",
    "ProviderEndpointArgs",
    "ProviderEndpointArgsDict",
    "ProviderIgnoreTagsArgs",
    "ProviderIgnoreTagsArgsDict",
    "GetAvailabilityZoneFilterArgs",
    "GetAvailabilityZoneFilterArgsDict",
    "GetAvailabilityZonesFilterArgs",
    "GetAvailabilityZonesFilterArgsDict",
    "GetRegionsFilterArgs",
    "GetRegionsFilterArgsDict",
]

class ProviderAssumeRoleArgsDict(TypedDict):
    duration: NotRequired[pulumi.Input[_builtins.str]]
    external_id: NotRequired[pulumi.Input[_builtins.str]]
    policy: NotRequired[pulumi.Input[_builtins.str]]
    policy_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]
    session_name: NotRequired[pulumi.Input[_builtins.str]]
    source_identity: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    transitive_tag_keys: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ProviderAssumeRoleArgs:
    def __init__(
        __self__,
        *,
        duration: Optional[pulumi.Input[_builtins.str]] = ...,
        external_id: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        session_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_identity: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transitive_tag_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyArns")
    def policy_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @policy_arns.setter
    def policy_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionName")
    def session_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @session_name.setter
    def session_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceIdentity")
    def source_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_identity.setter
    def source_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitiveTagKeys")
    def transitive_tag_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @transitive_tag_keys.setter
    def transitive_tag_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ProviderAssumeRoleWithWebIdentityArgsDict(TypedDict):
    duration: NotRequired[pulumi.Input[_builtins.str]]
    policy: NotRequired[pulumi.Input[_builtins.str]]
    policy_arns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]
    session_name: NotRequired[pulumi.Input[_builtins.str]]
    web_identity_token: NotRequired[pulumi.Input[_builtins.str]]
    web_identity_token_file: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProviderAssumeRoleWithWebIdentityArgs:
    def __init__(
        __self__,
        *,
        duration: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        session_name: Optional[pulumi.Input[_builtins.str]] = ...,
        web_identity_token: Optional[pulumi.Input[_builtins.str]] = ...,
        web_identity_token_file: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyArns")
    def policy_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @policy_arns.setter
    def policy_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionName")
    def session_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @session_name.setter
    def session_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webIdentityToken")
    def web_identity_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_identity_token.setter
    def web_identity_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webIdentityTokenFile")
    def web_identity_token_file(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_identity_token_file.setter
    def web_identity_token_file(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProviderDefaultTagsArgsDict(TypedDict):
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ProviderDefaultTagsArgs:
    def __init__(
        __self__,
        *,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ProviderEndpointArgsDict(TypedDict):
    accessanalyzer: NotRequired[pulumi.Input[_builtins.str]]
    account: NotRequired[pulumi.Input[_builtins.str]]
    acm: NotRequired[pulumi.Input[_builtins.str]]
    acmpca: NotRequired[pulumi.Input[_builtins.str]]
    amg: NotRequired[pulumi.Input[_builtins.str]]
    amp: NotRequired[pulumi.Input[_builtins.str]]
    amplify: NotRequired[pulumi.Input[_builtins.str]]
    apigateway: NotRequired[pulumi.Input[_builtins.str]]
    apigatewayv2: NotRequired[pulumi.Input[_builtins.str]]
    appautoscaling: NotRequired[pulumi.Input[_builtins.str]]
    appconfig: NotRequired[pulumi.Input[_builtins.str]]
    appfabric: NotRequired[pulumi.Input[_builtins.str]]
    appflow: NotRequired[pulumi.Input[_builtins.str]]
    appintegrations: NotRequired[pulumi.Input[_builtins.str]]
    appintegrationsservice: NotRequired[pulumi.Input[_builtins.str]]
    applicationautoscaling: NotRequired[pulumi.Input[_builtins.str]]
    applicationinsights: NotRequired[pulumi.Input[_builtins.str]]
    applicationsignals: NotRequired[pulumi.Input[_builtins.str]]
    appmesh: NotRequired[pulumi.Input[_builtins.str]]
    appregistry: NotRequired[pulumi.Input[_builtins.str]]
    apprunner: NotRequired[pulumi.Input[_builtins.str]]
    appstream: NotRequired[pulumi.Input[_builtins.str]]
    appsync: NotRequired[pulumi.Input[_builtins.str]]
    arcregionswitch: NotRequired[pulumi.Input[_builtins.str]]
    arczonalshift: NotRequired[pulumi.Input[_builtins.str]]
    athena: NotRequired[pulumi.Input[_builtins.str]]
    auditmanager: NotRequired[pulumi.Input[_builtins.str]]
    autoscaling: NotRequired[pulumi.Input[_builtins.str]]
    autoscalingplans: NotRequired[pulumi.Input[_builtins.str]]
    backup: NotRequired[pulumi.Input[_builtins.str]]
    batch: NotRequired[pulumi.Input[_builtins.str]]
    bcmdataexports: NotRequired[pulumi.Input[_builtins.str]]
    beanstalk: NotRequired[pulumi.Input[_builtins.str]]
    bedrock: NotRequired[pulumi.Input[_builtins.str]]
    bedrockagent: NotRequired[pulumi.Input[_builtins.str]]
    bedrockagentcore: NotRequired[pulumi.Input[_builtins.str]]
    billing: NotRequired[pulumi.Input[_builtins.str]]
    budgets: NotRequired[pulumi.Input[_builtins.str]]
    ce: NotRequired[pulumi.Input[_builtins.str]]
    chatbot: NotRequired[pulumi.Input[_builtins.str]]
    chime: NotRequired[pulumi.Input[_builtins.str]]
    chimesdkmediapipelines: NotRequired[pulumi.Input[_builtins.str]]
    chimesdkvoice: NotRequired[pulumi.Input[_builtins.str]]
    cleanrooms: NotRequired[pulumi.Input[_builtins.str]]
    cloud9: NotRequired[pulumi.Input[_builtins.str]]
    cloudcontrol: NotRequired[pulumi.Input[_builtins.str]]
    cloudcontrolapi: NotRequired[pulumi.Input[_builtins.str]]
    cloudformation: NotRequired[pulumi.Input[_builtins.str]]
    cloudfront: NotRequired[pulumi.Input[_builtins.str]]
    cloudfrontkeyvaluestore: NotRequired[pulumi.Input[_builtins.str]]
    cloudhsm: NotRequired[pulumi.Input[_builtins.str]]
    cloudhsmv2: NotRequired[pulumi.Input[_builtins.str]]
    cloudsearch: NotRequired[pulumi.Input[_builtins.str]]
    cloudtrail: NotRequired[pulumi.Input[_builtins.str]]
    cloudwatch: NotRequired[pulumi.Input[_builtins.str]]
    cloudwatchevents: NotRequired[pulumi.Input[_builtins.str]]
    cloudwatchevidently: NotRequired[pulumi.Input[_builtins.str]]
    cloudwatchlog: NotRequired[pulumi.Input[_builtins.str]]
    cloudwatchlogs: NotRequired[pulumi.Input[_builtins.str]]
    cloudwatchobservabilityaccessmanager: NotRequired[pulumi.Input[_builtins.str]]
    cloudwatchrum: NotRequired[pulumi.Input[_builtins.str]]
    codeartifact: NotRequired[pulumi.Input[_builtins.str]]
    codebuild: NotRequired[pulumi.Input[_builtins.str]]
    codecatalyst: NotRequired[pulumi.Input[_builtins.str]]
    codecommit: NotRequired[pulumi.Input[_builtins.str]]
    codeconnections: NotRequired[pulumi.Input[_builtins.str]]
    codedeploy: NotRequired[pulumi.Input[_builtins.str]]
    codeguruprofiler: NotRequired[pulumi.Input[_builtins.str]]
    codegurureviewer: NotRequired[pulumi.Input[_builtins.str]]
    codepipeline: NotRequired[pulumi.Input[_builtins.str]]
    codestarconnections: NotRequired[pulumi.Input[_builtins.str]]
    codestarnotifications: NotRequired[pulumi.Input[_builtins.str]]
    cognitoidentity: NotRequired[pulumi.Input[_builtins.str]]
    cognitoidentityprovider: NotRequired[pulumi.Input[_builtins.str]]
    cognitoidp: NotRequired[pulumi.Input[_builtins.str]]
    comprehend: NotRequired[pulumi.Input[_builtins.str]]
    computeoptimizer: NotRequired[pulumi.Input[_builtins.str]]
    config: NotRequired[pulumi.Input[_builtins.str]]
    configservice: NotRequired[pulumi.Input[_builtins.str]]
    connect: NotRequired[pulumi.Input[_builtins.str]]
    connectcases: NotRequired[pulumi.Input[_builtins.str]]
    controltower: NotRequired[pulumi.Input[_builtins.str]]
    costandusagereportservice: NotRequired[pulumi.Input[_builtins.str]]
    costexplorer: NotRequired[pulumi.Input[_builtins.str]]
    costoptimizationhub: NotRequired[pulumi.Input[_builtins.str]]
    cur: NotRequired[pulumi.Input[_builtins.str]]
    customerprofiles: NotRequired[pulumi.Input[_builtins.str]]
    databasemigration: NotRequired[pulumi.Input[_builtins.str]]
    databasemigrationservice: NotRequired[pulumi.Input[_builtins.str]]
    databrew: NotRequired[pulumi.Input[_builtins.str]]
    dataexchange: NotRequired[pulumi.Input[_builtins.str]]
    datapipeline: NotRequired[pulumi.Input[_builtins.str]]
    datasync: NotRequired[pulumi.Input[_builtins.str]]
    datazone: NotRequired[pulumi.Input[_builtins.str]]
    dax: NotRequired[pulumi.Input[_builtins.str]]
    deploy: NotRequired[pulumi.Input[_builtins.str]]
    detective: NotRequired[pulumi.Input[_builtins.str]]
    devicefarm: NotRequired[pulumi.Input[_builtins.str]]
    devopsguru: NotRequired[pulumi.Input[_builtins.str]]
    directconnect: NotRequired[pulumi.Input[_builtins.str]]
    directoryservice: NotRequired[pulumi.Input[_builtins.str]]
    dlm: NotRequired[pulumi.Input[_builtins.str]]
    dms: NotRequired[pulumi.Input[_builtins.str]]
    docdb: NotRequired[pulumi.Input[_builtins.str]]
    docdbelastic: NotRequired[pulumi.Input[_builtins.str]]
    drs: NotRequired[pulumi.Input[_builtins.str]]
    ds: NotRequired[pulumi.Input[_builtins.str]]
    dsql: NotRequired[pulumi.Input[_builtins.str]]
    dynamodb: NotRequired[pulumi.Input[_builtins.str]]
    ec2: NotRequired[pulumi.Input[_builtins.str]]
    ecr: NotRequired[pulumi.Input[_builtins.str]]
    ecrpublic: NotRequired[pulumi.Input[_builtins.str]]
    ecs: NotRequired[pulumi.Input[_builtins.str]]
    efs: NotRequired[pulumi.Input[_builtins.str]]
    eks: NotRequired[pulumi.Input[_builtins.str]]
    elasticache: NotRequired[pulumi.Input[_builtins.str]]
    elasticbeanstalk: NotRequired[pulumi.Input[_builtins.str]]
    elasticloadbalancing: NotRequired[pulumi.Input[_builtins.str]]
    elasticloadbalancingv2: NotRequired[pulumi.Input[_builtins.str]]
    elasticsearch: NotRequired[pulumi.Input[_builtins.str]]
    elasticsearchservice: NotRequired[pulumi.Input[_builtins.str]]
    elastictranscoder: NotRequired[pulumi.Input[_builtins.str]]
    elb: NotRequired[pulumi.Input[_builtins.str]]
    elbv2: NotRequired[pulumi.Input[_builtins.str]]
    emr: NotRequired[pulumi.Input[_builtins.str]]
    emrcontainers: NotRequired[pulumi.Input[_builtins.str]]
    emrserverless: NotRequired[pulumi.Input[_builtins.str]]
    es: NotRequired[pulumi.Input[_builtins.str]]
    eventbridge: NotRequired[pulumi.Input[_builtins.str]]
    events: NotRequired[pulumi.Input[_builtins.str]]
    evidently: NotRequired[pulumi.Input[_builtins.str]]
    evs: NotRequired[pulumi.Input[_builtins.str]]
    finspace: NotRequired[pulumi.Input[_builtins.str]]
    firehose: NotRequired[pulumi.Input[_builtins.str]]
    fis: NotRequired[pulumi.Input[_builtins.str]]
    fms: NotRequired[pulumi.Input[_builtins.str]]
    fsx: NotRequired[pulumi.Input[_builtins.str]]
    gamelift: NotRequired[pulumi.Input[_builtins.str]]
    glacier: NotRequired[pulumi.Input[_builtins.str]]
    globalaccelerator: NotRequired[pulumi.Input[_builtins.str]]
    glue: NotRequired[pulumi.Input[_builtins.str]]
    gluedatabrew: NotRequired[pulumi.Input[_builtins.str]]
    grafana: NotRequired[pulumi.Input[_builtins.str]]
    greengrass: NotRequired[pulumi.Input[_builtins.str]]
    groundstation: NotRequired[pulumi.Input[_builtins.str]]
    guardduty: NotRequired[pulumi.Input[_builtins.str]]
    healthlake: NotRequired[pulumi.Input[_builtins.str]]
    iam: NotRequired[pulumi.Input[_builtins.str]]
    identitystore: NotRequired[pulumi.Input[_builtins.str]]
    imagebuilder: NotRequired[pulumi.Input[_builtins.str]]
    inspector: NotRequired[pulumi.Input[_builtins.str]]
    inspector2: NotRequired[pulumi.Input[_builtins.str]]
    inspectorv2: NotRequired[pulumi.Input[_builtins.str]]
    internetmonitor: NotRequired[pulumi.Input[_builtins.str]]
    invoicing: NotRequired[pulumi.Input[_builtins.str]]
    iot: NotRequired[pulumi.Input[_builtins.str]]
    ivs: NotRequired[pulumi.Input[_builtins.str]]
    ivschat: NotRequired[pulumi.Input[_builtins.str]]
    kafka: NotRequired[pulumi.Input[_builtins.str]]
    kafkaconnect: NotRequired[pulumi.Input[_builtins.str]]
    kendra: NotRequired[pulumi.Input[_builtins.str]]
    keyspaces: NotRequired[pulumi.Input[_builtins.str]]
    kinesis: NotRequired[pulumi.Input[_builtins.str]]
    kinesisanalytics: NotRequired[pulumi.Input[_builtins.str]]
    kinesisanalyticsv2: NotRequired[pulumi.Input[_builtins.str]]
    kinesisvideo: NotRequired[pulumi.Input[_builtins.str]]
    kms: NotRequired[pulumi.Input[_builtins.str]]
    lakeformation: NotRequired[pulumi.Input[_builtins.str]]
    lambda_: NotRequired[pulumi.Input[_builtins.str]]
    launchwizard: NotRequired[pulumi.Input[_builtins.str]]
    lex: NotRequired[pulumi.Input[_builtins.str]]
    lexmodelbuilding: NotRequired[pulumi.Input[_builtins.str]]
    lexmodelbuildingservice: NotRequired[pulumi.Input[_builtins.str]]
    lexmodels: NotRequired[pulumi.Input[_builtins.str]]
    lexmodelsv2: NotRequired[pulumi.Input[_builtins.str]]
    lexv2models: NotRequired[pulumi.Input[_builtins.str]]
    licensemanager: NotRequired[pulumi.Input[_builtins.str]]
    lightsail: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    locationservice: NotRequired[pulumi.Input[_builtins.str]]
    logs: NotRequired[pulumi.Input[_builtins.str]]
    m2: NotRequired[pulumi.Input[_builtins.str]]
    macie2: NotRequired[pulumi.Input[_builtins.str]]
    managedgrafana: NotRequired[pulumi.Input[_builtins.str]]
    mediaconnect: NotRequired[pulumi.Input[_builtins.str]]
    mediaconvert: NotRequired[pulumi.Input[_builtins.str]]
    medialive: NotRequired[pulumi.Input[_builtins.str]]
    mediapackage: NotRequired[pulumi.Input[_builtins.str]]
    mediapackagev2: NotRequired[pulumi.Input[_builtins.str]]
    mediapackagevod: NotRequired[pulumi.Input[_builtins.str]]
    mediastore: NotRequired[pulumi.Input[_builtins.str]]
    memorydb: NotRequired[pulumi.Input[_builtins.str]]
    mgn: NotRequired[pulumi.Input[_builtins.str]]
    mpa: NotRequired[pulumi.Input[_builtins.str]]
    mq: NotRequired[pulumi.Input[_builtins.str]]
    msk: NotRequired[pulumi.Input[_builtins.str]]
    mwaa: NotRequired[pulumi.Input[_builtins.str]]
    mwaaserverless: NotRequired[pulumi.Input[_builtins.str]]
    neptune: NotRequired[pulumi.Input[_builtins.str]]
    neptunegraph: NotRequired[pulumi.Input[_builtins.str]]
    networkfirewall: NotRequired[pulumi.Input[_builtins.str]]
    networkflowmonitor: NotRequired[pulumi.Input[_builtins.str]]
    networkmanager: NotRequired[pulumi.Input[_builtins.str]]
    networkmonitor: NotRequired[pulumi.Input[_builtins.str]]
    notifications: NotRequired[pulumi.Input[_builtins.str]]
    notificationscontacts: NotRequired[pulumi.Input[_builtins.str]]
    oam: NotRequired[pulumi.Input[_builtins.str]]
    observabilityadmin: NotRequired[pulumi.Input[_builtins.str]]
    odb: NotRequired[pulumi.Input[_builtins.str]]
    opensearch: NotRequired[pulumi.Input[_builtins.str]]
    opensearchingestion: NotRequired[pulumi.Input[_builtins.str]]
    opensearchserverless: NotRequired[pulumi.Input[_builtins.str]]
    opensearchservice: NotRequired[pulumi.Input[_builtins.str]]
    organizations: NotRequired[pulumi.Input[_builtins.str]]
    osis: NotRequired[pulumi.Input[_builtins.str]]
    outposts: NotRequired[pulumi.Input[_builtins.str]]
    paymentcryptography: NotRequired[pulumi.Input[_builtins.str]]
    pcaconnectorad: NotRequired[pulumi.Input[_builtins.str]]
    pcs: NotRequired[pulumi.Input[_builtins.str]]
    pinpoint: NotRequired[pulumi.Input[_builtins.str]]
    pinpointsmsvoicev2: NotRequired[pulumi.Input[_builtins.str]]
    pipes: NotRequired[pulumi.Input[_builtins.str]]
    polly: NotRequired[pulumi.Input[_builtins.str]]
    pricing: NotRequired[pulumi.Input[_builtins.str]]
    prometheus: NotRequired[pulumi.Input[_builtins.str]]
    prometheusservice: NotRequired[pulumi.Input[_builtins.str]]
    qbusiness: NotRequired[pulumi.Input[_builtins.str]]
    qldb: NotRequired[pulumi.Input[_builtins.str]]
    quicksight: NotRequired[pulumi.Input[_builtins.str]]
    ram: NotRequired[pulumi.Input[_builtins.str]]
    rbin: NotRequired[pulumi.Input[_builtins.str]]
    rds: NotRequired[pulumi.Input[_builtins.str]]
    rdsdata: NotRequired[pulumi.Input[_builtins.str]]
    rdsdataservice: NotRequired[pulumi.Input[_builtins.str]]
    recyclebin: NotRequired[pulumi.Input[_builtins.str]]
    redshift: NotRequired[pulumi.Input[_builtins.str]]
    redshiftdata: NotRequired[pulumi.Input[_builtins.str]]
    redshiftdataapiservice: NotRequired[pulumi.Input[_builtins.str]]
    redshiftserverless: NotRequired[pulumi.Input[_builtins.str]]
    rekognition: NotRequired[pulumi.Input[_builtins.str]]
    resiliencehub: NotRequired[pulumi.Input[_builtins.str]]
    resourceexplorer2: NotRequired[pulumi.Input[_builtins.str]]
    resourcegroups: NotRequired[pulumi.Input[_builtins.str]]
    resourcegroupstagging: NotRequired[pulumi.Input[_builtins.str]]
    resourcegroupstaggingapi: NotRequired[pulumi.Input[_builtins.str]]
    rolesanywhere: NotRequired[pulumi.Input[_builtins.str]]
    route53: NotRequired[pulumi.Input[_builtins.str]]
    route53domains: NotRequired[pulumi.Input[_builtins.str]]
    route53profiles: NotRequired[pulumi.Input[_builtins.str]]
    route53recoverycontrolconfig: NotRequired[pulumi.Input[_builtins.str]]
    route53recoveryreadiness: NotRequired[pulumi.Input[_builtins.str]]
    route53resolver: NotRequired[pulumi.Input[_builtins.str]]
    rum: NotRequired[pulumi.Input[_builtins.str]]
    s3: NotRequired[pulumi.Input[_builtins.str]]
    s3api: NotRequired[pulumi.Input[_builtins.str]]
    s3control: NotRequired[pulumi.Input[_builtins.str]]
    s3outposts: NotRequired[pulumi.Input[_builtins.str]]
    s3tables: NotRequired[pulumi.Input[_builtins.str]]
    s3vectors: NotRequired[pulumi.Input[_builtins.str]]
    sagemaker: NotRequired[pulumi.Input[_builtins.str]]
    savingsplans: NotRequired[pulumi.Input[_builtins.str]]
    scheduler: NotRequired[pulumi.Input[_builtins.str]]
    schemas: NotRequired[pulumi.Input[_builtins.str]]
    secretsmanager: NotRequired[pulumi.Input[_builtins.str]]
    securityhub: NotRequired[pulumi.Input[_builtins.str]]
    securitylake: NotRequired[pulumi.Input[_builtins.str]]
    serverlessapplicationrepository: NotRequired[pulumi.Input[_builtins.str]]
    serverlessapprepo: NotRequired[pulumi.Input[_builtins.str]]
    serverlessrepo: NotRequired[pulumi.Input[_builtins.str]]
    servicecatalog: NotRequired[pulumi.Input[_builtins.str]]
    servicecatalogappregistry: NotRequired[pulumi.Input[_builtins.str]]
    servicediscovery: NotRequired[pulumi.Input[_builtins.str]]
    servicequotas: NotRequired[pulumi.Input[_builtins.str]]
    ses: NotRequired[pulumi.Input[_builtins.str]]
    sesv2: NotRequired[pulumi.Input[_builtins.str]]
    sfn: NotRequired[pulumi.Input[_builtins.str]]
    shield: NotRequired[pulumi.Input[_builtins.str]]
    signer: NotRequired[pulumi.Input[_builtins.str]]
    sns: NotRequired[pulumi.Input[_builtins.str]]
    sqs: NotRequired[pulumi.Input[_builtins.str]]
    ssm: NotRequired[pulumi.Input[_builtins.str]]
    ssmcontacts: NotRequired[pulumi.Input[_builtins.str]]
    ssmincidents: NotRequired[pulumi.Input[_builtins.str]]
    ssmquicksetup: NotRequired[pulumi.Input[_builtins.str]]
    ssmsap: NotRequired[pulumi.Input[_builtins.str]]
    sso: NotRequired[pulumi.Input[_builtins.str]]
    ssoadmin: NotRequired[pulumi.Input[_builtins.str]]
    stepfunctions: NotRequired[pulumi.Input[_builtins.str]]
    storagegateway: NotRequired[pulumi.Input[_builtins.str]]
    sts: NotRequired[pulumi.Input[_builtins.str]]
    swf: NotRequired[pulumi.Input[_builtins.str]]
    synthetics: NotRequired[pulumi.Input[_builtins.str]]
    taxsettings: NotRequired[pulumi.Input[_builtins.str]]
    timestreaminfluxdb: NotRequired[pulumi.Input[_builtins.str]]
    timestreamquery: NotRequired[pulumi.Input[_builtins.str]]
    timestreamwrite: NotRequired[pulumi.Input[_builtins.str]]
    transcribe: NotRequired[pulumi.Input[_builtins.str]]
    transcribeservice: NotRequired[pulumi.Input[_builtins.str]]
    transfer: NotRequired[pulumi.Input[_builtins.str]]
    verifiedpermissions: NotRequired[pulumi.Input[_builtins.str]]
    vpclattice: NotRequired[pulumi.Input[_builtins.str]]
    waf: NotRequired[pulumi.Input[_builtins.str]]
    wafregional: NotRequired[pulumi.Input[_builtins.str]]
    wafv2: NotRequired[pulumi.Input[_builtins.str]]
    wellarchitected: NotRequired[pulumi.Input[_builtins.str]]
    workmail: NotRequired[pulumi.Input[_builtins.str]]
    workspaces: NotRequired[pulumi.Input[_builtins.str]]
    workspacesweb: NotRequired[pulumi.Input[_builtins.str]]
    xray: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProviderEndpointArgs:
    def __init__(
        __self__,
        *,
        accessanalyzer: Optional[pulumi.Input[_builtins.str]] = ...,
        account: Optional[pulumi.Input[_builtins.str]] = ...,
        acm: Optional[pulumi.Input[_builtins.str]] = ...,
        acmpca: Optional[pulumi.Input[_builtins.str]] = ...,
        amg: Optional[pulumi.Input[_builtins.str]] = ...,
        amp: Optional[pulumi.Input[_builtins.str]] = ...,
        amplify: Optional[pulumi.Input[_builtins.str]] = ...,
        apigateway: Optional[pulumi.Input[_builtins.str]] = ...,
        apigatewayv2: Optional[pulumi.Input[_builtins.str]] = ...,
        appautoscaling: Optional[pulumi.Input[_builtins.str]] = ...,
        appconfig: Optional[pulumi.Input[_builtins.str]] = ...,
        appfabric: Optional[pulumi.Input[_builtins.str]] = ...,
        appflow: Optional[pulumi.Input[_builtins.str]] = ...,
        appintegrations: Optional[pulumi.Input[_builtins.str]] = ...,
        appintegrationsservice: Optional[pulumi.Input[_builtins.str]] = ...,
        applicationautoscaling: Optional[pulumi.Input[_builtins.str]] = ...,
        applicationinsights: Optional[pulumi.Input[_builtins.str]] = ...,
        applicationsignals: Optional[pulumi.Input[_builtins.str]] = ...,
        appmesh: Optional[pulumi.Input[_builtins.str]] = ...,
        appregistry: Optional[pulumi.Input[_builtins.str]] = ...,
        apprunner: Optional[pulumi.Input[_builtins.str]] = ...,
        appstream: Optional[pulumi.Input[_builtins.str]] = ...,
        appsync: Optional[pulumi.Input[_builtins.str]] = ...,
        arcregionswitch: Optional[pulumi.Input[_builtins.str]] = ...,
        arczonalshift: Optional[pulumi.Input[_builtins.str]] = ...,
        athena: Optional[pulumi.Input[_builtins.str]] = ...,
        auditmanager: Optional[pulumi.Input[_builtins.str]] = ...,
        autoscaling: Optional[pulumi.Input[_builtins.str]] = ...,
        autoscalingplans: Optional[pulumi.Input[_builtins.str]] = ...,
        backup: Optional[pulumi.Input[_builtins.str]] = ...,
        batch: Optional[pulumi.Input[_builtins.str]] = ...,
        bcmdataexports: Optional[pulumi.Input[_builtins.str]] = ...,
        beanstalk: Optional[pulumi.Input[_builtins.str]] = ...,
        bedrock: Optional[pulumi.Input[_builtins.str]] = ...,
        bedrockagent: Optional[pulumi.Input[_builtins.str]] = ...,
        bedrockagentcore: Optional[pulumi.Input[_builtins.str]] = ...,
        billing: Optional[pulumi.Input[_builtins.str]] = ...,
        budgets: Optional[pulumi.Input[_builtins.str]] = ...,
        ce: Optional[pulumi.Input[_builtins.str]] = ...,
        chatbot: Optional[pulumi.Input[_builtins.str]] = ...,
        chime: Optional[pulumi.Input[_builtins.str]] = ...,
        chimesdkmediapipelines: Optional[pulumi.Input[_builtins.str]] = ...,
        chimesdkvoice: Optional[pulumi.Input[_builtins.str]] = ...,
        cleanrooms: Optional[pulumi.Input[_builtins.str]] = ...,
        cloud9: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudcontrol: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudcontrolapi: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudformation: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudfront: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudfrontkeyvaluestore: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudhsm: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudhsmv2: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudsearch: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudtrail: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatch: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatchevents: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatchevidently: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatchlog: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatchlogs: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatchobservabilityaccessmanager: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        cloudwatchrum: Optional[pulumi.Input[_builtins.str]] = ...,
        codeartifact: Optional[pulumi.Input[_builtins.str]] = ...,
        codebuild: Optional[pulumi.Input[_builtins.str]] = ...,
        codecatalyst: Optional[pulumi.Input[_builtins.str]] = ...,
        codecommit: Optional[pulumi.Input[_builtins.str]] = ...,
        codeconnections: Optional[pulumi.Input[_builtins.str]] = ...,
        codedeploy: Optional[pulumi.Input[_builtins.str]] = ...,
        codeguruprofiler: Optional[pulumi.Input[_builtins.str]] = ...,
        codegurureviewer: Optional[pulumi.Input[_builtins.str]] = ...,
        codepipeline: Optional[pulumi.Input[_builtins.str]] = ...,
        codestarconnections: Optional[pulumi.Input[_builtins.str]] = ...,
        codestarnotifications: Optional[pulumi.Input[_builtins.str]] = ...,
        cognitoidentity: Optional[pulumi.Input[_builtins.str]] = ...,
        cognitoidentityprovider: Optional[pulumi.Input[_builtins.str]] = ...,
        cognitoidp: Optional[pulumi.Input[_builtins.str]] = ...,
        comprehend: Optional[pulumi.Input[_builtins.str]] = ...,
        computeoptimizer: Optional[pulumi.Input[_builtins.str]] = ...,
        config: Optional[pulumi.Input[_builtins.str]] = ...,
        configservice: Optional[pulumi.Input[_builtins.str]] = ...,
        connect: Optional[pulumi.Input[_builtins.str]] = ...,
        connectcases: Optional[pulumi.Input[_builtins.str]] = ...,
        controltower: Optional[pulumi.Input[_builtins.str]] = ...,
        costandusagereportservice: Optional[pulumi.Input[_builtins.str]] = ...,
        costexplorer: Optional[pulumi.Input[_builtins.str]] = ...,
        costoptimizationhub: Optional[pulumi.Input[_builtins.str]] = ...,
        cur: Optional[pulumi.Input[_builtins.str]] = ...,
        customerprofiles: Optional[pulumi.Input[_builtins.str]] = ...,
        databasemigration: Optional[pulumi.Input[_builtins.str]] = ...,
        databasemigrationservice: Optional[pulumi.Input[_builtins.str]] = ...,
        databrew: Optional[pulumi.Input[_builtins.str]] = ...,
        dataexchange: Optional[pulumi.Input[_builtins.str]] = ...,
        datapipeline: Optional[pulumi.Input[_builtins.str]] = ...,
        datasync: Optional[pulumi.Input[_builtins.str]] = ...,
        datazone: Optional[pulumi.Input[_builtins.str]] = ...,
        dax: Optional[pulumi.Input[_builtins.str]] = ...,
        deploy: Optional[pulumi.Input[_builtins.str]] = ...,
        detective: Optional[pulumi.Input[_builtins.str]] = ...,
        devicefarm: Optional[pulumi.Input[_builtins.str]] = ...,
        devopsguru: Optional[pulumi.Input[_builtins.str]] = ...,
        directconnect: Optional[pulumi.Input[_builtins.str]] = ...,
        directoryservice: Optional[pulumi.Input[_builtins.str]] = ...,
        dlm: Optional[pulumi.Input[_builtins.str]] = ...,
        dms: Optional[pulumi.Input[_builtins.str]] = ...,
        docdb: Optional[pulumi.Input[_builtins.str]] = ...,
        docdbelastic: Optional[pulumi.Input[_builtins.str]] = ...,
        drs: Optional[pulumi.Input[_builtins.str]] = ...,
        ds: Optional[pulumi.Input[_builtins.str]] = ...,
        dsql: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamodb: Optional[pulumi.Input[_builtins.str]] = ...,
        ec2: Optional[pulumi.Input[_builtins.str]] = ...,
        ecr: Optional[pulumi.Input[_builtins.str]] = ...,
        ecrpublic: Optional[pulumi.Input[_builtins.str]] = ...,
        ecs: Optional[pulumi.Input[_builtins.str]] = ...,
        efs: Optional[pulumi.Input[_builtins.str]] = ...,
        eks: Optional[pulumi.Input[_builtins.str]] = ...,
        elasticache: Optional[pulumi.Input[_builtins.str]] = ...,
        elasticbeanstalk: Optional[pulumi.Input[_builtins.str]] = ...,
        elasticloadbalancing: Optional[pulumi.Input[_builtins.str]] = ...,
        elasticloadbalancingv2: Optional[pulumi.Input[_builtins.str]] = ...,
        elasticsearch: Optional[pulumi.Input[_builtins.str]] = ...,
        elasticsearchservice: Optional[pulumi.Input[_builtins.str]] = ...,
        elastictranscoder: Optional[pulumi.Input[_builtins.str]] = ...,
        elb: Optional[pulumi.Input[_builtins.str]] = ...,
        elbv2: Optional[pulumi.Input[_builtins.str]] = ...,
        emr: Optional[pulumi.Input[_builtins.str]] = ...,
        emrcontainers: Optional[pulumi.Input[_builtins.str]] = ...,
        emrserverless: Optional[pulumi.Input[_builtins.str]] = ...,
        es: Optional[pulumi.Input[_builtins.str]] = ...,
        eventbridge: Optional[pulumi.Input[_builtins.str]] = ...,
        events: Optional[pulumi.Input[_builtins.str]] = ...,
        evidently: Optional[pulumi.Input[_builtins.str]] = ...,
        evs: Optional[pulumi.Input[_builtins.str]] = ...,
        finspace: Optional[pulumi.Input[_builtins.str]] = ...,
        firehose: Optional[pulumi.Input[_builtins.str]] = ...,
        fis: Optional[pulumi.Input[_builtins.str]] = ...,
        fms: Optional[pulumi.Input[_builtins.str]] = ...,
        fsx: Optional[pulumi.Input[_builtins.str]] = ...,
        gamelift: Optional[pulumi.Input[_builtins.str]] = ...,
        glacier: Optional[pulumi.Input[_builtins.str]] = ...,
        globalaccelerator: Optional[pulumi.Input[_builtins.str]] = ...,
        glue: Optional[pulumi.Input[_builtins.str]] = ...,
        gluedatabrew: Optional[pulumi.Input[_builtins.str]] = ...,
        grafana: Optional[pulumi.Input[_builtins.str]] = ...,
        greengrass: Optional[pulumi.Input[_builtins.str]] = ...,
        groundstation: Optional[pulumi.Input[_builtins.str]] = ...,
        guardduty: Optional[pulumi.Input[_builtins.str]] = ...,
        healthlake: Optional[pulumi.Input[_builtins.str]] = ...,
        iam: Optional[pulumi.Input[_builtins.str]] = ...,
        identitystore: Optional[pulumi.Input[_builtins.str]] = ...,
        imagebuilder: Optional[pulumi.Input[_builtins.str]] = ...,
        inspector: Optional[pulumi.Input[_builtins.str]] = ...,
        inspector2: Optional[pulumi.Input[_builtins.str]] = ...,
        inspectorv2: Optional[pulumi.Input[_builtins.str]] = ...,
        internetmonitor: Optional[pulumi.Input[_builtins.str]] = ...,
        invoicing: Optional[pulumi.Input[_builtins.str]] = ...,
        iot: Optional[pulumi.Input[_builtins.str]] = ...,
        ivs: Optional[pulumi.Input[_builtins.str]] = ...,
        ivschat: Optional[pulumi.Input[_builtins.str]] = ...,
        kafka: Optional[pulumi.Input[_builtins.str]] = ...,
        kafkaconnect: Optional[pulumi.Input[_builtins.str]] = ...,
        kendra: Optional[pulumi.Input[_builtins.str]] = ...,
        keyspaces: Optional[pulumi.Input[_builtins.str]] = ...,
        kinesis: Optional[pulumi.Input[_builtins.str]] = ...,
        kinesisanalytics: Optional[pulumi.Input[_builtins.str]] = ...,
        kinesisanalyticsv2: Optional[pulumi.Input[_builtins.str]] = ...,
        kinesisvideo: Optional[pulumi.Input[_builtins.str]] = ...,
        kms: Optional[pulumi.Input[_builtins.str]] = ...,
        lakeformation: Optional[pulumi.Input[_builtins.str]] = ...,
        lambda_: Optional[pulumi.Input[_builtins.str]] = ...,
        launchwizard: Optional[pulumi.Input[_builtins.str]] = ...,
        lex: Optional[pulumi.Input[_builtins.str]] = ...,
        lexmodelbuilding: Optional[pulumi.Input[_builtins.str]] = ...,
        lexmodelbuildingservice: Optional[pulumi.Input[_builtins.str]] = ...,
        lexmodels: Optional[pulumi.Input[_builtins.str]] = ...,
        lexmodelsv2: Optional[pulumi.Input[_builtins.str]] = ...,
        lexv2models: Optional[pulumi.Input[_builtins.str]] = ...,
        licensemanager: Optional[pulumi.Input[_builtins.str]] = ...,
        lightsail: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        locationservice: Optional[pulumi.Input[_builtins.str]] = ...,
        logs: Optional[pulumi.Input[_builtins.str]] = ...,
        m2: Optional[pulumi.Input[_builtins.str]] = ...,
        macie2: Optional[pulumi.Input[_builtins.str]] = ...,
        managedgrafana: Optional[pulumi.Input[_builtins.str]] = ...,
        mediaconnect: Optional[pulumi.Input[_builtins.str]] = ...,
        mediaconvert: Optional[pulumi.Input[_builtins.str]] = ...,
        medialive: Optional[pulumi.Input[_builtins.str]] = ...,
        mediapackage: Optional[pulumi.Input[_builtins.str]] = ...,
        mediapackagev2: Optional[pulumi.Input[_builtins.str]] = ...,
        mediapackagevod: Optional[pulumi.Input[_builtins.str]] = ...,
        mediastore: Optional[pulumi.Input[_builtins.str]] = ...,
        memorydb: Optional[pulumi.Input[_builtins.str]] = ...,
        mgn: Optional[pulumi.Input[_builtins.str]] = ...,
        mpa: Optional[pulumi.Input[_builtins.str]] = ...,
        mq: Optional[pulumi.Input[_builtins.str]] = ...,
        msk: Optional[pulumi.Input[_builtins.str]] = ...,
        mwaa: Optional[pulumi.Input[_builtins.str]] = ...,
        mwaaserverless: Optional[pulumi.Input[_builtins.str]] = ...,
        neptune: Optional[pulumi.Input[_builtins.str]] = ...,
        neptunegraph: Optional[pulumi.Input[_builtins.str]] = ...,
        networkfirewall: Optional[pulumi.Input[_builtins.str]] = ...,
        networkflowmonitor: Optional[pulumi.Input[_builtins.str]] = ...,
        networkmanager: Optional[pulumi.Input[_builtins.str]] = ...,
        networkmonitor: Optional[pulumi.Input[_builtins.str]] = ...,
        notifications: Optional[pulumi.Input[_builtins.str]] = ...,
        notificationscontacts: Optional[pulumi.Input[_builtins.str]] = ...,
        oam: Optional[pulumi.Input[_builtins.str]] = ...,
        observabilityadmin: Optional[pulumi.Input[_builtins.str]] = ...,
        odb: Optional[pulumi.Input[_builtins.str]] = ...,
        opensearch: Optional[pulumi.Input[_builtins.str]] = ...,
        opensearchingestion: Optional[pulumi.Input[_builtins.str]] = ...,
        opensearchserverless: Optional[pulumi.Input[_builtins.str]] = ...,
        opensearchservice: Optional[pulumi.Input[_builtins.str]] = ...,
        organizations: Optional[pulumi.Input[_builtins.str]] = ...,
        osis: Optional[pulumi.Input[_builtins.str]] = ...,
        outposts: Optional[pulumi.Input[_builtins.str]] = ...,
        paymentcryptography: Optional[pulumi.Input[_builtins.str]] = ...,
        pcaconnectorad: Optional[pulumi.Input[_builtins.str]] = ...,
        pcs: Optional[pulumi.Input[_builtins.str]] = ...,
        pinpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        pinpointsmsvoicev2: Optional[pulumi.Input[_builtins.str]] = ...,
        pipes: Optional[pulumi.Input[_builtins.str]] = ...,
        polly: Optional[pulumi.Input[_builtins.str]] = ...,
        pricing: Optional[pulumi.Input[_builtins.str]] = ...,
        prometheus: Optional[pulumi.Input[_builtins.str]] = ...,
        prometheusservice: Optional[pulumi.Input[_builtins.str]] = ...,
        qbusiness: Optional[pulumi.Input[_builtins.str]] = ...,
        qldb: Optional[pulumi.Input[_builtins.str]] = ...,
        quicksight: Optional[pulumi.Input[_builtins.str]] = ...,
        ram: Optional[pulumi.Input[_builtins.str]] = ...,
        rbin: Optional[pulumi.Input[_builtins.str]] = ...,
        rds: Optional[pulumi.Input[_builtins.str]] = ...,
        rdsdata: Optional[pulumi.Input[_builtins.str]] = ...,
        rdsdataservice: Optional[pulumi.Input[_builtins.str]] = ...,
        recyclebin: Optional[pulumi.Input[_builtins.str]] = ...,
        redshift: Optional[pulumi.Input[_builtins.str]] = ...,
        redshiftdata: Optional[pulumi.Input[_builtins.str]] = ...,
        redshiftdataapiservice: Optional[pulumi.Input[_builtins.str]] = ...,
        redshiftserverless: Optional[pulumi.Input[_builtins.str]] = ...,
        rekognition: Optional[pulumi.Input[_builtins.str]] = ...,
        resiliencehub: Optional[pulumi.Input[_builtins.str]] = ...,
        resourceexplorer2: Optional[pulumi.Input[_builtins.str]] = ...,
        resourcegroups: Optional[pulumi.Input[_builtins.str]] = ...,
        resourcegroupstagging: Optional[pulumi.Input[_builtins.str]] = ...,
        resourcegroupstaggingapi: Optional[pulumi.Input[_builtins.str]] = ...,
        rolesanywhere: Optional[pulumi.Input[_builtins.str]] = ...,
        route53: Optional[pulumi.Input[_builtins.str]] = ...,
        route53domains: Optional[pulumi.Input[_builtins.str]] = ...,
        route53profiles: Optional[pulumi.Input[_builtins.str]] = ...,
        route53recoverycontrolconfig: Optional[pulumi.Input[_builtins.str]] = ...,
        route53recoveryreadiness: Optional[pulumi.Input[_builtins.str]] = ...,
        route53resolver: Optional[pulumi.Input[_builtins.str]] = ...,
        rum: Optional[pulumi.Input[_builtins.str]] = ...,
        s3: Optional[pulumi.Input[_builtins.str]] = ...,
        s3api: Optional[pulumi.Input[_builtins.str]] = ...,
        s3control: Optional[pulumi.Input[_builtins.str]] = ...,
        s3outposts: Optional[pulumi.Input[_builtins.str]] = ...,
        s3tables: Optional[pulumi.Input[_builtins.str]] = ...,
        s3vectors: Optional[pulumi.Input[_builtins.str]] = ...,
        sagemaker: Optional[pulumi.Input[_builtins.str]] = ...,
        savingsplans: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduler: Optional[pulumi.Input[_builtins.str]] = ...,
        schemas: Optional[pulumi.Input[_builtins.str]] = ...,
        secretsmanager: Optional[pulumi.Input[_builtins.str]] = ...,
        securityhub: Optional[pulumi.Input[_builtins.str]] = ...,
        securitylake: Optional[pulumi.Input[_builtins.str]] = ...,
        serverlessapplicationrepository: Optional[pulumi.Input[_builtins.str]] = ...,
        serverlessapprepo: Optional[pulumi.Input[_builtins.str]] = ...,
        serverlessrepo: Optional[pulumi.Input[_builtins.str]] = ...,
        servicecatalog: Optional[pulumi.Input[_builtins.str]] = ...,
        servicecatalogappregistry: Optional[pulumi.Input[_builtins.str]] = ...,
        servicediscovery: Optional[pulumi.Input[_builtins.str]] = ...,
        servicequotas: Optional[pulumi.Input[_builtins.str]] = ...,
        ses: Optional[pulumi.Input[_builtins.str]] = ...,
        sesv2: Optional[pulumi.Input[_builtins.str]] = ...,
        sfn: Optional[pulumi.Input[_builtins.str]] = ...,
        shield: Optional[pulumi.Input[_builtins.str]] = ...,
        signer: Optional[pulumi.Input[_builtins.str]] = ...,
        sns: Optional[pulumi.Input[_builtins.str]] = ...,
        sqs: Optional[pulumi.Input[_builtins.str]] = ...,
        ssm: Optional[pulumi.Input[_builtins.str]] = ...,
        ssmcontacts: Optional[pulumi.Input[_builtins.str]] = ...,
        ssmincidents: Optional[pulumi.Input[_builtins.str]] = ...,
        ssmquicksetup: Optional[pulumi.Input[_builtins.str]] = ...,
        ssmsap: Optional[pulumi.Input[_builtins.str]] = ...,
        sso: Optional[pulumi.Input[_builtins.str]] = ...,
        ssoadmin: Optional[pulumi.Input[_builtins.str]] = ...,
        stepfunctions: Optional[pulumi.Input[_builtins.str]] = ...,
        storagegateway: Optional[pulumi.Input[_builtins.str]] = ...,
        sts: Optional[pulumi.Input[_builtins.str]] = ...,
        swf: Optional[pulumi.Input[_builtins.str]] = ...,
        synthetics: Optional[pulumi.Input[_builtins.str]] = ...,
        taxsettings: Optional[pulumi.Input[_builtins.str]] = ...,
        timestreaminfluxdb: Optional[pulumi.Input[_builtins.str]] = ...,
        timestreamquery: Optional[pulumi.Input[_builtins.str]] = ...,
        timestreamwrite: Optional[pulumi.Input[_builtins.str]] = ...,
        transcribe: Optional[pulumi.Input[_builtins.str]] = ...,
        transcribeservice: Optional[pulumi.Input[_builtins.str]] = ...,
        transfer: Optional[pulumi.Input[_builtins.str]] = ...,
        verifiedpermissions: Optional[pulumi.Input[_builtins.str]] = ...,
        vpclattice: Optional[pulumi.Input[_builtins.str]] = ...,
        waf: Optional[pulumi.Input[_builtins.str]] = ...,
        wafregional: Optional[pulumi.Input[_builtins.str]] = ...,
        wafv2: Optional[pulumi.Input[_builtins.str]] = ...,
        wellarchitected: Optional[pulumi.Input[_builtins.str]] = ...,
        workmail: Optional[pulumi.Input[_builtins.str]] = ...,
        workspaces: Optional[pulumi.Input[_builtins.str]] = ...,
        workspacesweb: Optional[pulumi.Input[_builtins.str]] = ...,
        xray: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accessanalyzer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accessanalyzer.setter
    def accessanalyzer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account.setter
    def account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def acm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @acm.setter
    def acm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def acmpca(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @acmpca.setter
    def acmpca(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def amg(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @amg.setter
    def amg(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def amp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @amp.setter
    def amp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def amplify(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @amplify.setter
    def amplify(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def apigateway(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @apigateway.setter
    def apigateway(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def apigatewayv2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @apigatewayv2.setter
    def apigatewayv2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def appautoscaling(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @appautoscaling.setter
    def appautoscaling(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def appconfig(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @appconfig.setter
    def appconfig(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def appfabric(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @appfabric.setter
    def appfabric(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def appflow(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @appflow.setter
    def appflow(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def appintegrations(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @appintegrations.setter
    def appintegrations(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def appintegrationsservice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @appintegrationsservice.setter
    def appintegrationsservice(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def applicationautoscaling(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @applicationautoscaling.setter
    def applicationautoscaling(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def applicationinsights(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @applicationinsights.setter
    def applicationinsights(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def applicationsignals(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @applicationsignals.setter
    def applicationsignals(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def appmesh(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @appmesh.setter
    def appmesh(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def appregistry(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @appregistry.setter
    def appregistry(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def apprunner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @apprunner.setter
    def apprunner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def appstream(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @appstream.setter
    def appstream(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def appsync(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @appsync.setter
    def appsync(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arcregionswitch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arcregionswitch.setter
    def arcregionswitch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arczonalshift(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arczonalshift.setter
    def arczonalshift(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def athena(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @athena.setter
    def athena(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def auditmanager(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auditmanager.setter
    def auditmanager(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def autoscaling(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @autoscaling.setter
    def autoscaling(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def autoscalingplans(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @autoscalingplans.setter
    def autoscalingplans(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def backup(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup.setter
    def backup(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def batch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @batch.setter
    def batch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def bcmdataexports(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bcmdataexports.setter
    def bcmdataexports(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def beanstalk(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @beanstalk.setter
    def beanstalk(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def bedrock(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bedrock.setter
    def bedrock(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def bedrockagent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bedrockagent.setter
    def bedrockagent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def bedrockagentcore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bedrockagentcore.setter
    def bedrockagentcore(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def billing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @billing.setter
    def billing(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def budgets(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @budgets.setter
    def budgets(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ce(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ce.setter
    def ce(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def chatbot(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @chatbot.setter
    def chatbot(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def chime(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @chime.setter
    def chime(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def chimesdkmediapipelines(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @chimesdkmediapipelines.setter
    def chimesdkmediapipelines(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def chimesdkvoice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @chimesdkvoice.setter
    def chimesdkvoice(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cleanrooms(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cleanrooms.setter
    def cleanrooms(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cloud9(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud9.setter
    def cloud9(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudcontrol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudcontrol.setter
    def cloudcontrol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudcontrolapi(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudcontrolapi.setter
    def cloudcontrolapi(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudformation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudformation.setter
    def cloudformation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudfront(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudfront.setter
    def cloudfront(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudfrontkeyvaluestore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudfrontkeyvaluestore.setter
    def cloudfrontkeyvaluestore(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudhsm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudhsm.setter
    def cloudhsm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudhsmv2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudhsmv2.setter
    def cloudhsmv2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudsearch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudsearch.setter
    def cloudsearch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudtrail(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudtrail.setter
    def cloudtrail(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudwatch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatch.setter
    def cloudwatch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudwatchevents(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatchevents.setter
    def cloudwatchevents(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudwatchevidently(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatchevidently.setter
    def cloudwatchevidently(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudwatchlog(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatchlog.setter
    def cloudwatchlog(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudwatchlogs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatchlogs.setter
    def cloudwatchlogs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudwatchobservabilityaccessmanager(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatchobservabilityaccessmanager.setter
    def cloudwatchobservabilityaccessmanager(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def cloudwatchrum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatchrum.setter
    def cloudwatchrum(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def codeartifact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @codeartifact.setter
    def codeartifact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def codebuild(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @codebuild.setter
    def codebuild(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def codecatalyst(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @codecatalyst.setter
    def codecatalyst(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def codecommit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @codecommit.setter
    def codecommit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def codeconnections(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @codeconnections.setter
    def codeconnections(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def codedeploy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @codedeploy.setter
    def codedeploy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def codeguruprofiler(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @codeguruprofiler.setter
    def codeguruprofiler(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def codegurureviewer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @codegurureviewer.setter
    def codegurureviewer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def codepipeline(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @codepipeline.setter
    def codepipeline(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def codestarconnections(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @codestarconnections.setter
    def codestarconnections(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def codestarnotifications(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @codestarnotifications.setter
    def codestarnotifications(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cognitoidentity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cognitoidentity.setter
    def cognitoidentity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cognitoidentityprovider(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cognitoidentityprovider.setter
    def cognitoidentityprovider(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cognitoidp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cognitoidp.setter
    def cognitoidp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def comprehend(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comprehend.setter
    def comprehend(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def computeoptimizer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @computeoptimizer.setter
    def computeoptimizer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @config.setter
    def config(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def configservice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configservice.setter
    def configservice(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def connect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connect.setter
    def connect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def connectcases(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connectcases.setter
    def connectcases(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def controltower(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @controltower.setter
    def controltower(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def costandusagereportservice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @costandusagereportservice.setter
    def costandusagereportservice(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def costexplorer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @costexplorer.setter
    def costexplorer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def costoptimizationhub(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @costoptimizationhub.setter
    def costoptimizationhub(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cur(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cur.setter
    def cur(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def customerprofiles(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customerprofiles.setter
    def customerprofiles(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def databasemigration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @databasemigration.setter
    def databasemigration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def databasemigrationservice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @databasemigrationservice.setter
    def databasemigrationservice(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def databrew(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @databrew.setter
    def databrew(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dataexchange(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataexchange.setter
    def dataexchange(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def datapipeline(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @datapipeline.setter
    def datapipeline(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def datasync(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @datasync.setter
    def datasync(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def datazone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @datazone.setter
    def datazone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dax(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dax.setter
    def dax(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def deploy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deploy.setter
    def deploy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def detective(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @detective.setter
    def detective(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def devicefarm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @devicefarm.setter
    def devicefarm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def devopsguru(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @devopsguru.setter
    def devopsguru(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def directconnect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directconnect.setter
    def directconnect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def directoryservice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directoryservice.setter
    def directoryservice(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dlm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dlm.setter
    def dlm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dms(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dms.setter
    def dms(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def docdb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @docdb.setter
    def docdb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def docdbelastic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @docdbelastic.setter
    def docdbelastic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def drs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @drs.setter
    def drs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ds(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ds.setter
    def ds(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dsql(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dsql.setter
    def dsql(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dynamodb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dynamodb.setter
    def dynamodb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ec2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ec2.setter
    def ec2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ecr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ecr.setter
    def ecr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ecrpublic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ecrpublic.setter
    def ecrpublic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ecs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ecs.setter
    def ecs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def efs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @efs.setter
    def efs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def eks(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @eks.setter
    def eks(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def elasticache(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @elasticache.setter
    def elasticache(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def elasticbeanstalk(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @elasticbeanstalk.setter
    def elasticbeanstalk(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def elasticloadbalancing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @elasticloadbalancing.setter
    def elasticloadbalancing(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def elasticloadbalancingv2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @elasticloadbalancingv2.setter
    def elasticloadbalancingv2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def elasticsearch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @elasticsearch.setter
    def elasticsearch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def elasticsearchservice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @elasticsearchservice.setter
    def elasticsearchservice(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def elastictranscoder(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @elastictranscoder.setter
    def elastictranscoder(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def elb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @elb.setter
    def elb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def elbv2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @elbv2.setter
    def elbv2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def emr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @emr.setter
    def emr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def emrcontainers(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @emrcontainers.setter
    def emrcontainers(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def emrserverless(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @emrserverless.setter
    def emrserverless(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def es(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @es.setter
    def es(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def eventbridge(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @eventbridge.setter
    def eventbridge(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @events.setter
    def events(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def evidently(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @evidently.setter
    def evidently(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def evs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @evs.setter
    def evs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def finspace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @finspace.setter
    def finspace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def firehose(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @firehose.setter
    def firehose(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def fis(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fis.setter
    def fis(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def fms(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fms.setter
    def fms(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def fsx(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fsx.setter
    def fsx(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def gamelift(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gamelift.setter
    def gamelift(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def glacier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @glacier.setter
    def glacier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def globalaccelerator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @globalaccelerator.setter
    def globalaccelerator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def glue(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @glue.setter
    def glue(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def gluedatabrew(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gluedatabrew.setter
    def gluedatabrew(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def grafana(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grafana.setter
    def grafana(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def greengrass(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @greengrass.setter
    def greengrass(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def groundstation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @groundstation.setter
    def groundstation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def guardduty(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @guardduty.setter
    def guardduty(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def healthlake(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @healthlake.setter
    def healthlake(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def iam(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iam.setter
    def iam(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identitystore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identitystore.setter
    def identitystore(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def imagebuilder(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @imagebuilder.setter
    def imagebuilder(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def inspector(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inspector.setter
    def inspector(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def inspector2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inspector2.setter
    def inspector2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def inspectorv2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inspectorv2.setter
    def inspectorv2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def internetmonitor(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @internetmonitor.setter
    def internetmonitor(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def invoicing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @invoicing.setter
    def invoicing(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def iot(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iot.setter
    def iot(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ivs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ivs.setter
    def ivs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ivschat(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ivschat.setter
    def ivschat(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kafka(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kafka.setter
    def kafka(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kafkaconnect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kafkaconnect.setter
    def kafkaconnect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kendra(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kendra.setter
    def kendra(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def keyspaces(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @keyspaces.setter
    def keyspaces(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kinesis(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kinesis.setter
    def kinesis(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kinesisanalytics(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kinesisanalytics.setter
    def kinesisanalytics(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kinesisanalyticsv2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kinesisanalyticsv2.setter
    def kinesisanalyticsv2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kinesisvideo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kinesisvideo.setter
    def kinesisvideo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kms(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms.setter
    def kms(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lakeformation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lakeformation.setter
    def lakeformation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lambda_.setter
    def lambda_(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def launchwizard(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @launchwizard.setter
    def launchwizard(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lex.setter
    def lex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lexmodelbuilding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lexmodelbuilding.setter
    def lexmodelbuilding(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lexmodelbuildingservice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lexmodelbuildingservice.setter
    def lexmodelbuildingservice(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lexmodels(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lexmodels.setter
    def lexmodels(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lexmodelsv2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lexmodelsv2.setter
    def lexmodelsv2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lexv2models(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lexv2models.setter
    def lexv2models(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def licensemanager(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @licensemanager.setter
    def licensemanager(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lightsail(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lightsail.setter
    def lightsail(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def locationservice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @locationservice.setter
    def locationservice(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def logs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logs.setter
    def logs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def m2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @m2.setter
    def m2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def macie2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @macie2.setter
    def macie2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def managedgrafana(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managedgrafana.setter
    def managedgrafana(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mediaconnect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mediaconnect.setter
    def mediaconnect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mediaconvert(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mediaconvert.setter
    def mediaconvert(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def medialive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @medialive.setter
    def medialive(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mediapackage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mediapackage.setter
    def mediapackage(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mediapackagev2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mediapackagev2.setter
    def mediapackagev2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mediapackagevod(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mediapackagevod.setter
    def mediapackagevod(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mediastore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mediastore.setter
    def mediastore(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def memorydb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memorydb.setter
    def memorydb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mgn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mgn.setter
    def mgn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mpa(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mpa.setter
    def mpa(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mq(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mq.setter
    def mq(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def msk(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @msk.setter
    def msk(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mwaa(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mwaa.setter
    def mwaa(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mwaaserverless(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mwaaserverless.setter
    def mwaaserverless(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def neptune(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @neptune.setter
    def neptune(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def neptunegraph(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @neptunegraph.setter
    def neptunegraph(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def networkfirewall(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @networkfirewall.setter
    def networkfirewall(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def networkflowmonitor(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @networkflowmonitor.setter
    def networkflowmonitor(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def networkmanager(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @networkmanager.setter
    def networkmanager(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def networkmonitor(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @networkmonitor.setter
    def networkmonitor(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def notifications(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notifications.setter
    def notifications(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def notificationscontacts(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notificationscontacts.setter
    def notificationscontacts(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def oam(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oam.setter
    def oam(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def observabilityadmin(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @observabilityadmin.setter
    def observabilityadmin(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def odb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @odb.setter
    def odb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def opensearch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @opensearch.setter
    def opensearch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def opensearchingestion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @opensearchingestion.setter
    def opensearchingestion(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def opensearchserverless(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @opensearchserverless.setter
    def opensearchserverless(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def opensearchservice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @opensearchservice.setter
    def opensearchservice(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def organizations(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organizations.setter
    def organizations(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def osis(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @osis.setter
    def osis(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def outposts(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @outposts.setter
    def outposts(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def paymentcryptography(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @paymentcryptography.setter
    def paymentcryptography(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def pcaconnectorad(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pcaconnectorad.setter
    def pcaconnectorad(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def pcs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pcs.setter
    def pcs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def pinpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pinpoint.setter
    def pinpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def pinpointsmsvoicev2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pinpointsmsvoicev2.setter
    def pinpointsmsvoicev2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def pipes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pipes.setter
    def pipes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def polly(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @polly.setter
    def polly(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def pricing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pricing.setter
    def pricing(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def prometheus(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prometheus.setter
    def prometheus(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def prometheusservice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prometheusservice.setter
    def prometheusservice(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def qbusiness(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @qbusiness.setter
    def qbusiness(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def qldb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @qldb.setter
    def qldb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def quicksight(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quicksight.setter
    def quicksight(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ram(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ram.setter
    def ram(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rbin(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rbin.setter
    def rbin(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rds(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rds.setter
    def rds(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rdsdata(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rdsdata.setter
    def rdsdata(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rdsdataservice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rdsdataservice.setter
    def rdsdataservice(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def recyclebin(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recyclebin.setter
    def recyclebin(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def redshift(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redshift.setter
    def redshift(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def redshiftdata(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redshiftdata.setter
    def redshiftdata(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def redshiftdataapiservice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redshiftdataapiservice.setter
    def redshiftdataapiservice(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def redshiftserverless(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redshiftserverless.setter
    def redshiftserverless(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rekognition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rekognition.setter
    def rekognition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resiliencehub(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resiliencehub.setter
    def resiliencehub(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resourceexplorer2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resourceexplorer2.setter
    def resourceexplorer2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resourcegroups(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resourcegroups.setter
    def resourcegroups(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resourcegroupstagging(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resourcegroupstagging.setter
    def resourcegroupstagging(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resourcegroupstaggingapi(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resourcegroupstaggingapi.setter
    def resourcegroupstaggingapi(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def rolesanywhere(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rolesanywhere.setter
    def rolesanywhere(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def route53(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @route53.setter
    def route53(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def route53domains(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @route53domains.setter
    def route53domains(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def route53profiles(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @route53profiles.setter
    def route53profiles(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def route53recoverycontrolconfig(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @route53recoverycontrolconfig.setter
    def route53recoverycontrolconfig(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def route53recoveryreadiness(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @route53recoveryreadiness.setter
    def route53recoveryreadiness(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def route53resolver(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @route53resolver.setter
    def route53resolver(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rum.setter
    def rum(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3.setter
    def s3(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def s3api(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3api.setter
    def s3api(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def s3control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3control.setter
    def s3control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def s3outposts(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3outposts.setter
    def s3outposts(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def s3tables(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3tables.setter
    def s3tables(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def s3vectors(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3vectors.setter
    def s3vectors(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sagemaker(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sagemaker.setter
    def sagemaker(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def savingsplans(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @savingsplans.setter
    def savingsplans(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scheduler(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scheduler.setter
    def scheduler(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schemas(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schemas.setter
    def schemas(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def secretsmanager(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secretsmanager.setter
    def secretsmanager(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def securityhub(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @securityhub.setter
    def securityhub(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def securitylake(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @securitylake.setter
    def securitylake(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def serverlessapplicationrepository(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @serverlessapplicationrepository.setter
    def serverlessapplicationrepository(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def serverlessapprepo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @serverlessapprepo.setter
    def serverlessapprepo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def serverlessrepo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @serverlessrepo.setter
    def serverlessrepo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def servicecatalog(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @servicecatalog.setter
    def servicecatalog(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def servicecatalogappregistry(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @servicecatalogappregistry.setter
    def servicecatalogappregistry(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def servicediscovery(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @servicediscovery.setter
    def servicediscovery(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def servicequotas(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @servicequotas.setter
    def servicequotas(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ses(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ses.setter
    def ses(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sesv2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sesv2.setter
    def sesv2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sfn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sfn.setter
    def sfn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def shield(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shield.setter
    def shield(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def signer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @signer.setter
    def signer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sns(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sns.setter
    def sns(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sqs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sqs.setter
    def sqs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ssm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssm.setter
    def ssm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ssmcontacts(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssmcontacts.setter
    def ssmcontacts(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ssmincidents(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssmincidents.setter
    def ssmincidents(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ssmquicksetup(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssmquicksetup.setter
    def ssmquicksetup(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ssmsap(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssmsap.setter
    def ssmsap(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sso(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sso.setter
    def sso(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ssoadmin(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssoadmin.setter
    def ssoadmin(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def stepfunctions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stepfunctions.setter
    def stepfunctions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def storagegateway(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storagegateway.setter
    def storagegateway(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sts(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sts.setter
    def sts(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def swf(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @swf.setter
    def swf(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def synthetics(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @synthetics.setter
    def synthetics(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def taxsettings(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @taxsettings.setter
    def taxsettings(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timestreaminfluxdb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestreaminfluxdb.setter
    def timestreaminfluxdb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timestreamquery(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestreamquery.setter
    def timestreamquery(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timestreamwrite(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestreamwrite.setter
    def timestreamwrite(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def transcribe(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transcribe.setter
    def transcribe(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def transcribeservice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transcribeservice.setter
    def transcribeservice(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def transfer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transfer.setter
    def transfer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def verifiedpermissions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @verifiedpermissions.setter
    def verifiedpermissions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def vpclattice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpclattice.setter
    def vpclattice(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def waf(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @waf.setter
    def waf(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def wafregional(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wafregional.setter
    def wafregional(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def wafv2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wafv2.setter
    def wafv2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def wellarchitected(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wellarchitected.setter
    def wellarchitected(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def workmail(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workmail.setter
    def workmail(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def workspaces(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspaces.setter
    def workspaces(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def workspacesweb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspacesweb.setter
    def workspacesweb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def xray(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @xray.setter
    def xray(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProviderIgnoreTagsArgsDict(TypedDict):
    key_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ProviderIgnoreTagsArgs:
    def __init__(
        __self__,
        *,
        key_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyPrefixes")
    def key_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @key_prefixes.setter
    def key_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @keys.setter
    def keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class GetAvailabilityZoneFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetAvailabilityZoneFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

class GetAvailabilityZonesFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetAvailabilityZonesFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

class GetRegionsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetRegionsFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...
