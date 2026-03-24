import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AgentAgentActionGroupActionGroupExecutor",
    "AgentAgentActionGroupApiSchema",
    "AgentAgentActionGroupApiSchemaS3",
    "AgentAgentActionGroupFunctionSchema",
    "AgentAgentActionGroupFunctionSchemaMemberFunctions",
    ...,
    ...,
    "AgentAgentActionGroupTimeouts",
    "AgentAgentAliasRoutingConfiguration",
    "AgentAgentAliasTimeouts",
    "AgentAgentCollaboratorAgentDescriptor",
    "AgentAgentCollaboratorTimeouts",
    "AgentAgentGuardrailConfiguration",
    "AgentAgentKnowledgeBaseAssociationTimeouts",
    "AgentAgentMemoryConfiguration",
    ...,
    "AgentAgentPromptOverrideConfiguration",
    ...,
    ...,
    "AgentAgentTimeouts",
    "AgentDataSourceDataSourceConfiguration",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AgentDataSourceServerSideEncryptionConfiguration",
    "AgentDataSourceTimeouts",
    "AgentDataSourceVectorIngestionConfiguration",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AgentFlowDefinition",
    "AgentFlowDefinitionConnection",
    "AgentFlowDefinitionConnectionConfiguration",
    ...,
    "AgentFlowDefinitionConnectionConfigurationData",
    "AgentFlowDefinitionNode",
    "AgentFlowDefinitionNodeConfiguration",
    "AgentFlowDefinitionNodeConfigurationAgent",
    "AgentFlowDefinitionNodeConfigurationCollector",
    "AgentFlowDefinitionNodeConfigurationCondition",
    ...,
    "AgentFlowDefinitionNodeConfigurationInlineCode",
    "AgentFlowDefinitionNodeConfigurationInput",
    "AgentFlowDefinitionNodeConfigurationIterator",
    "AgentFlowDefinitionNodeConfigurationKnowledgeBase",
    ...,
    ...,
    ...,
    "AgentFlowDefinitionNodeConfigurationLambdaFunction",
    "AgentFlowDefinitionNodeConfigurationLex",
    "AgentFlowDefinitionNodeConfigurationOutput",
    "AgentFlowDefinitionNodeConfigurationPrompt",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AgentFlowDefinitionNodeConfigurationRetrieval",
    ...,
    ...,
    "AgentFlowDefinitionNodeConfigurationStorage",
    ...,
    ...,
    "AgentFlowDefinitionNodeInput",
    "AgentFlowDefinitionNodeOutput",
    "AgentFlowTimeouts",
    "AgentKnowledgeBaseKnowledgeBaseConfiguration",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AgentKnowledgeBaseStorageConfiguration",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AgentKnowledgeBaseTimeouts",
    "AgentPromptVariant",
    "AgentPromptVariantGenAiResource",
    "AgentPromptVariantGenAiResourceAgent",
    "AgentPromptVariantInferenceConfiguration",
    "AgentPromptVariantInferenceConfigurationText",
    "AgentPromptVariantMetadata",
    "AgentPromptVariantTemplateConfiguration",
    "AgentPromptVariantTemplateConfigurationChat",
    ...,
    "AgentPromptVariantTemplateConfigurationChatMessage",
    ...,
    ...,
    "AgentPromptVariantTemplateConfigurationChatSystem",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AgentPromptVariantTemplateConfigurationText",
    ...,
    ...,
    "AgentcoreAgentRuntimeAgentRuntimeArtifact",
    ...,
    ...,
    ...,
    ...,
    "AgentcoreAgentRuntimeAuthorizerConfiguration",
    ...,
    "AgentcoreAgentRuntimeEndpointTimeouts",
    "AgentcoreAgentRuntimeLifecycleConfiguration",
    "AgentcoreAgentRuntimeNetworkConfiguration",
    ...,
    "AgentcoreAgentRuntimeProtocolConfiguration",
    "AgentcoreAgentRuntimeRequestHeaderConfiguration",
    "AgentcoreAgentRuntimeTimeouts",
    "AgentcoreAgentRuntimeWorkloadIdentityDetail",
    "AgentcoreApiKeyCredentialProviderApiKeySecretArn",
    "AgentcoreBrowserNetworkConfiguration",
    "AgentcoreBrowserNetworkConfigurationVpcConfig",
    "AgentcoreBrowserRecording",
    "AgentcoreBrowserRecordingS3Location",
    "AgentcoreBrowserTimeouts",
    "AgentcoreCodeInterpreterNetworkConfiguration",
    ...,
    "AgentcoreCodeInterpreterTimeouts",
    "AgentcoreGatewayAuthorizerConfiguration",
    ...,
    "AgentcoreGatewayInterceptorConfiguration",
    ...,
    ...,
    ...,
    "AgentcoreGatewayProtocolConfiguration",
    "AgentcoreGatewayProtocolConfigurationMcp",
    ...,
    ...,
    ...,
    ...,
    "AgentcoreGatewayTargetMetadataConfiguration",
    "AgentcoreGatewayTargetTargetConfiguration",
    "AgentcoreGatewayTargetTargetConfigurationMcp",
    "AgentcoreGatewayTargetTargetConfigurationMcpLambda",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AgentcoreGatewayTargetTimeouts",
    "AgentcoreGatewayTimeouts",
    "AgentcoreGatewayWorkloadIdentityDetail",
    "AgentcoreMemoryStrategyConfiguration",
    "AgentcoreMemoryStrategyConfigurationConsolidation",
    "AgentcoreMemoryStrategyConfigurationExtraction",
    "AgentcoreMemoryStrategyTimeouts",
    "AgentcoreMemoryTimeouts",
    "AgentcoreOauth2CredentialProviderClientSecretArn",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AgentcoreTokenVaultCmkKmsConfiguration",
    "CustomModelOutputDataConfig",
    "CustomModelTimeouts",
    "CustomModelTrainingDataConfig",
    "CustomModelTrainingMetric",
    "CustomModelValidationDataConfig",
    "CustomModelValidationDataConfigValidator",
    "CustomModelValidationMetric",
    "CustomModelVpcConfig",
    "GuardrailContentPolicyConfig",
    "GuardrailContentPolicyConfigFiltersConfig",
    "GuardrailContentPolicyConfigTierConfig",
    "GuardrailContextualGroundingPolicyConfig",
    ...,
    "GuardrailCrossRegionConfig",
    "GuardrailSensitiveInformationPolicyConfig",
    ...,
    ...,
    "GuardrailTimeouts",
    "GuardrailTopicPolicyConfig",
    "GuardrailTopicPolicyConfigTierConfig",
    "GuardrailTopicPolicyConfigTopicsConfig",
    "GuardrailVersionTimeouts",
    "GuardrailWordPolicyConfig",
    "GuardrailWordPolicyConfigManagedWordListsConfig",
    "GuardrailWordPolicyConfigWordsConfig",
    "InferenceProfileModel",
    "InferenceProfileModelSource",
    "InferenceProfileTimeouts",
    "ProvisionedModelThroughputTimeouts",
    "GetAgentAgentVersionsAgentVersionSummaryResult",
    ...,
    "GetCustomModelOutputDataConfigResult",
    "GetCustomModelTrainingDataConfigResult",
    "GetCustomModelTrainingMetricResult",
    "GetCustomModelValidationDataConfigResult",
    "GetCustomModelValidationDataConfigValidatorResult",
    "GetCustomModelValidationMetricResult",
    "GetCustomModelsModelSummaryResult",
    "GetInferenceProfileModelResult",
    "GetInferenceProfilesInferenceProfileSummaryResult",
    ...,
]

@pulumi.output_type
class AgentAgentActionGroupActionGroupExecutor(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_control: Optional[_builtins.str] = ...,
        lambda_: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customControl")
    def custom_control(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentAgentActionGroupApiSchema(dict):
    def __init__(
        __self__,
        *,
        payload: Optional[_builtins.str] = ...,
        s3: Optional[outputs.AgentAgentActionGroupApiSchemaS3] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[outputs.AgentAgentActionGroupApiSchemaS3]: ...

@pulumi.output_type
class AgentAgentActionGroupApiSchemaS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_bucket_name: Optional[_builtins.str] = ...,
        s3_object_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3ObjectKey")
    def s3_object_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentAgentActionGroupFunctionSchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        member_functions: Optional[
            outputs.AgentAgentActionGroupFunctionSchemaMemberFunctions
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memberFunctions")
    def member_functions(
        self,
    ) -> Optional[outputs.AgentAgentActionGroupFunctionSchemaMemberFunctions]: ...

@pulumi.output_type
class AgentAgentActionGroupFunctionSchemaMemberFunctions(dict):
    def __init__(
        __self__,
        *,
        functions: Optional[
            Sequence[outputs.AgentAgentActionGroupFunctionSchemaMemberFunctionsFunction]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def functions(
        self,
    ) -> Optional[
        Sequence[outputs.AgentAgentActionGroupFunctionSchemaMemberFunctionsFunction]
    ]: ...

@pulumi.output_type
class AgentAgentActionGroupFunctionSchemaMemberFunctionsFunction(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        description: Optional[_builtins.str] = ...,
        parameters: Optional[
            Sequence[
                outputs.AgentAgentActionGroupFunctionSchemaMemberFunctionsFunctionParameter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentAgentActionGroupFunctionSchemaMemberFunctionsFunctionParameter
        ]
    ]: ...

@pulumi.output_type
class AgentAgentActionGroupFunctionSchemaMemberFunctionsFunctionParameter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        map_block_key: _builtins.str,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        required: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AgentAgentActionGroupTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentAgentAliasRoutingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, agent_version: _builtins.str, provisioned_throughput: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> _builtins.str: ...

@pulumi.output_type
class AgentAgentAliasTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentAgentCollaboratorAgentDescriptor(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, alias_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aliasArn")
    def alias_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AgentAgentCollaboratorTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentAgentGuardrailConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        guardrail_identifier: _builtins.str,
        guardrail_version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="guardrailIdentifier")
    def guardrail_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="guardrailVersion")
    def guardrail_version(self) -> _builtins.str: ...

@pulumi.output_type
class AgentAgentKnowledgeBaseAssociationTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentAgentMemoryConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled_memory_types: Sequence[_builtins.str],
        session_summary_configurations: Sequence[
            outputs.AgentAgentMemoryConfigurationSessionSummaryConfiguration
        ],
        storage_days: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledMemoryTypes")
    def enabled_memory_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionSummaryConfigurations")
    def session_summary_configurations(
        self,
    ) -> Sequence[outputs.AgentAgentMemoryConfigurationSessionSummaryConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="storageDays")
    def storage_days(self) -> _builtins.int: ...

@pulumi.output_type
class AgentAgentMemoryConfigurationSessionSummaryConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, max_recent_sessions: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRecentSessions")
    def max_recent_sessions(self) -> _builtins.int: ...

@pulumi.output_type
class AgentAgentPromptOverrideConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        override_lambda: _builtins.str,
        prompt_configurations: Sequence[
            outputs.AgentAgentPromptOverrideConfigurationPromptConfiguration
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="overrideLambda")
    def override_lambda(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="promptConfigurations")
    def prompt_configurations(
        self,
    ) -> Sequence[outputs.AgentAgentPromptOverrideConfigurationPromptConfiguration]: ...

@pulumi.output_type
class AgentAgentPromptOverrideConfigurationPromptConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_prompt_template: _builtins.str,
        inference_configurations: Sequence[
            outputs.AgentAgentPromptOverrideConfigurationPromptConfigurationInferenceConfiguration
        ],
        parser_mode: _builtins.str,
        prompt_creation_mode: _builtins.str,
        prompt_state: _builtins.str,
        prompt_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="basePromptTemplate")
    def base_prompt_template(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inferenceConfigurations")
    def inference_configurations(
        self,
    ) -> Sequence[
        outputs.AgentAgentPromptOverrideConfigurationPromptConfigurationInferenceConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="parserMode")
    def parser_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="promptCreationMode")
    def prompt_creation_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="promptState")
    def prompt_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="promptType")
    def prompt_type(self) -> _builtins.str: ...

@pulumi.output_type
class AgentAgentPromptOverrideConfigurationPromptConfigurationInferenceConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_length: _builtins.int,
        stop_sequences: Sequence[_builtins.str],
        temperature: _builtins.float,
        top_k: _builtins.int,
        top_p: _builtins.float,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxLength")
    def max_length(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="stopSequences")
    def stop_sequences(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="topK")
    def top_k(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="topP")
    def top_p(self) -> _builtins.float: ...

@pulumi.output_type
class AgentAgentTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        confluence_configuration: Optional[
            outputs.AgentDataSourceDataSourceConfigurationConfluenceConfiguration
        ] = ...,
        s3_configuration: Optional[
            outputs.AgentDataSourceDataSourceConfigurationS3Configuration
        ] = ...,
        salesforce_configuration: Optional[
            outputs.AgentDataSourceDataSourceConfigurationSalesforceConfiguration
        ] = ...,
        share_point_configuration: Optional[
            outputs.AgentDataSourceDataSourceConfigurationSharePointConfiguration
        ] = ...,
        web_configuration: Optional[
            outputs.AgentDataSourceDataSourceConfigurationWebConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="confluenceConfiguration")
    def confluence_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceDataSourceConfigurationConfluenceConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> Optional[outputs.AgentDataSourceDataSourceConfigurationS3Configuration]: ...
    @_builtins.property
    @pulumi.getter(name="salesforceConfiguration")
    def salesforce_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceDataSourceConfigurationSalesforceConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sharePointConfiguration")
    def share_point_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceDataSourceConfigurationSharePointConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="webConfiguration")
    def web_configuration(
        self,
    ) -> Optional[outputs.AgentDataSourceDataSourceConfigurationWebConfiguration]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationConfluenceConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        crawler_configuration: Optional[
            outputs.AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfiguration
        ] = ...,
        source_configuration: Optional[
            outputs.AgentDataSourceDataSourceConfigurationConfluenceConfigurationSourceConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crawlerConfiguration")
    def crawler_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceDataSourceConfigurationConfluenceConfigurationSourceConfiguration
    ]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        filter_configuration: Optional[
            outputs.AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterConfiguration")
    def filter_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfiguration
    ]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        pattern_object_filters: Optional[
            Sequence[
                outputs.AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="patternObjectFilters")
    def pattern_object_filters(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilter
        ]
    ]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilter(
    dict
):
    def __init__(
        __self__,
        *,
        filters: Optional[
            Sequence[
                outputs.AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilter
        ]
    ]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object_type: _builtins.str,
        exclusion_filters: Optional[Sequence[_builtins.str]] = ...,
        inclusion_filters: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectType")
    def object_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exclusionFilters")
    def exclusion_filters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inclusionFilters")
    def inclusion_filters(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationConfluenceConfigurationSourceConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_type: _builtins.str,
        credentials_secret_arn: _builtins.str,
        host_type: _builtins.str,
        host_url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="credentialsSecretArn")
    def credentials_secret_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostType")
    def host_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostUrl")
    def host_url(self) -> _builtins.str: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationS3Configuration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        bucket_owner_account_id: Optional[_builtins.str] = ...,
        inclusion_prefixes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketOwnerAccountId")
    def bucket_owner_account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inclusionPrefixes")
    def inclusion_prefixes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationSalesforceConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        crawler_configuration: Optional[
            outputs.AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfiguration
        ] = ...,
        source_configuration: Optional[
            outputs.AgentDataSourceDataSourceConfigurationSalesforceConfigurationSourceConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crawlerConfiguration")
    def crawler_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceDataSourceConfigurationSalesforceConfigurationSourceConfiguration
    ]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        filter_configuration: Optional[
            outputs.AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterConfiguration")
    def filter_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfiguration
    ]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        pattern_object_filters: Optional[
            Sequence[
                outputs.AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="patternObjectFilters")
    def pattern_object_filters(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilter
        ]
    ]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilter(
    dict
):
    def __init__(
        __self__,
        *,
        filters: Optional[
            Sequence[
                outputs.AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilter
        ]
    ]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object_type: _builtins.str,
        exclusion_filters: Optional[Sequence[_builtins.str]] = ...,
        inclusion_filters: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectType")
    def object_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exclusionFilters")
    def exclusion_filters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inclusionFilters")
    def inclusion_filters(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationSalesforceConfigurationSourceConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_type: _builtins.str,
        credentials_secret_arn: _builtins.str,
        host_url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="credentialsSecretArn")
    def credentials_secret_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostUrl")
    def host_url(self) -> _builtins.str: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationSharePointConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        crawler_configuration: Optional[
            outputs.AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfiguration
        ] = ...,
        source_configuration: Optional[
            outputs.AgentDataSourceDataSourceConfigurationSharePointConfigurationSourceConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crawlerConfiguration")
    def crawler_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceDataSourceConfigurationSharePointConfigurationSourceConfiguration
    ]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        filter_configuration: Optional[
            outputs.AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterConfiguration")
    def filter_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfiguration
    ]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        pattern_object_filters: Optional[
            Sequence[
                outputs.AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="patternObjectFilters")
    def pattern_object_filters(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilter
        ]
    ]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilter(
    dict
):
    def __init__(
        __self__,
        *,
        filters: Optional[
            Sequence[
                outputs.AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilter
        ]
    ]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilter(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object_type: _builtins.str,
        exclusion_filters: Optional[Sequence[_builtins.str]] = ...,
        inclusion_filters: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectType")
    def object_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exclusionFilters")
    def exclusion_filters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inclusionFilters")
    def inclusion_filters(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationSharePointConfigurationSourceConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_type: _builtins.str,
        credentials_secret_arn: _builtins.str,
        domain: _builtins.str,
        host_type: _builtins.str,
        site_urls: Sequence[_builtins.str],
        tenant_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="credentialsSecretArn")
    def credentials_secret_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostType")
    def host_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="siteUrls")
    def site_urls(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationWebConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        crawler_configuration: Optional[
            outputs.AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfiguration
        ] = ...,
        source_configuration: Optional[
            outputs.AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crawlerConfiguration")
    def crawler_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfiguration
    ]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        crawler_limits: Optional[
            outputs.AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfigurationCrawlerLimits
        ] = ...,
        exclusion_filters: Optional[Sequence[_builtins.str]] = ...,
        inclusion_filters: Optional[Sequence[_builtins.str]] = ...,
        scope: Optional[_builtins.str] = ...,
        user_agent: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crawlerLimits")
    def crawler_limits(
        self,
    ) -> Optional[
        outputs.AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfigurationCrawlerLimits
    ]: ...
    @_builtins.property
    @pulumi.getter(name="exclusionFilters")
    def exclusion_filters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="inclusionFilters")
    def inclusion_filters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAgent")
    def user_agent(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfigurationCrawlerLimits(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_pages: Optional[_builtins.int] = ...,
        rate_limit: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPages")
    def max_pages(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rateLimit")
    def rate_limit(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        url_configuration: outputs.AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfiguration,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="urlConfiguration")
    def url_configuration(
        self,
    ) -> outputs.AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfiguration: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        seed_urls: Optional[
            Sequence[
                outputs.AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfigurationSeedUrl
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="seedUrls")
    def seed_urls(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfigurationSeedUrl
        ]
    ]: ...

@pulumi.output_type
class AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfigurationSeedUrl(
    dict
):
    def __init__(__self__, *, url: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentDataSourceServerSideEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_arn: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentDataSourceTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentDataSourceVectorIngestionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        chunking_configuration: Optional[
            outputs.AgentDataSourceVectorIngestionConfigurationChunkingConfiguration
        ] = ...,
        custom_transformation_configuration: Optional[
            outputs.AgentDataSourceVectorIngestionConfigurationCustomTransformationConfiguration
        ] = ...,
        parsing_configuration: Optional[
            outputs.AgentDataSourceVectorIngestionConfigurationParsingConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="chunkingConfiguration")
    def chunking_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceVectorIngestionConfigurationChunkingConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="customTransformationConfiguration")
    def custom_transformation_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceVectorIngestionConfigurationCustomTransformationConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="parsingConfiguration")
    def parsing_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceVectorIngestionConfigurationParsingConfiguration
    ]: ...

@pulumi.output_type
class AgentDataSourceVectorIngestionConfigurationChunkingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        chunking_strategy: _builtins.str,
        fixed_size_chunking_configuration: Optional[
            outputs.AgentDataSourceVectorIngestionConfigurationChunkingConfigurationFixedSizeChunkingConfiguration
        ] = ...,
        hierarchical_chunking_configuration: Optional[
            outputs.AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfiguration
        ] = ...,
        semantic_chunking_configuration: Optional[
            outputs.AgentDataSourceVectorIngestionConfigurationChunkingConfigurationSemanticChunkingConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="chunkingStrategy")
    def chunking_strategy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fixedSizeChunkingConfiguration")
    def fixed_size_chunking_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceVectorIngestionConfigurationChunkingConfigurationFixedSizeChunkingConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hierarchicalChunkingConfiguration")
    def hierarchical_chunking_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="semanticChunkingConfiguration")
    def semantic_chunking_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceVectorIngestionConfigurationChunkingConfigurationSemanticChunkingConfiguration
    ]: ...

@pulumi.output_type
class AgentDataSourceVectorIngestionConfigurationChunkingConfigurationFixedSizeChunkingConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, max_tokens: _builtins.int, overlap_percentage: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxTokens")
    def max_tokens(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="overlapPercentage")
    def overlap_percentage(self) -> _builtins.int: ...

@pulumi.output_type
class AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        overlap_tokens: _builtins.int,
        level_configurations: Optional[
            Sequence[
                outputs.AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfigurationLevelConfiguration
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="overlapTokens")
    def overlap_tokens(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="levelConfigurations")
    def level_configurations(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfigurationLevelConfiguration
        ]
    ]: ...

@pulumi.output_type
class AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfigurationLevelConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, max_tokens: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxTokens")
    def max_tokens(self) -> _builtins.int: ...

@pulumi.output_type
class AgentDataSourceVectorIngestionConfigurationChunkingConfigurationSemanticChunkingConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        breakpoint_percentile_threshold: _builtins.int,
        buffer_size: _builtins.int,
        max_token: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="breakpointPercentileThreshold")
    def breakpoint_percentile_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="bufferSize")
    def buffer_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxToken")
    def max_token(self) -> _builtins.int: ...

@pulumi.output_type
class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        intermediate_storage: Optional[
            outputs.AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorage
        ] = ...,
        transformation: Optional[
            outputs.AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformation
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="intermediateStorage")
    def intermediate_storage(
        self,
    ) -> Optional[
        outputs.AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorage
    ]: ...
    @_builtins.property
    @pulumi.getter
    def transformation(
        self,
    ) -> Optional[
        outputs.AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformation
    ]: ...

@pulumi.output_type
class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorage(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_location: Optional[
            outputs.AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorageS3Location
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Location")
    def s3_location(
        self,
    ) -> Optional[
        outputs.AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorageS3Location
    ]: ...

@pulumi.output_type
class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorageS3Location(
    dict
):
    def __init__(__self__, *, uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

@pulumi.output_type
class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformation(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        step_to_apply: _builtins.str,
        transformation_function: Optional[
            outputs.AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunction
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stepToApply")
    def step_to_apply(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transformationFunction")
    def transformation_function(
        self,
    ) -> Optional[
        outputs.AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunction
    ]: ...

@pulumi.output_type
class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunction(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        transformation_lambda_configuration: Optional[
            outputs.AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunctionTransformationLambdaConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="transformationLambdaConfiguration")
    def transformation_lambda_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunctionTransformationLambdaConfiguration
    ]: ...

@pulumi.output_type
class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunctionTransformationLambdaConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, lambda_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AgentDataSourceVectorIngestionConfigurationParsingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        parsing_strategy: _builtins.str,
        bedrock_data_automation_configuration: Optional[
            outputs.AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockDataAutomationConfiguration
        ] = ...,
        bedrock_foundation_model_configuration: Optional[
            outputs.AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parsingStrategy")
    def parsing_strategy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bedrockDataAutomationConfiguration")
    def bedrock_data_automation_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockDataAutomationConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="bedrockFoundationModelConfiguration")
    def bedrock_foundation_model_configuration(
        self,
    ) -> Optional[
        outputs.AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfiguration
    ]: ...

@pulumi.output_type
class AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockDataAutomationConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, parsing_modality: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parsingModality")
    def parsing_modality(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        model_arn: _builtins.str,
        parsing_modality: Optional[_builtins.str] = ...,
        parsing_prompt: Optional[
            outputs.AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfigurationParsingPrompt
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelArn")
    def model_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parsingModality")
    def parsing_modality(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parsingPrompt")
    def parsing_prompt(
        self,
    ) -> Optional[
        outputs.AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfigurationParsingPrompt
    ]: ...

@pulumi.output_type
class AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfigurationParsingPrompt(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, parsing_prompt_string: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parsingPromptString")
    def parsing_prompt_string(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinition(dict):
    def __init__(
        __self__,
        *,
        connections: Optional[Sequence[outputs.AgentFlowDefinitionConnection]] = ...,
        nodes: Optional[Sequence[outputs.AgentFlowDefinitionNode]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connections(
        self,
    ) -> Optional[Sequence[outputs.AgentFlowDefinitionConnection]]: ...
    @_builtins.property
    @pulumi.getter
    def nodes(self) -> Optional[Sequence[outputs.AgentFlowDefinitionNode]]: ...

@pulumi.output_type
class AgentFlowDefinitionConnection(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        source: _builtins.str,
        target: _builtins.str,
        type: _builtins.str,
        configuration: Optional[
            outputs.AgentFlowDefinitionConnectionConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.AgentFlowDefinitionConnectionConfiguration]: ...

@pulumi.output_type
class AgentFlowDefinitionConnectionConfiguration(dict):
    def __init__(
        __self__,
        *,
        conditional: Optional[
            outputs.AgentFlowDefinitionConnectionConfigurationConditional
        ] = ...,
        data: Optional[outputs.AgentFlowDefinitionConnectionConfigurationData] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditional(
        self,
    ) -> Optional[outputs.AgentFlowDefinitionConnectionConfigurationConditional]: ...
    @_builtins.property
    @pulumi.getter
    def data(
        self,
    ) -> Optional[outputs.AgentFlowDefinitionConnectionConfigurationData]: ...

@pulumi.output_type
class AgentFlowDefinitionConnectionConfigurationConditional(dict):
    def __init__(__self__, *, condition: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionConnectionConfigurationData(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, source_output: _builtins.str, target_input: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceOutput")
    def source_output(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetInput")
    def target_input(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNode(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        configuration: Optional[outputs.AgentFlowDefinitionNodeConfiguration] = ...,
        inputs: Optional[Sequence[outputs.AgentFlowDefinitionNodeInput]] = ...,
        outputs: Optional[Sequence[outputs.AgentFlowDefinitionNodeOutput]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[outputs.AgentFlowDefinitionNodeConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[Sequence[outputs.AgentFlowDefinitionNodeInput]]: ...
    @_builtins.property
    @pulumi.getter
    def outputs(self) -> Optional[Sequence[outputs.AgentFlowDefinitionNodeOutput]]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        agent: Optional[outputs.AgentFlowDefinitionNodeConfigurationAgent] = ...,
        collector: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationCollector
        ] = ...,
        condition: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationCondition
        ] = ...,
        inline_code: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationInlineCode
        ] = ...,
        input: Optional[outputs.AgentFlowDefinitionNodeConfigurationInput] = ...,
        iterator: Optional[outputs.AgentFlowDefinitionNodeConfigurationIterator] = ...,
        knowledge_base: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationKnowledgeBase
        ] = ...,
        lambda_function: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationLambdaFunction
        ] = ...,
        lex: Optional[outputs.AgentFlowDefinitionNodeConfigurationLex] = ...,
        output: Optional[outputs.AgentFlowDefinitionNodeConfigurationOutput] = ...,
        prompt: Optional[outputs.AgentFlowDefinitionNodeConfigurationPrompt] = ...,
        retrieval: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationRetrieval
        ] = ...,
        storage: Optional[outputs.AgentFlowDefinitionNodeConfigurationStorage] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def agent(self) -> Optional[outputs.AgentFlowDefinitionNodeConfigurationAgent]: ...
    @_builtins.property
    @pulumi.getter
    def collector(
        self,
    ) -> Optional[outputs.AgentFlowDefinitionNodeConfigurationCollector]: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[outputs.AgentFlowDefinitionNodeConfigurationCondition]: ...
    @_builtins.property
    @pulumi.getter(name="inlineCode")
    def inline_code(
        self,
    ) -> Optional[outputs.AgentFlowDefinitionNodeConfigurationInlineCode]: ...
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[outputs.AgentFlowDefinitionNodeConfigurationInput]: ...
    @_builtins.property
    @pulumi.getter
    def iterator(
        self,
    ) -> Optional[outputs.AgentFlowDefinitionNodeConfigurationIterator]: ...
    @_builtins.property
    @pulumi.getter(name="knowledgeBase")
    def knowledge_base(
        self,
    ) -> Optional[outputs.AgentFlowDefinitionNodeConfigurationKnowledgeBase]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunction")
    def lambda_function(
        self,
    ) -> Optional[outputs.AgentFlowDefinitionNodeConfigurationLambdaFunction]: ...
    @_builtins.property
    @pulumi.getter
    def lex(self) -> Optional[outputs.AgentFlowDefinitionNodeConfigurationLex]: ...
    @_builtins.property
    @pulumi.getter
    def output(
        self,
    ) -> Optional[outputs.AgentFlowDefinitionNodeConfigurationOutput]: ...
    @_builtins.property
    @pulumi.getter
    def prompt(
        self,
    ) -> Optional[outputs.AgentFlowDefinitionNodeConfigurationPrompt]: ...
    @_builtins.property
    @pulumi.getter
    def retrieval(
        self,
    ) -> Optional[outputs.AgentFlowDefinitionNodeConfigurationRetrieval]: ...
    @_builtins.property
    @pulumi.getter
    def storage(
        self,
    ) -> Optional[outputs.AgentFlowDefinitionNodeConfigurationStorage]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationAgent(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, agent_alias_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentAliasArn")
    def agent_alias_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationCollector(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationCondition(dict):
    def __init__(
        __self__,
        *,
        conditions: Optional[
            Sequence[outputs.AgentFlowDefinitionNodeConfigurationConditionCondition]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        Sequence[outputs.AgentFlowDefinitionNodeConfigurationConditionCondition]
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationConditionCondition(dict):
    def __init__(
        __self__, *, name: _builtins.str, expression: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationInlineCode(dict):
    def __init__(__self__, *, code: _builtins.str, language: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def language(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationInput(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationIterator(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationKnowledgeBase(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        knowledge_base_id: _builtins.str,
        model_id: _builtins.str,
        guardrail_configuration: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationKnowledgeBaseGuardrailConfiguration
        ] = ...,
        inference_configuration: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfiguration
        ] = ...,
        number_of_results: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="knowledgeBaseId")
    def knowledge_base_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="guardrailConfiguration")
    def guardrail_configuration(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationKnowledgeBaseGuardrailConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inferenceConfiguration")
    def inference_configuration(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="numberOfResults")
    def number_of_results(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationKnowledgeBaseGuardrailConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        guardrail_identifier: _builtins.str,
        guardrail_version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="guardrailIdentifier")
    def guardrail_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="guardrailVersion")
    def guardrail_version(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfiguration(dict):
    def __init__(
        __self__,
        *,
        text: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfigurationText
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfigurationText
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfigurationText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_tokens: Optional[_builtins.int] = ...,
        stop_sequences: Optional[Sequence[_builtins.str]] = ...,
        temperature: Optional[_builtins.float] = ...,
        top_p: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxTokens")
    def max_tokens(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="stopSequences")
    def stop_sequences(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="topP")
    def top_p(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationLambdaFunction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, lambda_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationLex(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, bot_alias_arn: _builtins.str, locale_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="botAliasArn")
    def bot_alias_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localeId")
    def locale_id(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationOutput(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPrompt(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        guardrail_configuration: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptGuardrailConfiguration
        ] = ...,
        source_configuration: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="guardrailConfiguration")
    def guardrail_configuration(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptGuardrailConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfiguration
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptGuardrailConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        guardrail_identifier: _builtins.str,
        guardrail_version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="guardrailIdentifier")
    def guardrail_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="guardrailVersion")
    def guardrail_version(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfiguration(dict):
    def __init__(
        __self__,
        *,
        inline: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInline
        ] = ...,
        resource: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationResource
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def inline(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInline
    ]: ...
    @_builtins.property
    @pulumi.getter
    def resource(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationResource
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInline(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        model_id: _builtins.str,
        template_type: _builtins.str,
        additional_model_request_fields: Optional[_builtins.str] = ...,
        inference_configuration: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfiguration
        ] = ...,
        template_configuration: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="templateType")
    def template_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="additionalModelRequestFields")
    def additional_model_request_fields(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inferenceConfiguration")
    def inference_configuration(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="templateConfiguration")
    def template_configuration(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfiguration
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfiguration(
    dict
):
    def __init__(
        __self__,
        *,
        text: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfigurationText
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfigurationText
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfigurationText(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_tokens: Optional[_builtins.int] = ...,
        stop_sequences: Optional[Sequence[_builtins.str]] = ...,
        temperature: Optional[_builtins.float] = ...,
        top_p: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxTokens")
    def max_tokens(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="stopSequences")
    def stop_sequences(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="topP")
    def top_p(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfiguration(
    dict
):
    def __init__(
        __self__,
        *,
        chat: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChat
        ] = ...,
        text: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationText
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def chat(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChat
    ]: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationText
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChat(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        messages: Sequence[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessage
        ],
        input_variables: Optional[
            Sequence[
                outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatInputVariable
            ]
        ] = ...,
        systems: Optional[
            Sequence[
                outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystem
            ]
        ] = ...,
        tool_configuration: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def messages(
        self,
    ) -> Sequence[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessage
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inputVariables")
    def input_variables(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatInputVariable
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def systems(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystem
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="toolConfiguration")
    def tool_configuration(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfiguration
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatInputVariable(
    dict
):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessage(
    dict
):
    def __init__(
        __self__,
        *,
        role: _builtins.str,
        content: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContent
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def content(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContent
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContent(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cache_point: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContentCachePoint
        ] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cachePoint")
    def cache_point(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContentCachePoint
    ]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContentCachePoint(
    dict
):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystem(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cache_point: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystemCachePoint
        ] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cachePoint")
    def cache_point(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystemCachePoint
    ]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystemCachePoint(
    dict
):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        tool_choice: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoice
        ] = ...,
        tools: Optional[
            Sequence[
                outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationTool
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="toolChoice")
    def tool_choice(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoice
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tools(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationTool
        ]
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationTool(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cache_point: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolCachePoint
        ] = ...,
        tool_spec: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpec
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cachePoint")
    def cache_point(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolCachePoint
    ]: ...
    @_builtins.property
    @pulumi.getter(name="toolSpec")
    def tool_spec(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpec
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolCachePoint(
    dict
):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoice(
    dict
):
    def __init__(
        __self__,
        *,
        any: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAny
        ] = ...,
        auto: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAuto
        ] = ...,
        tool: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceTool
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def any(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAny
    ]: ...
    @_builtins.property
    @pulumi.getter
    def auto(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAuto
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tool(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceTool
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAny(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAuto(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceTool(
    dict
):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpec(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        description: Optional[_builtins.str] = ...,
        input_schema: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpecInputSchema
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputSchema")
    def input_schema(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpecInputSchema
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpecInputSchema(
    dict
):
    def __init__(__self__, *, json: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def json(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationText(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        text: _builtins.str,
        cache_point: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextCachePoint
        ] = ...,
        input_variables: Optional[
            Sequence[
                outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextInputVariable
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cachePoint")
    def cache_point(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextCachePoint
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inputVariables")
    def input_variables(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextInputVariable
        ]
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextCachePoint(
    dict
):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextInputVariable(
    dict
):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, prompt_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="promptArn")
    def prompt_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationRetrieval(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_configuration: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationRetrievalServiceConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceConfiguration")
    def service_configuration(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationRetrievalServiceConfiguration
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationRetrievalServiceConfiguration(dict):
    def __init__(
        __self__,
        *,
        s3: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationRetrievalServiceConfigurationS3
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationRetrievalServiceConfigurationS3
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationRetrievalServiceConfigurationS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, bucket_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationStorage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_configuration: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationStorageServiceConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceConfiguration")
    def service_configuration(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationStorageServiceConfiguration
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationStorageServiceConfiguration(dict):
    def __init__(
        __self__,
        *,
        s3: Optional[
            outputs.AgentFlowDefinitionNodeConfigurationStorageServiceConfigurationS3
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[
        outputs.AgentFlowDefinitionNodeConfigurationStorageServiceConfigurationS3
    ]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeConfigurationStorageServiceConfigurationS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, bucket_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowDefinitionNodeInput(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        name: _builtins.str,
        type: _builtins.str,
        category: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentFlowDefinitionNodeOutput(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class AgentFlowTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        kendra_knowledge_base_configuration: Optional[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationKendraKnowledgeBaseConfiguration
        ] = ...,
        sql_knowledge_base_configuration: Optional[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfiguration
        ] = ...,
        vector_knowledge_base_configuration: Optional[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kendraKnowledgeBaseConfiguration")
    def kendra_knowledge_base_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationKendraKnowledgeBaseConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sqlKnowledgeBaseConfiguration")
    def sql_knowledge_base_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="vectorKnowledgeBaseConfiguration")
    def vector_knowledge_base_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfiguration
    ]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationKendraKnowledgeBaseConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kendra_index_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kendraIndexArn")
    def kendra_index_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        redshift_configuration: Optional[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="redshiftConfiguration")
    def redshift_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfiguration
    ]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        query_engine_configuration: outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfiguration,
        storage_configuration: outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfiguration,
        query_generation_configuration: Optional[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryEngineConfiguration")
    def query_engine_configuration(
        self,
    ) -> outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="storageConfiguration")
    def storage_configuration(
        self,
    ) -> outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="queryGenerationConfiguration")
    def query_generation_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfiguration
    ]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        provisioned_configuration: Optional[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfiguration
        ] = ...,
        serverless_configuration: Optional[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisionedConfiguration")
    def provisioned_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serverlessConfiguration")
    def serverless_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfiguration
    ]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_configuration: outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfigurationAuthConfiguration,
        cluster_identifier: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authConfiguration")
    def auth_configuration(
        self,
    ) -> outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfigurationAuthConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> _builtins.str: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfigurationAuthConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        database_user: Optional[_builtins.str] = ...,
        username_password_secret_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseUser")
    def database_user(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="usernamePasswordSecretArn")
    def username_password_secret_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_configuration: outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfigurationAuthConfiguration,
        workgroup_arn: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authConfiguration")
    def auth_configuration(
        self,
    ) -> outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfigurationAuthConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="workgroupArn")
    def workgroup_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfigurationAuthConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        username_password_secret_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="usernamePasswordSecretArn")
    def username_password_secret_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        execution_timeout_seconds: Optional[_builtins.int] = ...,
        generation_context: Optional[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContext
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionTimeoutSeconds")
    def execution_timeout_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="generationContext")
    def generation_context(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContext
    ]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContext(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        curated_queries: Optional[
            Sequence[
                outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextCuratedQuery
            ]
        ] = ...,
        tables: Optional[
            Sequence[
                outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTable
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="curatedQueries")
    def curated_queries(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextCuratedQuery
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTable
        ]
    ]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextCuratedQuery(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, natural_language: _builtins.str, sql: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="naturalLanguage")
    def natural_language(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sql(self) -> _builtins.str: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTable(
    dict
):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        columns: Optional[
            Sequence[
                outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTableColumn
            ]
        ] = ...,
        description: Optional[_builtins.str] = ...,
        inclusion: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTableColumn
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def inclusion(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTableColumn(
    dict
):
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        inclusion: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def inclusion(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        aws_data_catalog_configuration: Optional[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationAwsDataCatalogConfiguration
        ] = ...,
        redshift_configuration: Optional[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationRedshiftConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="awsDataCatalogConfiguration")
    def aws_data_catalog_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationAwsDataCatalogConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="redshiftConfiguration")
    def redshift_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationRedshiftConfiguration
    ]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationAwsDataCatalogConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, table_names: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableNames")
    def table_names(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationRedshiftConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, database_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        embedding_model_arn: _builtins.str,
        embedding_model_configuration: Optional[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfiguration
        ] = ...,
        supplemental_data_storage_configuration: Optional[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="embeddingModelArn")
    def embedding_model_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="embeddingModelConfiguration")
    def embedding_model_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="supplementalDataStorageConfiguration")
    def supplemental_data_storage_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfiguration
    ]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bedrock_embedding_model_configuration: Optional[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfigurationBedrockEmbeddingModelConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bedrockEmbeddingModelConfiguration")
    def bedrock_embedding_model_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfigurationBedrockEmbeddingModelConfiguration
    ]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfigurationBedrockEmbeddingModelConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dimensions: Optional[_builtins.int] = ...,
        embedding_data_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="embeddingDataType")
    def embedding_data_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        storage_locations: Sequence[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocation
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageLocations")
    def storage_locations(
        self,
    ) -> Sequence[
        outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocation
    ]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocation(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        s3_location: Optional[
            outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocationS3Location
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Location")
    def s3_location(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocationS3Location
    ]: ...

@pulumi.output_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocationS3Location(
    dict
):
    def __init__(__self__, *, uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

@pulumi.output_type
class AgentKnowledgeBaseStorageConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        mongo_db_atlas_configuration: Optional[
            outputs.AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfiguration
        ] = ...,
        neptune_analytics_configuration: Optional[
            outputs.AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfiguration
        ] = ...,
        opensearch_managed_cluster_configuration: Optional[
            outputs.AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfiguration
        ] = ...,
        opensearch_serverless_configuration: Optional[
            outputs.AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfiguration
        ] = ...,
        pinecone_configuration: Optional[
            outputs.AgentKnowledgeBaseStorageConfigurationPineconeConfiguration
        ] = ...,
        rds_configuration: Optional[
            outputs.AgentKnowledgeBaseStorageConfigurationRdsConfiguration
        ] = ...,
        redis_enterprise_cloud_configuration: Optional[
            outputs.AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfiguration
        ] = ...,
        s3_vectors_configuration: Optional[
            outputs.AgentKnowledgeBaseStorageConfigurationS3VectorsConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mongoDbAtlasConfiguration")
    def mongo_db_atlas_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="neptuneAnalyticsConfiguration")
    def neptune_analytics_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="opensearchManagedClusterConfiguration")
    def opensearch_managed_cluster_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="opensearchServerlessConfiguration")
    def opensearch_serverless_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="pineconeConfiguration")
    def pinecone_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseStorageConfigurationPineconeConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="rdsConfiguration")
    def rds_configuration(
        self,
    ) -> Optional[outputs.AgentKnowledgeBaseStorageConfigurationRdsConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="redisEnterpriseCloudConfiguration")
    def redis_enterprise_cloud_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="s3VectorsConfiguration")
    def s3_vectors_configuration(
        self,
    ) -> Optional[
        outputs.AgentKnowledgeBaseStorageConfigurationS3VectorsConfiguration
    ]: ...

@pulumi.output_type
class AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        collection_name: _builtins.str,
        credentials_secret_arn: _builtins.str,
        database_name: _builtins.str,
        endpoint: _builtins.str,
        field_mapping: outputs.AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfigurationFieldMapping,
        vector_index_name: _builtins.str,
        endpoint_service_name: Optional[_builtins.str] = ...,
        text_index_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collectionName")
    def collection_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="credentialsSecretArn")
    def credentials_secret_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fieldMapping")
    def field_mapping(
        self,
    ) -> outputs.AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfigurationFieldMapping: ...
    @_builtins.property
    @pulumi.getter(name="vectorIndexName")
    def vector_index_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointServiceName")
    def endpoint_service_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="textIndexName")
    def text_index_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfigurationFieldMapping(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metadata_field: _builtins.str,
        text_field: _builtins.str,
        vector_field: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataField")
    def metadata_field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="textField")
    def text_field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vectorField")
    def vector_field(self) -> _builtins.str: ...

@pulumi.output_type
class AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        field_mapping: outputs.AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfigurationFieldMapping,
        graph_arn: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldMapping")
    def field_mapping(
        self,
    ) -> outputs.AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfigurationFieldMapping: ...
    @_builtins.property
    @pulumi.getter(name="graphArn")
    def graph_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfigurationFieldMapping(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, metadata_field: _builtins.str, text_field: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataField")
    def metadata_field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="textField")
    def text_field(self) -> _builtins.str: ...

@pulumi.output_type
class AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain_arn: _builtins.str,
        domain_endpoint: _builtins.str,
        field_mapping: outputs.AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfigurationFieldMapping,
        vector_index_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainEndpoint")
    def domain_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fieldMapping")
    def field_mapping(
        self,
    ) -> outputs.AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfigurationFieldMapping: ...
    @_builtins.property
    @pulumi.getter(name="vectorIndexName")
    def vector_index_name(self) -> _builtins.str: ...

@pulumi.output_type
class AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfigurationFieldMapping(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metadata_field: _builtins.str,
        text_field: _builtins.str,
        vector_field: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataField")
    def metadata_field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="textField")
    def text_field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vectorField")
    def vector_field(self) -> _builtins.str: ...

@pulumi.output_type
class AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        collection_arn: _builtins.str,
        field_mapping: outputs.AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfigurationFieldMapping,
        vector_index_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collectionArn")
    def collection_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fieldMapping")
    def field_mapping(
        self,
    ) -> outputs.AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfigurationFieldMapping: ...
    @_builtins.property
    @pulumi.getter(name="vectorIndexName")
    def vector_index_name(self) -> _builtins.str: ...

@pulumi.output_type
class AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfigurationFieldMapping(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metadata_field: _builtins.str,
        text_field: _builtins.str,
        vector_field: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataField")
    def metadata_field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="textField")
    def text_field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vectorField")
    def vector_field(self) -> _builtins.str: ...

@pulumi.output_type
class AgentKnowledgeBaseStorageConfigurationPineconeConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_string: _builtins.str,
        credentials_secret_arn: _builtins.str,
        field_mapping: outputs.AgentKnowledgeBaseStorageConfigurationPineconeConfigurationFieldMapping,
        namespace: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="credentialsSecretArn")
    def credentials_secret_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fieldMapping")
    def field_mapping(
        self,
    ) -> (
        outputs.AgentKnowledgeBaseStorageConfigurationPineconeConfigurationFieldMapping
    ): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentKnowledgeBaseStorageConfigurationPineconeConfigurationFieldMapping(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, metadata_field: _builtins.str, text_field: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataField")
    def metadata_field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="textField")
    def text_field(self) -> _builtins.str: ...

@pulumi.output_type
class AgentKnowledgeBaseStorageConfigurationRdsConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        credentials_secret_arn: _builtins.str,
        database_name: _builtins.str,
        field_mapping: outputs.AgentKnowledgeBaseStorageConfigurationRdsConfigurationFieldMapping,
        resource_arn: _builtins.str,
        table_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="credentialsSecretArn")
    def credentials_secret_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fieldMapping")
    def field_mapping(
        self,
    ) -> outputs.AgentKnowledgeBaseStorageConfigurationRdsConfigurationFieldMapping: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str: ...

@pulumi.output_type
class AgentKnowledgeBaseStorageConfigurationRdsConfigurationFieldMapping(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metadata_field: _builtins.str,
        primary_key_field: _builtins.str,
        text_field: _builtins.str,
        vector_field: _builtins.str,
        custom_metadata_field: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataField")
    def metadata_field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="primaryKeyField")
    def primary_key_field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="textField")
    def text_field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vectorField")
    def vector_field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customMetadataField")
    def custom_metadata_field(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        credentials_secret_arn: _builtins.str,
        endpoint: _builtins.str,
        field_mapping: outputs.AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfigurationFieldMapping,
        vector_index_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="credentialsSecretArn")
    def credentials_secret_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fieldMapping")
    def field_mapping(
        self,
    ) -> outputs.AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfigurationFieldMapping: ...
    @_builtins.property
    @pulumi.getter(name="vectorIndexName")
    def vector_index_name(self) -> _builtins.str: ...

@pulumi.output_type
class AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfigurationFieldMapping(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metadata_field: Optional[_builtins.str] = ...,
        text_field: Optional[_builtins.str] = ...,
        vector_field: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataField")
    def metadata_field(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="textField")
    def text_field(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vectorField")
    def vector_field(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentKnowledgeBaseStorageConfigurationS3VectorsConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        index_arn: Optional[_builtins.str] = ...,
        index_name: Optional[_builtins.str] = ...,
        vector_bucket_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="indexArn")
    def index_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vectorBucketArn")
    def vector_bucket_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentKnowledgeBaseTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentPromptVariant(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        template_type: _builtins.str,
        additional_model_request_fields: Optional[_builtins.str] = ...,
        gen_ai_resource: Optional[outputs.AgentPromptVariantGenAiResource] = ...,
        inference_configuration: Optional[
            outputs.AgentPromptVariantInferenceConfiguration
        ] = ...,
        metadatas: Optional[Sequence[outputs.AgentPromptVariantMetadata]] = ...,
        model_id: Optional[_builtins.str] = ...,
        template_configuration: Optional[
            outputs.AgentPromptVariantTemplateConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="templateType")
    def template_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="additionalModelRequestFields")
    def additional_model_request_fields(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="genAiResource")
    def gen_ai_resource(self) -> Optional[outputs.AgentPromptVariantGenAiResource]: ...
    @_builtins.property
    @pulumi.getter(name="inferenceConfiguration")
    def inference_configuration(
        self,
    ) -> Optional[outputs.AgentPromptVariantInferenceConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def metadatas(self) -> Optional[Sequence[outputs.AgentPromptVariantMetadata]]: ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="templateConfiguration")
    def template_configuration(
        self,
    ) -> Optional[outputs.AgentPromptVariantTemplateConfiguration]: ...

@pulumi.output_type
class AgentPromptVariantGenAiResource(dict):
    def __init__(
        __self__, *, agent: Optional[outputs.AgentPromptVariantGenAiResourceAgent] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def agent(self) -> Optional[outputs.AgentPromptVariantGenAiResourceAgent]: ...

@pulumi.output_type
class AgentPromptVariantGenAiResourceAgent(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, agent_identifier: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentIdentifier")
    def agent_identifier(self) -> _builtins.str: ...

@pulumi.output_type
class AgentPromptVariantInferenceConfiguration(dict):
    def __init__(
        __self__,
        *,
        text: Optional[outputs.AgentPromptVariantInferenceConfigurationText] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[outputs.AgentPromptVariantInferenceConfigurationText]: ...

@pulumi.output_type
class AgentPromptVariantInferenceConfigurationText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_tokens: Optional[_builtins.int] = ...,
        stop_sequences: Optional[Sequence[_builtins.str]] = ...,
        temperature: Optional[_builtins.float] = ...,
        top_p: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxTokens")
    def max_tokens(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="stopSequences")
    def stop_sequences(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="topP")
    def top_p(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class AgentPromptVariantMetadata(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfiguration(dict):
    def __init__(
        __self__,
        *,
        chat: Optional[outputs.AgentPromptVariantTemplateConfigurationChat] = ...,
        text: Optional[outputs.AgentPromptVariantTemplateConfigurationText] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def chat(self) -> Optional[outputs.AgentPromptVariantTemplateConfigurationChat]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[outputs.AgentPromptVariantTemplateConfigurationText]: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationChat(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        messages: Sequence[outputs.AgentPromptVariantTemplateConfigurationChatMessage],
        input_variables: Optional[
            Sequence[outputs.AgentPromptVariantTemplateConfigurationChatInputVariable]
        ] = ...,
        systems: Optional[
            Sequence[outputs.AgentPromptVariantTemplateConfigurationChatSystem]
        ] = ...,
        tool_configuration: Optional[
            outputs.AgentPromptVariantTemplateConfigurationChatToolConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def messages(
        self,
    ) -> Sequence[outputs.AgentPromptVariantTemplateConfigurationChatMessage]: ...
    @_builtins.property
    @pulumi.getter(name="inputVariables")
    def input_variables(
        self,
    ) -> Optional[
        Sequence[outputs.AgentPromptVariantTemplateConfigurationChatInputVariable]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def systems(
        self,
    ) -> Optional[
        Sequence[outputs.AgentPromptVariantTemplateConfigurationChatSystem]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="toolConfiguration")
    def tool_configuration(
        self,
    ) -> Optional[
        outputs.AgentPromptVariantTemplateConfigurationChatToolConfiguration
    ]: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationChatInputVariable(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationChatMessage(dict):
    def __init__(
        __self__,
        *,
        role: _builtins.str,
        content: Optional[
            outputs.AgentPromptVariantTemplateConfigurationChatMessageContent
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def content(
        self,
    ) -> Optional[
        outputs.AgentPromptVariantTemplateConfigurationChatMessageContent
    ]: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationChatMessageContent(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cache_point: Optional[
            outputs.AgentPromptVariantTemplateConfigurationChatMessageContentCachePoint
        ] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cachePoint")
    def cache_point(
        self,
    ) -> Optional[
        outputs.AgentPromptVariantTemplateConfigurationChatMessageContentCachePoint
    ]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationChatMessageContentCachePoint(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationChatSystem(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cache_point: Optional[
            outputs.AgentPromptVariantTemplateConfigurationChatSystemCachePoint
        ] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cachePoint")
    def cache_point(
        self,
    ) -> Optional[
        outputs.AgentPromptVariantTemplateConfigurationChatSystemCachePoint
    ]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationChatSystemCachePoint(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationChatToolConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        tool_choice: Optional[
            outputs.AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoice
        ] = ...,
        tools: Optional[
            Sequence[
                outputs.AgentPromptVariantTemplateConfigurationChatToolConfigurationTool
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="toolChoice")
    def tool_choice(
        self,
    ) -> Optional[
        outputs.AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoice
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tools(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentPromptVariantTemplateConfigurationChatToolConfigurationTool
        ]
    ]: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationTool(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cache_point: Optional[
            outputs.AgentPromptVariantTemplateConfigurationChatToolConfigurationToolCachePoint
        ] = ...,
        tool_spec: Optional[
            outputs.AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpec
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cachePoint")
    def cache_point(
        self,
    ) -> Optional[
        outputs.AgentPromptVariantTemplateConfigurationChatToolConfigurationToolCachePoint
    ]: ...
    @_builtins.property
    @pulumi.getter(name="toolSpec")
    def tool_spec(
        self,
    ) -> Optional[
        outputs.AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpec
    ]: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolCachePoint(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoice(dict):
    def __init__(
        __self__,
        *,
        any: Optional[
            outputs.AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAny
        ] = ...,
        auto: Optional[
            outputs.AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAuto
        ] = ...,
        tool: Optional[
            outputs.AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceTool
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def any(
        self,
    ) -> Optional[
        outputs.AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAny
    ]: ...
    @_builtins.property
    @pulumi.getter
    def auto(
        self,
    ) -> Optional[
        outputs.AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAuto
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tool(
        self,
    ) -> Optional[
        outputs.AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceTool
    ]: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAny(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAuto(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceTool(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        description: Optional[_builtins.str] = ...,
        input_schema: Optional[
            outputs.AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpecInputSchema
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputSchema")
    def input_schema(
        self,
    ) -> Optional[
        outputs.AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpecInputSchema
    ]: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpecInputSchema(
    dict
):
    def __init__(__self__, *, json: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def json(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        text: _builtins.str,
        cache_point: Optional[
            outputs.AgentPromptVariantTemplateConfigurationTextCachePoint
        ] = ...,
        input_variables: Optional[
            Sequence[outputs.AgentPromptVariantTemplateConfigurationTextInputVariable]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cachePoint")
    def cache_point(
        self,
    ) -> Optional[outputs.AgentPromptVariantTemplateConfigurationTextCachePoint]: ...
    @_builtins.property
    @pulumi.getter(name="inputVariables")
    def input_variables(
        self,
    ) -> Optional[
        Sequence[outputs.AgentPromptVariantTemplateConfigurationTextInputVariable]
    ]: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationTextCachePoint(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class AgentPromptVariantTemplateConfigurationTextInputVariable(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreAgentRuntimeAgentRuntimeArtifact(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code_configuration: Optional[
            outputs.AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfiguration
        ] = ...,
        container_configuration: Optional[
            outputs.AgentcoreAgentRuntimeAgentRuntimeArtifactContainerConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="codeConfiguration")
    def code_configuration(
        self,
    ) -> Optional[
        outputs.AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="containerConfiguration")
    def container_configuration(
        self,
    ) -> Optional[
        outputs.AgentcoreAgentRuntimeAgentRuntimeArtifactContainerConfiguration
    ]: ...

@pulumi.output_type
class AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        entry_points: Sequence[_builtins.str],
        runtime: _builtins.str,
        code: Optional[
            outputs.AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCode
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entryPoints")
    def entry_points(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def code(
        self,
    ) -> Optional[
        outputs.AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCode
    ]: ...

@pulumi.output_type
class AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCode(dict):
    def __init__(
        __self__,
        *,
        s3: Optional[
            outputs.AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCodeS3
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[
        outputs.AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCodeS3
    ]: ...

@pulumi.output_type
class AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCodeS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        prefix: _builtins.str,
        version_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreAgentRuntimeAgentRuntimeArtifactContainerConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, container_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerUri")
    def container_uri(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreAgentRuntimeAuthorizerConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_jwt_authorizer: Optional[
            outputs.AgentcoreAgentRuntimeAuthorizerConfigurationCustomJwtAuthorizer
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customJwtAuthorizer")
    def custom_jwt_authorizer(
        self,
    ) -> Optional[
        outputs.AgentcoreAgentRuntimeAuthorizerConfigurationCustomJwtAuthorizer
    ]: ...

@pulumi.output_type
class AgentcoreAgentRuntimeAuthorizerConfigurationCustomJwtAuthorizer(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        discovery_url: _builtins.str,
        allowed_audiences: Optional[Sequence[_builtins.str]] = ...,
        allowed_clients: Optional[Sequence[_builtins.str]] = ...,
        allowed_scopes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedClients")
    def allowed_clients(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedScopes")
    def allowed_scopes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AgentcoreAgentRuntimeEndpointTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreAgentRuntimeLifecycleConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle_runtime_session_timeout: _builtins.int,
        max_lifetime: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleRuntimeSessionTimeout")
    def idle_runtime_session_timeout(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxLifetime")
    def max_lifetime(self) -> _builtins.int: ...

@pulumi.output_type
class AgentcoreAgentRuntimeNetworkConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network_mode: _builtins.str,
        network_mode_config: Optional[
            outputs.AgentcoreAgentRuntimeNetworkConfigurationNetworkModeConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkMode")
    def network_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkModeConfig")
    def network_mode_config(
        self,
    ) -> Optional[
        outputs.AgentcoreAgentRuntimeNetworkConfigurationNetworkModeConfig
    ]: ...

@pulumi.output_type
class AgentcoreAgentRuntimeNetworkConfigurationNetworkModeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_groups: Sequence[_builtins.str],
        subnets: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class AgentcoreAgentRuntimeProtocolConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, server_protocol: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serverProtocol")
    def server_protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreAgentRuntimeRequestHeaderConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, request_header_allowlists: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requestHeaderAllowlists")
    def request_header_allowlists(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AgentcoreAgentRuntimeTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreAgentRuntimeWorkloadIdentityDetail(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, workload_identity_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityArn")
    def workload_identity_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreApiKeyCredentialProviderApiKeySecretArn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreBrowserNetworkConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network_mode: _builtins.str,
        vpc_config: Optional[
            outputs.AgentcoreBrowserNetworkConfigurationVpcConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkMode")
    def network_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(
        self,
    ) -> Optional[outputs.AgentcoreBrowserNetworkConfigurationVpcConfig]: ...

@pulumi.output_type
class AgentcoreBrowserNetworkConfigurationVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_groups: Sequence[_builtins.str],
        subnets: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class AgentcoreBrowserRecording(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        s3_location: Optional[outputs.AgentcoreBrowserRecordingS3Location] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="s3Location")
    def s3_location(self) -> Optional[outputs.AgentcoreBrowserRecordingS3Location]: ...

@pulumi.output_type
class AgentcoreBrowserRecordingS3Location(dict):
    def __init__(__self__, *, bucket: _builtins.str, prefix: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreBrowserTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreCodeInterpreterNetworkConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network_mode: _builtins.str,
        vpc_config: Optional[
            outputs.AgentcoreCodeInterpreterNetworkConfigurationVpcConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkMode")
    def network_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(
        self,
    ) -> Optional[outputs.AgentcoreCodeInterpreterNetworkConfigurationVpcConfig]: ...

@pulumi.output_type
class AgentcoreCodeInterpreterNetworkConfigurationVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_groups: Sequence[_builtins.str],
        subnets: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class AgentcoreCodeInterpreterTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreGatewayAuthorizerConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_jwt_authorizer: Optional[
            outputs.AgentcoreGatewayAuthorizerConfigurationCustomJwtAuthorizer
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customJwtAuthorizer")
    def custom_jwt_authorizer(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayAuthorizerConfigurationCustomJwtAuthorizer
    ]: ...

@pulumi.output_type
class AgentcoreGatewayAuthorizerConfigurationCustomJwtAuthorizer(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_scopes: Sequence[_builtins.str],
        discovery_url: _builtins.str,
        allowed_audiences: Optional[Sequence[_builtins.str]] = ...,
        allowed_clients: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedScopes")
    def allowed_scopes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedClients")
    def allowed_clients(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AgentcoreGatewayInterceptorConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        interception_points: Sequence[_builtins.str],
        input_configuration: Optional[
            outputs.AgentcoreGatewayInterceptorConfigurationInputConfiguration
        ] = ...,
        interceptor: Optional[
            outputs.AgentcoreGatewayInterceptorConfigurationInterceptor
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="interceptionPoints")
    def interception_points(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputConfiguration")
    def input_configuration(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayInterceptorConfigurationInputConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter
    def interceptor(
        self,
    ) -> Optional[outputs.AgentcoreGatewayInterceptorConfigurationInterceptor]: ...

@pulumi.output_type
class AgentcoreGatewayInterceptorConfigurationInputConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, pass_request_headers: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="passRequestHeaders")
    def pass_request_headers(self) -> _builtins.bool: ...

@pulumi.output_type
class AgentcoreGatewayInterceptorConfigurationInterceptor(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        lambda_: Optional[
            outputs.AgentcoreGatewayInterceptorConfigurationInterceptorLambda
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayInterceptorConfigurationInterceptorLambda
    ]: ...

@pulumi.output_type
class AgentcoreGatewayInterceptorConfigurationInterceptorLambda(dict):
    def __init__(__self__, *, arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreGatewayProtocolConfiguration(dict):
    def __init__(
        __self__,
        *,
        mcp: Optional[outputs.AgentcoreGatewayProtocolConfigurationMcp] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mcp(self) -> Optional[outputs.AgentcoreGatewayProtocolConfigurationMcp]: ...

@pulumi.output_type
class AgentcoreGatewayProtocolConfigurationMcp(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instructions: Optional[_builtins.str] = ...,
        search_type: Optional[_builtins.str] = ...,
        supported_versions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instructions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="searchType")
    def search_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportedVersions")
    def supported_versions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AgentcoreGatewayTargetCredentialProviderConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_key: Optional[
            outputs.AgentcoreGatewayTargetCredentialProviderConfigurationApiKey
        ] = ...,
        gateway_iam_role: Optional[
            outputs.AgentcoreGatewayTargetCredentialProviderConfigurationGatewayIamRole
        ] = ...,
        oauth: Optional[
            outputs.AgentcoreGatewayTargetCredentialProviderConfigurationOauth
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetCredentialProviderConfigurationApiKey
    ]: ...
    @_builtins.property
    @pulumi.getter(name="gatewayIamRole")
    def gateway_iam_role(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetCredentialProviderConfigurationGatewayIamRole
    ]: ...
    @_builtins.property
    @pulumi.getter
    def oauth(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetCredentialProviderConfigurationOauth
    ]: ...

@pulumi.output_type
class AgentcoreGatewayTargetCredentialProviderConfigurationApiKey(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provider_arn: _builtins.str,
        credential_location: Optional[_builtins.str] = ...,
        credential_parameter_name: Optional[_builtins.str] = ...,
        credential_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="providerArn")
    def provider_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="credentialLocation")
    def credential_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="credentialParameterName")
    def credential_parameter_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="credentialPrefix")
    def credential_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreGatewayTargetCredentialProviderConfigurationGatewayIamRole(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class AgentcoreGatewayTargetCredentialProviderConfigurationOauth(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provider_arn: _builtins.str,
        scopes: Sequence[_builtins.str],
        custom_parameters: Optional[Mapping[str, _builtins.str]] = ...,
        default_return_url: Optional[_builtins.str] = ...,
        grant_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="providerArn")
    def provider_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customParameters")
    def custom_parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultReturnUrl")
    def default_return_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="grantType")
    def grant_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreGatewayTargetMetadataConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_query_parameters: Optional[Sequence[_builtins.str]] = ...,
        allowed_request_headers: Optional[Sequence[_builtins.str]] = ...,
        allowed_response_headers: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedQueryParameters")
    def allowed_query_parameters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedRequestHeaders")
    def allowed_request_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedResponseHeaders")
    def allowed_response_headers(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfiguration(dict):
    def __init__(
        __self__,
        *,
        mcp: Optional[outputs.AgentcoreGatewayTargetTargetConfigurationMcp] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mcp(self) -> Optional[outputs.AgentcoreGatewayTargetTargetConfigurationMcp]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcp(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        lambda_: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambda
        ] = ...,
        mcp_server: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpMcpServer
        ] = ...,
        open_api_schema: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchema
        ] = ...,
        smithy_model: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpSmithyModel
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(
        self,
    ) -> Optional[outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambda]: ...
    @_builtins.property
    @pulumi.getter(name="mcpServer")
    def mcp_server(
        self,
    ) -> Optional[outputs.AgentcoreGatewayTargetTargetConfigurationMcpMcpServer]: ...
    @_builtins.property
    @pulumi.getter(name="openApiSchema")
    def open_api_schema(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchema
    ]: ...
    @_builtins.property
    @pulumi.getter(name="smithyModel")
    def smithy_model(
        self,
    ) -> Optional[outputs.AgentcoreGatewayTargetTargetConfigurationMcpSmithyModel]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambda(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        lambda_arn: _builtins.str,
        tool_schema: outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchema,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="toolSchema")
    def tool_schema(
        self,
    ) -> outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchema: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        inline_payloads: Optional[
            Sequence[
                outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayload
            ]
        ] = ...,
        s3: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaS3
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inlinePayloads")
    def inline_payloads(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayload
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaS3
    ]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayload(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        input_schema: outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchema,
        name: _builtins.str,
        output_schema: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchema
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputSchema")
    def input_schema(
        self,
    ) -> outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchema: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outputSchema")
    def output_schema(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchema
    ]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchema(
    dict
):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItems
        ] = ...,
        properties: Optional[
            Sequence[
                outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaProperty
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItems
    ]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaProperty
        ]
    ]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItems(
    dict
):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsItems
        ] = ...,
        properties: Optional[
            Sequence[
                outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsProperty
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsItems
    ]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsProperty
        ]
    ]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsItems(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items_json: Optional[_builtins.str] = ...,
        properties_json: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsProperty(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items_json: Optional[_builtins.str] = ...,
        properties_json: Optional[_builtins.str] = ...,
        required: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaProperty(
    dict
):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItems
        ] = ...,
        properties: Optional[
            Sequence[
                outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyProperty
            ]
        ] = ...,
        required: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItems
    ]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyProperty
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItems(
    dict
):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsItems
        ] = ...,
        properties: Optional[
            Sequence[
                outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsProperty
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsItems
    ]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsProperty
        ]
    ]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsItems(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items_json: Optional[_builtins.str] = ...,
        properties_json: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsProperty(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items_json: Optional[_builtins.str] = ...,
        properties_json: Optional[_builtins.str] = ...,
        required: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyProperty(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items_json: Optional[_builtins.str] = ...,
        properties_json: Optional[_builtins.str] = ...,
        required: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchema(
    dict
):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItems
        ] = ...,
        properties: Optional[
            Sequence[
                outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaProperty
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItems
    ]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaProperty
        ]
    ]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItems(
    dict
):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsItems
        ] = ...,
        properties: Optional[
            Sequence[
                outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsProperty
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsItems
    ]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsProperty
        ]
    ]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsItems(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items_json: Optional[_builtins.str] = ...,
        properties_json: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsProperty(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items_json: Optional[_builtins.str] = ...,
        properties_json: Optional[_builtins.str] = ...,
        required: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaProperty(
    dict
):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItems
        ] = ...,
        properties: Optional[
            Sequence[
                outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyProperty
            ]
        ] = ...,
        required: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItems
    ]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyProperty
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItems(
    dict
):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsItems
        ] = ...,
        properties: Optional[
            Sequence[
                outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsProperty
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsItems
    ]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsProperty
        ]
    ]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsItems(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items_json: Optional[_builtins.str] = ...,
        properties_json: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsProperty(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items_json: Optional[_builtins.str] = ...,
        properties_json: Optional[_builtins.str] = ...,
        required: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyProperty(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        description: Optional[_builtins.str] = ...,
        items_json: Optional[_builtins.str] = ...,
        properties_json: Optional[_builtins.str] = ...,
        required: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_owner_account_id: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketOwnerAccountId")
    def bucket_owner_account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpMcpServer(dict):
    def __init__(__self__, *, endpoint: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        inline_payload: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaInlinePayload
        ] = ...,
        s3: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaS3
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inlinePayload")
    def inline_payload(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaInlinePayload
    ]: ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaS3
    ]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaInlinePayload(dict):
    def __init__(__self__, *, payload: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_owner_account_id: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketOwnerAccountId")
    def bucket_owner_account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpSmithyModel(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        inline_payload: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelInlinePayload
        ] = ...,
        s3: Optional[
            outputs.AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelS3
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inlinePayload")
    def inline_payload(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelInlinePayload
    ]: ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[
        outputs.AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelS3
    ]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelInlinePayload(dict):
    def __init__(__self__, *, payload: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_owner_account_id: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketOwnerAccountId")
    def bucket_owner_account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreGatewayTargetTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreGatewayTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreGatewayWorkloadIdentityDetail(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, workload_identity_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityArn")
    def workload_identity_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreMemoryStrategyConfiguration(dict):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        consolidation: Optional[
            outputs.AgentcoreMemoryStrategyConfigurationConsolidation
        ] = ...,
        extraction: Optional[
            outputs.AgentcoreMemoryStrategyConfigurationExtraction
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def consolidation(
        self,
    ) -> Optional[outputs.AgentcoreMemoryStrategyConfigurationConsolidation]: ...
    @_builtins.property
    @pulumi.getter
    def extraction(
        self,
    ) -> Optional[outputs.AgentcoreMemoryStrategyConfigurationExtraction]: ...

@pulumi.output_type
class AgentcoreMemoryStrategyConfigurationConsolidation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, append_to_prompt: _builtins.str, model_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appendToPrompt")
    def append_to_prompt(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreMemoryStrategyConfigurationExtraction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, append_to_prompt: _builtins.str, model_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appendToPrompt")
    def append_to_prompt(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreMemoryStrategyTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreMemoryTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderClientSecretArn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_oauth2_provider_config: Optional[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfig
        ] = ...,
        github_oauth2_provider_config: Optional[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfig
        ] = ...,
        google_oauth2_provider_config: Optional[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfig
        ] = ...,
        microsoft_oauth2_provider_config: Optional[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfig
        ] = ...,
        salesforce_oauth2_provider_config: Optional[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfig
        ] = ...,
        slack_oauth2_provider_config: Optional[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customOauth2ProviderConfig")
    def custom_oauth2_provider_config(
        self,
    ) -> Optional[
        outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="githubOauth2ProviderConfig")
    def github_oauth2_provider_config(
        self,
    ) -> Optional[
        outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="googleOauth2ProviderConfig")
    def google_oauth2_provider_config(
        self,
    ) -> Optional[
        outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="microsoftOauth2ProviderConfig")
    def microsoft_oauth2_provider_config(
        self,
    ) -> Optional[
        outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="salesforceOauth2ProviderConfig")
    def salesforce_oauth2_provider_config(
        self,
    ) -> Optional[
        outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="slackOauth2ProviderConfig")
    def slack_oauth2_provider_config(
        self,
    ) -> Optional[
        outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfig
    ]: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_credentials_wo_version: Optional[_builtins.int] = ...,
        client_id: Optional[_builtins.str] = ...,
        client_id_wo: Optional[_builtins.str] = ...,
        client_secret: Optional[_builtins.str] = ...,
        client_secret_wo: Optional[_builtins.str] = ...,
        oauth_discovery: Optional[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscovery
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCredentialsWoVersion")
    def client_credentials_wo_version(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientIdWo")
    def client_id_wo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretWo")
    def client_secret_wo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthDiscovery")
    def oauth_discovery(
        self,
    ) -> Optional[
        outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscovery
    ]: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscovery(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_server_metadata: Optional[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata
        ] = ...,
        discovery_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationServerMetadata")
    def authorization_server_metadata(
        self,
    ) -> Optional[
        outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata
    ]: ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_endpoint: _builtins.str,
        issuer: _builtins.str,
        token_endpoint: _builtins.str,
        response_types: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="responseTypes")
    def response_types(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_credentials_wo_version: Optional[_builtins.int] = ...,
        client_id: Optional[_builtins.str] = ...,
        client_id_wo: Optional[_builtins.str] = ...,
        client_secret: Optional[_builtins.str] = ...,
        client_secret_wo: Optional[_builtins.str] = ...,
        oauth_discoveries: Optional[
            Sequence[
                outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscovery
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCredentialsWoVersion")
    def client_credentials_wo_version(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientIdWo")
    def client_id_wo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretWo")
    def client_secret_wo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthDiscoveries")
    def oauth_discoveries(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscovery
        ]
    ]: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscovery(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_server_metadatas: Sequence[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata
        ],
        discovery_url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationServerMetadatas")
    def authorization_server_metadatas(
        self,
    ) -> Sequence[
        outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata
    ]: ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_endpoint: _builtins.str,
        issuer: _builtins.str,
        response_types: Sequence[_builtins.str],
        token_endpoint: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="responseTypes")
    def response_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_credentials_wo_version: Optional[_builtins.int] = ...,
        client_id: Optional[_builtins.str] = ...,
        client_id_wo: Optional[_builtins.str] = ...,
        client_secret: Optional[_builtins.str] = ...,
        client_secret_wo: Optional[_builtins.str] = ...,
        oauth_discoveries: Optional[
            Sequence[
                outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscovery
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCredentialsWoVersion")
    def client_credentials_wo_version(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientIdWo")
    def client_id_wo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretWo")
    def client_secret_wo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthDiscoveries")
    def oauth_discoveries(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscovery
        ]
    ]: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscovery(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_server_metadatas: Sequence[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata
        ],
        discovery_url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationServerMetadatas")
    def authorization_server_metadatas(
        self,
    ) -> Sequence[
        outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata
    ]: ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_endpoint: _builtins.str,
        issuer: _builtins.str,
        response_types: Sequence[_builtins.str],
        token_endpoint: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="responseTypes")
    def response_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_credentials_wo_version: Optional[_builtins.int] = ...,
        client_id: Optional[_builtins.str] = ...,
        client_id_wo: Optional[_builtins.str] = ...,
        client_secret: Optional[_builtins.str] = ...,
        client_secret_wo: Optional[_builtins.str] = ...,
        oauth_discoveries: Optional[
            Sequence[
                outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscovery
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCredentialsWoVersion")
    def client_credentials_wo_version(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientIdWo")
    def client_id_wo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretWo")
    def client_secret_wo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthDiscoveries")
    def oauth_discoveries(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscovery
        ]
    ]: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscovery(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_server_metadatas: Sequence[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata
        ],
        discovery_url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationServerMetadatas")
    def authorization_server_metadatas(
        self,
    ) -> Sequence[
        outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata
    ]: ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_endpoint: _builtins.str,
        issuer: _builtins.str,
        response_types: Sequence[_builtins.str],
        token_endpoint: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="responseTypes")
    def response_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_credentials_wo_version: Optional[_builtins.int] = ...,
        client_id: Optional[_builtins.str] = ...,
        client_id_wo: Optional[_builtins.str] = ...,
        client_secret: Optional[_builtins.str] = ...,
        client_secret_wo: Optional[_builtins.str] = ...,
        oauth_discoveries: Optional[
            Sequence[
                outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscovery
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCredentialsWoVersion")
    def client_credentials_wo_version(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientIdWo")
    def client_id_wo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretWo")
    def client_secret_wo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthDiscoveries")
    def oauth_discoveries(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscovery
        ]
    ]: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscovery(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_server_metadatas: Sequence[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata
        ],
        discovery_url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationServerMetadatas")
    def authorization_server_metadatas(
        self,
    ) -> Sequence[
        outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata
    ]: ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_endpoint: _builtins.str,
        issuer: _builtins.str,
        response_types: Sequence[_builtins.str],
        token_endpoint: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="responseTypes")
    def response_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_credentials_wo_version: Optional[_builtins.int] = ...,
        client_id: Optional[_builtins.str] = ...,
        client_id_wo: Optional[_builtins.str] = ...,
        client_secret: Optional[_builtins.str] = ...,
        client_secret_wo: Optional[_builtins.str] = ...,
        oauth_discoveries: Optional[
            Sequence[
                outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscovery
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCredentialsWoVersion")
    def client_credentials_wo_version(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientIdWo")
    def client_id_wo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretWo")
    def client_secret_wo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthDiscoveries")
    def oauth_discoveries(
        self,
    ) -> Optional[
        Sequence[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscovery
        ]
    ]: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscovery(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_server_metadatas: Sequence[
            outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata
        ],
        discovery_url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationServerMetadatas")
    def authorization_server_metadatas(
        self,
    ) -> Sequence[
        outputs.AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata
    ]: ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadata(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_endpoint: _builtins.str,
        issuer: _builtins.str,
        response_types: Sequence[_builtins.str],
        token_endpoint: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="responseTypes")
    def response_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class AgentcoreTokenVaultCmkKmsConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, key_type: _builtins.str, kms_key_arn: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomModelOutputDataConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, s3_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...

@pulumi.output_type
class CustomModelTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomModelTrainingDataConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, s3_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...

@pulumi.output_type
class CustomModelTrainingMetric(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, training_loss: _builtins.float) -> None: ...
    @_builtins.property
    @pulumi.getter(name="trainingLoss")
    def training_loss(self) -> _builtins.float: ...

@pulumi.output_type
class CustomModelValidationDataConfig(dict):
    def __init__(
        __self__,
        *,
        validators: Sequence[outputs.CustomModelValidationDataConfigValidator],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validators(
        self,
    ) -> Sequence[outputs.CustomModelValidationDataConfigValidator]: ...

@pulumi.output_type
class CustomModelValidationDataConfigValidator(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, s3_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...

@pulumi.output_type
class CustomModelValidationMetric(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, validation_loss: _builtins.float) -> None: ...
    @_builtins.property
    @pulumi.getter(name="validationLoss")
    def validation_loss(self) -> _builtins.float: ...

@pulumi.output_type
class CustomModelVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Sequence[_builtins.str],
        subnet_ids: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GuardrailContentPolicyConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        filters_configs: Optional[
            Sequence[outputs.GuardrailContentPolicyConfigFiltersConfig]
        ] = ...,
        tier_configs: Optional[
            Sequence[outputs.GuardrailContentPolicyConfigTierConfig]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filtersConfigs")
    def filters_configs(
        self,
    ) -> Optional[Sequence[outputs.GuardrailContentPolicyConfigFiltersConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="tierConfigs")
    def tier_configs(
        self,
    ) -> Optional[Sequence[outputs.GuardrailContentPolicyConfigTierConfig]]: ...

@pulumi.output_type
class GuardrailContentPolicyConfigFiltersConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        input_strength: _builtins.str,
        output_strength: _builtins.str,
        type: _builtins.str,
        input_action: Optional[_builtins.str] = ...,
        input_enabled: Optional[_builtins.bool] = ...,
        input_modalities: Optional[Sequence[_builtins.str]] = ...,
        output_action: Optional[_builtins.str] = ...,
        output_enabled: Optional[_builtins.bool] = ...,
        output_modalities: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputStrength")
    def input_strength(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outputStrength")
    def output_strength(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputAction")
    def input_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputEnabled")
    def input_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="inputModalities")
    def input_modalities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="outputAction")
    def output_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputEnabled")
    def output_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="outputModalities")
    def output_modalities(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GuardrailContentPolicyConfigTierConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, tier_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tierName")
    def tier_name(self) -> _builtins.str: ...

@pulumi.output_type
class GuardrailContextualGroundingPolicyConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        filters_configs: Optional[
            Sequence[outputs.GuardrailContextualGroundingPolicyConfigFiltersConfig]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filtersConfigs")
    def filters_configs(
        self,
    ) -> Optional[
        Sequence[outputs.GuardrailContextualGroundingPolicyConfigFiltersConfig]
    ]: ...

@pulumi.output_type
class GuardrailContextualGroundingPolicyConfigFiltersConfig(dict):
    def __init__(
        __self__, *, threshold: _builtins.float, type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GuardrailCrossRegionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, guardrail_profile_identifier: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="guardrailProfileIdentifier")
    def guardrail_profile_identifier(self) -> _builtins.str: ...

@pulumi.output_type
class GuardrailSensitiveInformationPolicyConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        pii_entities_configs: Optional[
            Sequence[outputs.GuardrailSensitiveInformationPolicyConfigPiiEntitiesConfig]
        ] = ...,
        regexes_configs: Optional[
            Sequence[outputs.GuardrailSensitiveInformationPolicyConfigRegexesConfig]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="piiEntitiesConfigs")
    def pii_entities_configs(
        self,
    ) -> Optional[
        Sequence[outputs.GuardrailSensitiveInformationPolicyConfigPiiEntitiesConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="regexesConfigs")
    def regexes_configs(
        self,
    ) -> Optional[
        Sequence[outputs.GuardrailSensitiveInformationPolicyConfigRegexesConfig]
    ]: ...

@pulumi.output_type
class GuardrailSensitiveInformationPolicyConfigPiiEntitiesConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        type: _builtins.str,
        input_action: Optional[_builtins.str] = ...,
        input_enabled: Optional[_builtins.bool] = ...,
        output_action: Optional[_builtins.str] = ...,
        output_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputAction")
    def input_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputEnabled")
    def input_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="outputAction")
    def output_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputEnabled")
    def output_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class GuardrailSensitiveInformationPolicyConfigRegexesConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        name: _builtins.str,
        pattern: _builtins.str,
        description: Optional[_builtins.str] = ...,
        input_action: Optional[_builtins.str] = ...,
        input_enabled: Optional[_builtins.bool] = ...,
        output_action: Optional[_builtins.str] = ...,
        output_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputAction")
    def input_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputEnabled")
    def input_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="outputAction")
    def output_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputEnabled")
    def output_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class GuardrailTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuardrailTopicPolicyConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        tier_configs: Optional[
            Sequence[outputs.GuardrailTopicPolicyConfigTierConfig]
        ] = ...,
        topics_configs: Optional[
            Sequence[outputs.GuardrailTopicPolicyConfigTopicsConfig]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tierConfigs")
    def tier_configs(
        self,
    ) -> Optional[Sequence[outputs.GuardrailTopicPolicyConfigTierConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="topicsConfigs")
    def topics_configs(
        self,
    ) -> Optional[Sequence[outputs.GuardrailTopicPolicyConfigTopicsConfig]]: ...

@pulumi.output_type
class GuardrailTopicPolicyConfigTierConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, tier_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tierName")
    def tier_name(self) -> _builtins.str: ...

@pulumi.output_type
class GuardrailTopicPolicyConfigTopicsConfig(dict):
    def __init__(
        __self__,
        *,
        definition: _builtins.str,
        name: _builtins.str,
        type: _builtins.str,
        examples: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def definition(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def examples(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GuardrailVersionTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GuardrailWordPolicyConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        managed_word_lists_configs: Optional[
            Sequence[outputs.GuardrailWordPolicyConfigManagedWordListsConfig]
        ] = ...,
        words_configs: Optional[
            Sequence[outputs.GuardrailWordPolicyConfigWordsConfig]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedWordListsConfigs")
    def managed_word_lists_configs(
        self,
    ) -> Optional[
        Sequence[outputs.GuardrailWordPolicyConfigManagedWordListsConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="wordsConfigs")
    def words_configs(
        self,
    ) -> Optional[Sequence[outputs.GuardrailWordPolicyConfigWordsConfig]]: ...

@pulumi.output_type
class GuardrailWordPolicyConfigManagedWordListsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        input_action: Optional[_builtins.str] = ...,
        input_enabled: Optional[_builtins.bool] = ...,
        output_action: Optional[_builtins.str] = ...,
        output_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputAction")
    def input_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputEnabled")
    def input_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="outputAction")
    def output_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputEnabled")
    def output_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class GuardrailWordPolicyConfigWordsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        text: _builtins.str,
        input_action: Optional[_builtins.str] = ...,
        input_enabled: Optional[_builtins.bool] = ...,
        output_action: Optional[_builtins.str] = ...,
        output_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputAction")
    def input_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputEnabled")
    def input_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="outputAction")
    def output_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputEnabled")
    def output_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class InferenceProfileModel(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, model_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelArn")
    def model_arn(self) -> _builtins.str: ...

@pulumi.output_type
class InferenceProfileModelSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, copy_from: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="copyFrom")
    def copy_from(self) -> _builtins.str: ...

@pulumi.output_type
class InferenceProfileTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProvisionedModelThroughputTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetAgentAgentVersionsAgentVersionSummaryResult(dict):
    def __init__(
        __self__,
        *,
        agent_name: _builtins.str,
        agent_status: _builtins.str,
        agent_version: _builtins.str,
        created_at: _builtins.str,
        description: _builtins.str,
        updated_at: _builtins.str,
        guardrail_configurations: Optional[
            Sequence[
                outputs.GetAgentAgentVersionsAgentVersionSummaryGuardrailConfigurationResult
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentName")
    def agent_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="agentStatus")
    def agent_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="guardrailConfigurations")
    def guardrail_configurations(
        self,
    ) -> Optional[
        Sequence[
            outputs.GetAgentAgentVersionsAgentVersionSummaryGuardrailConfigurationResult
        ]
    ]: ...

@pulumi.output_type
class GetAgentAgentVersionsAgentVersionSummaryGuardrailConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        guardrail_identifier: _builtins.str,
        guardrail_version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="guardrailIdentifier")
    def guardrail_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="guardrailVersion")
    def guardrail_version(self) -> _builtins.str: ...

@pulumi.output_type
class GetCustomModelOutputDataConfigResult(dict):
    def __init__(__self__, *, s3_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetCustomModelTrainingDataConfigResult(dict):
    def __init__(__self__, *, s3_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetCustomModelTrainingMetricResult(dict):
    def __init__(__self__, *, training_loss: _builtins.float) -> None: ...
    @_builtins.property
    @pulumi.getter(name="trainingLoss")
    def training_loss(self) -> _builtins.float: ...

@pulumi.output_type
class GetCustomModelValidationDataConfigResult(dict):
    def __init__(
        __self__,
        *,
        validators: Sequence[outputs.GetCustomModelValidationDataConfigValidatorResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validators(
        self,
    ) -> Sequence[outputs.GetCustomModelValidationDataConfigValidatorResult]: ...

@pulumi.output_type
class GetCustomModelValidationDataConfigValidatorResult(dict):
    def __init__(__self__, *, s3_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetCustomModelValidationMetricResult(dict):
    def __init__(__self__, *, validation_loss: _builtins.float) -> None: ...
    @_builtins.property
    @pulumi.getter(name="validationLoss")
    def validation_loss(self) -> _builtins.float: ...

@pulumi.output_type
class GetCustomModelsModelSummaryResult(dict):
    def __init__(
        __self__,
        *,
        creation_time: _builtins.str,
        model_arn: _builtins.str,
        model_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelArn")
    def model_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelName")
    def model_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetInferenceProfileModelResult(dict):
    def __init__(__self__, *, model_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelArn")
    def model_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetInferenceProfilesInferenceProfileSummaryResult(dict):
    def __init__(
        __self__,
        *,
        created_at: _builtins.str,
        description: _builtins.str,
        inference_profile_arn: _builtins.str,
        inference_profile_id: _builtins.str,
        inference_profile_name: _builtins.str,
        models: Sequence[
            outputs.GetInferenceProfilesInferenceProfileSummaryModelResult
        ],
        status: _builtins.str,
        type: _builtins.str,
        updated_at: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inferenceProfileArn")
    def inference_profile_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inferenceProfileId")
    def inference_profile_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inferenceProfileName")
    def inference_profile_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def models(
        self,
    ) -> Sequence[outputs.GetInferenceProfilesInferenceProfileSummaryModelResult]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str: ...

@pulumi.output_type
class GetInferenceProfilesInferenceProfileSummaryModelResult(dict):
    def __init__(__self__, *, model_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelArn")
    def model_arn(self) -> _builtins.str: ...
