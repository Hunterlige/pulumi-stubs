import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AssumeRoleWithWebIdentity",
    "AssumeRoles",
    "DefaultTags",
    "Endpoints",
    "IgnoreTags",
]

@pulumi.output_type
class AssumeRoleWithWebIdentity(dict):
    def __init__(
        __self__,
        *,
        duration: Optional[_builtins.str] = ...,
        policy: Optional[_builtins.str] = ...,
        policy_arns: Optional[Sequence[_builtins.str]] = ...,
        role_arn: Optional[_builtins.str] = ...,
        session_name: Optional[_builtins.str] = ...,
        web_identity_token: Optional[_builtins.str] = ...,
        web_identity_token_file: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyArns")
    def policy_arns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionName")
    def session_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="webIdentityToken")
    def web_identity_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="webIdentityTokenFile")
    def web_identity_token_file(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AssumeRoles(dict):
    def __init__(
        __self__,
        *,
        duration: Optional[_builtins.str] = ...,
        external_id: Optional[_builtins.str] = ...,
        policy: Optional[_builtins.str] = ...,
        policy_arns: Optional[Sequence[_builtins.str]] = ...,
        role_arn: Optional[_builtins.str] = ...,
        session_name: Optional[_builtins.str] = ...,
        source_identity: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
        transitive_tag_keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyArns")
    def policy_arns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionName")
    def session_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceIdentity")
    def source_identity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transitiveTagKeys")
    def transitive_tag_keys(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DefaultTags(dict):
    def __init__(
        __self__, *, tags: Optional[Mapping[str, _builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class Endpoints(dict):
    def __init__(
        __self__,
        *,
        accessanalyzer: Optional[_builtins.str] = ...,
        account: Optional[_builtins.str] = ...,
        acm: Optional[_builtins.str] = ...,
        acmpca: Optional[_builtins.str] = ...,
        amg: Optional[_builtins.str] = ...,
        amp: Optional[_builtins.str] = ...,
        amplify: Optional[_builtins.str] = ...,
        apigateway: Optional[_builtins.str] = ...,
        apigatewayv2: Optional[_builtins.str] = ...,
        appautoscaling: Optional[_builtins.str] = ...,
        appconfig: Optional[_builtins.str] = ...,
        appfabric: Optional[_builtins.str] = ...,
        appflow: Optional[_builtins.str] = ...,
        appintegrations: Optional[_builtins.str] = ...,
        appintegrationsservice: Optional[_builtins.str] = ...,
        applicationautoscaling: Optional[_builtins.str] = ...,
        applicationinsights: Optional[_builtins.str] = ...,
        applicationsignals: Optional[_builtins.str] = ...,
        appmesh: Optional[_builtins.str] = ...,
        appregistry: Optional[_builtins.str] = ...,
        apprunner: Optional[_builtins.str] = ...,
        appstream: Optional[_builtins.str] = ...,
        appsync: Optional[_builtins.str] = ...,
        arcregionswitch: Optional[_builtins.str] = ...,
        arczonalshift: Optional[_builtins.str] = ...,
        athena: Optional[_builtins.str] = ...,
        auditmanager: Optional[_builtins.str] = ...,
        autoscaling: Optional[_builtins.str] = ...,
        autoscalingplans: Optional[_builtins.str] = ...,
        backup: Optional[_builtins.str] = ...,
        batch: Optional[_builtins.str] = ...,
        bcmdataexports: Optional[_builtins.str] = ...,
        beanstalk: Optional[_builtins.str] = ...,
        bedrock: Optional[_builtins.str] = ...,
        bedrockagent: Optional[_builtins.str] = ...,
        bedrockagentcore: Optional[_builtins.str] = ...,
        billing: Optional[_builtins.str] = ...,
        budgets: Optional[_builtins.str] = ...,
        ce: Optional[_builtins.str] = ...,
        chatbot: Optional[_builtins.str] = ...,
        chime: Optional[_builtins.str] = ...,
        chimesdkmediapipelines: Optional[_builtins.str] = ...,
        chimesdkvoice: Optional[_builtins.str] = ...,
        cleanrooms: Optional[_builtins.str] = ...,
        cloud9: Optional[_builtins.str] = ...,
        cloudcontrol: Optional[_builtins.str] = ...,
        cloudcontrolapi: Optional[_builtins.str] = ...,
        cloudformation: Optional[_builtins.str] = ...,
        cloudfront: Optional[_builtins.str] = ...,
        cloudfrontkeyvaluestore: Optional[_builtins.str] = ...,
        cloudhsm: Optional[_builtins.str] = ...,
        cloudhsmv2: Optional[_builtins.str] = ...,
        cloudsearch: Optional[_builtins.str] = ...,
        cloudtrail: Optional[_builtins.str] = ...,
        cloudwatch: Optional[_builtins.str] = ...,
        cloudwatchevents: Optional[_builtins.str] = ...,
        cloudwatchevidently: Optional[_builtins.str] = ...,
        cloudwatchlog: Optional[_builtins.str] = ...,
        cloudwatchlogs: Optional[_builtins.str] = ...,
        cloudwatchobservabilityaccessmanager: Optional[_builtins.str] = ...,
        cloudwatchrum: Optional[_builtins.str] = ...,
        codeartifact: Optional[_builtins.str] = ...,
        codebuild: Optional[_builtins.str] = ...,
        codecatalyst: Optional[_builtins.str] = ...,
        codecommit: Optional[_builtins.str] = ...,
        codeconnections: Optional[_builtins.str] = ...,
        codedeploy: Optional[_builtins.str] = ...,
        codeguruprofiler: Optional[_builtins.str] = ...,
        codegurureviewer: Optional[_builtins.str] = ...,
        codepipeline: Optional[_builtins.str] = ...,
        codestarconnections: Optional[_builtins.str] = ...,
        codestarnotifications: Optional[_builtins.str] = ...,
        cognitoidentity: Optional[_builtins.str] = ...,
        cognitoidentityprovider: Optional[_builtins.str] = ...,
        cognitoidp: Optional[_builtins.str] = ...,
        comprehend: Optional[_builtins.str] = ...,
        computeoptimizer: Optional[_builtins.str] = ...,
        config: Optional[_builtins.str] = ...,
        configservice: Optional[_builtins.str] = ...,
        connect: Optional[_builtins.str] = ...,
        connectcases: Optional[_builtins.str] = ...,
        controltower: Optional[_builtins.str] = ...,
        costandusagereportservice: Optional[_builtins.str] = ...,
        costexplorer: Optional[_builtins.str] = ...,
        costoptimizationhub: Optional[_builtins.str] = ...,
        cur: Optional[_builtins.str] = ...,
        customerprofiles: Optional[_builtins.str] = ...,
        databasemigration: Optional[_builtins.str] = ...,
        databasemigrationservice: Optional[_builtins.str] = ...,
        databrew: Optional[_builtins.str] = ...,
        dataexchange: Optional[_builtins.str] = ...,
        datapipeline: Optional[_builtins.str] = ...,
        datasync: Optional[_builtins.str] = ...,
        datazone: Optional[_builtins.str] = ...,
        dax: Optional[_builtins.str] = ...,
        deploy: Optional[_builtins.str] = ...,
        detective: Optional[_builtins.str] = ...,
        devicefarm: Optional[_builtins.str] = ...,
        devopsguru: Optional[_builtins.str] = ...,
        directconnect: Optional[_builtins.str] = ...,
        directoryservice: Optional[_builtins.str] = ...,
        dlm: Optional[_builtins.str] = ...,
        dms: Optional[_builtins.str] = ...,
        docdb: Optional[_builtins.str] = ...,
        docdbelastic: Optional[_builtins.str] = ...,
        drs: Optional[_builtins.str] = ...,
        ds: Optional[_builtins.str] = ...,
        dsql: Optional[_builtins.str] = ...,
        dynamodb: Optional[_builtins.str] = ...,
        ec2: Optional[_builtins.str] = ...,
        ecr: Optional[_builtins.str] = ...,
        ecrpublic: Optional[_builtins.str] = ...,
        ecs: Optional[_builtins.str] = ...,
        efs: Optional[_builtins.str] = ...,
        eks: Optional[_builtins.str] = ...,
        elasticache: Optional[_builtins.str] = ...,
        elasticbeanstalk: Optional[_builtins.str] = ...,
        elasticloadbalancing: Optional[_builtins.str] = ...,
        elasticloadbalancingv2: Optional[_builtins.str] = ...,
        elasticsearch: Optional[_builtins.str] = ...,
        elasticsearchservice: Optional[_builtins.str] = ...,
        elastictranscoder: Optional[_builtins.str] = ...,
        elb: Optional[_builtins.str] = ...,
        elbv2: Optional[_builtins.str] = ...,
        emr: Optional[_builtins.str] = ...,
        emrcontainers: Optional[_builtins.str] = ...,
        emrserverless: Optional[_builtins.str] = ...,
        es: Optional[_builtins.str] = ...,
        eventbridge: Optional[_builtins.str] = ...,
        events: Optional[_builtins.str] = ...,
        evidently: Optional[_builtins.str] = ...,
        evs: Optional[_builtins.str] = ...,
        finspace: Optional[_builtins.str] = ...,
        firehose: Optional[_builtins.str] = ...,
        fis: Optional[_builtins.str] = ...,
        fms: Optional[_builtins.str] = ...,
        fsx: Optional[_builtins.str] = ...,
        gamelift: Optional[_builtins.str] = ...,
        glacier: Optional[_builtins.str] = ...,
        globalaccelerator: Optional[_builtins.str] = ...,
        glue: Optional[_builtins.str] = ...,
        gluedatabrew: Optional[_builtins.str] = ...,
        grafana: Optional[_builtins.str] = ...,
        greengrass: Optional[_builtins.str] = ...,
        groundstation: Optional[_builtins.str] = ...,
        guardduty: Optional[_builtins.str] = ...,
        healthlake: Optional[_builtins.str] = ...,
        iam: Optional[_builtins.str] = ...,
        identitystore: Optional[_builtins.str] = ...,
        imagebuilder: Optional[_builtins.str] = ...,
        inspector: Optional[_builtins.str] = ...,
        inspector2: Optional[_builtins.str] = ...,
        inspectorv2: Optional[_builtins.str] = ...,
        internetmonitor: Optional[_builtins.str] = ...,
        invoicing: Optional[_builtins.str] = ...,
        iot: Optional[_builtins.str] = ...,
        ivs: Optional[_builtins.str] = ...,
        ivschat: Optional[_builtins.str] = ...,
        kafka: Optional[_builtins.str] = ...,
        kafkaconnect: Optional[_builtins.str] = ...,
        kendra: Optional[_builtins.str] = ...,
        keyspaces: Optional[_builtins.str] = ...,
        kinesis: Optional[_builtins.str] = ...,
        kinesisanalytics: Optional[_builtins.str] = ...,
        kinesisanalyticsv2: Optional[_builtins.str] = ...,
        kinesisvideo: Optional[_builtins.str] = ...,
        kms: Optional[_builtins.str] = ...,
        lakeformation: Optional[_builtins.str] = ...,
        lambda_: Optional[_builtins.str] = ...,
        launchwizard: Optional[_builtins.str] = ...,
        lex: Optional[_builtins.str] = ...,
        lexmodelbuilding: Optional[_builtins.str] = ...,
        lexmodelbuildingservice: Optional[_builtins.str] = ...,
        lexmodels: Optional[_builtins.str] = ...,
        lexmodelsv2: Optional[_builtins.str] = ...,
        lexv2models: Optional[_builtins.str] = ...,
        licensemanager: Optional[_builtins.str] = ...,
        lightsail: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        locationservice: Optional[_builtins.str] = ...,
        logs: Optional[_builtins.str] = ...,
        m2: Optional[_builtins.str] = ...,
        macie2: Optional[_builtins.str] = ...,
        managedgrafana: Optional[_builtins.str] = ...,
        mediaconnect: Optional[_builtins.str] = ...,
        mediaconvert: Optional[_builtins.str] = ...,
        medialive: Optional[_builtins.str] = ...,
        mediapackage: Optional[_builtins.str] = ...,
        mediapackagev2: Optional[_builtins.str] = ...,
        mediapackagevod: Optional[_builtins.str] = ...,
        mediastore: Optional[_builtins.str] = ...,
        memorydb: Optional[_builtins.str] = ...,
        mgn: Optional[_builtins.str] = ...,
        mpa: Optional[_builtins.str] = ...,
        mq: Optional[_builtins.str] = ...,
        msk: Optional[_builtins.str] = ...,
        mwaa: Optional[_builtins.str] = ...,
        mwaaserverless: Optional[_builtins.str] = ...,
        neptune: Optional[_builtins.str] = ...,
        neptunegraph: Optional[_builtins.str] = ...,
        networkfirewall: Optional[_builtins.str] = ...,
        networkflowmonitor: Optional[_builtins.str] = ...,
        networkmanager: Optional[_builtins.str] = ...,
        networkmonitor: Optional[_builtins.str] = ...,
        notifications: Optional[_builtins.str] = ...,
        notificationscontacts: Optional[_builtins.str] = ...,
        oam: Optional[_builtins.str] = ...,
        observabilityadmin: Optional[_builtins.str] = ...,
        odb: Optional[_builtins.str] = ...,
        opensearch: Optional[_builtins.str] = ...,
        opensearchingestion: Optional[_builtins.str] = ...,
        opensearchserverless: Optional[_builtins.str] = ...,
        opensearchservice: Optional[_builtins.str] = ...,
        organizations: Optional[_builtins.str] = ...,
        osis: Optional[_builtins.str] = ...,
        outposts: Optional[_builtins.str] = ...,
        paymentcryptography: Optional[_builtins.str] = ...,
        pcaconnectorad: Optional[_builtins.str] = ...,
        pcs: Optional[_builtins.str] = ...,
        pinpoint: Optional[_builtins.str] = ...,
        pinpointsmsvoicev2: Optional[_builtins.str] = ...,
        pipes: Optional[_builtins.str] = ...,
        polly: Optional[_builtins.str] = ...,
        pricing: Optional[_builtins.str] = ...,
        prometheus: Optional[_builtins.str] = ...,
        prometheusservice: Optional[_builtins.str] = ...,
        qbusiness: Optional[_builtins.str] = ...,
        qldb: Optional[_builtins.str] = ...,
        quicksight: Optional[_builtins.str] = ...,
        ram: Optional[_builtins.str] = ...,
        rbin: Optional[_builtins.str] = ...,
        rds: Optional[_builtins.str] = ...,
        rdsdata: Optional[_builtins.str] = ...,
        rdsdataservice: Optional[_builtins.str] = ...,
        recyclebin: Optional[_builtins.str] = ...,
        redshift: Optional[_builtins.str] = ...,
        redshiftdata: Optional[_builtins.str] = ...,
        redshiftdataapiservice: Optional[_builtins.str] = ...,
        redshiftserverless: Optional[_builtins.str] = ...,
        rekognition: Optional[_builtins.str] = ...,
        resiliencehub: Optional[_builtins.str] = ...,
        resourceexplorer2: Optional[_builtins.str] = ...,
        resourcegroups: Optional[_builtins.str] = ...,
        resourcegroupstagging: Optional[_builtins.str] = ...,
        resourcegroupstaggingapi: Optional[_builtins.str] = ...,
        rolesanywhere: Optional[_builtins.str] = ...,
        route53: Optional[_builtins.str] = ...,
        route53domains: Optional[_builtins.str] = ...,
        route53profiles: Optional[_builtins.str] = ...,
        route53recoverycontrolconfig: Optional[_builtins.str] = ...,
        route53recoveryreadiness: Optional[_builtins.str] = ...,
        route53resolver: Optional[_builtins.str] = ...,
        rum: Optional[_builtins.str] = ...,
        s3: Optional[_builtins.str] = ...,
        s3api: Optional[_builtins.str] = ...,
        s3control: Optional[_builtins.str] = ...,
        s3outposts: Optional[_builtins.str] = ...,
        s3tables: Optional[_builtins.str] = ...,
        s3vectors: Optional[_builtins.str] = ...,
        sagemaker: Optional[_builtins.str] = ...,
        savingsplans: Optional[_builtins.str] = ...,
        scheduler: Optional[_builtins.str] = ...,
        schemas: Optional[_builtins.str] = ...,
        secretsmanager: Optional[_builtins.str] = ...,
        securityhub: Optional[_builtins.str] = ...,
        securitylake: Optional[_builtins.str] = ...,
        serverlessapplicationrepository: Optional[_builtins.str] = ...,
        serverlessapprepo: Optional[_builtins.str] = ...,
        serverlessrepo: Optional[_builtins.str] = ...,
        servicecatalog: Optional[_builtins.str] = ...,
        servicecatalogappregistry: Optional[_builtins.str] = ...,
        servicediscovery: Optional[_builtins.str] = ...,
        servicequotas: Optional[_builtins.str] = ...,
        ses: Optional[_builtins.str] = ...,
        sesv2: Optional[_builtins.str] = ...,
        sfn: Optional[_builtins.str] = ...,
        shield: Optional[_builtins.str] = ...,
        signer: Optional[_builtins.str] = ...,
        sns: Optional[_builtins.str] = ...,
        sqs: Optional[_builtins.str] = ...,
        ssm: Optional[_builtins.str] = ...,
        ssmcontacts: Optional[_builtins.str] = ...,
        ssmincidents: Optional[_builtins.str] = ...,
        ssmquicksetup: Optional[_builtins.str] = ...,
        ssmsap: Optional[_builtins.str] = ...,
        sso: Optional[_builtins.str] = ...,
        ssoadmin: Optional[_builtins.str] = ...,
        stepfunctions: Optional[_builtins.str] = ...,
        storagegateway: Optional[_builtins.str] = ...,
        sts: Optional[_builtins.str] = ...,
        swf: Optional[_builtins.str] = ...,
        synthetics: Optional[_builtins.str] = ...,
        taxsettings: Optional[_builtins.str] = ...,
        timestreaminfluxdb: Optional[_builtins.str] = ...,
        timestreamquery: Optional[_builtins.str] = ...,
        timestreamwrite: Optional[_builtins.str] = ...,
        transcribe: Optional[_builtins.str] = ...,
        transcribeservice: Optional[_builtins.str] = ...,
        transfer: Optional[_builtins.str] = ...,
        verifiedpermissions: Optional[_builtins.str] = ...,
        vpclattice: Optional[_builtins.str] = ...,
        waf: Optional[_builtins.str] = ...,
        wafregional: Optional[_builtins.str] = ...,
        wafv2: Optional[_builtins.str] = ...,
        wellarchitected: Optional[_builtins.str] = ...,
        workmail: Optional[_builtins.str] = ...,
        workspaces: Optional[_builtins.str] = ...,
        workspacesweb: Optional[_builtins.str] = ...,
        xray: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accessanalyzer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def account(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def acm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def acmpca(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def amg(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def amp(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def amplify(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def apigateway(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def apigatewayv2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def appautoscaling(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def appconfig(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def appfabric(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def appflow(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def appintegrations(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def appintegrationsservice(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def applicationautoscaling(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def applicationinsights(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def applicationsignals(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def appmesh(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def appregistry(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def apprunner(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def appstream(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def appsync(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arcregionswitch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arczonalshift(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def athena(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def auditmanager(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def autoscaling(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def autoscalingplans(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def backup(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def batch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def bcmdataexports(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def beanstalk(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def bedrock(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def bedrockagent(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def bedrockagentcore(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def billing(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def budgets(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ce(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def chatbot(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def chime(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def chimesdkmediapipelines(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def chimesdkvoice(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cleanrooms(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloud9(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloudcontrol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloudcontrolapi(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloudformation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloudfront(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloudfrontkeyvaluestore(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloudhsm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloudhsmv2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloudsearch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloudtrail(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloudwatch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloudwatchevents(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloudwatchevidently(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloudwatchlog(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloudwatchlogs(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloudwatchobservabilityaccessmanager(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cloudwatchrum(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def codeartifact(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def codebuild(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def codecatalyst(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def codecommit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def codeconnections(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def codedeploy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def codeguruprofiler(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def codegurureviewer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def codepipeline(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def codestarconnections(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def codestarnotifications(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cognitoidentity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cognitoidentityprovider(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cognitoidp(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def comprehend(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def computeoptimizer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def configservice(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def connect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def connectcases(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def controltower(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def costandusagereportservice(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def costexplorer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def costoptimizationhub(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cur(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def customerprofiles(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def databasemigration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def databasemigrationservice(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def databrew(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dataexchange(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def datapipeline(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def datasync(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def datazone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dax(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def deploy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def detective(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def devicefarm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def devopsguru(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def directconnect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def directoryservice(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dlm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dms(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def docdb(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def docdbelastic(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def drs(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ds(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dsql(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dynamodb(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ec2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ecr(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ecrpublic(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ecs(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def efs(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def eks(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def elasticache(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def elasticbeanstalk(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def elasticloadbalancing(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def elasticloadbalancingv2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def elasticsearch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def elasticsearchservice(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def elastictranscoder(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def elb(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def elbv2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def emr(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def emrcontainers(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def emrserverless(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def es(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def eventbridge(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def evidently(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def evs(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def finspace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def firehose(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def fis(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def fms(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def fsx(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def gamelift(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def glacier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def globalaccelerator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def glue(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def gluedatabrew(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def grafana(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def greengrass(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def groundstation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def guardduty(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def healthlake(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def iam(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identitystore(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def imagebuilder(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def inspector(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def inspector2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def inspectorv2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def internetmonitor(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def invoicing(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def iot(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ivs(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ivschat(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kafka(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kafkaconnect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kendra(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def keyspaces(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kinesis(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kinesisanalytics(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kinesisanalyticsv2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kinesisvideo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kms(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def lakeformation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def launchwizard(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def lex(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def lexmodelbuilding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def lexmodelbuildingservice(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def lexmodels(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def lexmodelsv2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def lexv2models(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def licensemanager(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def lightsail(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def locationservice(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def logs(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def m2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def macie2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def managedgrafana(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mediaconnect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mediaconvert(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def medialive(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mediapackage(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mediapackagev2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mediapackagevod(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mediastore(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def memorydb(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mgn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mpa(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mq(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def msk(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mwaa(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mwaaserverless(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def neptune(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def neptunegraph(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def networkfirewall(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def networkflowmonitor(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def networkmanager(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def networkmonitor(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def notifications(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def notificationscontacts(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def oam(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def observabilityadmin(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def odb(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def opensearch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def opensearchingestion(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def opensearchserverless(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def opensearchservice(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def organizations(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def osis(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def outposts(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def paymentcryptography(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def pcaconnectorad(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def pcs(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def pinpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def pinpointsmsvoicev2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def pipes(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def polly(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def pricing(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prometheus(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prometheusservice(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def qbusiness(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def qldb(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def quicksight(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ram(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rbin(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rds(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rdsdata(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rdsdataservice(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def recyclebin(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def redshift(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def redshiftdata(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def redshiftdataapiservice(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def redshiftserverless(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rekognition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resiliencehub(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resourceexplorer2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resourcegroups(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resourcegroupstagging(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resourcegroupstaggingapi(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rolesanywhere(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def route53(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def route53domains(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def route53profiles(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def route53recoverycontrolconfig(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def route53recoveryreadiness(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def route53resolver(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rum(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def s3api(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def s3control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def s3outposts(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def s3tables(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def s3vectors(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sagemaker(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def savingsplans(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scheduler(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def schemas(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def secretsmanager(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def securityhub(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def securitylake(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def serverlessapplicationrepository(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def serverlessapprepo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def serverlessrepo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def servicecatalog(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def servicecatalogappregistry(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def servicediscovery(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def servicequotas(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ses(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sesv2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sfn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def shield(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def signer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sns(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sqs(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ssm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ssmcontacts(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ssmincidents(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ssmquicksetup(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ssmsap(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sso(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ssoadmin(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def stepfunctions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def storagegateway(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sts(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def swf(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def synthetics(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def taxsettings(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timestreaminfluxdb(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timestreamquery(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timestreamwrite(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def transcribe(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def transcribeservice(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def transfer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def verifiedpermissions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def vpclattice(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def waf(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def wafregional(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def wafv2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def wellarchitected(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def workmail(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def workspaces(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def workspacesweb(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def xray(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IgnoreTags(dict):
    def __init__(
        __self__,
        *,
        key_prefixes: Optional[Sequence[_builtins.str]] = ...,
        keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyPrefixes")
    def key_prefixes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Optional[Sequence[_builtins.str]]: ...
