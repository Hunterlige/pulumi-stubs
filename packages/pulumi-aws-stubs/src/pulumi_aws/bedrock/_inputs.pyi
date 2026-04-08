import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AgentAgentActionGroupActionGroupExecutorArgs",
    "AgentAgentActionGroupActionGroupExecutorArgsDict",
    "AgentAgentActionGroupApiSchemaArgs",
    "AgentAgentActionGroupApiSchemaArgsDict",
    "AgentAgentActionGroupApiSchemaS3Args",
    "AgentAgentActionGroupApiSchemaS3ArgsDict",
    "AgentAgentActionGroupFunctionSchemaArgs",
    "AgentAgentActionGroupFunctionSchemaArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AgentAgentActionGroupTimeoutsArgs",
    "AgentAgentActionGroupTimeoutsArgsDict",
    "AgentAgentAliasRoutingConfigurationArgs",
    "AgentAgentAliasRoutingConfigurationArgsDict",
    "AgentAgentAliasTimeoutsArgs",
    "AgentAgentAliasTimeoutsArgsDict",
    "AgentAgentCollaboratorAgentDescriptorArgs",
    "AgentAgentCollaboratorAgentDescriptorArgsDict",
    "AgentAgentCollaboratorTimeoutsArgs",
    "AgentAgentCollaboratorTimeoutsArgsDict",
    "AgentAgentGuardrailConfigurationArgs",
    "AgentAgentGuardrailConfigurationArgsDict",
    "AgentAgentKnowledgeBaseAssociationTimeoutsArgs",
    "AgentAgentKnowledgeBaseAssociationTimeoutsArgsDict",
    "AgentAgentMemoryConfigurationArgs",
    "AgentAgentMemoryConfigurationArgsDict",
    ...,
    ...,
    "AgentAgentPromptOverrideConfigurationArgs",
    "AgentAgentPromptOverrideConfigurationArgsDict",
    ...,
    ...,
    ...,
    ...,
    "AgentAgentTimeoutsArgs",
    "AgentAgentTimeoutsArgsDict",
    "AgentDataSourceDataSourceConfigurationArgs",
    "AgentDataSourceDataSourceConfigurationArgsDict",
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
    "AgentDataSourceTimeoutsArgs",
    "AgentDataSourceTimeoutsArgsDict",
    "AgentDataSourceVectorIngestionConfigurationArgs",
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
    ...,
    ...,
    ...,
    "AgentFlowDefinitionArgs",
    "AgentFlowDefinitionArgsDict",
    "AgentFlowDefinitionConnectionArgs",
    "AgentFlowDefinitionConnectionArgsDict",
    "AgentFlowDefinitionConnectionConfigurationArgs",
    "AgentFlowDefinitionConnectionConfigurationArgsDict",
    ...,
    ...,
    "AgentFlowDefinitionConnectionConfigurationDataArgs",
    ...,
    "AgentFlowDefinitionNodeArgs",
    "AgentFlowDefinitionNodeArgsDict",
    "AgentFlowDefinitionNodeConfigurationArgs",
    "AgentFlowDefinitionNodeConfigurationArgsDict",
    "AgentFlowDefinitionNodeConfigurationAgentArgs",
    "AgentFlowDefinitionNodeConfigurationAgentArgsDict",
    "AgentFlowDefinitionNodeConfigurationCollectorArgs",
    ...,
    "AgentFlowDefinitionNodeConfigurationConditionArgs",
    ...,
    ...,
    ...,
    "AgentFlowDefinitionNodeConfigurationInlineCodeArgs",
    ...,
    "AgentFlowDefinitionNodeConfigurationInputArgs",
    "AgentFlowDefinitionNodeConfigurationInputArgsDict",
    "AgentFlowDefinitionNodeConfigurationIteratorArgs",
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
    "AgentFlowDefinitionNodeConfigurationLexArgs",
    "AgentFlowDefinitionNodeConfigurationLexArgsDict",
    "AgentFlowDefinitionNodeConfigurationOutputArgs",
    "AgentFlowDefinitionNodeConfigurationOutputArgsDict",
    "AgentFlowDefinitionNodeConfigurationPromptArgs",
    "AgentFlowDefinitionNodeConfigurationPromptArgsDict",
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
    "AgentFlowDefinitionNodeConfigurationRetrievalArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "AgentFlowDefinitionNodeConfigurationStorageArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "AgentFlowDefinitionNodeInputArgs",
    "AgentFlowDefinitionNodeInputArgsDict",
    "AgentFlowDefinitionNodeOutputArgs",
    "AgentFlowDefinitionNodeOutputArgsDict",
    "AgentFlowTimeoutsArgs",
    "AgentFlowTimeoutsArgsDict",
    "AgentKnowledgeBaseKnowledgeBaseConfigurationArgs",
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
    "AgentKnowledgeBaseStorageConfigurationArgs",
    "AgentKnowledgeBaseStorageConfigurationArgsDict",
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
    ...,
    ...,
    "AgentKnowledgeBaseTimeoutsArgs",
    "AgentKnowledgeBaseTimeoutsArgsDict",
    "AgentPromptVariantArgs",
    "AgentPromptVariantArgsDict",
    "AgentPromptVariantGenAiResourceArgs",
    "AgentPromptVariantGenAiResourceArgsDict",
    "AgentPromptVariantGenAiResourceAgentArgs",
    "AgentPromptVariantGenAiResourceAgentArgsDict",
    "AgentPromptVariantInferenceConfigurationArgs",
    "AgentPromptVariantInferenceConfigurationArgsDict",
    "AgentPromptVariantInferenceConfigurationTextArgs",
    ...,
    "AgentPromptVariantMetadataArgs",
    "AgentPromptVariantMetadataArgsDict",
    "AgentPromptVariantTemplateConfigurationArgs",
    "AgentPromptVariantTemplateConfigurationArgsDict",
    "AgentPromptVariantTemplateConfigurationChatArgs",
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
    ...,
    ...,
    ...,
    "AgentPromptVariantTemplateConfigurationTextArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "AgentcoreAgentRuntimeAgentRuntimeArtifactArgs",
    "AgentcoreAgentRuntimeAgentRuntimeArtifactArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AgentcoreAgentRuntimeAuthorizerConfigurationArgs",
    ...,
    ...,
    ...,
    "AgentcoreAgentRuntimeEndpointTimeoutsArgs",
    "AgentcoreAgentRuntimeEndpointTimeoutsArgsDict",
    "AgentcoreAgentRuntimeLifecycleConfigurationArgs",
    ...,
    "AgentcoreAgentRuntimeNetworkConfigurationArgs",
    "AgentcoreAgentRuntimeNetworkConfigurationArgsDict",
    ...,
    ...,
    "AgentcoreAgentRuntimeProtocolConfigurationArgs",
    "AgentcoreAgentRuntimeProtocolConfigurationArgsDict",
    ...,
    ...,
    "AgentcoreAgentRuntimeTimeoutsArgs",
    "AgentcoreAgentRuntimeTimeoutsArgsDict",
    "AgentcoreAgentRuntimeWorkloadIdentityDetailArgs",
    ...,
    ...,
    ...,
    "AgentcoreBrowserNetworkConfigurationArgs",
    "AgentcoreBrowserNetworkConfigurationArgsDict",
    "AgentcoreBrowserNetworkConfigurationVpcConfigArgs",
    ...,
    "AgentcoreBrowserRecordingArgs",
    "AgentcoreBrowserRecordingArgsDict",
    "AgentcoreBrowserRecordingS3LocationArgs",
    "AgentcoreBrowserRecordingS3LocationArgsDict",
    "AgentcoreBrowserTimeoutsArgs",
    "AgentcoreBrowserTimeoutsArgsDict",
    "AgentcoreCodeInterpreterNetworkConfigurationArgs",
    ...,
    ...,
    ...,
    "AgentcoreCodeInterpreterTimeoutsArgs",
    "AgentcoreCodeInterpreterTimeoutsArgsDict",
    "AgentcoreGatewayAuthorizerConfigurationArgs",
    "AgentcoreGatewayAuthorizerConfigurationArgsDict",
    ...,
    ...,
    "AgentcoreGatewayInterceptorConfigurationArgs",
    "AgentcoreGatewayInterceptorConfigurationArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AgentcoreGatewayProtocolConfigurationArgs",
    "AgentcoreGatewayProtocolConfigurationArgsDict",
    "AgentcoreGatewayProtocolConfigurationMcpArgs",
    "AgentcoreGatewayProtocolConfigurationMcpArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AgentcoreGatewayTargetMetadataConfigurationArgs",
    ...,
    "AgentcoreGatewayTargetTargetConfigurationArgs",
    "AgentcoreGatewayTargetTargetConfigurationArgsDict",
    "AgentcoreGatewayTargetTargetConfigurationMcpArgs",
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
    ...,
    ...,
    ...,
    "AgentcoreGatewayTargetTimeoutsArgs",
    "AgentcoreGatewayTargetTimeoutsArgsDict",
    "AgentcoreGatewayTimeoutsArgs",
    "AgentcoreGatewayTimeoutsArgsDict",
    "AgentcoreGatewayWorkloadIdentityDetailArgs",
    "AgentcoreGatewayWorkloadIdentityDetailArgsDict",
    "AgentcoreMemoryStrategyConfigurationArgs",
    "AgentcoreMemoryStrategyConfigurationArgsDict",
    ...,
    ...,
    "AgentcoreMemoryStrategyConfigurationExtractionArgs",
    ...,
    "AgentcoreMemoryStrategyTimeoutsArgs",
    "AgentcoreMemoryStrategyTimeoutsArgsDict",
    "AgentcoreMemoryTimeoutsArgs",
    "AgentcoreMemoryTimeoutsArgsDict",
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
    "AgentcoreTokenVaultCmkKmsConfigurationArgs",
    "AgentcoreTokenVaultCmkKmsConfigurationArgsDict",
    "CustomModelOutputDataConfigArgs",
    "CustomModelOutputDataConfigArgsDict",
    "CustomModelTimeoutsArgs",
    "CustomModelTimeoutsArgsDict",
    "CustomModelTrainingDataConfigArgs",
    "CustomModelTrainingDataConfigArgsDict",
    "CustomModelTrainingMetricArgs",
    "CustomModelTrainingMetricArgsDict",
    "CustomModelValidationDataConfigArgs",
    "CustomModelValidationDataConfigArgsDict",
    "CustomModelValidationDataConfigValidatorArgs",
    "CustomModelValidationDataConfigValidatorArgsDict",
    "CustomModelValidationMetricArgs",
    "CustomModelValidationMetricArgsDict",
    "CustomModelVpcConfigArgs",
    "CustomModelVpcConfigArgsDict",
    "GuardrailContentPolicyConfigArgs",
    "GuardrailContentPolicyConfigArgsDict",
    "GuardrailContentPolicyConfigFiltersConfigArgs",
    "GuardrailContentPolicyConfigFiltersConfigArgsDict",
    "GuardrailContentPolicyConfigTierConfigArgs",
    "GuardrailContentPolicyConfigTierConfigArgsDict",
    "GuardrailContextualGroundingPolicyConfigArgs",
    "GuardrailContextualGroundingPolicyConfigArgsDict",
    ...,
    ...,
    "GuardrailCrossRegionConfigArgs",
    "GuardrailCrossRegionConfigArgsDict",
    "GuardrailSensitiveInformationPolicyConfigArgs",
    "GuardrailSensitiveInformationPolicyConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "GuardrailTimeoutsArgs",
    "GuardrailTimeoutsArgsDict",
    "GuardrailTopicPolicyConfigArgs",
    "GuardrailTopicPolicyConfigArgsDict",
    "GuardrailTopicPolicyConfigTierConfigArgs",
    "GuardrailTopicPolicyConfigTierConfigArgsDict",
    "GuardrailTopicPolicyConfigTopicsConfigArgs",
    "GuardrailTopicPolicyConfigTopicsConfigArgsDict",
    "GuardrailVersionTimeoutsArgs",
    "GuardrailVersionTimeoutsArgsDict",
    "GuardrailWordPolicyConfigArgs",
    "GuardrailWordPolicyConfigArgsDict",
    ...,
    ...,
    "GuardrailWordPolicyConfigWordsConfigArgs",
    "GuardrailWordPolicyConfigWordsConfigArgsDict",
    "InferenceProfileModelArgs",
    "InferenceProfileModelArgsDict",
    "InferenceProfileModelSourceArgs",
    "InferenceProfileModelSourceArgsDict",
    "InferenceProfileTimeoutsArgs",
    "InferenceProfileTimeoutsArgsDict",
    "ProvisionedModelThroughputTimeoutsArgs",
    "ProvisionedModelThroughputTimeoutsArgsDict",
    "GetAgentAgentVersionsAgentVersionSummaryArgs",
    "GetAgentAgentVersionsAgentVersionSummaryArgsDict",
    ...,
    ...,
]

class AgentAgentActionGroupActionGroupExecutorArgsDict(TypedDict):
    custom_control: NotRequired[pulumi.Input[_builtins.str]]
    lambda_: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentAgentActionGroupActionGroupExecutorArgs:
    def __init__(
        __self__,
        *,
        custom_control: Optional[pulumi.Input[_builtins.str]] = ...,
        lambda_: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customControl")
    def custom_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_control.setter
    def custom_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lambda_.setter
    def lambda_(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentAgentActionGroupApiSchemaArgsDict(TypedDict):
    payload: NotRequired[pulumi.Input[_builtins.str]]
    s3: NotRequired[pulumi.Input[AgentAgentActionGroupApiSchemaS3ArgsDict]]

@pulumi.input_type
class AgentAgentActionGroupApiSchemaArgs:
    def __init__(
        __self__,
        *,
        payload: Optional[pulumi.Input[_builtins.str]] = ...,
        s3: Optional[pulumi.Input[AgentAgentActionGroupApiSchemaS3Args]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @payload.setter
    def payload(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input[AgentAgentActionGroupApiSchemaS3Args]]: ...
    @s3.setter
    def s3(
        self, value: Optional[pulumi.Input[AgentAgentActionGroupApiSchemaS3Args]]
    ): ...

class AgentAgentActionGroupApiSchemaS3ArgsDict(TypedDict):
    s3_bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    s3_object_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentAgentActionGroupApiSchemaS3Args:
    def __init__(
        __self__,
        *,
        s3_bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_object_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_bucket_name.setter
    def s3_bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3ObjectKey")
    def s3_object_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_object_key.setter
    def s3_object_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentAgentActionGroupFunctionSchemaArgsDict(TypedDict):
    member_functions: NotRequired[
        pulumi.Input[AgentAgentActionGroupFunctionSchemaMemberFunctionsArgsDict]
    ]

@pulumi.input_type
class AgentAgentActionGroupFunctionSchemaArgs:
    def __init__(
        __self__,
        *,
        member_functions: Optional[
            pulumi.Input[AgentAgentActionGroupFunctionSchemaMemberFunctionsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memberFunctions")
    def member_functions(
        self,
    ) -> Optional[
        pulumi.Input[AgentAgentActionGroupFunctionSchemaMemberFunctionsArgs]
    ]: ...
    @member_functions.setter
    def member_functions(
        self,
        value: Optional[
            pulumi.Input[AgentAgentActionGroupFunctionSchemaMemberFunctionsArgs]
        ],
    ): ...

class AgentAgentActionGroupFunctionSchemaMemberFunctionsArgsDict(TypedDict):
    functions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentAgentActionGroupFunctionSchemaMemberFunctionsFunctionArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentAgentActionGroupFunctionSchemaMemberFunctionsArgs:
    def __init__(
        __self__,
        *,
        functions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentAgentActionGroupFunctionSchemaMemberFunctionsFunctionArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def functions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentAgentActionGroupFunctionSchemaMemberFunctionsFunctionArgs
                ]
            ]
        ]
    ]: ...
    @functions.setter
    def functions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentAgentActionGroupFunctionSchemaMemberFunctionsFunctionArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentAgentActionGroupFunctionSchemaMemberFunctionsFunctionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentAgentActionGroupFunctionSchemaMemberFunctionsFunctionParameterArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentAgentActionGroupFunctionSchemaMemberFunctionsFunctionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentAgentActionGroupFunctionSchemaMemberFunctionsFunctionParameterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentAgentActionGroupFunctionSchemaMemberFunctionsFunctionParameterArgs
                ]
            ]
        ]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentAgentActionGroupFunctionSchemaMemberFunctionsFunctionParameterArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentAgentActionGroupFunctionSchemaMemberFunctionsFunctionParameterArgsDict(
    TypedDict
):
    map_block_key: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    required: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AgentAgentActionGroupFunctionSchemaMemberFunctionsFunctionParameterArgs:
    def __init__(
        __self__,
        *,
        map_block_key: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        required: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> pulumi.Input[_builtins.str]: ...
    @map_block_key.setter
    def map_block_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AgentAgentActionGroupTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentAgentActionGroupTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentAgentAliasRoutingConfigurationArgsDict(TypedDict):
    agent_version: pulumi.Input[_builtins.str]
    provisioned_throughput: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentAgentAliasRoutingConfigurationArgs:
    def __init__(
        __self__,
        *,
        agent_version: pulumi.Input[_builtins.str],
        provisioned_throughput: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> pulumi.Input[_builtins.str]: ...
    @agent_version.setter
    def agent_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> pulumi.Input[_builtins.str]: ...
    @provisioned_throughput.setter
    def provisioned_throughput(self, value: pulumi.Input[_builtins.str]): ...

class AgentAgentAliasTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentAgentAliasTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentAgentCollaboratorAgentDescriptorArgsDict(TypedDict):
    alias_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentAgentCollaboratorAgentDescriptorArgs:
    def __init__(__self__, *, alias_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aliasArn")
    def alias_arn(self) -> pulumi.Input[_builtins.str]: ...
    @alias_arn.setter
    def alias_arn(self, value: pulumi.Input[_builtins.str]): ...

class AgentAgentCollaboratorTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentAgentCollaboratorTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentAgentGuardrailConfigurationArgsDict(TypedDict):
    guardrail_identifier: pulumi.Input[_builtins.str]
    guardrail_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentAgentGuardrailConfigurationArgs:
    def __init__(
        __self__,
        *,
        guardrail_identifier: pulumi.Input[_builtins.str],
        guardrail_version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="guardrailIdentifier")
    def guardrail_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @guardrail_identifier.setter
    def guardrail_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="guardrailVersion")
    def guardrail_version(self) -> pulumi.Input[_builtins.str]: ...
    @guardrail_version.setter
    def guardrail_version(self, value: pulumi.Input[_builtins.str]): ...

class AgentAgentKnowledgeBaseAssociationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentAgentKnowledgeBaseAssociationTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentAgentMemoryConfigurationArgsDict(TypedDict):
    enabled_memory_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    session_summary_configurations: pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentAgentMemoryConfigurationSessionSummaryConfigurationArgsDict
            ]
        ]
    ]
    storage_days: pulumi.Input[_builtins.int]

@pulumi.input_type
class AgentAgentMemoryConfigurationArgs:
    def __init__(
        __self__,
        *,
        enabled_memory_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        session_summary_configurations: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentAgentMemoryConfigurationSessionSummaryConfigurationArgs
                ]
            ]
        ],
        storage_days: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledMemoryTypes")
    def enabled_memory_types(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @enabled_memory_types.setter
    def enabled_memory_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sessionSummaryConfigurations")
    def session_summary_configurations(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[AgentAgentMemoryConfigurationSessionSummaryConfigurationArgs]
        ]
    ]: ...
    @session_summary_configurations.setter
    def session_summary_configurations(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentAgentMemoryConfigurationSessionSummaryConfigurationArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageDays")
    def storage_days(self) -> pulumi.Input[_builtins.int]: ...
    @storage_days.setter
    def storage_days(self, value: pulumi.Input[_builtins.int]): ...

class AgentAgentMemoryConfigurationSessionSummaryConfigurationArgsDict(TypedDict):
    max_recent_sessions: pulumi.Input[_builtins.int]

@pulumi.input_type
class AgentAgentMemoryConfigurationSessionSummaryConfigurationArgs:
    def __init__(
        __self__, *, max_recent_sessions: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRecentSessions")
    def max_recent_sessions(self) -> pulumi.Input[_builtins.int]: ...
    @max_recent_sessions.setter
    def max_recent_sessions(self, value: pulumi.Input[_builtins.int]): ...

class AgentAgentPromptOverrideConfigurationArgsDict(TypedDict):
    override_lambda: pulumi.Input[_builtins.str]
    prompt_configurations: pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentAgentPromptOverrideConfigurationPromptConfigurationArgsDict
            ]
        ]
    ]

@pulumi.input_type
class AgentAgentPromptOverrideConfigurationArgs:
    def __init__(
        __self__,
        *,
        override_lambda: pulumi.Input[_builtins.str],
        prompt_configurations: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentAgentPromptOverrideConfigurationPromptConfigurationArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="overrideLambda")
    def override_lambda(self) -> pulumi.Input[_builtins.str]: ...
    @override_lambda.setter
    def override_lambda(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="promptConfigurations")
    def prompt_configurations(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[AgentAgentPromptOverrideConfigurationPromptConfigurationArgs]
        ]
    ]: ...
    @prompt_configurations.setter
    def prompt_configurations(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentAgentPromptOverrideConfigurationPromptConfigurationArgs
                ]
            ]
        ],
    ): ...

class AgentAgentPromptOverrideConfigurationPromptConfigurationArgsDict(TypedDict):
    base_prompt_template: pulumi.Input[_builtins.str]
    inference_configurations: pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentAgentPromptOverrideConfigurationPromptConfigurationInferenceConfigurationArgsDict
            ]
        ]
    ]
    parser_mode: pulumi.Input[_builtins.str]
    prompt_creation_mode: pulumi.Input[_builtins.str]
    prompt_state: pulumi.Input[_builtins.str]
    prompt_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentAgentPromptOverrideConfigurationPromptConfigurationArgs:
    def __init__(
        __self__,
        *,
        base_prompt_template: pulumi.Input[_builtins.str],
        inference_configurations: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentAgentPromptOverrideConfigurationPromptConfigurationInferenceConfigurationArgs
                ]
            ]
        ],
        parser_mode: pulumi.Input[_builtins.str],
        prompt_creation_mode: pulumi.Input[_builtins.str],
        prompt_state: pulumi.Input[_builtins.str],
        prompt_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="basePromptTemplate")
    def base_prompt_template(self) -> pulumi.Input[_builtins.str]: ...
    @base_prompt_template.setter
    def base_prompt_template(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="inferenceConfigurations")
    def inference_configurations(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentAgentPromptOverrideConfigurationPromptConfigurationInferenceConfigurationArgs
            ]
        ]
    ]: ...
    @inference_configurations.setter
    def inference_configurations(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentAgentPromptOverrideConfigurationPromptConfigurationInferenceConfigurationArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parserMode")
    def parser_mode(self) -> pulumi.Input[_builtins.str]: ...
    @parser_mode.setter
    def parser_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="promptCreationMode")
    def prompt_creation_mode(self) -> pulumi.Input[_builtins.str]: ...
    @prompt_creation_mode.setter
    def prompt_creation_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="promptState")
    def prompt_state(self) -> pulumi.Input[_builtins.str]: ...
    @prompt_state.setter
    def prompt_state(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="promptType")
    def prompt_type(self) -> pulumi.Input[_builtins.str]: ...
    @prompt_type.setter
    def prompt_type(self, value: pulumi.Input[_builtins.str]): ...

class AgentAgentPromptOverrideConfigurationPromptConfigurationInferenceConfigurationArgsDict(
    TypedDict
):
    max_length: pulumi.Input[_builtins.int]
    stop_sequences: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    temperature: pulumi.Input[_builtins.float]
    top_k: pulumi.Input[_builtins.int]
    top_p: pulumi.Input[_builtins.float]

@pulumi.input_type
class AgentAgentPromptOverrideConfigurationPromptConfigurationInferenceConfigurationArgs:
    def __init__(
        __self__,
        *,
        max_length: pulumi.Input[_builtins.int],
        stop_sequences: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        temperature: pulumi.Input[_builtins.float],
        top_k: pulumi.Input[_builtins.int],
        top_p: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxLength")
    def max_length(self) -> pulumi.Input[_builtins.int]: ...
    @max_length.setter
    def max_length(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="stopSequences")
    def stop_sequences(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @stop_sequences.setter
    def stop_sequences(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> pulumi.Input[_builtins.float]: ...
    @temperature.setter
    def temperature(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="topK")
    def top_k(self) -> pulumi.Input[_builtins.int]: ...
    @top_k.setter
    def top_k(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="topP")
    def top_p(self) -> pulumi.Input[_builtins.float]: ...
    @top_p.setter
    def top_p(self, value: pulumi.Input[_builtins.float]): ...

class AgentAgentTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentAgentTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentDataSourceDataSourceConfigurationArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    confluence_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationConfluenceConfigurationArgsDict
        ]
    ]
    s3_configuration: NotRequired[
        pulumi.Input[AgentDataSourceDataSourceConfigurationS3ConfigurationArgsDict]
    ]
    salesforce_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationSalesforceConfigurationArgsDict
        ]
    ]
    share_point_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationSharePointConfigurationArgsDict
        ]
    ]
    web_configuration: NotRequired[
        pulumi.Input[AgentDataSourceDataSourceConfigurationWebConfigurationArgsDict]
    ]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        confluence_configuration: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationConfluenceConfigurationArgs
            ]
        ] = ...,
        s3_configuration: Optional[
            pulumi.Input[AgentDataSourceDataSourceConfigurationS3ConfigurationArgs]
        ] = ...,
        salesforce_configuration: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationSalesforceConfigurationArgs
            ]
        ] = ...,
        share_point_configuration: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationSharePointConfigurationArgs
            ]
        ] = ...,
        web_configuration: Optional[
            pulumi.Input[AgentDataSourceDataSourceConfigurationWebConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="confluenceConfiguration")
    def confluence_configuration(
        self,
    ) -> Optional[
        pulumi.Input[AgentDataSourceDataSourceConfigurationConfluenceConfigurationArgs]
    ]: ...
    @confluence_configuration.setter
    def confluence_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationConfluenceConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> Optional[
        pulumi.Input[AgentDataSourceDataSourceConfigurationS3ConfigurationArgs]
    ]: ...
    @s3_configuration.setter
    def s3_configuration(
        self,
        value: Optional[
            pulumi.Input[AgentDataSourceDataSourceConfigurationS3ConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="salesforceConfiguration")
    def salesforce_configuration(
        self,
    ) -> Optional[
        pulumi.Input[AgentDataSourceDataSourceConfigurationSalesforceConfigurationArgs]
    ]: ...
    @salesforce_configuration.setter
    def salesforce_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationSalesforceConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharePointConfiguration")
    def share_point_configuration(
        self,
    ) -> Optional[
        pulumi.Input[AgentDataSourceDataSourceConfigurationSharePointConfigurationArgs]
    ]: ...
    @share_point_configuration.setter
    def share_point_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationSharePointConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="webConfiguration")
    def web_configuration(
        self,
    ) -> Optional[
        pulumi.Input[AgentDataSourceDataSourceConfigurationWebConfigurationArgs]
    ]: ...
    @web_configuration.setter
    def web_configuration(
        self,
        value: Optional[
            pulumi.Input[AgentDataSourceDataSourceConfigurationWebConfigurationArgs]
        ],
    ): ...

class AgentDataSourceDataSourceConfigurationConfluenceConfigurationArgsDict(TypedDict):
    crawler_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationArgsDict
        ]
    ]
    source_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationConfluenceConfigurationSourceConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationConfluenceConfigurationArgs:
    def __init__(
        __self__,
        *,
        crawler_configuration: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationArgs
            ]
        ] = ...,
        source_configuration: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationConfluenceConfigurationSourceConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crawlerConfiguration")
    def crawler_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationArgs
        ]
    ]: ...
    @crawler_configuration.setter
    def crawler_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationConfluenceConfigurationSourceConfigurationArgs
        ]
    ]: ...
    @source_configuration.setter
    def source_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationConfluenceConfigurationSourceConfigurationArgs
            ]
        ],
    ): ...

class AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationArgsDict(
    TypedDict
):
    filter_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationArgs:
    def __init__(
        __self__,
        *,
        filter_configuration: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterConfiguration")
    def filter_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationArgs
        ]
    ]: ...
    @filter_configuration.setter
    def filter_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationArgs
            ]
        ],
    ): ...

class AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    pattern_object_filters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        pattern_object_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="patternObjectFilters")
    def pattern_object_filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgs
                ]
            ]
        ]
    ]: ...
    @pattern_object_filters.setter
    def pattern_object_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgsDict(
    TypedDict
):
    filters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgs:
    def __init__(
        __self__,
        *,
        filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgs
                ]
            ]
        ]
    ]: ...
    @filters.setter
    def filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgsDict(
    TypedDict
):
    object_type: pulumi.Input[_builtins.str]
    exclusion_filters: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    inclusion_filters: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationConfluenceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgs:
    def __init__(
        __self__,
        *,
        object_type: pulumi.Input[_builtins.str],
        exclusion_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        inclusion_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectType")
    def object_type(self) -> pulumi.Input[_builtins.str]: ...
    @object_type.setter
    def object_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="exclusionFilters")
    def exclusion_filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclusion_filters.setter
    def exclusion_filters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inclusionFilters")
    def inclusion_filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @inclusion_filters.setter
    def inclusion_filters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AgentDataSourceDataSourceConfigurationConfluenceConfigurationSourceConfigurationArgsDict(
    TypedDict
):
    auth_type: pulumi.Input[_builtins.str]
    credentials_secret_arn: pulumi.Input[_builtins.str]
    host_type: pulumi.Input[_builtins.str]
    host_url: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationConfluenceConfigurationSourceConfigurationArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        credentials_secret_arn: pulumi.Input[_builtins.str],
        host_type: pulumi.Input[_builtins.str],
        host_url: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="credentialsSecretArn")
    def credentials_secret_arn(self) -> pulumi.Input[_builtins.str]: ...
    @credentials_secret_arn.setter
    def credentials_secret_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hostType")
    def host_type(self) -> pulumi.Input[_builtins.str]: ...
    @host_type.setter
    def host_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hostUrl")
    def host_url(self) -> pulumi.Input[_builtins.str]: ...
    @host_url.setter
    def host_url(self, value: pulumi.Input[_builtins.str]): ...

class AgentDataSourceDataSourceConfigurationS3ConfigurationArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    bucket_owner_account_id: NotRequired[pulumi.Input[_builtins.str]]
    inclusion_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationS3ConfigurationArgs:
    def __init__(
        __self__,
        *,
        bucket_arn: pulumi.Input[_builtins.str],
        bucket_owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        inclusion_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bucketOwnerAccountId")
    def bucket_owner_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_owner_account_id.setter
    def bucket_owner_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inclusionPrefixes")
    def inclusion_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @inclusion_prefixes.setter
    def inclusion_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AgentDataSourceDataSourceConfigurationSalesforceConfigurationArgsDict(TypedDict):
    crawler_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationArgsDict
        ]
    ]
    source_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationSalesforceConfigurationSourceConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationSalesforceConfigurationArgs:
    def __init__(
        __self__,
        *,
        crawler_configuration: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationArgs
            ]
        ] = ...,
        source_configuration: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationSalesforceConfigurationSourceConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crawlerConfiguration")
    def crawler_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationArgs
        ]
    ]: ...
    @crawler_configuration.setter
    def crawler_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationSalesforceConfigurationSourceConfigurationArgs
        ]
    ]: ...
    @source_configuration.setter
    def source_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationSalesforceConfigurationSourceConfigurationArgs
            ]
        ],
    ): ...

class AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationArgsDict(
    TypedDict
):
    filter_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationArgs:
    def __init__(
        __self__,
        *,
        filter_configuration: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterConfiguration")
    def filter_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationArgs
        ]
    ]: ...
    @filter_configuration.setter
    def filter_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationArgs
            ]
        ],
    ): ...

class AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    pattern_object_filters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        pattern_object_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="patternObjectFilters")
    def pattern_object_filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgs
                ]
            ]
        ]
    ]: ...
    @pattern_object_filters.setter
    def pattern_object_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgsDict(
    TypedDict
):
    filters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgs:
    def __init__(
        __self__,
        *,
        filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgs
                ]
            ]
        ]
    ]: ...
    @filters.setter
    def filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgsDict(
    TypedDict
):
    object_type: pulumi.Input[_builtins.str]
    exclusion_filters: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    inclusion_filters: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationSalesforceConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgs:
    def __init__(
        __self__,
        *,
        object_type: pulumi.Input[_builtins.str],
        exclusion_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        inclusion_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectType")
    def object_type(self) -> pulumi.Input[_builtins.str]: ...
    @object_type.setter
    def object_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="exclusionFilters")
    def exclusion_filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclusion_filters.setter
    def exclusion_filters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inclusionFilters")
    def inclusion_filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @inclusion_filters.setter
    def inclusion_filters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AgentDataSourceDataSourceConfigurationSalesforceConfigurationSourceConfigurationArgsDict(
    TypedDict
):
    auth_type: pulumi.Input[_builtins.str]
    credentials_secret_arn: pulumi.Input[_builtins.str]
    host_url: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationSalesforceConfigurationSourceConfigurationArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        credentials_secret_arn: pulumi.Input[_builtins.str],
        host_url: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="credentialsSecretArn")
    def credentials_secret_arn(self) -> pulumi.Input[_builtins.str]: ...
    @credentials_secret_arn.setter
    def credentials_secret_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hostUrl")
    def host_url(self) -> pulumi.Input[_builtins.str]: ...
    @host_url.setter
    def host_url(self, value: pulumi.Input[_builtins.str]): ...

class AgentDataSourceDataSourceConfigurationSharePointConfigurationArgsDict(TypedDict):
    crawler_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationArgsDict
        ]
    ]
    source_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationSharePointConfigurationSourceConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationSharePointConfigurationArgs:
    def __init__(
        __self__,
        *,
        crawler_configuration: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationArgs
            ]
        ] = ...,
        source_configuration: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationSharePointConfigurationSourceConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crawlerConfiguration")
    def crawler_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationArgs
        ]
    ]: ...
    @crawler_configuration.setter
    def crawler_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationSharePointConfigurationSourceConfigurationArgs
        ]
    ]: ...
    @source_configuration.setter
    def source_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationSharePointConfigurationSourceConfigurationArgs
            ]
        ],
    ): ...

class AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationArgsDict(
    TypedDict
):
    filter_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationArgs:
    def __init__(
        __self__,
        *,
        filter_configuration: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterConfiguration")
    def filter_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationArgs
        ]
    ]: ...
    @filter_configuration.setter
    def filter_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationArgs
            ]
        ],
    ): ...

class AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    pattern_object_filters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        pattern_object_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="patternObjectFilters")
    def pattern_object_filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgs
                ]
            ]
        ]
    ]: ...
    @pattern_object_filters.setter
    def pattern_object_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgsDict(
    TypedDict
):
    filters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterArgs:
    def __init__(
        __self__,
        *,
        filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgs
                ]
            ]
        ]
    ]: ...
    @filters.setter
    def filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgsDict(
    TypedDict
):
    object_type: pulumi.Input[_builtins.str]
    exclusion_filters: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    inclusion_filters: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationSharePointConfigurationCrawlerConfigurationFilterConfigurationPatternObjectFilterFilterArgs:
    def __init__(
        __self__,
        *,
        object_type: pulumi.Input[_builtins.str],
        exclusion_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        inclusion_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectType")
    def object_type(self) -> pulumi.Input[_builtins.str]: ...
    @object_type.setter
    def object_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="exclusionFilters")
    def exclusion_filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclusion_filters.setter
    def exclusion_filters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inclusionFilters")
    def inclusion_filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @inclusion_filters.setter
    def inclusion_filters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AgentDataSourceDataSourceConfigurationSharePointConfigurationSourceConfigurationArgsDict(
    TypedDict
):
    auth_type: pulumi.Input[_builtins.str]
    credentials_secret_arn: pulumi.Input[_builtins.str]
    domain: pulumi.Input[_builtins.str]
    host_type: pulumi.Input[_builtins.str]
    site_urls: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationSharePointConfigurationSourceConfigurationArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        credentials_secret_arn: pulumi.Input[_builtins.str],
        domain: pulumi.Input[_builtins.str],
        host_type: pulumi.Input[_builtins.str],
        site_urls: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="credentialsSecretArn")
    def credentials_secret_arn(self) -> pulumi.Input[_builtins.str]: ...
    @credentials_secret_arn.setter
    def credentials_secret_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]: ...
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hostType")
    def host_type(self) -> pulumi.Input[_builtins.str]: ...
    @host_type.setter
    def host_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="siteUrls")
    def site_urls(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @site_urls.setter
    def site_urls(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentDataSourceDataSourceConfigurationWebConfigurationArgsDict(TypedDict):
    crawler_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfigurationArgsDict
        ]
    ]
    source_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationWebConfigurationArgs:
    def __init__(
        __self__,
        *,
        crawler_configuration: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfigurationArgs
            ]
        ] = ...,
        source_configuration: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crawlerConfiguration")
    def crawler_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfigurationArgs
        ]
    ]: ...
    @crawler_configuration.setter
    def crawler_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationArgs
        ]
    ]: ...
    @source_configuration.setter
    def source_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationArgs
            ]
        ],
    ): ...

class AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfigurationArgsDict(
    TypedDict
):
    crawler_limits: NotRequired[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfigurationCrawlerLimitsArgsDict
        ]
    ]
    exclusion_filters: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    inclusion_filters: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    user_agent: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfigurationArgs:
    def __init__(
        __self__,
        *,
        crawler_limits: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfigurationCrawlerLimitsArgs
            ]
        ] = ...,
        exclusion_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        inclusion_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        user_agent: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crawlerLimits")
    def crawler_limits(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfigurationCrawlerLimitsArgs
        ]
    ]: ...
    @crawler_limits.setter
    def crawler_limits(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfigurationCrawlerLimitsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="exclusionFilters")
    def exclusion_filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclusion_filters.setter
    def exclusion_filters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inclusionFilters")
    def inclusion_filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @inclusion_filters.setter
    def inclusion_filters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userAgent")
    def user_agent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_agent.setter
    def user_agent(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfigurationCrawlerLimitsArgsDict(
    TypedDict
):
    max_pages: NotRequired[pulumi.Input[_builtins.int]]
    rate_limit: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationWebConfigurationCrawlerConfigurationCrawlerLimitsArgs:
    def __init__(
        __self__,
        *,
        max_pages: Optional[pulumi.Input[_builtins.int]] = ...,
        rate_limit: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPages")
    def max_pages(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_pages.setter
    def max_pages(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="rateLimit")
    def rate_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rate_limit.setter
    def rate_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationArgsDict(
    TypedDict
):
    url_configuration: pulumi.Input[
        AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfigurationArgsDict
    ]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationArgs:
    def __init__(
        __self__,
        *,
        url_configuration: pulumi.Input[
            AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfigurationArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="urlConfiguration")
    def url_configuration(
        self,
    ) -> pulumi.Input[
        AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfigurationArgs
    ]: ...
    @url_configuration.setter
    def url_configuration(
        self,
        value: pulumi.Input[
            AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfigurationArgs
        ],
    ): ...

class AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfigurationArgsDict(
    TypedDict
):
    seed_urls: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfigurationSeedUrlArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfigurationArgs:
    def __init__(
        __self__,
        *,
        seed_urls: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfigurationSeedUrlArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="seedUrls")
    def seed_urls(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfigurationSeedUrlArgs
                ]
            ]
        ]
    ]: ...
    @seed_urls.setter
    def seed_urls(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfigurationSeedUrlArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfigurationSeedUrlArgsDict(
    TypedDict
):
    url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentDataSourceDataSourceConfigurationWebConfigurationSourceConfigurationUrlConfigurationSeedUrlArgs:
    def __init__(
        __self__, *, url: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentDataSourceServerSideEncryptionConfigurationArgsDict(TypedDict):
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentDataSourceServerSideEncryptionConfigurationArgs:
    def __init__(
        __self__, *, kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentDataSourceTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentDataSourceTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentDataSourceVectorIngestionConfigurationArgsDict(TypedDict):
    chunking_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationChunkingConfigurationArgsDict
        ]
    ]
    custom_transformation_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationArgsDict
        ]
    ]
    parsing_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationParsingConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentDataSourceVectorIngestionConfigurationArgs:
    def __init__(
        __self__,
        *,
        chunking_configuration: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationChunkingConfigurationArgs
            ]
        ] = ...,
        custom_transformation_configuration: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationArgs
            ]
        ] = ...,
        parsing_configuration: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationParsingConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="chunkingConfiguration")
    def chunking_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationChunkingConfigurationArgs
        ]
    ]: ...
    @chunking_configuration.setter
    def chunking_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationChunkingConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customTransformationConfiguration")
    def custom_transformation_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationArgs
        ]
    ]: ...
    @custom_transformation_configuration.setter
    def custom_transformation_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parsingConfiguration")
    def parsing_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationParsingConfigurationArgs
        ]
    ]: ...
    @parsing_configuration.setter
    def parsing_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationParsingConfigurationArgs
            ]
        ],
    ): ...

class AgentDataSourceVectorIngestionConfigurationChunkingConfigurationArgsDict(
    TypedDict
):
    chunking_strategy: pulumi.Input[_builtins.str]
    fixed_size_chunking_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationChunkingConfigurationFixedSizeChunkingConfigurationArgsDict
        ]
    ]
    hierarchical_chunking_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfigurationArgsDict
        ]
    ]
    semantic_chunking_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationChunkingConfigurationSemanticChunkingConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentDataSourceVectorIngestionConfigurationChunkingConfigurationArgs:
    def __init__(
        __self__,
        *,
        chunking_strategy: pulumi.Input[_builtins.str],
        fixed_size_chunking_configuration: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationChunkingConfigurationFixedSizeChunkingConfigurationArgs
            ]
        ] = ...,
        hierarchical_chunking_configuration: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfigurationArgs
            ]
        ] = ...,
        semantic_chunking_configuration: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationChunkingConfigurationSemanticChunkingConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="chunkingStrategy")
    def chunking_strategy(self) -> pulumi.Input[_builtins.str]: ...
    @chunking_strategy.setter
    def chunking_strategy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fixedSizeChunkingConfiguration")
    def fixed_size_chunking_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationChunkingConfigurationFixedSizeChunkingConfigurationArgs
        ]
    ]: ...
    @fixed_size_chunking_configuration.setter
    def fixed_size_chunking_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationChunkingConfigurationFixedSizeChunkingConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hierarchicalChunkingConfiguration")
    def hierarchical_chunking_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfigurationArgs
        ]
    ]: ...
    @hierarchical_chunking_configuration.setter
    def hierarchical_chunking_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="semanticChunkingConfiguration")
    def semantic_chunking_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationChunkingConfigurationSemanticChunkingConfigurationArgs
        ]
    ]: ...
    @semantic_chunking_configuration.setter
    def semantic_chunking_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationChunkingConfigurationSemanticChunkingConfigurationArgs
            ]
        ],
    ): ...

class AgentDataSourceVectorIngestionConfigurationChunkingConfigurationFixedSizeChunkingConfigurationArgsDict(
    TypedDict
):
    max_tokens: pulumi.Input[_builtins.int]
    overlap_percentage: pulumi.Input[_builtins.int]

@pulumi.input_type
class AgentDataSourceVectorIngestionConfigurationChunkingConfigurationFixedSizeChunkingConfigurationArgs:
    def __init__(
        __self__,
        *,
        max_tokens: pulumi.Input[_builtins.int],
        overlap_percentage: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxTokens")
    def max_tokens(self) -> pulumi.Input[_builtins.int]: ...
    @max_tokens.setter
    def max_tokens(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="overlapPercentage")
    def overlap_percentage(self) -> pulumi.Input[_builtins.int]: ...
    @overlap_percentage.setter
    def overlap_percentage(self, value: pulumi.Input[_builtins.int]): ...

class AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfigurationArgsDict(
    TypedDict
):
    overlap_tokens: pulumi.Input[_builtins.int]
    level_configurations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfigurationLevelConfigurationArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfigurationArgs:
    def __init__(
        __self__,
        *,
        overlap_tokens: pulumi.Input[_builtins.int],
        level_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfigurationLevelConfigurationArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="overlapTokens")
    def overlap_tokens(self) -> pulumi.Input[_builtins.int]: ...
    @overlap_tokens.setter
    def overlap_tokens(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="levelConfigurations")
    def level_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfigurationLevelConfigurationArgs
                ]
            ]
        ]
    ]: ...
    @level_configurations.setter
    def level_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfigurationLevelConfigurationArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfigurationLevelConfigurationArgsDict(
    TypedDict
):
    max_tokens: pulumi.Input[_builtins.int]

@pulumi.input_type
class AgentDataSourceVectorIngestionConfigurationChunkingConfigurationHierarchicalChunkingConfigurationLevelConfigurationArgs:
    def __init__(__self__, *, max_tokens: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxTokens")
    def max_tokens(self) -> pulumi.Input[_builtins.int]: ...
    @max_tokens.setter
    def max_tokens(self, value: pulumi.Input[_builtins.int]): ...

class AgentDataSourceVectorIngestionConfigurationChunkingConfigurationSemanticChunkingConfigurationArgsDict(
    TypedDict
):
    breakpoint_percentile_threshold: pulumi.Input[_builtins.int]
    buffer_size: pulumi.Input[_builtins.int]
    max_token: pulumi.Input[_builtins.int]

@pulumi.input_type
class AgentDataSourceVectorIngestionConfigurationChunkingConfigurationSemanticChunkingConfigurationArgs:
    def __init__(
        __self__,
        *,
        breakpoint_percentile_threshold: pulumi.Input[_builtins.int],
        buffer_size: pulumi.Input[_builtins.int],
        max_token: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="breakpointPercentileThreshold")
    def breakpoint_percentile_threshold(self) -> pulumi.Input[_builtins.int]: ...
    @breakpoint_percentile_threshold.setter
    def breakpoint_percentile_threshold(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="bufferSize")
    def buffer_size(self) -> pulumi.Input[_builtins.int]: ...
    @buffer_size.setter
    def buffer_size(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="maxToken")
    def max_token(self) -> pulumi.Input[_builtins.int]: ...
    @max_token.setter
    def max_token(self, value: pulumi.Input[_builtins.int]): ...

class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationArgsDict(
    TypedDict
):
    intermediate_storage: NotRequired[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorageArgsDict
        ]
    ]
    transformation: NotRequired[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationArgsDict
        ]
    ]

@pulumi.input_type
class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationArgs:
    def __init__(
        __self__,
        *,
        intermediate_storage: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorageArgs
            ]
        ] = ...,
        transformation: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="intermediateStorage")
    def intermediate_storage(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorageArgs
        ]
    ]: ...
    @intermediate_storage.setter
    def intermediate_storage(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorageArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def transformation(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationArgs
        ]
    ]: ...
    @transformation.setter
    def transformation(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationArgs
            ]
        ],
    ): ...

class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorageArgsDict(
    TypedDict
):
    s3_location: NotRequired[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorageS3LocationArgsDict
        ]
    ]

@pulumi.input_type
class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorageArgs:
    def __init__(
        __self__,
        *,
        s3_location: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorageS3LocationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Location")
    def s3_location(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorageS3LocationArgs
        ]
    ]: ...
    @s3_location.setter
    def s3_location(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorageS3LocationArgs
            ]
        ],
    ): ...

class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorageS3LocationArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationIntermediateStorageS3LocationArgs:
    def __init__(__self__, *, uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...

class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationArgsDict(
    TypedDict
):
    step_to_apply: pulumi.Input[_builtins.str]
    transformation_function: NotRequired[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunctionArgsDict
        ]
    ]

@pulumi.input_type
class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationArgs:
    def __init__(
        __self__,
        *,
        step_to_apply: pulumi.Input[_builtins.str],
        transformation_function: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunctionArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stepToApply")
    def step_to_apply(self) -> pulumi.Input[_builtins.str]: ...
    @step_to_apply.setter
    def step_to_apply(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="transformationFunction")
    def transformation_function(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunctionArgs
        ]
    ]: ...
    @transformation_function.setter
    def transformation_function(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunctionArgs
            ]
        ],
    ): ...

class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunctionArgsDict(
    TypedDict
):
    transformation_lambda_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunctionTransformationLambdaConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunctionArgs:
    def __init__(
        __self__,
        *,
        transformation_lambda_configuration: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunctionTransformationLambdaConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="transformationLambdaConfiguration")
    def transformation_lambda_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunctionTransformationLambdaConfigurationArgs
        ]
    ]: ...
    @transformation_lambda_configuration.setter
    def transformation_lambda_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunctionTransformationLambdaConfigurationArgs
            ]
        ],
    ): ...

class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunctionTransformationLambdaConfigurationArgsDict(
    TypedDict
):
    lambda_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentDataSourceVectorIngestionConfigurationCustomTransformationConfigurationTransformationTransformationFunctionTransformationLambdaConfigurationArgs:
    def __init__(__self__, *, lambda_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> pulumi.Input[_builtins.str]: ...
    @lambda_arn.setter
    def lambda_arn(self, value: pulumi.Input[_builtins.str]): ...

class AgentDataSourceVectorIngestionConfigurationParsingConfigurationArgsDict(
    TypedDict
):
    parsing_strategy: pulumi.Input[_builtins.str]
    bedrock_data_automation_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockDataAutomationConfigurationArgsDict
        ]
    ]
    bedrock_foundation_model_configuration: NotRequired[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentDataSourceVectorIngestionConfigurationParsingConfigurationArgs:
    def __init__(
        __self__,
        *,
        parsing_strategy: pulumi.Input[_builtins.str],
        bedrock_data_automation_configuration: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockDataAutomationConfigurationArgs
            ]
        ] = ...,
        bedrock_foundation_model_configuration: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parsingStrategy")
    def parsing_strategy(self) -> pulumi.Input[_builtins.str]: ...
    @parsing_strategy.setter
    def parsing_strategy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bedrockDataAutomationConfiguration")
    def bedrock_data_automation_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockDataAutomationConfigurationArgs
        ]
    ]: ...
    @bedrock_data_automation_configuration.setter
    def bedrock_data_automation_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockDataAutomationConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bedrockFoundationModelConfiguration")
    def bedrock_foundation_model_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfigurationArgs
        ]
    ]: ...
    @bedrock_foundation_model_configuration.setter
    def bedrock_foundation_model_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfigurationArgs
            ]
        ],
    ): ...

class AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockDataAutomationConfigurationArgsDict(
    TypedDict
):
    parsing_modality: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockDataAutomationConfigurationArgs:
    def __init__(
        __self__, *, parsing_modality: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parsingModality")
    def parsing_modality(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parsing_modality.setter
    def parsing_modality(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfigurationArgsDict(
    TypedDict
):
    model_arn: pulumi.Input[_builtins.str]
    parsing_modality: NotRequired[pulumi.Input[_builtins.str]]
    parsing_prompt: NotRequired[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfigurationParsingPromptArgsDict
        ]
    ]

@pulumi.input_type
class AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfigurationArgs:
    def __init__(
        __self__,
        *,
        model_arn: pulumi.Input[_builtins.str],
        parsing_modality: Optional[pulumi.Input[_builtins.str]] = ...,
        parsing_prompt: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfigurationParsingPromptArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelArn")
    def model_arn(self) -> pulumi.Input[_builtins.str]: ...
    @model_arn.setter
    def model_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="parsingModality")
    def parsing_modality(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parsing_modality.setter
    def parsing_modality(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parsingPrompt")
    def parsing_prompt(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfigurationParsingPromptArgs
        ]
    ]: ...
    @parsing_prompt.setter
    def parsing_prompt(
        self,
        value: Optional[
            pulumi.Input[
                AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfigurationParsingPromptArgs
            ]
        ],
    ): ...

class AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfigurationParsingPromptArgsDict(
    TypedDict
):
    parsing_prompt_string: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentDataSourceVectorIngestionConfigurationParsingConfigurationBedrockFoundationModelConfigurationParsingPromptArgs:
    def __init__(
        __self__, *, parsing_prompt_string: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parsingPromptString")
    def parsing_prompt_string(self) -> pulumi.Input[_builtins.str]: ...
    @parsing_prompt_string.setter
    def parsing_prompt_string(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionArgsDict(TypedDict):
    connections: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AgentFlowDefinitionConnectionArgsDict]]]
    ]
    nodes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AgentFlowDefinitionNodeArgsDict]]]
    ]

@pulumi.input_type
class AgentFlowDefinitionArgs:
    def __init__(
        __self__,
        *,
        connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[AgentFlowDefinitionConnectionArgs]]]
        ] = ...,
        nodes: Optional[
            pulumi.Input[Sequence[pulumi.Input[AgentFlowDefinitionNodeArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connections(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AgentFlowDefinitionConnectionArgs]]]
    ]: ...
    @connections.setter
    def connections(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AgentFlowDefinitionConnectionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def nodes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AgentFlowDefinitionNodeArgs]]]
    ]: ...
    @nodes.setter
    def nodes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AgentFlowDefinitionNodeArgs]]]
        ],
    ): ...

class AgentFlowDefinitionConnectionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    source: pulumi.Input[_builtins.str]
    target: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    configuration: NotRequired[
        pulumi.Input[AgentFlowDefinitionConnectionConfigurationArgsDict]
    ]

@pulumi.input_type
class AgentFlowDefinitionConnectionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        source: pulumi.Input[_builtins.str],
        target: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        configuration: Optional[
            pulumi.Input[AgentFlowDefinitionConnectionConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[pulumi.Input[AgentFlowDefinitionConnectionConfigurationArgs]]: ...
    @configuration.setter
    def configuration(
        self,
        value: Optional[pulumi.Input[AgentFlowDefinitionConnectionConfigurationArgs]],
    ): ...

class AgentFlowDefinitionConnectionConfigurationArgsDict(TypedDict):
    conditional: NotRequired[
        pulumi.Input[AgentFlowDefinitionConnectionConfigurationConditionalArgsDict]
    ]
    data: NotRequired[
        pulumi.Input[AgentFlowDefinitionConnectionConfigurationDataArgsDict]
    ]

@pulumi.input_type
class AgentFlowDefinitionConnectionConfigurationArgs:
    def __init__(
        __self__,
        *,
        conditional: Optional[
            pulumi.Input[AgentFlowDefinitionConnectionConfigurationConditionalArgs]
        ] = ...,
        data: Optional[
            pulumi.Input[AgentFlowDefinitionConnectionConfigurationDataArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditional(
        self,
    ) -> Optional[
        pulumi.Input[AgentFlowDefinitionConnectionConfigurationConditionalArgs]
    ]: ...
    @conditional.setter
    def conditional(
        self,
        value: Optional[
            pulumi.Input[AgentFlowDefinitionConnectionConfigurationConditionalArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def data(
        self,
    ) -> Optional[pulumi.Input[AgentFlowDefinitionConnectionConfigurationDataArgs]]: ...
    @data.setter
    def data(
        self,
        value: Optional[
            pulumi.Input[AgentFlowDefinitionConnectionConfigurationDataArgs]
        ],
    ): ...

class AgentFlowDefinitionConnectionConfigurationConditionalArgsDict(TypedDict):
    condition: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionConnectionConfigurationConditionalArgs:
    def __init__(__self__, *, condition: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Input[_builtins.str]: ...
    @condition.setter
    def condition(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionConnectionConfigurationDataArgsDict(TypedDict):
    source_output: pulumi.Input[_builtins.str]
    target_input: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionConnectionConfigurationDataArgs:
    def __init__(
        __self__,
        *,
        source_output: pulumi.Input[_builtins.str],
        target_input: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceOutput")
    def source_output(self) -> pulumi.Input[_builtins.str]: ...
    @source_output.setter
    def source_output(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetInput")
    def target_input(self) -> pulumi.Input[_builtins.str]: ...
    @target_input.setter
    def target_input(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    configuration: NotRequired[
        pulumi.Input[AgentFlowDefinitionNodeConfigurationArgsDict]
    ]
    inputs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AgentFlowDefinitionNodeInputArgsDict]]]
    ]
    outputs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AgentFlowDefinitionNodeOutputArgsDict]]]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        configuration: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationArgs]
        ] = ...,
        inputs: Optional[
            pulumi.Input[Sequence[pulumi.Input[AgentFlowDefinitionNodeInputArgs]]]
        ] = ...,
        outputs: Optional[
            pulumi.Input[Sequence[pulumi.Input[AgentFlowDefinitionNodeOutputArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationArgs]]: ...
    @configuration.setter
    def configuration(
        self, value: Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def inputs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AgentFlowDefinitionNodeInputArgs]]]
    ]: ...
    @inputs.setter
    def inputs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AgentFlowDefinitionNodeInputArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def outputs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AgentFlowDefinitionNodeOutputArgs]]]
    ]: ...
    @outputs.setter
    def outputs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AgentFlowDefinitionNodeOutputArgs]]]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationArgsDict(TypedDict):
    agent: NotRequired[pulumi.Input[AgentFlowDefinitionNodeConfigurationAgentArgsDict]]
    collector: NotRequired[
        pulumi.Input[AgentFlowDefinitionNodeConfigurationCollectorArgsDict]
    ]
    condition: NotRequired[
        pulumi.Input[AgentFlowDefinitionNodeConfigurationConditionArgsDict]
    ]
    inline_code: NotRequired[
        pulumi.Input[AgentFlowDefinitionNodeConfigurationInlineCodeArgsDict]
    ]
    input: NotRequired[pulumi.Input[AgentFlowDefinitionNodeConfigurationInputArgsDict]]
    iterator: NotRequired[
        pulumi.Input[AgentFlowDefinitionNodeConfigurationIteratorArgsDict]
    ]
    knowledge_base: NotRequired[
        pulumi.Input[AgentFlowDefinitionNodeConfigurationKnowledgeBaseArgsDict]
    ]
    lambda_function: NotRequired[
        pulumi.Input[AgentFlowDefinitionNodeConfigurationLambdaFunctionArgsDict]
    ]
    lex: NotRequired[pulumi.Input[AgentFlowDefinitionNodeConfigurationLexArgsDict]]
    output: NotRequired[
        pulumi.Input[AgentFlowDefinitionNodeConfigurationOutputArgsDict]
    ]
    prompt: NotRequired[
        pulumi.Input[AgentFlowDefinitionNodeConfigurationPromptArgsDict]
    ]
    retrieval: NotRequired[
        pulumi.Input[AgentFlowDefinitionNodeConfigurationRetrievalArgsDict]
    ]
    storage: NotRequired[
        pulumi.Input[AgentFlowDefinitionNodeConfigurationStorageArgsDict]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationArgs:
    def __init__(
        __self__,
        *,
        agent: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationAgentArgs]
        ] = ...,
        collector: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationCollectorArgs]
        ] = ...,
        condition: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationConditionArgs]
        ] = ...,
        inline_code: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationInlineCodeArgs]
        ] = ...,
        input: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationInputArgs]
        ] = ...,
        iterator: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationIteratorArgs]
        ] = ...,
        knowledge_base: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationKnowledgeBaseArgs]
        ] = ...,
        lambda_function: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationLambdaFunctionArgs]
        ] = ...,
        lex: Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationLexArgs]] = ...,
        output: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationOutputArgs]
        ] = ...,
        prompt: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationPromptArgs]
        ] = ...,
        retrieval: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationRetrievalArgs]
        ] = ...,
        storage: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationStorageArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def agent(
        self,
    ) -> Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationAgentArgs]]: ...
    @agent.setter
    def agent(
        self,
        value: Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationAgentArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def collector(
        self,
    ) -> Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationCollectorArgs]]: ...
    @collector.setter
    def collector(
        self,
        value: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationCollectorArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationConditionArgs]]: ...
    @condition.setter
    def condition(
        self,
        value: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationConditionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inlineCode")
    def inline_code(
        self,
    ) -> Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationInlineCodeArgs]]: ...
    @inline_code.setter
    def inline_code(
        self,
        value: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationInlineCodeArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def input(
        self,
    ) -> Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationInputArgs]]: ...
    @input.setter
    def input(
        self,
        value: Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationInputArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def iterator(
        self,
    ) -> Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationIteratorArgs]]: ...
    @iterator.setter
    def iterator(
        self,
        value: Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationIteratorArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="knowledgeBase")
    def knowledge_base(
        self,
    ) -> Optional[
        pulumi.Input[AgentFlowDefinitionNodeConfigurationKnowledgeBaseArgs]
    ]: ...
    @knowledge_base.setter
    def knowledge_base(
        self,
        value: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationKnowledgeBaseArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunction")
    def lambda_function(
        self,
    ) -> Optional[
        pulumi.Input[AgentFlowDefinitionNodeConfigurationLambdaFunctionArgs]
    ]: ...
    @lambda_function.setter
    def lambda_function(
        self,
        value: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationLambdaFunctionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def lex(
        self,
    ) -> Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationLexArgs]]: ...
    @lex.setter
    def lex(
        self, value: Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationLexArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def output(
        self,
    ) -> Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationOutputArgs]]: ...
    @output.setter
    def output(
        self,
        value: Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationOutputArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def prompt(
        self,
    ) -> Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationPromptArgs]]: ...
    @prompt.setter
    def prompt(
        self,
        value: Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationPromptArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def retrieval(
        self,
    ) -> Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationRetrievalArgs]]: ...
    @retrieval.setter
    def retrieval(
        self,
        value: Optional[
            pulumi.Input[AgentFlowDefinitionNodeConfigurationRetrievalArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def storage(
        self,
    ) -> Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationStorageArgs]]: ...
    @storage.setter
    def storage(
        self,
        value: Optional[pulumi.Input[AgentFlowDefinitionNodeConfigurationStorageArgs]],
    ): ...

class AgentFlowDefinitionNodeConfigurationAgentArgsDict(TypedDict):
    agent_alias_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationAgentArgs:
    def __init__(__self__, *, agent_alias_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentAliasArn")
    def agent_alias_arn(self) -> pulumi.Input[_builtins.str]: ...
    @agent_alias_arn.setter
    def agent_alias_arn(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeConfigurationCollectorArgsDict(TypedDict): ...

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationCollectorArgs:
    def __init__(__self__) -> None: ...

class AgentFlowDefinitionNodeConfigurationConditionArgsDict(TypedDict):
    conditions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentFlowDefinitionNodeConfigurationConditionConditionArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationConditionArgs:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentFlowDefinitionNodeConfigurationConditionConditionArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AgentFlowDefinitionNodeConfigurationConditionConditionArgs]
            ]
        ]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentFlowDefinitionNodeConfigurationConditionConditionArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationConditionConditionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    expression: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationConditionConditionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentFlowDefinitionNodeConfigurationInlineCodeArgsDict(TypedDict):
    code: pulumi.Input[_builtins.str]
    language: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationInlineCodeArgs:
    def __init__(
        __self__,
        *,
        code: pulumi.Input[_builtins.str],
        language: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> pulumi.Input[_builtins.str]: ...
    @code.setter
    def code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def language(self) -> pulumi.Input[_builtins.str]: ...
    @language.setter
    def language(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeConfigurationInputArgsDict(TypedDict): ...

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationInputArgs:
    def __init__(__self__) -> None: ...

class AgentFlowDefinitionNodeConfigurationIteratorArgsDict(TypedDict): ...

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationIteratorArgs:
    def __init__(__self__) -> None: ...

class AgentFlowDefinitionNodeConfigurationKnowledgeBaseArgsDict(TypedDict):
    knowledge_base_id: pulumi.Input[_builtins.str]
    model_id: pulumi.Input[_builtins.str]
    guardrail_configuration: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationKnowledgeBaseGuardrailConfigurationArgsDict
        ]
    ]
    inference_configuration: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfigurationArgsDict
        ]
    ]
    number_of_results: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationKnowledgeBaseArgs:
    def __init__(
        __self__,
        *,
        knowledge_base_id: pulumi.Input[_builtins.str],
        model_id: pulumi.Input[_builtins.str],
        guardrail_configuration: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationKnowledgeBaseGuardrailConfigurationArgs
            ]
        ] = ...,
        inference_configuration: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfigurationArgs
            ]
        ] = ...,
        number_of_results: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="knowledgeBaseId")
    def knowledge_base_id(self) -> pulumi.Input[_builtins.str]: ...
    @knowledge_base_id.setter
    def knowledge_base_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> pulumi.Input[_builtins.str]: ...
    @model_id.setter
    def model_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="guardrailConfiguration")
    def guardrail_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationKnowledgeBaseGuardrailConfigurationArgs
        ]
    ]: ...
    @guardrail_configuration.setter
    def guardrail_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationKnowledgeBaseGuardrailConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inferenceConfiguration")
    def inference_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfigurationArgs
        ]
    ]: ...
    @inference_configuration.setter
    def inference_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="numberOfResults")
    def number_of_results(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_results.setter
    def number_of_results(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AgentFlowDefinitionNodeConfigurationKnowledgeBaseGuardrailConfigurationArgsDict(
    TypedDict
):
    guardrail_identifier: pulumi.Input[_builtins.str]
    guardrail_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationKnowledgeBaseGuardrailConfigurationArgs:
    def __init__(
        __self__,
        *,
        guardrail_identifier: pulumi.Input[_builtins.str],
        guardrail_version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="guardrailIdentifier")
    def guardrail_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @guardrail_identifier.setter
    def guardrail_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="guardrailVersion")
    def guardrail_version(self) -> pulumi.Input[_builtins.str]: ...
    @guardrail_version.setter
    def guardrail_version(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfigurationArgsDict(
    TypedDict
):
    text: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfigurationTextArgsDict
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfigurationArgs:
    def __init__(
        __self__,
        *,
        text: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfigurationTextArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfigurationTextArgs
        ]
    ]: ...
    @text.setter
    def text(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfigurationTextArgs
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfigurationTextArgsDict(
    TypedDict
):
    max_tokens: NotRequired[pulumi.Input[_builtins.int]]
    stop_sequences: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    top_p: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationKnowledgeBaseInferenceConfigurationTextArgs:
    def __init__(
        __self__,
        *,
        max_tokens: Optional[pulumi.Input[_builtins.int]] = ...,
        stop_sequences: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        temperature: Optional[pulumi.Input[_builtins.float]] = ...,
        top_p: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxTokens")
    def max_tokens(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_tokens.setter
    def max_tokens(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="stopSequences")
    def stop_sequences(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @stop_sequences.setter
    def stop_sequences(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="topP")
    def top_p(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @top_p.setter
    def top_p(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AgentFlowDefinitionNodeConfigurationLambdaFunctionArgsDict(TypedDict):
    lambda_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationLambdaFunctionArgs:
    def __init__(__self__, *, lambda_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> pulumi.Input[_builtins.str]: ...
    @lambda_arn.setter
    def lambda_arn(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeConfigurationLexArgsDict(TypedDict):
    bot_alias_arn: pulumi.Input[_builtins.str]
    locale_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationLexArgs:
    def __init__(
        __self__,
        *,
        bot_alias_arn: pulumi.Input[_builtins.str],
        locale_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="botAliasArn")
    def bot_alias_arn(self) -> pulumi.Input[_builtins.str]: ...
    @bot_alias_arn.setter
    def bot_alias_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="localeId")
    def locale_id(self) -> pulumi.Input[_builtins.str]: ...
    @locale_id.setter
    def locale_id(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeConfigurationOutputArgsDict(TypedDict): ...

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationOutputArgs:
    def __init__(__self__) -> None: ...

class AgentFlowDefinitionNodeConfigurationPromptArgsDict(TypedDict):
    guardrail_configuration: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptGuardrailConfigurationArgsDict
        ]
    ]
    source_configuration: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptArgs:
    def __init__(
        __self__,
        *,
        guardrail_configuration: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptGuardrailConfigurationArgs
            ]
        ] = ...,
        source_configuration: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="guardrailConfiguration")
    def guardrail_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptGuardrailConfigurationArgs
        ]
    ]: ...
    @guardrail_configuration.setter
    def guardrail_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptGuardrailConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> Optional[
        pulumi.Input[AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationArgs]
    ]: ...
    @source_configuration.setter
    def source_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationArgs
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationPromptGuardrailConfigurationArgsDict(
    TypedDict
):
    guardrail_identifier: pulumi.Input[_builtins.str]
    guardrail_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptGuardrailConfigurationArgs:
    def __init__(
        __self__,
        *,
        guardrail_identifier: pulumi.Input[_builtins.str],
        guardrail_version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="guardrailIdentifier")
    def guardrail_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @guardrail_identifier.setter
    def guardrail_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="guardrailVersion")
    def guardrail_version(self) -> pulumi.Input[_builtins.str]: ...
    @guardrail_version.setter
    def guardrail_version(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationArgsDict(TypedDict):
    inline: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineArgsDict
        ]
    ]
    resource: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationResourceArgsDict
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationArgs:
    def __init__(
        __self__,
        *,
        inline: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineArgs
            ]
        ] = ...,
        resource: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationResourceArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def inline(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineArgs
        ]
    ]: ...
    @inline.setter
    def inline(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resource(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationResourceArgs
        ]
    ]: ...
    @resource.setter
    def resource(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationResourceArgs
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineArgsDict(
    TypedDict
):
    model_id: pulumi.Input[_builtins.str]
    template_type: pulumi.Input[_builtins.str]
    additional_model_request_fields: NotRequired[pulumi.Input[_builtins.str]]
    inference_configuration: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfigurationArgsDict
        ]
    ]
    template_configuration: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineArgs:
    def __init__(
        __self__,
        *,
        model_id: pulumi.Input[_builtins.str],
        template_type: pulumi.Input[_builtins.str],
        additional_model_request_fields: Optional[pulumi.Input[_builtins.str]] = ...,
        inference_configuration: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfigurationArgs
            ]
        ] = ...,
        template_configuration: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> pulumi.Input[_builtins.str]: ...
    @model_id.setter
    def model_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="templateType")
    def template_type(self) -> pulumi.Input[_builtins.str]: ...
    @template_type.setter
    def template_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalModelRequestFields")
    def additional_model_request_fields(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_model_request_fields.setter
    def additional_model_request_fields(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inferenceConfiguration")
    def inference_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfigurationArgs
        ]
    ]: ...
    @inference_configuration.setter
    def inference_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="templateConfiguration")
    def template_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationArgs
        ]
    ]: ...
    @template_configuration.setter
    def template_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationArgs
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfigurationArgsDict(
    TypedDict
):
    text: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfigurationTextArgsDict
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfigurationArgs:
    def __init__(
        __self__,
        *,
        text: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfigurationTextArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfigurationTextArgs
        ]
    ]: ...
    @text.setter
    def text(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfigurationTextArgs
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfigurationTextArgsDict(
    TypedDict
):
    max_tokens: NotRequired[pulumi.Input[_builtins.int]]
    stop_sequences: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    top_p: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineInferenceConfigurationTextArgs:
    def __init__(
        __self__,
        *,
        max_tokens: Optional[pulumi.Input[_builtins.int]] = ...,
        stop_sequences: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        temperature: Optional[pulumi.Input[_builtins.float]] = ...,
        top_p: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxTokens")
    def max_tokens(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_tokens.setter
    def max_tokens(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="stopSequences")
    def stop_sequences(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @stop_sequences.setter
    def stop_sequences(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="topP")
    def top_p(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @top_p.setter
    def top_p(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationArgsDict(
    TypedDict
):
    chat: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatArgsDict
        ]
    ]
    text: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextArgsDict
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationArgs:
    def __init__(
        __self__,
        *,
        chat: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatArgs
            ]
        ] = ...,
        text: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def chat(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatArgs
        ]
    ]: ...
    @chat.setter
    def chat(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextArgs
        ]
    ]: ...
    @text.setter
    def text(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextArgs
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatArgsDict(
    TypedDict
):
    messages: pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageArgsDict
            ]
        ]
    ]
    input_variables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatInputVariableArgsDict
                ]
            ]
        ]
    ]
    systems: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystemArgsDict
                ]
            ]
        ]
    ]
    tool_configuration: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatArgs:
    def __init__(
        __self__,
        *,
        messages: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageArgs
                ]
            ]
        ],
        input_variables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatInputVariableArgs
                    ]
                ]
            ]
        ] = ...,
        systems: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystemArgs
                    ]
                ]
            ]
        ] = ...,
        tool_configuration: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def messages(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageArgs
            ]
        ]
    ]: ...
    @messages.setter
    def messages(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputVariables")
    def input_variables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatInputVariableArgs
                ]
            ]
        ]
    ]: ...
    @input_variables.setter
    def input_variables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatInputVariableArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def systems(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystemArgs
                ]
            ]
        ]
    ]: ...
    @systems.setter
    def systems(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystemArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="toolConfiguration")
    def tool_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationArgs
        ]
    ]: ...
    @tool_configuration.setter
    def tool_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationArgs
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatInputVariableArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatInputVariableArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageArgsDict(
    TypedDict
):
    role: pulumi.Input[_builtins.str]
    content: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContentArgsDict
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageArgs:
    def __init__(
        __self__,
        *,
        role: pulumi.Input[_builtins.str],
        content: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContentArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]: ...
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def content(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContentArgs
        ]
    ]: ...
    @content.setter
    def content(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContentArgs
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContentArgsDict(
    TypedDict
):
    cache_point: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContentCachePointArgsDict
        ]
    ]
    text: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContentArgs:
    def __init__(
        __self__,
        *,
        cache_point: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContentCachePointArgs
            ]
        ] = ...,
        text: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cachePoint")
    def cache_point(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContentCachePointArgs
        ]
    ]: ...
    @cache_point.setter
    def cache_point(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContentCachePointArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContentCachePointArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatMessageContentCachePointArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystemArgsDict(
    TypedDict
):
    cache_point: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystemCachePointArgsDict
        ]
    ]
    text: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystemArgs:
    def __init__(
        __self__,
        *,
        cache_point: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystemCachePointArgs
            ]
        ] = ...,
        text: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cachePoint")
    def cache_point(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystemCachePointArgs
        ]
    ]: ...
    @cache_point.setter
    def cache_point(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystemCachePointArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystemCachePointArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatSystemCachePointArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationArgsDict(
    TypedDict
):
    tool_choice: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceArgsDict
        ]
    ]
    tools: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationArgs:
    def __init__(
        __self__,
        *,
        tool_choice: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceArgs
            ]
        ] = ...,
        tools: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="toolChoice")
    def tool_choice(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceArgs
        ]
    ]: ...
    @tool_choice.setter
    def tool_choice(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tools(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolArgs
                ]
            ]
        ]
    ]: ...
    @tools.setter
    def tools(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolArgsDict(
    TypedDict
):
    cache_point: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolCachePointArgsDict
        ]
    ]
    tool_spec: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpecArgsDict
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolArgs:
    def __init__(
        __self__,
        *,
        cache_point: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolCachePointArgs
            ]
        ] = ...,
        tool_spec: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpecArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cachePoint")
    def cache_point(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolCachePointArgs
        ]
    ]: ...
    @cache_point.setter
    def cache_point(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolCachePointArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="toolSpec")
    def tool_spec(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpecArgs
        ]
    ]: ...
    @tool_spec.setter
    def tool_spec(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpecArgs
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolCachePointArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolCachePointArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceArgsDict(
    TypedDict
):
    any: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAnyArgsDict
        ]
    ]
    auto: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAutoArgsDict
        ]
    ]
    tool: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceToolArgsDict
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceArgs:
    def __init__(
        __self__,
        *,
        any: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAnyArgs
            ]
        ] = ...,
        auto: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAutoArgs
            ]
        ] = ...,
        tool: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceToolArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def any(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAnyArgs
        ]
    ]: ...
    @any.setter
    def any(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAnyArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def auto(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAutoArgs
        ]
    ]: ...
    @auto.setter
    def auto(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAutoArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tool(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceToolArgs
        ]
    ]: ...
    @tool.setter
    def tool(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceToolArgs
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAnyArgsDict(
    TypedDict
): ...

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAnyArgs:
    def __init__(__self__) -> None: ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAutoArgsDict(
    TypedDict
): ...

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceAutoArgs:
    def __init__(__self__) -> None: ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceToolArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolChoiceToolArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpecArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    input_schema: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpecInputSchemaArgsDict
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpecArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        input_schema: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpecInputSchemaArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputSchema")
    def input_schema(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpecInputSchemaArgs
        ]
    ]: ...
    @input_schema.setter
    def input_schema(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpecInputSchemaArgs
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpecInputSchemaArgsDict(
    TypedDict
):
    json: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationChatToolConfigurationToolToolSpecInputSchemaArgs:
    def __init__(
        __self__, *, json: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @json.setter
    def json(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextArgsDict(
    TypedDict
):
    text: pulumi.Input[_builtins.str]
    cache_point: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextCachePointArgsDict
        ]
    ]
    input_variables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextInputVariableArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextArgs:
    def __init__(
        __self__,
        *,
        text: pulumi.Input[_builtins.str],
        cache_point: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextCachePointArgs
            ]
        ] = ...,
        input_variables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextInputVariableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> pulumi.Input[_builtins.str]: ...
    @text.setter
    def text(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cachePoint")
    def cache_point(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextCachePointArgs
        ]
    ]: ...
    @cache_point.setter
    def cache_point(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextCachePointArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputVariables")
    def input_variables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextInputVariableArgs
                ]
            ]
        ]
    ]: ...
    @input_variables.setter
    def input_variables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextInputVariableArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextCachePointArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextCachePointArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextInputVariableArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationInlineTemplateConfigurationTextInputVariableArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationResourceArgsDict(
    TypedDict
):
    prompt_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationPromptSourceConfigurationResourceArgs:
    def __init__(__self__, *, prompt_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="promptArn")
    def prompt_arn(self) -> pulumi.Input[_builtins.str]: ...
    @prompt_arn.setter
    def prompt_arn(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeConfigurationRetrievalArgsDict(TypedDict):
    service_configuration: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationRetrievalServiceConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationRetrievalArgs:
    def __init__(
        __self__,
        *,
        service_configuration: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationRetrievalServiceConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceConfiguration")
    def service_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationRetrievalServiceConfigurationArgs
        ]
    ]: ...
    @service_configuration.setter
    def service_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationRetrievalServiceConfigurationArgs
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationRetrievalServiceConfigurationArgsDict(
    TypedDict
):
    s3: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationRetrievalServiceConfigurationS3ArgsDict
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationRetrievalServiceConfigurationArgs:
    def __init__(
        __self__,
        *,
        s3: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationRetrievalServiceConfigurationS3Args
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationRetrievalServiceConfigurationS3Args
        ]
    ]: ...
    @s3.setter
    def s3(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationRetrievalServiceConfigurationS3Args
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationRetrievalServiceConfigurationS3ArgsDict(
    TypedDict
):
    bucket_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationRetrievalServiceConfigurationS3Args:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeConfigurationStorageArgsDict(TypedDict):
    service_configuration: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationStorageServiceConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationStorageArgs:
    def __init__(
        __self__,
        *,
        service_configuration: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationStorageServiceConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceConfiguration")
    def service_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationStorageServiceConfigurationArgs
        ]
    ]: ...
    @service_configuration.setter
    def service_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationStorageServiceConfigurationArgs
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationStorageServiceConfigurationArgsDict(
    TypedDict
):
    s3: NotRequired[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationStorageServiceConfigurationS3ArgsDict
        ]
    ]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationStorageServiceConfigurationArgs:
    def __init__(
        __self__,
        *,
        s3: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationStorageServiceConfigurationS3Args
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentFlowDefinitionNodeConfigurationStorageServiceConfigurationS3Args
        ]
    ]: ...
    @s3.setter
    def s3(
        self,
        value: Optional[
            pulumi.Input[
                AgentFlowDefinitionNodeConfigurationStorageServiceConfigurationS3Args
            ]
        ],
    ): ...

class AgentFlowDefinitionNodeConfigurationStorageServiceConfigurationS3ArgsDict(
    TypedDict
):
    bucket_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeConfigurationStorageServiceConfigurationS3Args:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowDefinitionNodeInputArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    category: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentFlowDefinitionNodeInputArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        category: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @category.setter
    def category(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentFlowDefinitionNodeOutputArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentFlowDefinitionNodeOutputArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class AgentFlowTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentFlowTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    kendra_knowledge_base_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationKendraKnowledgeBaseConfigurationArgsDict
        ]
    ]
    sql_knowledge_base_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationArgsDict
        ]
    ]
    vector_knowledge_base_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        kendra_knowledge_base_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationKendraKnowledgeBaseConfigurationArgs
            ]
        ] = ...,
        sql_knowledge_base_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationArgs
            ]
        ] = ...,
        vector_knowledge_base_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kendraKnowledgeBaseConfiguration")
    def kendra_knowledge_base_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationKendraKnowledgeBaseConfigurationArgs
        ]
    ]: ...
    @kendra_knowledge_base_configuration.setter
    def kendra_knowledge_base_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationKendraKnowledgeBaseConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqlKnowledgeBaseConfiguration")
    def sql_knowledge_base_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationArgs
        ]
    ]: ...
    @sql_knowledge_base_configuration.setter
    def sql_knowledge_base_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vectorKnowledgeBaseConfiguration")
    def vector_knowledge_base_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationArgs
        ]
    ]: ...
    @vector_knowledge_base_configuration.setter
    def vector_knowledge_base_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationArgs
            ]
        ],
    ): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationKendraKnowledgeBaseConfigurationArgsDict(
    TypedDict
):
    kendra_index_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationKendraKnowledgeBaseConfigurationArgs:
    def __init__(
        __self__, *, kendra_index_arn: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kendraIndexArn")
    def kendra_index_arn(self) -> pulumi.Input[_builtins.str]: ...
    @kendra_index_arn.setter
    def kendra_index_arn(self, value: pulumi.Input[_builtins.str]): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    redshift_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        redshift_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="redshiftConfiguration")
    def redshift_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationArgs
        ]
    ]: ...
    @redshift_configuration.setter
    def redshift_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationArgs
            ]
        ],
    ): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationArgsDict(
    TypedDict
):
    query_engine_configuration: pulumi.Input[
        AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationArgsDict
    ]
    storage_configuration: pulumi.Input[
        AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationArgsDict
    ]
    query_generation_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationArgs:
    def __init__(
        __self__,
        *,
        query_engine_configuration: pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationArgs
        ],
        storage_configuration: pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationArgs
        ],
        query_generation_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryEngineConfiguration")
    def query_engine_configuration(
        self,
    ) -> pulumi.Input[
        AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationArgs
    ]: ...
    @query_engine_configuration.setter
    def query_engine_configuration(
        self,
        value: pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageConfiguration")
    def storage_configuration(
        self,
    ) -> pulumi.Input[
        AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationArgs
    ]: ...
    @storage_configuration.setter
    def storage_configuration(
        self,
        value: pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryGenerationConfiguration")
    def query_generation_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationArgs
        ]
    ]: ...
    @query_generation_configuration.setter
    def query_generation_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationArgs
            ]
        ],
    ): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    provisioned_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfigurationArgsDict
        ]
    ]
    serverless_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        provisioned_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfigurationArgs
            ]
        ] = ...,
        serverless_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedConfiguration")
    def provisioned_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfigurationArgs
        ]
    ]: ...
    @provisioned_configuration.setter
    def provisioned_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverlessConfiguration")
    def serverless_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfigurationArgs
        ]
    ]: ...
    @serverless_configuration.setter
    def serverless_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfigurationArgs
            ]
        ],
    ): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfigurationArgsDict(
    TypedDict
):
    auth_configuration: pulumi.Input[
        AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfigurationAuthConfigurationArgsDict
    ]
    cluster_identifier: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfigurationArgs:
    def __init__(
        __self__,
        *,
        auth_configuration: pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfigurationAuthConfigurationArgs
        ],
        cluster_identifier: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authConfiguration")
    def auth_configuration(
        self,
    ) -> pulumi.Input[
        AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfigurationAuthConfigurationArgs
    ]: ...
    @auth_configuration.setter
    def auth_configuration(
        self,
        value: pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfigurationAuthConfigurationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_identifier.setter
    def cluster_identifier(self, value: pulumi.Input[_builtins.str]): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfigurationAuthConfigurationArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    database_user: NotRequired[pulumi.Input[_builtins.str]]
    username_password_secret_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationProvisionedConfigurationAuthConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        database_user: Optional[pulumi.Input[_builtins.str]] = ...,
        username_password_secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseUser")
    def database_user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_user.setter
    def database_user(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="usernamePasswordSecretArn")
    def username_password_secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username_password_secret_arn.setter
    def username_password_secret_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfigurationArgsDict(
    TypedDict
):
    auth_configuration: pulumi.Input[
        AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfigurationAuthConfigurationArgsDict
    ]
    workgroup_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfigurationArgs:
    def __init__(
        __self__,
        *,
        auth_configuration: pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfigurationAuthConfigurationArgs
        ],
        workgroup_arn: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authConfiguration")
    def auth_configuration(
        self,
    ) -> pulumi.Input[
        AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfigurationAuthConfigurationArgs
    ]: ...
    @auth_configuration.setter
    def auth_configuration(
        self,
        value: pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfigurationAuthConfigurationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="workgroupArn")
    def workgroup_arn(self) -> pulumi.Input[_builtins.str]: ...
    @workgroup_arn.setter
    def workgroup_arn(self, value: pulumi.Input[_builtins.str]): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfigurationAuthConfigurationArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    username_password_secret_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryEngineConfigurationServerlessConfigurationAuthConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        username_password_secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="usernamePasswordSecretArn")
    def username_password_secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username_password_secret_arn.setter
    def username_password_secret_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationArgsDict(
    TypedDict
):
    execution_timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]
    generation_context: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextArgsDict
        ]
    ]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationArgs:
    def __init__(
        __self__,
        *,
        execution_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        generation_context: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionTimeoutSeconds")
    def execution_timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @execution_timeout_seconds.setter
    def execution_timeout_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="generationContext")
    def generation_context(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextArgs
        ]
    ]: ...
    @generation_context.setter
    def generation_context(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextArgs
            ]
        ],
    ): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextArgsDict(
    TypedDict
):
    curated_queries: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextCuratedQueryArgsDict
                ]
            ]
        ]
    ]
    tables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTableArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextArgs:
    def __init__(
        __self__,
        *,
        curated_queries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextCuratedQueryArgs
                    ]
                ]
            ]
        ] = ...,
        tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="curatedQueries")
    def curated_queries(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextCuratedQueryArgs
                ]
            ]
        ]
    ]: ...
    @curated_queries.setter
    def curated_queries(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextCuratedQueryArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTableArgs
                ]
            ]
        ]
    ]: ...
    @tables.setter
    def tables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTableArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextCuratedQueryArgsDict(
    TypedDict
):
    natural_language: pulumi.Input[_builtins.str]
    sql: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextCuratedQueryArgs:
    def __init__(
        __self__,
        *,
        natural_language: pulumi.Input[_builtins.str],
        sql: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="naturalLanguage")
    def natural_language(self) -> pulumi.Input[_builtins.str]: ...
    @natural_language.setter
    def natural_language(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sql(self) -> pulumi.Input[_builtins.str]: ...
    @sql.setter
    def sql(self, value: pulumi.Input[_builtins.str]): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTableArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTableColumnArgsDict
                ]
            ]
        ]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    inclusion: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTableArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTableColumnArgs
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        inclusion: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTableColumnArgs
                ]
            ]
        ]
    ]: ...
    @columns.setter
    def columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTableColumnArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def inclusion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inclusion.setter
    def inclusion(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTableColumnArgsDict(
    TypedDict
):
    description: NotRequired[pulumi.Input[_builtins.str]]
    inclusion: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationQueryGenerationConfigurationGenerationContextTableColumnArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        inclusion: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def inclusion(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inclusion.setter
    def inclusion(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    aws_data_catalog_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationAwsDataCatalogConfigurationArgsDict
        ]
    ]
    redshift_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationRedshiftConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        aws_data_catalog_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationAwsDataCatalogConfigurationArgs
            ]
        ] = ...,
        redshift_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationRedshiftConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="awsDataCatalogConfiguration")
    def aws_data_catalog_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationAwsDataCatalogConfigurationArgs
        ]
    ]: ...
    @aws_data_catalog_configuration.setter
    def aws_data_catalog_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationAwsDataCatalogConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="redshiftConfiguration")
    def redshift_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationRedshiftConfigurationArgs
        ]
    ]: ...
    @redshift_configuration.setter
    def redshift_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationRedshiftConfigurationArgs
            ]
        ],
    ): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationAwsDataCatalogConfigurationArgsDict(
    TypedDict
):
    table_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationAwsDataCatalogConfigurationArgs:
    def __init__(
        __self__, *, table_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableNames")
    def table_names(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @table_names.setter
    def table_names(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationRedshiftConfigurationArgsDict(
    TypedDict
):
    database_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationSqlKnowledgeBaseConfigurationRedshiftConfigurationStorageConfigurationRedshiftConfigurationArgs:
    def __init__(__self__, *, database_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationArgsDict(
    TypedDict
):
    embedding_model_arn: pulumi.Input[_builtins.str]
    embedding_model_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfigurationArgsDict
        ]
    ]
    supplemental_data_storage_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationArgs:
    def __init__(
        __self__,
        *,
        embedding_model_arn: pulumi.Input[_builtins.str],
        embedding_model_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfigurationArgs
            ]
        ] = ...,
        supplemental_data_storage_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="embeddingModelArn")
    def embedding_model_arn(self) -> pulumi.Input[_builtins.str]: ...
    @embedding_model_arn.setter
    def embedding_model_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="embeddingModelConfiguration")
    def embedding_model_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfigurationArgs
        ]
    ]: ...
    @embedding_model_configuration.setter
    def embedding_model_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="supplementalDataStorageConfiguration")
    def supplemental_data_storage_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationArgs
        ]
    ]: ...
    @supplemental_data_storage_configuration.setter
    def supplemental_data_storage_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationArgs
            ]
        ],
    ): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfigurationArgsDict(
    TypedDict
):
    bedrock_embedding_model_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfigurationBedrockEmbeddingModelConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfigurationArgs:
    def __init__(
        __self__,
        *,
        bedrock_embedding_model_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfigurationBedrockEmbeddingModelConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bedrockEmbeddingModelConfiguration")
    def bedrock_embedding_model_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfigurationBedrockEmbeddingModelConfigurationArgs
        ]
    ]: ...
    @bedrock_embedding_model_configuration.setter
    def bedrock_embedding_model_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfigurationBedrockEmbeddingModelConfigurationArgs
            ]
        ],
    ): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfigurationBedrockEmbeddingModelConfigurationArgsDict(
    TypedDict
):
    dimensions: NotRequired[pulumi.Input[_builtins.int]]
    embedding_data_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationEmbeddingModelConfigurationBedrockEmbeddingModelConfigurationArgs:
    def __init__(
        __self__,
        *,
        dimensions: Optional[pulumi.Input[_builtins.int]] = ...,
        embedding_data_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="embeddingDataType")
    def embedding_data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @embedding_data_type.setter
    def embedding_data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationArgsDict(
    TypedDict
):
    storage_locations: pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocationArgsDict
            ]
        ]
    ]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationArgs:
    def __init__(
        __self__,
        *,
        storage_locations: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocationArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageLocations")
    def storage_locations(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocationArgs
            ]
        ]
    ]: ...
    @storage_locations.setter
    def storage_locations(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocationArgs
                ]
            ]
        ],
    ): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocationArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    s3_location: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocationS3LocationArgsDict
        ]
    ]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        s3_location: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocationS3LocationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3Location")
    def s3_location(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocationS3LocationArgs
        ]
    ]: ...
    @s3_location.setter
    def s3_location(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocationS3LocationArgs
            ]
        ],
    ): ...

class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocationS3LocationArgsDict(
    TypedDict
):
    uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentKnowledgeBaseKnowledgeBaseConfigurationVectorKnowledgeBaseConfigurationSupplementalDataStorageConfigurationStorageLocationS3LocationArgs:
    def __init__(__self__, *, uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...

class AgentKnowledgeBaseStorageConfigurationArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    mongo_db_atlas_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfigurationArgsDict
        ]
    ]
    neptune_analytics_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfigurationArgsDict
        ]
    ]
    opensearch_managed_cluster_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfigurationArgsDict
        ]
    ]
    opensearch_serverless_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfigurationArgsDict
        ]
    ]
    pinecone_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationPineconeConfigurationArgsDict
        ]
    ]
    rds_configuration: NotRequired[
        pulumi.Input[AgentKnowledgeBaseStorageConfigurationRdsConfigurationArgsDict]
    ]
    redis_enterprise_cloud_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfigurationArgsDict
        ]
    ]
    s3_vectors_configuration: NotRequired[
        pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationS3VectorsConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentKnowledgeBaseStorageConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        mongo_db_atlas_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfigurationArgs
            ]
        ] = ...,
        neptune_analytics_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfigurationArgs
            ]
        ] = ...,
        opensearch_managed_cluster_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfigurationArgs
            ]
        ] = ...,
        opensearch_serverless_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfigurationArgs
            ]
        ] = ...,
        pinecone_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseStorageConfigurationPineconeConfigurationArgs
            ]
        ] = ...,
        rds_configuration: Optional[
            pulumi.Input[AgentKnowledgeBaseStorageConfigurationRdsConfigurationArgs]
        ] = ...,
        redis_enterprise_cloud_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfigurationArgs
            ]
        ] = ...,
        s3_vectors_configuration: Optional[
            pulumi.Input[
                AgentKnowledgeBaseStorageConfigurationS3VectorsConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mongoDbAtlasConfiguration")
    def mongo_db_atlas_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfigurationArgs
        ]
    ]: ...
    @mongo_db_atlas_configuration.setter
    def mongo_db_atlas_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="neptuneAnalyticsConfiguration")
    def neptune_analytics_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfigurationArgs
        ]
    ]: ...
    @neptune_analytics_configuration.setter
    def neptune_analytics_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="opensearchManagedClusterConfiguration")
    def opensearch_managed_cluster_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfigurationArgs
        ]
    ]: ...
    @opensearch_managed_cluster_configuration.setter
    def opensearch_managed_cluster_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="opensearchServerlessConfiguration")
    def opensearch_serverless_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfigurationArgs
        ]
    ]: ...
    @opensearch_serverless_configuration.setter
    def opensearch_serverless_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pineconeConfiguration")
    def pinecone_configuration(
        self,
    ) -> Optional[
        pulumi.Input[AgentKnowledgeBaseStorageConfigurationPineconeConfigurationArgs]
    ]: ...
    @pinecone_configuration.setter
    def pinecone_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseStorageConfigurationPineconeConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rdsConfiguration")
    def rds_configuration(
        self,
    ) -> Optional[
        pulumi.Input[AgentKnowledgeBaseStorageConfigurationRdsConfigurationArgs]
    ]: ...
    @rds_configuration.setter
    def rds_configuration(
        self,
        value: Optional[
            pulumi.Input[AgentKnowledgeBaseStorageConfigurationRdsConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="redisEnterpriseCloudConfiguration")
    def redis_enterprise_cloud_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfigurationArgs
        ]
    ]: ...
    @redis_enterprise_cloud_configuration.setter
    def redis_enterprise_cloud_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3VectorsConfiguration")
    def s3_vectors_configuration(
        self,
    ) -> Optional[
        pulumi.Input[AgentKnowledgeBaseStorageConfigurationS3VectorsConfigurationArgs]
    ]: ...
    @s3_vectors_configuration.setter
    def s3_vectors_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentKnowledgeBaseStorageConfigurationS3VectorsConfigurationArgs
            ]
        ],
    ): ...

class AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfigurationArgsDict(
    TypedDict
):
    collection_name: pulumi.Input[_builtins.str]
    credentials_secret_arn: pulumi.Input[_builtins.str]
    database_name: pulumi.Input[_builtins.str]
    endpoint: pulumi.Input[_builtins.str]
    field_mapping: pulumi.Input[
        AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfigurationFieldMappingArgsDict
    ]
    vector_index_name: pulumi.Input[_builtins.str]
    endpoint_service_name: NotRequired[pulumi.Input[_builtins.str]]
    text_index_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfigurationArgs:
    def __init__(
        __self__,
        *,
        collection_name: pulumi.Input[_builtins.str],
        credentials_secret_arn: pulumi.Input[_builtins.str],
        database_name: pulumi.Input[_builtins.str],
        endpoint: pulumi.Input[_builtins.str],
        field_mapping: pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfigurationFieldMappingArgs
        ],
        vector_index_name: pulumi.Input[_builtins.str],
        endpoint_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        text_index_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collectionName")
    def collection_name(self) -> pulumi.Input[_builtins.str]: ...
    @collection_name.setter
    def collection_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="credentialsSecretArn")
    def credentials_secret_arn(self) -> pulumi.Input[_builtins.str]: ...
    @credentials_secret_arn.setter
    def credentials_secret_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fieldMapping")
    def field_mapping(
        self,
    ) -> pulumi.Input[
        AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfigurationFieldMappingArgs
    ]: ...
    @field_mapping.setter
    def field_mapping(
        self,
        value: pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfigurationFieldMappingArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vectorIndexName")
    def vector_index_name(self) -> pulumi.Input[_builtins.str]: ...
    @vector_index_name.setter
    def vector_index_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointServiceName")
    def endpoint_service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_service_name.setter
    def endpoint_service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="textIndexName")
    def text_index_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @text_index_name.setter
    def text_index_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfigurationFieldMappingArgsDict(
    TypedDict
):
    metadata_field: pulumi.Input[_builtins.str]
    text_field: pulumi.Input[_builtins.str]
    vector_field: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentKnowledgeBaseStorageConfigurationMongoDbAtlasConfigurationFieldMappingArgs:
    def __init__(
        __self__,
        *,
        metadata_field: pulumi.Input[_builtins.str],
        text_field: pulumi.Input[_builtins.str],
        vector_field: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataField")
    def metadata_field(self) -> pulumi.Input[_builtins.str]: ...
    @metadata_field.setter
    def metadata_field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="textField")
    def text_field(self) -> pulumi.Input[_builtins.str]: ...
    @text_field.setter
    def text_field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vectorField")
    def vector_field(self) -> pulumi.Input[_builtins.str]: ...
    @vector_field.setter
    def vector_field(self, value: pulumi.Input[_builtins.str]): ...

class AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfigurationArgsDict(
    TypedDict
):
    field_mapping: pulumi.Input[
        AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfigurationFieldMappingArgsDict
    ]
    graph_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfigurationArgs:
    def __init__(
        __self__,
        *,
        field_mapping: pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfigurationFieldMappingArgs
        ],
        graph_arn: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldMapping")
    def field_mapping(
        self,
    ) -> pulumi.Input[
        AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfigurationFieldMappingArgs
    ]: ...
    @field_mapping.setter
    def field_mapping(
        self,
        value: pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfigurationFieldMappingArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="graphArn")
    def graph_arn(self) -> pulumi.Input[_builtins.str]: ...
    @graph_arn.setter
    def graph_arn(self, value: pulumi.Input[_builtins.str]): ...

class AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfigurationFieldMappingArgsDict(
    TypedDict
):
    metadata_field: pulumi.Input[_builtins.str]
    text_field: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentKnowledgeBaseStorageConfigurationNeptuneAnalyticsConfigurationFieldMappingArgs:
    def __init__(
        __self__,
        *,
        metadata_field: pulumi.Input[_builtins.str],
        text_field: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataField")
    def metadata_field(self) -> pulumi.Input[_builtins.str]: ...
    @metadata_field.setter
    def metadata_field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="textField")
    def text_field(self) -> pulumi.Input[_builtins.str]: ...
    @text_field.setter
    def text_field(self, value: pulumi.Input[_builtins.str]): ...

class AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfigurationArgsDict(
    TypedDict
):
    domain_arn: pulumi.Input[_builtins.str]
    domain_endpoint: pulumi.Input[_builtins.str]
    field_mapping: pulumi.Input[
        AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfigurationFieldMappingArgsDict
    ]
    vector_index_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfigurationArgs:
    def __init__(
        __self__,
        *,
        domain_arn: pulumi.Input[_builtins.str],
        domain_endpoint: pulumi.Input[_builtins.str],
        field_mapping: pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfigurationFieldMappingArgs
        ],
        vector_index_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainArn")
    def domain_arn(self) -> pulumi.Input[_builtins.str]: ...
    @domain_arn.setter
    def domain_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="domainEndpoint")
    def domain_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @domain_endpoint.setter
    def domain_endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fieldMapping")
    def field_mapping(
        self,
    ) -> pulumi.Input[
        AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfigurationFieldMappingArgs
    ]: ...
    @field_mapping.setter
    def field_mapping(
        self,
        value: pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfigurationFieldMappingArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vectorIndexName")
    def vector_index_name(self) -> pulumi.Input[_builtins.str]: ...
    @vector_index_name.setter
    def vector_index_name(self, value: pulumi.Input[_builtins.str]): ...

class AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfigurationFieldMappingArgsDict(
    TypedDict
):
    metadata_field: pulumi.Input[_builtins.str]
    text_field: pulumi.Input[_builtins.str]
    vector_field: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentKnowledgeBaseStorageConfigurationOpensearchManagedClusterConfigurationFieldMappingArgs:
    def __init__(
        __self__,
        *,
        metadata_field: pulumi.Input[_builtins.str],
        text_field: pulumi.Input[_builtins.str],
        vector_field: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataField")
    def metadata_field(self) -> pulumi.Input[_builtins.str]: ...
    @metadata_field.setter
    def metadata_field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="textField")
    def text_field(self) -> pulumi.Input[_builtins.str]: ...
    @text_field.setter
    def text_field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vectorField")
    def vector_field(self) -> pulumi.Input[_builtins.str]: ...
    @vector_field.setter
    def vector_field(self, value: pulumi.Input[_builtins.str]): ...

class AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfigurationArgsDict(
    TypedDict
):
    collection_arn: pulumi.Input[_builtins.str]
    field_mapping: pulumi.Input[
        AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfigurationFieldMappingArgsDict
    ]
    vector_index_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfigurationArgs:
    def __init__(
        __self__,
        *,
        collection_arn: pulumi.Input[_builtins.str],
        field_mapping: pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfigurationFieldMappingArgs
        ],
        vector_index_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collectionArn")
    def collection_arn(self) -> pulumi.Input[_builtins.str]: ...
    @collection_arn.setter
    def collection_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fieldMapping")
    def field_mapping(
        self,
    ) -> pulumi.Input[
        AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfigurationFieldMappingArgs
    ]: ...
    @field_mapping.setter
    def field_mapping(
        self,
        value: pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfigurationFieldMappingArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vectorIndexName")
    def vector_index_name(self) -> pulumi.Input[_builtins.str]: ...
    @vector_index_name.setter
    def vector_index_name(self, value: pulumi.Input[_builtins.str]): ...

class AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfigurationFieldMappingArgsDict(
    TypedDict
):
    metadata_field: pulumi.Input[_builtins.str]
    text_field: pulumi.Input[_builtins.str]
    vector_field: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentKnowledgeBaseStorageConfigurationOpensearchServerlessConfigurationFieldMappingArgs:
    def __init__(
        __self__,
        *,
        metadata_field: pulumi.Input[_builtins.str],
        text_field: pulumi.Input[_builtins.str],
        vector_field: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataField")
    def metadata_field(self) -> pulumi.Input[_builtins.str]: ...
    @metadata_field.setter
    def metadata_field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="textField")
    def text_field(self) -> pulumi.Input[_builtins.str]: ...
    @text_field.setter
    def text_field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vectorField")
    def vector_field(self) -> pulumi.Input[_builtins.str]: ...
    @vector_field.setter
    def vector_field(self, value: pulumi.Input[_builtins.str]): ...

class AgentKnowledgeBaseStorageConfigurationPineconeConfigurationArgsDict(TypedDict):
    connection_string: pulumi.Input[_builtins.str]
    credentials_secret_arn: pulumi.Input[_builtins.str]
    field_mapping: pulumi.Input[
        AgentKnowledgeBaseStorageConfigurationPineconeConfigurationFieldMappingArgsDict
    ]
    namespace: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentKnowledgeBaseStorageConfigurationPineconeConfigurationArgs:
    def __init__(
        __self__,
        *,
        connection_string: pulumi.Input[_builtins.str],
        credentials_secret_arn: pulumi.Input[_builtins.str],
        field_mapping: pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationPineconeConfigurationFieldMappingArgs
        ],
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Input[_builtins.str]: ...
    @connection_string.setter
    def connection_string(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="credentialsSecretArn")
    def credentials_secret_arn(self) -> pulumi.Input[_builtins.str]: ...
    @credentials_secret_arn.setter
    def credentials_secret_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fieldMapping")
    def field_mapping(
        self,
    ) -> pulumi.Input[
        AgentKnowledgeBaseStorageConfigurationPineconeConfigurationFieldMappingArgs
    ]: ...
    @field_mapping.setter
    def field_mapping(
        self,
        value: pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationPineconeConfigurationFieldMappingArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentKnowledgeBaseStorageConfigurationPineconeConfigurationFieldMappingArgsDict(
    TypedDict
):
    metadata_field: pulumi.Input[_builtins.str]
    text_field: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentKnowledgeBaseStorageConfigurationPineconeConfigurationFieldMappingArgs:
    def __init__(
        __self__,
        *,
        metadata_field: pulumi.Input[_builtins.str],
        text_field: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataField")
    def metadata_field(self) -> pulumi.Input[_builtins.str]: ...
    @metadata_field.setter
    def metadata_field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="textField")
    def text_field(self) -> pulumi.Input[_builtins.str]: ...
    @text_field.setter
    def text_field(self, value: pulumi.Input[_builtins.str]): ...

class AgentKnowledgeBaseStorageConfigurationRdsConfigurationArgsDict(TypedDict):
    credentials_secret_arn: pulumi.Input[_builtins.str]
    database_name: pulumi.Input[_builtins.str]
    field_mapping: pulumi.Input[
        AgentKnowledgeBaseStorageConfigurationRdsConfigurationFieldMappingArgsDict
    ]
    resource_arn: pulumi.Input[_builtins.str]
    table_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentKnowledgeBaseStorageConfigurationRdsConfigurationArgs:
    def __init__(
        __self__,
        *,
        credentials_secret_arn: pulumi.Input[_builtins.str],
        database_name: pulumi.Input[_builtins.str],
        field_mapping: pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationRdsConfigurationFieldMappingArgs
        ],
        resource_arn: pulumi.Input[_builtins.str],
        table_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="credentialsSecretArn")
    def credentials_secret_arn(self) -> pulumi.Input[_builtins.str]: ...
    @credentials_secret_arn.setter
    def credentials_secret_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fieldMapping")
    def field_mapping(
        self,
    ) -> pulumi.Input[
        AgentKnowledgeBaseStorageConfigurationRdsConfigurationFieldMappingArgs
    ]: ...
    @field_mapping.setter
    def field_mapping(
        self,
        value: pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationRdsConfigurationFieldMappingArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[_builtins.str]: ...
    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...

class AgentKnowledgeBaseStorageConfigurationRdsConfigurationFieldMappingArgsDict(
    TypedDict
):
    metadata_field: pulumi.Input[_builtins.str]
    primary_key_field: pulumi.Input[_builtins.str]
    text_field: pulumi.Input[_builtins.str]
    vector_field: pulumi.Input[_builtins.str]
    custom_metadata_field: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentKnowledgeBaseStorageConfigurationRdsConfigurationFieldMappingArgs:
    def __init__(
        __self__,
        *,
        metadata_field: pulumi.Input[_builtins.str],
        primary_key_field: pulumi.Input[_builtins.str],
        text_field: pulumi.Input[_builtins.str],
        vector_field: pulumi.Input[_builtins.str],
        custom_metadata_field: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataField")
    def metadata_field(self) -> pulumi.Input[_builtins.str]: ...
    @metadata_field.setter
    def metadata_field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="primaryKeyField")
    def primary_key_field(self) -> pulumi.Input[_builtins.str]: ...
    @primary_key_field.setter
    def primary_key_field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="textField")
    def text_field(self) -> pulumi.Input[_builtins.str]: ...
    @text_field.setter
    def text_field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vectorField")
    def vector_field(self) -> pulumi.Input[_builtins.str]: ...
    @vector_field.setter
    def vector_field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customMetadataField")
    def custom_metadata_field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_metadata_field.setter
    def custom_metadata_field(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfigurationArgsDict(
    TypedDict
):
    credentials_secret_arn: pulumi.Input[_builtins.str]
    endpoint: pulumi.Input[_builtins.str]
    field_mapping: pulumi.Input[
        AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfigurationFieldMappingArgsDict
    ]
    vector_index_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfigurationArgs:
    def __init__(
        __self__,
        *,
        credentials_secret_arn: pulumi.Input[_builtins.str],
        endpoint: pulumi.Input[_builtins.str],
        field_mapping: pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfigurationFieldMappingArgs
        ],
        vector_index_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="credentialsSecretArn")
    def credentials_secret_arn(self) -> pulumi.Input[_builtins.str]: ...
    @credentials_secret_arn.setter
    def credentials_secret_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fieldMapping")
    def field_mapping(
        self,
    ) -> pulumi.Input[
        AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfigurationFieldMappingArgs
    ]: ...
    @field_mapping.setter
    def field_mapping(
        self,
        value: pulumi.Input[
            AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfigurationFieldMappingArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vectorIndexName")
    def vector_index_name(self) -> pulumi.Input[_builtins.str]: ...
    @vector_index_name.setter
    def vector_index_name(self, value: pulumi.Input[_builtins.str]): ...

class AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfigurationFieldMappingArgsDict(
    TypedDict
):
    metadata_field: NotRequired[pulumi.Input[_builtins.str]]
    text_field: NotRequired[pulumi.Input[_builtins.str]]
    vector_field: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentKnowledgeBaseStorageConfigurationRedisEnterpriseCloudConfigurationFieldMappingArgs:
    def __init__(
        __self__,
        *,
        metadata_field: Optional[pulumi.Input[_builtins.str]] = ...,
        text_field: Optional[pulumi.Input[_builtins.str]] = ...,
        vector_field: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataField")
    def metadata_field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metadata_field.setter
    def metadata_field(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="textField")
    def text_field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @text_field.setter
    def text_field(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vectorField")
    def vector_field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vector_field.setter
    def vector_field(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentKnowledgeBaseStorageConfigurationS3VectorsConfigurationArgsDict(TypedDict):
    index_arn: NotRequired[pulumi.Input[_builtins.str]]
    index_name: NotRequired[pulumi.Input[_builtins.str]]
    vector_bucket_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentKnowledgeBaseStorageConfigurationS3VectorsConfigurationArgs:
    def __init__(
        __self__,
        *,
        index_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        index_name: Optional[pulumi.Input[_builtins.str]] = ...,
        vector_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="indexArn")
    def index_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @index_arn.setter
    def index_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @index_name.setter
    def index_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vectorBucketArn")
    def vector_bucket_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vector_bucket_arn.setter
    def vector_bucket_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentKnowledgeBaseTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentKnowledgeBaseTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentPromptVariantArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    template_type: pulumi.Input[_builtins.str]
    additional_model_request_fields: NotRequired[pulumi.Input[_builtins.str]]
    gen_ai_resource: NotRequired[pulumi.Input[AgentPromptVariantGenAiResourceArgsDict]]
    inference_configuration: NotRequired[
        pulumi.Input[AgentPromptVariantInferenceConfigurationArgsDict]
    ]
    metadatas: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AgentPromptVariantMetadataArgsDict]]]
    ]
    model_id: NotRequired[pulumi.Input[_builtins.str]]
    template_configuration: NotRequired[
        pulumi.Input[AgentPromptVariantTemplateConfigurationArgsDict]
    ]

@pulumi.input_type
class AgentPromptVariantArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        template_type: pulumi.Input[_builtins.str],
        additional_model_request_fields: Optional[pulumi.Input[_builtins.str]] = ...,
        gen_ai_resource: Optional[
            pulumi.Input[AgentPromptVariantGenAiResourceArgs]
        ] = ...,
        inference_configuration: Optional[
            pulumi.Input[AgentPromptVariantInferenceConfigurationArgs]
        ] = ...,
        metadatas: Optional[
            pulumi.Input[Sequence[pulumi.Input[AgentPromptVariantMetadataArgs]]]
        ] = ...,
        model_id: Optional[pulumi.Input[_builtins.str]] = ...,
        template_configuration: Optional[
            pulumi.Input[AgentPromptVariantTemplateConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="templateType")
    def template_type(self) -> pulumi.Input[_builtins.str]: ...
    @template_type.setter
    def template_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalModelRequestFields")
    def additional_model_request_fields(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_model_request_fields.setter
    def additional_model_request_fields(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="genAiResource")
    def gen_ai_resource(
        self,
    ) -> Optional[pulumi.Input[AgentPromptVariantGenAiResourceArgs]]: ...
    @gen_ai_resource.setter
    def gen_ai_resource(
        self, value: Optional[pulumi.Input[AgentPromptVariantGenAiResourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inferenceConfiguration")
    def inference_configuration(
        self,
    ) -> Optional[pulumi.Input[AgentPromptVariantInferenceConfigurationArgs]]: ...
    @inference_configuration.setter
    def inference_configuration(
        self,
        value: Optional[pulumi.Input[AgentPromptVariantInferenceConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def metadatas(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AgentPromptVariantMetadataArgs]]]
    ]: ...
    @metadatas.setter
    def metadatas(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AgentPromptVariantMetadataArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_id.setter
    def model_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="templateConfiguration")
    def template_configuration(
        self,
    ) -> Optional[pulumi.Input[AgentPromptVariantTemplateConfigurationArgs]]: ...
    @template_configuration.setter
    def template_configuration(
        self, value: Optional[pulumi.Input[AgentPromptVariantTemplateConfigurationArgs]]
    ): ...

class AgentPromptVariantGenAiResourceArgsDict(TypedDict):
    agent: NotRequired[pulumi.Input[AgentPromptVariantGenAiResourceAgentArgsDict]]

@pulumi.input_type
class AgentPromptVariantGenAiResourceArgs:
    def __init__(
        __self__,
        *,
        agent: Optional[pulumi.Input[AgentPromptVariantGenAiResourceAgentArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def agent(
        self,
    ) -> Optional[pulumi.Input[AgentPromptVariantGenAiResourceAgentArgs]]: ...
    @agent.setter
    def agent(
        self, value: Optional[pulumi.Input[AgentPromptVariantGenAiResourceAgentArgs]]
    ): ...

class AgentPromptVariantGenAiResourceAgentArgsDict(TypedDict):
    agent_identifier: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentPromptVariantGenAiResourceAgentArgs:
    def __init__(
        __self__, *, agent_identifier: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentIdentifier")
    def agent_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @agent_identifier.setter
    def agent_identifier(self, value: pulumi.Input[_builtins.str]): ...

class AgentPromptVariantInferenceConfigurationArgsDict(TypedDict):
    text: NotRequired[
        pulumi.Input[AgentPromptVariantInferenceConfigurationTextArgsDict]
    ]

@pulumi.input_type
class AgentPromptVariantInferenceConfigurationArgs:
    def __init__(
        __self__,
        *,
        text: Optional[
            pulumi.Input[AgentPromptVariantInferenceConfigurationTextArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[pulumi.Input[AgentPromptVariantInferenceConfigurationTextArgs]]: ...
    @text.setter
    def text(
        self,
        value: Optional[pulumi.Input[AgentPromptVariantInferenceConfigurationTextArgs]],
    ): ...

class AgentPromptVariantInferenceConfigurationTextArgsDict(TypedDict):
    max_tokens: NotRequired[pulumi.Input[_builtins.int]]
    stop_sequences: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    top_p: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class AgentPromptVariantInferenceConfigurationTextArgs:
    def __init__(
        __self__,
        *,
        max_tokens: Optional[pulumi.Input[_builtins.int]] = ...,
        stop_sequences: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        temperature: Optional[pulumi.Input[_builtins.float]] = ...,
        top_p: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxTokens")
    def max_tokens(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_tokens.setter
    def max_tokens(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="stopSequences")
    def stop_sequences(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @stop_sequences.setter
    def stop_sequences(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="topP")
    def top_p(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @top_p.setter
    def top_p(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AgentPromptVariantMetadataArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentPromptVariantMetadataArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AgentPromptVariantTemplateConfigurationArgsDict(TypedDict):
    chat: NotRequired[pulumi.Input[AgentPromptVariantTemplateConfigurationChatArgsDict]]
    text: NotRequired[pulumi.Input[AgentPromptVariantTemplateConfigurationTextArgsDict]]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationArgs:
    def __init__(
        __self__,
        *,
        chat: Optional[
            pulumi.Input[AgentPromptVariantTemplateConfigurationChatArgs]
        ] = ...,
        text: Optional[
            pulumi.Input[AgentPromptVariantTemplateConfigurationTextArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def chat(
        self,
    ) -> Optional[pulumi.Input[AgentPromptVariantTemplateConfigurationChatArgs]]: ...
    @chat.setter
    def chat(
        self,
        value: Optional[pulumi.Input[AgentPromptVariantTemplateConfigurationChatArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[pulumi.Input[AgentPromptVariantTemplateConfigurationTextArgs]]: ...
    @text.setter
    def text(
        self,
        value: Optional[pulumi.Input[AgentPromptVariantTemplateConfigurationTextArgs]],
    ): ...

class AgentPromptVariantTemplateConfigurationChatArgsDict(TypedDict):
    messages: pulumi.Input[
        Sequence[
            pulumi.Input[AgentPromptVariantTemplateConfigurationChatMessageArgsDict]
        ]
    ]
    input_variables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentPromptVariantTemplateConfigurationChatInputVariableArgsDict
                ]
            ]
        ]
    ]
    systems: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AgentPromptVariantTemplateConfigurationChatSystemArgsDict]
            ]
        ]
    ]
    tool_configuration: NotRequired[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatToolConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationChatArgs:
    def __init__(
        __self__,
        *,
        messages: pulumi.Input[
            Sequence[
                pulumi.Input[AgentPromptVariantTemplateConfigurationChatMessageArgs]
            ]
        ],
        input_variables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentPromptVariantTemplateConfigurationChatInputVariableArgs
                    ]
                ]
            ]
        ] = ...,
        systems: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AgentPromptVariantTemplateConfigurationChatSystemArgs]
                ]
            ]
        ] = ...,
        tool_configuration: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatToolConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def messages(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[AgentPromptVariantTemplateConfigurationChatMessageArgs]]
    ]: ...
    @messages.setter
    def messages(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[AgentPromptVariantTemplateConfigurationChatMessageArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputVariables")
    def input_variables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentPromptVariantTemplateConfigurationChatInputVariableArgs
                ]
            ]
        ]
    ]: ...
    @input_variables.setter
    def input_variables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentPromptVariantTemplateConfigurationChatInputVariableArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def systems(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AgentPromptVariantTemplateConfigurationChatSystemArgs]
            ]
        ]
    ]: ...
    @systems.setter
    def systems(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AgentPromptVariantTemplateConfigurationChatSystemArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="toolConfiguration")
    def tool_configuration(
        self,
    ) -> Optional[
        pulumi.Input[AgentPromptVariantTemplateConfigurationChatToolConfigurationArgs]
    ]: ...
    @tool_configuration.setter
    def tool_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatToolConfigurationArgs
            ]
        ],
    ): ...

class AgentPromptVariantTemplateConfigurationChatInputVariableArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationChatInputVariableArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class AgentPromptVariantTemplateConfigurationChatMessageArgsDict(TypedDict):
    role: pulumi.Input[_builtins.str]
    content: NotRequired[
        pulumi.Input[AgentPromptVariantTemplateConfigurationChatMessageContentArgsDict]
    ]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationChatMessageArgs:
    def __init__(
        __self__,
        *,
        role: pulumi.Input[_builtins.str],
        content: Optional[
            pulumi.Input[AgentPromptVariantTemplateConfigurationChatMessageContentArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]: ...
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def content(
        self,
    ) -> Optional[
        pulumi.Input[AgentPromptVariantTemplateConfigurationChatMessageContentArgs]
    ]: ...
    @content.setter
    def content(
        self,
        value: Optional[
            pulumi.Input[AgentPromptVariantTemplateConfigurationChatMessageContentArgs]
        ],
    ): ...

class AgentPromptVariantTemplateConfigurationChatMessageContentArgsDict(TypedDict):
    cache_point: NotRequired[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatMessageContentCachePointArgsDict
        ]
    ]
    text: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationChatMessageContentArgs:
    def __init__(
        __self__,
        *,
        cache_point: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatMessageContentCachePointArgs
            ]
        ] = ...,
        text: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cachePoint")
    def cache_point(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatMessageContentCachePointArgs
        ]
    ]: ...
    @cache_point.setter
    def cache_point(
        self,
        value: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatMessageContentCachePointArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentPromptVariantTemplateConfigurationChatMessageContentCachePointArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationChatMessageContentCachePointArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class AgentPromptVariantTemplateConfigurationChatSystemArgsDict(TypedDict):
    cache_point: NotRequired[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatSystemCachePointArgsDict
        ]
    ]
    text: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationChatSystemArgs:
    def __init__(
        __self__,
        *,
        cache_point: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatSystemCachePointArgs
            ]
        ] = ...,
        text: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cachePoint")
    def cache_point(
        self,
    ) -> Optional[
        pulumi.Input[AgentPromptVariantTemplateConfigurationChatSystemCachePointArgs]
    ]: ...
    @cache_point.setter
    def cache_point(
        self,
        value: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatSystemCachePointArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentPromptVariantTemplateConfigurationChatSystemCachePointArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationChatSystemCachePointArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class AgentPromptVariantTemplateConfigurationChatToolConfigurationArgsDict(TypedDict):
    tool_choice: NotRequired[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceArgsDict
        ]
    ]
    tools: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentPromptVariantTemplateConfigurationChatToolConfigurationToolArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationArgs:
    def __init__(
        __self__,
        *,
        tool_choice: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceArgs
            ]
        ] = ...,
        tools: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentPromptVariantTemplateConfigurationChatToolConfigurationToolArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="toolChoice")
    def tool_choice(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceArgs
        ]
    ]: ...
    @tool_choice.setter
    def tool_choice(
        self,
        value: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tools(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentPromptVariantTemplateConfigurationChatToolConfigurationToolArgs
                ]
            ]
        ]
    ]: ...
    @tools.setter
    def tools(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentPromptVariantTemplateConfigurationChatToolConfigurationToolArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolArgsDict(
    TypedDict
):
    cache_point: NotRequired[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatToolConfigurationToolCachePointArgsDict
        ]
    ]
    tool_spec: NotRequired[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpecArgsDict
        ]
    ]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolArgs:
    def __init__(
        __self__,
        *,
        cache_point: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatToolConfigurationToolCachePointArgs
            ]
        ] = ...,
        tool_spec: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpecArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cachePoint")
    def cache_point(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatToolConfigurationToolCachePointArgs
        ]
    ]: ...
    @cache_point.setter
    def cache_point(
        self,
        value: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatToolConfigurationToolCachePointArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="toolSpec")
    def tool_spec(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpecArgs
        ]
    ]: ...
    @tool_spec.setter
    def tool_spec(
        self,
        value: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpecArgs
            ]
        ],
    ): ...

class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolCachePointArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolCachePointArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceArgsDict(
    TypedDict
):
    any: NotRequired[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAnyArgsDict
        ]
    ]
    auto: NotRequired[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAutoArgsDict
        ]
    ]
    tool: NotRequired[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceToolArgsDict
        ]
    ]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceArgs:
    def __init__(
        __self__,
        *,
        any: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAnyArgs
            ]
        ] = ...,
        auto: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAutoArgs
            ]
        ] = ...,
        tool: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceToolArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def any(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAnyArgs
        ]
    ]: ...
    @any.setter
    def any(
        self,
        value: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAnyArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def auto(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAutoArgs
        ]
    ]: ...
    @auto.setter
    def auto(
        self,
        value: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAutoArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tool(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceToolArgs
        ]
    ]: ...
    @tool.setter
    def tool(
        self,
        value: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceToolArgs
            ]
        ],
    ): ...

class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAnyArgsDict(
    TypedDict
): ...

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAnyArgs:
    def __init__(__self__) -> None: ...

class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAutoArgsDict(
    TypedDict
): ...

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceAutoArgs:
    def __init__(__self__) -> None: ...

class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceToolArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolChoiceToolArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpecArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    input_schema: NotRequired[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpecInputSchemaArgsDict
        ]
    ]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpecArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        input_schema: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpecInputSchemaArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputSchema")
    def input_schema(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpecInputSchemaArgs
        ]
    ]: ...
    @input_schema.setter
    def input_schema(
        self,
        value: Optional[
            pulumi.Input[
                AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpecInputSchemaArgs
            ]
        ],
    ): ...

class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpecInputSchemaArgsDict(
    TypedDict
):
    json: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationChatToolConfigurationToolToolSpecInputSchemaArgs:
    def __init__(
        __self__, *, json: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @json.setter
    def json(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentPromptVariantTemplateConfigurationTextArgsDict(TypedDict):
    text: pulumi.Input[_builtins.str]
    cache_point: NotRequired[
        pulumi.Input[AgentPromptVariantTemplateConfigurationTextCachePointArgsDict]
    ]
    input_variables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentPromptVariantTemplateConfigurationTextInputVariableArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationTextArgs:
    def __init__(
        __self__,
        *,
        text: pulumi.Input[_builtins.str],
        cache_point: Optional[
            pulumi.Input[AgentPromptVariantTemplateConfigurationTextCachePointArgs]
        ] = ...,
        input_variables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentPromptVariantTemplateConfigurationTextInputVariableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> pulumi.Input[_builtins.str]: ...
    @text.setter
    def text(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cachePoint")
    def cache_point(
        self,
    ) -> Optional[
        pulumi.Input[AgentPromptVariantTemplateConfigurationTextCachePointArgs]
    ]: ...
    @cache_point.setter
    def cache_point(
        self,
        value: Optional[
            pulumi.Input[AgentPromptVariantTemplateConfigurationTextCachePointArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputVariables")
    def input_variables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentPromptVariantTemplateConfigurationTextInputVariableArgs
                ]
            ]
        ]
    ]: ...
    @input_variables.setter
    def input_variables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentPromptVariantTemplateConfigurationTextInputVariableArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentPromptVariantTemplateConfigurationTextCachePointArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationTextCachePointArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class AgentPromptVariantTemplateConfigurationTextInputVariableArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentPromptVariantTemplateConfigurationTextInputVariableArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreAgentRuntimeAgentRuntimeArtifactArgsDict(TypedDict):
    code_configuration: NotRequired[
        pulumi.Input[AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationArgsDict]
    ]
    container_configuration: NotRequired[
        pulumi.Input[
            AgentcoreAgentRuntimeAgentRuntimeArtifactContainerConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class AgentcoreAgentRuntimeAgentRuntimeArtifactArgs:
    def __init__(
        __self__,
        *,
        code_configuration: Optional[
            pulumi.Input[AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationArgs]
        ] = ...,
        container_configuration: Optional[
            pulumi.Input[
                AgentcoreAgentRuntimeAgentRuntimeArtifactContainerConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="codeConfiguration")
    def code_configuration(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationArgs]
    ]: ...
    @code_configuration.setter
    def code_configuration(
        self,
        value: Optional[
            pulumi.Input[AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerConfiguration")
    def container_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreAgentRuntimeAgentRuntimeArtifactContainerConfigurationArgs
        ]
    ]: ...
    @container_configuration.setter
    def container_configuration(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreAgentRuntimeAgentRuntimeArtifactContainerConfigurationArgs
            ]
        ],
    ): ...

class AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationArgsDict(TypedDict):
    entry_points: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    runtime: pulumi.Input[_builtins.str]
    code: NotRequired[
        pulumi.Input[
            AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCodeArgsDict
        ]
    ]

@pulumi.input_type
class AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationArgs:
    def __init__(
        __self__,
        *,
        entry_points: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        runtime: pulumi.Input[_builtins.str],
        code: Optional[
            pulumi.Input[
                AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCodeArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entryPoints")
    def entry_points(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @entry_points.setter
    def entry_points(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> pulumi.Input[_builtins.str]: ...
    @runtime.setter
    def runtime(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def code(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCodeArgs]
    ]: ...
    @code.setter
    def code(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCodeArgs
            ]
        ],
    ): ...

class AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCodeArgsDict(TypedDict):
    s3: NotRequired[
        pulumi.Input[
            AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCodeS3ArgsDict
        ]
    ]

@pulumi.input_type
class AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCodeArgs:
    def __init__(
        __self__,
        *,
        s3: Optional[
            pulumi.Input[
                AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCodeS3Args
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCodeS3Args
        ]
    ]: ...
    @s3.setter
    def s3(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCodeS3Args
            ]
        ],
    ): ...

class AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCodeS3ArgsDict(
    TypedDict
):
    bucket: pulumi.Input[_builtins.str]
    prefix: pulumi.Input[_builtins.str]
    version_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreAgentRuntimeAgentRuntimeArtifactCodeConfigurationCodeS3Args:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        prefix: pulumi.Input[_builtins.str],
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> pulumi.Input[_builtins.str]: ...
    @prefix.setter
    def prefix(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreAgentRuntimeAgentRuntimeArtifactContainerConfigurationArgsDict(
    TypedDict
):
    container_uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreAgentRuntimeAgentRuntimeArtifactContainerConfigurationArgs:
    def __init__(__self__, *, container_uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerUri")
    def container_uri(self) -> pulumi.Input[_builtins.str]: ...
    @container_uri.setter
    def container_uri(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreAgentRuntimeAuthorizerConfigurationArgsDict(TypedDict):
    custom_jwt_authorizer: NotRequired[
        pulumi.Input[
            AgentcoreAgentRuntimeAuthorizerConfigurationCustomJwtAuthorizerArgsDict
        ]
    ]

@pulumi.input_type
class AgentcoreAgentRuntimeAuthorizerConfigurationArgs:
    def __init__(
        __self__,
        *,
        custom_jwt_authorizer: Optional[
            pulumi.Input[
                AgentcoreAgentRuntimeAuthorizerConfigurationCustomJwtAuthorizerArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customJwtAuthorizer")
    def custom_jwt_authorizer(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreAgentRuntimeAuthorizerConfigurationCustomJwtAuthorizerArgs
        ]
    ]: ...
    @custom_jwt_authorizer.setter
    def custom_jwt_authorizer(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreAgentRuntimeAuthorizerConfigurationCustomJwtAuthorizerArgs
            ]
        ],
    ): ...

class AgentcoreAgentRuntimeAuthorizerConfigurationCustomJwtAuthorizerArgsDict(
    TypedDict
):
    discovery_url: pulumi.Input[_builtins.str]
    allowed_audiences: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allowed_clients: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allowed_scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AgentcoreAgentRuntimeAuthorizerConfigurationCustomJwtAuthorizerArgs:
    def __init__(
        __self__,
        *,
        discovery_url: pulumi.Input[_builtins.str],
        allowed_audiences: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_clients: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> pulumi.Input[_builtins.str]: ...
    @discovery_url.setter
    def discovery_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_audiences.setter
    def allowed_audiences(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedClients")
    def allowed_clients(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_clients.setter
    def allowed_clients(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedScopes")
    def allowed_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_scopes.setter
    def allowed_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AgentcoreAgentRuntimeEndpointTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreAgentRuntimeEndpointTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreAgentRuntimeLifecycleConfigurationArgsDict(TypedDict):
    idle_runtime_session_timeout: pulumi.Input[_builtins.int]
    max_lifetime: pulumi.Input[_builtins.int]

@pulumi.input_type
class AgentcoreAgentRuntimeLifecycleConfigurationArgs:
    def __init__(
        __self__,
        *,
        idle_runtime_session_timeout: pulumi.Input[_builtins.int],
        max_lifetime: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleRuntimeSessionTimeout")
    def idle_runtime_session_timeout(self) -> pulumi.Input[_builtins.int]: ...
    @idle_runtime_session_timeout.setter
    def idle_runtime_session_timeout(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="maxLifetime")
    def max_lifetime(self) -> pulumi.Input[_builtins.int]: ...
    @max_lifetime.setter
    def max_lifetime(self, value: pulumi.Input[_builtins.int]): ...

class AgentcoreAgentRuntimeNetworkConfigurationArgsDict(TypedDict):
    network_mode: pulumi.Input[_builtins.str]
    network_mode_config: NotRequired[
        pulumi.Input[AgentcoreAgentRuntimeNetworkConfigurationNetworkModeConfigArgsDict]
    ]

@pulumi.input_type
class AgentcoreAgentRuntimeNetworkConfigurationArgs:
    def __init__(
        __self__,
        *,
        network_mode: pulumi.Input[_builtins.str],
        network_mode_config: Optional[
            pulumi.Input[AgentcoreAgentRuntimeNetworkConfigurationNetworkModeConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkMode")
    def network_mode(self) -> pulumi.Input[_builtins.str]: ...
    @network_mode.setter
    def network_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="networkModeConfig")
    def network_mode_config(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreAgentRuntimeNetworkConfigurationNetworkModeConfigArgs]
    ]: ...
    @network_mode_config.setter
    def network_mode_config(
        self,
        value: Optional[
            pulumi.Input[AgentcoreAgentRuntimeNetworkConfigurationNetworkModeConfigArgs]
        ],
    ): ...

class AgentcoreAgentRuntimeNetworkConfigurationNetworkModeConfigArgsDict(TypedDict):
    security_groups: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class AgentcoreAgentRuntimeNetworkConfigurationNetworkModeConfigArgs:
    def __init__(
        __self__,
        *,
        security_groups: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @security_groups.setter
    def security_groups(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class AgentcoreAgentRuntimeProtocolConfigurationArgsDict(TypedDict):
    server_protocol: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreAgentRuntimeProtocolConfigurationArgs:
    def __init__(
        __self__, *, server_protocol: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serverProtocol")
    def server_protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_protocol.setter
    def server_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreAgentRuntimeRequestHeaderConfigurationArgsDict(TypedDict):
    request_header_allowlists: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class AgentcoreAgentRuntimeRequestHeaderConfigurationArgs:
    def __init__(
        __self__,
        *,
        request_header_allowlists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requestHeaderAllowlists")
    def request_header_allowlists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @request_header_allowlists.setter
    def request_header_allowlists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AgentcoreAgentRuntimeTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreAgentRuntimeTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreAgentRuntimeWorkloadIdentityDetailArgsDict(TypedDict):
    workload_identity_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreAgentRuntimeWorkloadIdentityDetailArgs:
    def __init__(
        __self__, *, workload_identity_arn: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityArn")
    def workload_identity_arn(self) -> pulumi.Input[_builtins.str]: ...
    @workload_identity_arn.setter
    def workload_identity_arn(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreApiKeyCredentialProviderApiKeySecretArnArgsDict(TypedDict):
    secret_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreApiKeyCredentialProviderApiKeySecretArnArgs:
    def __init__(__self__, *, secret_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> pulumi.Input[_builtins.str]: ...
    @secret_arn.setter
    def secret_arn(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreBrowserNetworkConfigurationArgsDict(TypedDict):
    network_mode: pulumi.Input[_builtins.str]
    vpc_config: NotRequired[
        pulumi.Input[AgentcoreBrowserNetworkConfigurationVpcConfigArgsDict]
    ]

@pulumi.input_type
class AgentcoreBrowserNetworkConfigurationArgs:
    def __init__(
        __self__,
        *,
        network_mode: pulumi.Input[_builtins.str],
        vpc_config: Optional[
            pulumi.Input[AgentcoreBrowserNetworkConfigurationVpcConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkMode")
    def network_mode(self) -> pulumi.Input[_builtins.str]: ...
    @network_mode.setter
    def network_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(
        self,
    ) -> Optional[pulumi.Input[AgentcoreBrowserNetworkConfigurationVpcConfigArgs]]: ...
    @vpc_config.setter
    def vpc_config(
        self,
        value: Optional[
            pulumi.Input[AgentcoreBrowserNetworkConfigurationVpcConfigArgs]
        ],
    ): ...

class AgentcoreBrowserNetworkConfigurationVpcConfigArgsDict(TypedDict):
    security_groups: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class AgentcoreBrowserNetworkConfigurationVpcConfigArgs:
    def __init__(
        __self__,
        *,
        security_groups: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @security_groups.setter
    def security_groups(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class AgentcoreBrowserRecordingArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    s3_location: NotRequired[pulumi.Input[AgentcoreBrowserRecordingS3LocationArgsDict]]

@pulumi.input_type
class AgentcoreBrowserRecordingArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        s3_location: Optional[
            pulumi.Input[AgentcoreBrowserRecordingS3LocationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="s3Location")
    def s3_location(
        self,
    ) -> Optional[pulumi.Input[AgentcoreBrowserRecordingS3LocationArgs]]: ...
    @s3_location.setter
    def s3_location(
        self, value: Optional[pulumi.Input[AgentcoreBrowserRecordingS3LocationArgs]]
    ): ...

class AgentcoreBrowserRecordingS3LocationArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    prefix: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreBrowserRecordingS3LocationArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        prefix: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> pulumi.Input[_builtins.str]: ...
    @prefix.setter
    def prefix(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreBrowserTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreBrowserTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreCodeInterpreterNetworkConfigurationArgsDict(TypedDict):
    network_mode: pulumi.Input[_builtins.str]
    vpc_config: NotRequired[
        pulumi.Input[AgentcoreCodeInterpreterNetworkConfigurationVpcConfigArgsDict]
    ]

@pulumi.input_type
class AgentcoreCodeInterpreterNetworkConfigurationArgs:
    def __init__(
        __self__,
        *,
        network_mode: pulumi.Input[_builtins.str],
        vpc_config: Optional[
            pulumi.Input[AgentcoreCodeInterpreterNetworkConfigurationVpcConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkMode")
    def network_mode(self) -> pulumi.Input[_builtins.str]: ...
    @network_mode.setter
    def network_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreCodeInterpreterNetworkConfigurationVpcConfigArgs]
    ]: ...
    @vpc_config.setter
    def vpc_config(
        self,
        value: Optional[
            pulumi.Input[AgentcoreCodeInterpreterNetworkConfigurationVpcConfigArgs]
        ],
    ): ...

class AgentcoreCodeInterpreterNetworkConfigurationVpcConfigArgsDict(TypedDict):
    security_groups: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class AgentcoreCodeInterpreterNetworkConfigurationVpcConfigArgs:
    def __init__(
        __self__,
        *,
        security_groups: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @security_groups.setter
    def security_groups(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class AgentcoreCodeInterpreterTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreCodeInterpreterTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreGatewayAuthorizerConfigurationArgsDict(TypedDict):
    custom_jwt_authorizer: NotRequired[
        pulumi.Input[AgentcoreGatewayAuthorizerConfigurationCustomJwtAuthorizerArgsDict]
    ]

@pulumi.input_type
class AgentcoreGatewayAuthorizerConfigurationArgs:
    def __init__(
        __self__,
        *,
        custom_jwt_authorizer: Optional[
            pulumi.Input[AgentcoreGatewayAuthorizerConfigurationCustomJwtAuthorizerArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customJwtAuthorizer")
    def custom_jwt_authorizer(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreGatewayAuthorizerConfigurationCustomJwtAuthorizerArgs]
    ]: ...
    @custom_jwt_authorizer.setter
    def custom_jwt_authorizer(
        self,
        value: Optional[
            pulumi.Input[AgentcoreGatewayAuthorizerConfigurationCustomJwtAuthorizerArgs]
        ],
    ): ...

class AgentcoreGatewayAuthorizerConfigurationCustomJwtAuthorizerArgsDict(TypedDict):
    allowed_scopes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    discovery_url: pulumi.Input[_builtins.str]
    allowed_audiences: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allowed_clients: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AgentcoreGatewayAuthorizerConfigurationCustomJwtAuthorizerArgs:
    def __init__(
        __self__,
        *,
        allowed_scopes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        discovery_url: pulumi.Input[_builtins.str],
        allowed_audiences: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_clients: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedScopes")
    def allowed_scopes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @allowed_scopes.setter
    def allowed_scopes(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> pulumi.Input[_builtins.str]: ...
    @discovery_url.setter
    def discovery_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_audiences.setter
    def allowed_audiences(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedClients")
    def allowed_clients(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_clients.setter
    def allowed_clients(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AgentcoreGatewayInterceptorConfigurationArgsDict(TypedDict):
    interception_points: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    input_configuration: NotRequired[
        pulumi.Input[AgentcoreGatewayInterceptorConfigurationInputConfigurationArgsDict]
    ]
    interceptor: NotRequired[
        pulumi.Input[AgentcoreGatewayInterceptorConfigurationInterceptorArgsDict]
    ]

@pulumi.input_type
class AgentcoreGatewayInterceptorConfigurationArgs:
    def __init__(
        __self__,
        *,
        interception_points: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        input_configuration: Optional[
            pulumi.Input[AgentcoreGatewayInterceptorConfigurationInputConfigurationArgs]
        ] = ...,
        interceptor: Optional[
            pulumi.Input[AgentcoreGatewayInterceptorConfigurationInterceptorArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="interceptionPoints")
    def interception_points(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @interception_points.setter
    def interception_points(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputConfiguration")
    def input_configuration(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreGatewayInterceptorConfigurationInputConfigurationArgs]
    ]: ...
    @input_configuration.setter
    def input_configuration(
        self,
        value: Optional[
            pulumi.Input[AgentcoreGatewayInterceptorConfigurationInputConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def interceptor(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreGatewayInterceptorConfigurationInterceptorArgs]
    ]: ...
    @interceptor.setter
    def interceptor(
        self,
        value: Optional[
            pulumi.Input[AgentcoreGatewayInterceptorConfigurationInterceptorArgs]
        ],
    ): ...

class AgentcoreGatewayInterceptorConfigurationInputConfigurationArgsDict(TypedDict):
    pass_request_headers: pulumi.Input[_builtins.bool]

@pulumi.input_type
class AgentcoreGatewayInterceptorConfigurationInputConfigurationArgs:
    def __init__(
        __self__, *, pass_request_headers: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="passRequestHeaders")
    def pass_request_headers(self) -> pulumi.Input[_builtins.bool]: ...
    @pass_request_headers.setter
    def pass_request_headers(self, value: pulumi.Input[_builtins.bool]): ...

class AgentcoreGatewayInterceptorConfigurationInterceptorArgsDict(TypedDict):
    lambda_: NotRequired[
        pulumi.Input[AgentcoreGatewayInterceptorConfigurationInterceptorLambdaArgsDict]
    ]

@pulumi.input_type
class AgentcoreGatewayInterceptorConfigurationInterceptorArgs:
    def __init__(
        __self__,
        *,
        lambda_: Optional[
            pulumi.Input[AgentcoreGatewayInterceptorConfigurationInterceptorLambdaArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreGatewayInterceptorConfigurationInterceptorLambdaArgs]
    ]: ...
    @lambda_.setter
    def lambda_(
        self,
        value: Optional[
            pulumi.Input[AgentcoreGatewayInterceptorConfigurationInterceptorLambdaArgs]
        ],
    ): ...

class AgentcoreGatewayInterceptorConfigurationInterceptorLambdaArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreGatewayInterceptorConfigurationInterceptorLambdaArgs:
    def __init__(__self__, *, arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreGatewayProtocolConfigurationArgsDict(TypedDict):
    mcp: NotRequired[pulumi.Input[AgentcoreGatewayProtocolConfigurationMcpArgsDict]]

@pulumi.input_type
class AgentcoreGatewayProtocolConfigurationArgs:
    def __init__(
        __self__,
        *,
        mcp: Optional[pulumi.Input[AgentcoreGatewayProtocolConfigurationMcpArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mcp(
        self,
    ) -> Optional[pulumi.Input[AgentcoreGatewayProtocolConfigurationMcpArgs]]: ...
    @mcp.setter
    def mcp(
        self,
        value: Optional[pulumi.Input[AgentcoreGatewayProtocolConfigurationMcpArgs]],
    ): ...

class AgentcoreGatewayProtocolConfigurationMcpArgsDict(TypedDict):
    instructions: NotRequired[pulumi.Input[_builtins.str]]
    search_type: NotRequired[pulumi.Input[_builtins.str]]
    supported_versions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AgentcoreGatewayProtocolConfigurationMcpArgs:
    def __init__(
        __self__,
        *,
        instructions: Optional[pulumi.Input[_builtins.str]] = ...,
        search_type: Optional[pulumi.Input[_builtins.str]] = ...,
        supported_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instructions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instructions.setter
    def instructions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="searchType")
    def search_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @search_type.setter
    def search_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="supportedVersions")
    def supported_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @supported_versions.setter
    def supported_versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AgentcoreGatewayTargetCredentialProviderConfigurationArgsDict(TypedDict):
    api_key: NotRequired[
        pulumi.Input[
            AgentcoreGatewayTargetCredentialProviderConfigurationApiKeyArgsDict
        ]
    ]
    gateway_iam_role: NotRequired[
        pulumi.Input[
            AgentcoreGatewayTargetCredentialProviderConfigurationGatewayIamRoleArgsDict
        ]
    ]
    oauth: NotRequired[
        pulumi.Input[AgentcoreGatewayTargetCredentialProviderConfigurationOauthArgsDict]
    ]

@pulumi.input_type
class AgentcoreGatewayTargetCredentialProviderConfigurationArgs:
    def __init__(
        __self__,
        *,
        api_key: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetCredentialProviderConfigurationApiKeyArgs
            ]
        ] = ...,
        gateway_iam_role: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetCredentialProviderConfigurationGatewayIamRoleArgs
            ]
        ] = ...,
        oauth: Optional[
            pulumi.Input[AgentcoreGatewayTargetCredentialProviderConfigurationOauthArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreGatewayTargetCredentialProviderConfigurationApiKeyArgs]
    ]: ...
    @api_key.setter
    def api_key(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetCredentialProviderConfigurationApiKeyArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gatewayIamRole")
    def gateway_iam_role(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreGatewayTargetCredentialProviderConfigurationGatewayIamRoleArgs
        ]
    ]: ...
    @gateway_iam_role.setter
    def gateway_iam_role(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetCredentialProviderConfigurationGatewayIamRoleArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def oauth(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreGatewayTargetCredentialProviderConfigurationOauthArgs]
    ]: ...
    @oauth.setter
    def oauth(
        self,
        value: Optional[
            pulumi.Input[AgentcoreGatewayTargetCredentialProviderConfigurationOauthArgs]
        ],
    ): ...

class AgentcoreGatewayTargetCredentialProviderConfigurationApiKeyArgsDict(TypedDict):
    provider_arn: pulumi.Input[_builtins.str]
    credential_location: NotRequired[pulumi.Input[_builtins.str]]
    credential_parameter_name: NotRequired[pulumi.Input[_builtins.str]]
    credential_prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreGatewayTargetCredentialProviderConfigurationApiKeyArgs:
    def __init__(
        __self__,
        *,
        provider_arn: pulumi.Input[_builtins.str],
        credential_location: Optional[pulumi.Input[_builtins.str]] = ...,
        credential_parameter_name: Optional[pulumi.Input[_builtins.str]] = ...,
        credential_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="providerArn")
    def provider_arn(self) -> pulumi.Input[_builtins.str]: ...
    @provider_arn.setter
    def provider_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="credentialLocation")
    def credential_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credential_location.setter
    def credential_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="credentialParameterName")
    def credential_parameter_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credential_parameter_name.setter
    def credential_parameter_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="credentialPrefix")
    def credential_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credential_prefix.setter
    def credential_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreGatewayTargetCredentialProviderConfigurationGatewayIamRoleArgsDict(
    TypedDict
): ...

@pulumi.input_type
class AgentcoreGatewayTargetCredentialProviderConfigurationGatewayIamRoleArgs:
    def __init__(__self__) -> None: ...

class AgentcoreGatewayTargetCredentialProviderConfigurationOauthArgsDict(TypedDict):
    provider_arn: pulumi.Input[_builtins.str]
    scopes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    custom_parameters: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    default_return_url: NotRequired[pulumi.Input[_builtins.str]]
    grant_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreGatewayTargetCredentialProviderConfigurationOauthArgs:
    def __init__(
        __self__,
        *,
        provider_arn: pulumi.Input[_builtins.str],
        scopes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        custom_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        default_return_url: Optional[pulumi.Input[_builtins.str]] = ...,
        grant_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="providerArn")
    def provider_arn(self) -> pulumi.Input[_builtins.str]: ...
    @provider_arn.setter
    def provider_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @scopes.setter
    def scopes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="customParameters")
    def custom_parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @custom_parameters.setter
    def custom_parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultReturnUrl")
    def default_return_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_return_url.setter
    def default_return_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grantType")
    def grant_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grant_type.setter
    def grant_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreGatewayTargetMetadataConfigurationArgsDict(TypedDict):
    allowed_query_parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    allowed_request_headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    allowed_response_headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class AgentcoreGatewayTargetMetadataConfigurationArgs:
    def __init__(
        __self__,
        *,
        allowed_query_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_request_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_response_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedQueryParameters")
    def allowed_query_parameters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_query_parameters.setter
    def allowed_query_parameters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedRequestHeaders")
    def allowed_request_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_request_headers.setter
    def allowed_request_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedResponseHeaders")
    def allowed_response_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_response_headers.setter
    def allowed_response_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AgentcoreGatewayTargetTargetConfigurationArgsDict(TypedDict):
    mcp: NotRequired[pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpArgsDict]]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationArgs:
    def __init__(
        __self__,
        *,
        mcp: Optional[
            pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mcp(
        self,
    ) -> Optional[pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpArgs]]: ...
    @mcp.setter
    def mcp(
        self,
        value: Optional[pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpArgs]],
    ): ...

class AgentcoreGatewayTargetTargetConfigurationMcpArgsDict(TypedDict):
    lambda_: NotRequired[
        pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpLambdaArgsDict]
    ]
    mcp_server: NotRequired[
        pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpMcpServerArgsDict]
    ]
    open_api_schema: NotRequired[
        pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaArgsDict]
    ]
    smithy_model: NotRequired[
        pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelArgsDict]
    ]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpArgs:
    def __init__(
        __self__,
        *,
        lambda_: Optional[
            pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpLambdaArgs]
        ] = ...,
        mcp_server: Optional[
            pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpMcpServerArgs]
        ] = ...,
        open_api_schema: Optional[
            pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaArgs]
        ] = ...,
        smithy_model: Optional[
            pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpLambdaArgs]
    ]: ...
    @lambda_.setter
    def lambda_(
        self,
        value: Optional[
            pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpLambdaArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mcpServer")
    def mcp_server(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpMcpServerArgs]
    ]: ...
    @mcp_server.setter
    def mcp_server(
        self,
        value: Optional[
            pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpMcpServerArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="openApiSchema")
    def open_api_schema(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaArgs]
    ]: ...
    @open_api_schema.setter
    def open_api_schema(
        self,
        value: Optional[
            pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="smithyModel")
    def smithy_model(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelArgs]
    ]: ...
    @smithy_model.setter
    def smithy_model(
        self,
        value: Optional[
            pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelArgs]
        ],
    ): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaArgsDict(TypedDict):
    lambda_arn: pulumi.Input[_builtins.str]
    tool_schema: pulumi.Input[
        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaArgsDict
    ]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaArgs:
    def __init__(
        __self__,
        *,
        lambda_arn: pulumi.Input[_builtins.str],
        tool_schema: pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> pulumi.Input[_builtins.str]: ...
    @lambda_arn.setter
    def lambda_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="toolSchema")
    def tool_schema(
        self,
    ) -> pulumi.Input[
        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaArgs
    ]: ...
    @tool_schema.setter
    def tool_schema(
        self,
        value: pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaArgs
        ],
    ): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaArgsDict(TypedDict):
    inline_payloads: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadArgsDict
                ]
            ]
        ]
    ]
    s3: NotRequired[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaS3ArgsDict
        ]
    ]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaArgs:
    def __init__(
        __self__,
        *,
        inline_payloads: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadArgs
                    ]
                ]
            ]
        ] = ...,
        s3: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaS3Args
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inlinePayloads")
    def inline_payloads(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadArgs
                ]
            ]
        ]
    ]: ...
    @inline_payloads.setter
    def inline_payloads(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaS3Args]
    ]: ...
    @s3.setter
    def s3(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaS3Args
            ]
        ],
    ): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadArgsDict(
    TypedDict
):
    description: pulumi.Input[_builtins.str]
    input_schema: pulumi.Input[
        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaArgsDict
    ]
    name: pulumi.Input[_builtins.str]
    output_schema: NotRequired[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaArgsDict
        ]
    ]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadArgs:
    def __init__(
        __self__,
        *,
        description: pulumi.Input[_builtins.str],
        input_schema: pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaArgs
        ],
        name: pulumi.Input[_builtins.str],
        output_schema: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]: ...
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="inputSchema")
    def input_schema(
        self,
    ) -> pulumi.Input[
        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaArgs
    ]: ...
    @input_schema.setter
    def input_schema(
        self,
        value: pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="outputSchema")
    def output_schema(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaArgs
        ]
    ]: ...
    @output_schema.setter
    def output_schema(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaArgs
            ]
        ],
    ): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items: NotRequired[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsArgsDict
        ]
    ]
    properties: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsArgs
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsArgs
        ]
    ]: ...
    @items.setter
    def items(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyArgs
                ]
            ]
        ]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items: NotRequired[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsItemsArgsDict
        ]
    ]
    properties: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsPropertyArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsItemsArgs
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsPropertyArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsItemsArgs
        ]
    ]: ...
    @items.setter
    def items(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsItemsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsPropertyArgs
                ]
            ]
        ]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsPropertyArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsItemsArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items_json: NotRequired[pulumi.Input[_builtins.str]]
    properties_json: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsItemsArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items_json: Optional[pulumi.Input[_builtins.str]] = ...,
        properties_json: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @items_json.setter
    def items_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties_json.setter
    def properties_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsPropertyArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items_json: NotRequired[pulumi.Input[_builtins.str]]
    properties_json: NotRequired[pulumi.Input[_builtins.str]]
    required: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaItemsPropertyArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items_json: Optional[pulumi.Input[_builtins.str]] = ...,
        properties_json: Optional[pulumi.Input[_builtins.str]] = ...,
        required: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @items_json.setter
    def items_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties_json.setter
    def properties_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items: NotRequired[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsArgsDict
        ]
    ]
    properties: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyPropertyArgsDict
                ]
            ]
        ]
    ]
    required: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsArgs
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyPropertyArgs
                    ]
                ]
            ]
        ] = ...,
        required: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsArgs
        ]
    ]: ...
    @items.setter
    def items(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyPropertyArgs
                ]
            ]
        ]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyPropertyArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items: NotRequired[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsItemsArgsDict
        ]
    ]
    properties: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsPropertyArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsItemsArgs
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsPropertyArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsItemsArgs
        ]
    ]: ...
    @items.setter
    def items(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsItemsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsPropertyArgs
                ]
            ]
        ]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsPropertyArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsItemsArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items_json: NotRequired[pulumi.Input[_builtins.str]]
    properties_json: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsItemsArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items_json: Optional[pulumi.Input[_builtins.str]] = ...,
        properties_json: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @items_json.setter
    def items_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties_json.setter
    def properties_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsPropertyArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items_json: NotRequired[pulumi.Input[_builtins.str]]
    properties_json: NotRequired[pulumi.Input[_builtins.str]]
    required: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyItemsPropertyArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items_json: Optional[pulumi.Input[_builtins.str]] = ...,
        properties_json: Optional[pulumi.Input[_builtins.str]] = ...,
        required: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @items_json.setter
    def items_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties_json.setter
    def properties_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyPropertyArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items_json: NotRequired[pulumi.Input[_builtins.str]]
    properties_json: NotRequired[pulumi.Input[_builtins.str]]
    required: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadInputSchemaPropertyPropertyArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items_json: Optional[pulumi.Input[_builtins.str]] = ...,
        properties_json: Optional[pulumi.Input[_builtins.str]] = ...,
        required: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @items_json.setter
    def items_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties_json.setter
    def properties_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items: NotRequired[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsArgsDict
        ]
    ]
    properties: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsArgs
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsArgs
        ]
    ]: ...
    @items.setter
    def items(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyArgs
                ]
            ]
        ]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items: NotRequired[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsItemsArgsDict
        ]
    ]
    properties: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsPropertyArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsItemsArgs
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsPropertyArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsItemsArgs
        ]
    ]: ...
    @items.setter
    def items(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsItemsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsPropertyArgs
                ]
            ]
        ]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsPropertyArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsItemsArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items_json: NotRequired[pulumi.Input[_builtins.str]]
    properties_json: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsItemsArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items_json: Optional[pulumi.Input[_builtins.str]] = ...,
        properties_json: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @items_json.setter
    def items_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties_json.setter
    def properties_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsPropertyArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items_json: NotRequired[pulumi.Input[_builtins.str]]
    properties_json: NotRequired[pulumi.Input[_builtins.str]]
    required: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaItemsPropertyArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items_json: Optional[pulumi.Input[_builtins.str]] = ...,
        properties_json: Optional[pulumi.Input[_builtins.str]] = ...,
        required: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @items_json.setter
    def items_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties_json.setter
    def properties_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items: NotRequired[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsArgsDict
        ]
    ]
    properties: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyPropertyArgsDict
                ]
            ]
        ]
    ]
    required: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsArgs
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyPropertyArgs
                    ]
                ]
            ]
        ] = ...,
        required: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsArgs
        ]
    ]: ...
    @items.setter
    def items(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyPropertyArgs
                ]
            ]
        ]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyPropertyArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items: NotRequired[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsItemsArgsDict
        ]
    ]
    properties: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsPropertyArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsItemsArgs
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsPropertyArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsItemsArgs
        ]
    ]: ...
    @items.setter
    def items(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsItemsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsPropertyArgs
                ]
            ]
        ]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsPropertyArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsItemsArgsDict(
    TypedDict
):
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items_json: NotRequired[pulumi.Input[_builtins.str]]
    properties_json: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsItemsArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items_json: Optional[pulumi.Input[_builtins.str]] = ...,
        properties_json: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @items_json.setter
    def items_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties_json.setter
    def properties_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsPropertyArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items_json: NotRequired[pulumi.Input[_builtins.str]]
    properties_json: NotRequired[pulumi.Input[_builtins.str]]
    required: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyItemsPropertyArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items_json: Optional[pulumi.Input[_builtins.str]] = ...,
        properties_json: Optional[pulumi.Input[_builtins.str]] = ...,
        required: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @items_json.setter
    def items_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties_json.setter
    def properties_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyPropertyArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    items_json: NotRequired[pulumi.Input[_builtins.str]]
    properties_json: NotRequired[pulumi.Input[_builtins.str]]
    required: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaInlinePayloadOutputSchemaPropertyPropertyArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        items_json: Optional[pulumi.Input[_builtins.str]] = ...,
        properties_json: Optional[pulumi.Input[_builtins.str]] = ...,
        required: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="itemsJson")
    def items_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @items_json.setter
    def items_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="propertiesJson")
    def properties_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties_json.setter
    def properties_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaS3ArgsDict(TypedDict):
    bucket_owner_account_id: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpLambdaToolSchemaS3Args:
    def __init__(
        __self__,
        *,
        bucket_owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketOwnerAccountId")
    def bucket_owner_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_owner_account_id.setter
    def bucket_owner_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpMcpServerArgsDict(TypedDict):
    endpoint: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpMcpServerArgs:
    def __init__(__self__, *, endpoint: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaArgsDict(TypedDict):
    inline_payload: NotRequired[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaInlinePayloadArgsDict
        ]
    ]
    s3: NotRequired[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaS3ArgsDict
        ]
    ]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaArgs:
    def __init__(
        __self__,
        *,
        inline_payload: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaInlinePayloadArgs
            ]
        ] = ...,
        s3: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaS3Args
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inlinePayload")
    def inline_payload(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaInlinePayloadArgs
        ]
    ]: ...
    @inline_payload.setter
    def inline_payload(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaInlinePayloadArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaS3Args]
    ]: ...
    @s3.setter
    def s3(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaS3Args
            ]
        ],
    ): ...

class AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaInlinePayloadArgsDict(
    TypedDict
):
    payload: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaInlinePayloadArgs:
    def __init__(__self__, *, payload: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> pulumi.Input[_builtins.str]: ...
    @payload.setter
    def payload(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaS3ArgsDict(TypedDict):
    bucket_owner_account_id: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpOpenApiSchemaS3Args:
    def __init__(
        __self__,
        *,
        bucket_owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketOwnerAccountId")
    def bucket_owner_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_owner_account_id.setter
    def bucket_owner_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelArgsDict(TypedDict):
    inline_payload: NotRequired[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelInlinePayloadArgsDict
        ]
    ]
    s3: NotRequired[
        pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelS3ArgsDict]
    ]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelArgs:
    def __init__(
        __self__,
        *,
        inline_payload: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelInlinePayloadArgs
            ]
        ] = ...,
        s3: Optional[
            pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelS3Args]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inlinePayload")
    def inline_payload(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelInlinePayloadArgs
        ]
    ]: ...
    @inline_payload.setter
    def inline_payload(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelInlinePayloadArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelS3Args]
    ]: ...
    @s3.setter
    def s3(
        self,
        value: Optional[
            pulumi.Input[AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelS3Args]
        ],
    ): ...

class AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelInlinePayloadArgsDict(
    TypedDict
):
    payload: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelInlinePayloadArgs:
    def __init__(__self__, *, payload: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> pulumi.Input[_builtins.str]: ...
    @payload.setter
    def payload(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelS3ArgsDict(TypedDict):
    bucket_owner_account_id: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreGatewayTargetTargetConfigurationMcpSmithyModelS3Args:
    def __init__(
        __self__,
        *,
        bucket_owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketOwnerAccountId")
    def bucket_owner_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_owner_account_id.setter
    def bucket_owner_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreGatewayTargetTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreGatewayTargetTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreGatewayTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreGatewayTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreGatewayWorkloadIdentityDetailArgsDict(TypedDict):
    workload_identity_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreGatewayWorkloadIdentityDetailArgs:
    def __init__(
        __self__, *, workload_identity_arn: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityArn")
    def workload_identity_arn(self) -> pulumi.Input[_builtins.str]: ...
    @workload_identity_arn.setter
    def workload_identity_arn(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreMemoryStrategyConfigurationArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    consolidation: NotRequired[
        pulumi.Input[AgentcoreMemoryStrategyConfigurationConsolidationArgsDict]
    ]
    extraction: NotRequired[
        pulumi.Input[AgentcoreMemoryStrategyConfigurationExtractionArgsDict]
    ]

@pulumi.input_type
class AgentcoreMemoryStrategyConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        consolidation: Optional[
            pulumi.Input[AgentcoreMemoryStrategyConfigurationConsolidationArgs]
        ] = ...,
        extraction: Optional[
            pulumi.Input[AgentcoreMemoryStrategyConfigurationExtractionArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def consolidation(
        self,
    ) -> Optional[
        pulumi.Input[AgentcoreMemoryStrategyConfigurationConsolidationArgs]
    ]: ...
    @consolidation.setter
    def consolidation(
        self,
        value: Optional[
            pulumi.Input[AgentcoreMemoryStrategyConfigurationConsolidationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def extraction(
        self,
    ) -> Optional[pulumi.Input[AgentcoreMemoryStrategyConfigurationExtractionArgs]]: ...
    @extraction.setter
    def extraction(
        self,
        value: Optional[
            pulumi.Input[AgentcoreMemoryStrategyConfigurationExtractionArgs]
        ],
    ): ...

class AgentcoreMemoryStrategyConfigurationConsolidationArgsDict(TypedDict):
    append_to_prompt: pulumi.Input[_builtins.str]
    model_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreMemoryStrategyConfigurationConsolidationArgs:
    def __init__(
        __self__,
        *,
        append_to_prompt: pulumi.Input[_builtins.str],
        model_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appendToPrompt")
    def append_to_prompt(self) -> pulumi.Input[_builtins.str]: ...
    @append_to_prompt.setter
    def append_to_prompt(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> pulumi.Input[_builtins.str]: ...
    @model_id.setter
    def model_id(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreMemoryStrategyConfigurationExtractionArgsDict(TypedDict):
    append_to_prompt: pulumi.Input[_builtins.str]
    model_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreMemoryStrategyConfigurationExtractionArgs:
    def __init__(
        __self__,
        *,
        append_to_prompt: pulumi.Input[_builtins.str],
        model_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appendToPrompt")
    def append_to_prompt(self) -> pulumi.Input[_builtins.str]: ...
    @append_to_prompt.setter
    def append_to_prompt(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> pulumi.Input[_builtins.str]: ...
    @model_id.setter
    def model_id(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreMemoryStrategyTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreMemoryStrategyTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreMemoryTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreMemoryTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreOauth2CredentialProviderClientSecretArnArgsDict(TypedDict):
    secret_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderClientSecretArnArgs:
    def __init__(__self__, *, secret_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> pulumi.Input[_builtins.str]: ...
    @secret_arn.setter
    def secret_arn(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigArgsDict(TypedDict):
    custom_oauth2_provider_config: NotRequired[
        pulumi.Input[
            AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigArgsDict
        ]
    ]
    github_oauth2_provider_config: NotRequired[
        pulumi.Input[
            AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigArgsDict
        ]
    ]
    google_oauth2_provider_config: NotRequired[
        pulumi.Input[
            AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigArgsDict
        ]
    ]
    microsoft_oauth2_provider_config: NotRequired[
        pulumi.Input[
            AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigArgsDict
        ]
    ]
    salesforce_oauth2_provider_config: NotRequired[
        pulumi.Input[
            AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigArgsDict
        ]
    ]
    slack_oauth2_provider_config: NotRequired[
        pulumi.Input[
            AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigArgsDict
        ]
    ]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigArgs:
    def __init__(
        __self__,
        *,
        custom_oauth2_provider_config: Optional[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigArgs
            ]
        ] = ...,
        github_oauth2_provider_config: Optional[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigArgs
            ]
        ] = ...,
        google_oauth2_provider_config: Optional[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigArgs
            ]
        ] = ...,
        microsoft_oauth2_provider_config: Optional[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigArgs
            ]
        ] = ...,
        salesforce_oauth2_provider_config: Optional[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigArgs
            ]
        ] = ...,
        slack_oauth2_provider_config: Optional[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customOauth2ProviderConfig")
    def custom_oauth2_provider_config(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigArgs
        ]
    ]: ...
    @custom_oauth2_provider_config.setter
    def custom_oauth2_provider_config(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="githubOauth2ProviderConfig")
    def github_oauth2_provider_config(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigArgs
        ]
    ]: ...
    @github_oauth2_provider_config.setter
    def github_oauth2_provider_config(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="googleOauth2ProviderConfig")
    def google_oauth2_provider_config(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigArgs
        ]
    ]: ...
    @google_oauth2_provider_config.setter
    def google_oauth2_provider_config(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="microsoftOauth2ProviderConfig")
    def microsoft_oauth2_provider_config(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigArgs
        ]
    ]: ...
    @microsoft_oauth2_provider_config.setter
    def microsoft_oauth2_provider_config(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="salesforceOauth2ProviderConfig")
    def salesforce_oauth2_provider_config(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigArgs
        ]
    ]: ...
    @salesforce_oauth2_provider_config.setter
    def salesforce_oauth2_provider_config(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="slackOauth2ProviderConfig")
    def slack_oauth2_provider_config(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigArgs
        ]
    ]: ...
    @slack_oauth2_provider_config.setter
    def slack_oauth2_provider_config(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigArgs
            ]
        ],
    ): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigArgsDict(
    TypedDict
):
    client_credentials_wo_version: NotRequired[pulumi.Input[_builtins.int]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_id_wo: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_wo: NotRequired[pulumi.Input[_builtins.str]]
    oauth_discovery: NotRequired[
        pulumi.Input[
            AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscoveryArgsDict
        ]
    ]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigArgs:
    def __init__(
        __self__,
        *,
        client_credentials_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_id_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_discovery: Optional[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscoveryArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCredentialsWoVersion")
    def client_credentials_wo_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @client_credentials_wo_version.setter
    def client_credentials_wo_version(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientIdWo")
    def client_id_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id_wo.setter
    def client_id_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecretWo")
    def client_secret_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret_wo.setter
    def client_secret_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthDiscovery")
    def oauth_discovery(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscoveryArgs
        ]
    ]: ...
    @oauth_discovery.setter
    def oauth_discovery(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscoveryArgs
            ]
        ],
    ): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscoveryArgsDict(
    TypedDict
):
    authorization_server_metadata: NotRequired[
        pulumi.Input[
            AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgsDict
        ]
    ]
    discovery_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscoveryArgs:
    def __init__(
        __self__,
        *,
        authorization_server_metadata: Optional[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
            ]
        ] = ...,
        discovery_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationServerMetadata")
    def authorization_server_metadata(
        self,
    ) -> Optional[
        pulumi.Input[
            AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
        ]
    ]: ...
    @authorization_server_metadata.setter
    def authorization_server_metadata(
        self,
        value: Optional[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @discovery_url.setter
    def discovery_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgsDict(
    TypedDict
):
    authorization_endpoint: pulumi.Input[_builtins.str]
    issuer: pulumi.Input[_builtins.str]
    token_endpoint: pulumi.Input[_builtins.str]
    response_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigCustomOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs:
    def __init__(
        __self__,
        *,
        authorization_endpoint: pulumi.Input[_builtins.str],
        issuer: pulumi.Input[_builtins.str],
        token_endpoint: pulumi.Input[_builtins.str],
        response_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @authorization_endpoint.setter
    def authorization_endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]: ...
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="responseTypes")
    def response_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @response_types.setter
    def response_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigArgsDict(
    TypedDict
):
    client_credentials_wo_version: NotRequired[pulumi.Input[_builtins.int]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_id_wo: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_wo: NotRequired[pulumi.Input[_builtins.str]]
    oauth_discoveries: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscoveryArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigArgs:
    def __init__(
        __self__,
        *,
        client_credentials_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_id_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_discoveries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscoveryArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCredentialsWoVersion")
    def client_credentials_wo_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @client_credentials_wo_version.setter
    def client_credentials_wo_version(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientIdWo")
    def client_id_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id_wo.setter
    def client_id_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecretWo")
    def client_secret_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret_wo.setter
    def client_secret_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthDiscoveries")
    def oauth_discoveries(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscoveryArgs
                ]
            ]
        ]
    ]: ...
    @oauth_discoveries.setter
    def oauth_discoveries(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscoveryArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscoveryArgsDict(
    TypedDict
):
    authorization_server_metadatas: pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgsDict
            ]
        ]
    ]
    discovery_url: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscoveryArgs:
    def __init__(
        __self__,
        *,
        authorization_server_metadatas: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
                ]
            ]
        ],
        discovery_url: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationServerMetadatas")
    def authorization_server_metadatas(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
            ]
        ]
    ]: ...
    @authorization_server_metadatas.setter
    def authorization_server_metadatas(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> pulumi.Input[_builtins.str]: ...
    @discovery_url.setter
    def discovery_url(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgsDict(
    TypedDict
):
    authorization_endpoint: pulumi.Input[_builtins.str]
    issuer: pulumi.Input[_builtins.str]
    response_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    token_endpoint: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGithubOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs:
    def __init__(
        __self__,
        *,
        authorization_endpoint: pulumi.Input[_builtins.str],
        issuer: pulumi.Input[_builtins.str],
        response_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        token_endpoint: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @authorization_endpoint.setter
    def authorization_endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]: ...
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="responseTypes")
    def response_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @response_types.setter
    def response_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigArgsDict(
    TypedDict
):
    client_credentials_wo_version: NotRequired[pulumi.Input[_builtins.int]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_id_wo: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_wo: NotRequired[pulumi.Input[_builtins.str]]
    oauth_discoveries: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscoveryArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigArgs:
    def __init__(
        __self__,
        *,
        client_credentials_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_id_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_discoveries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscoveryArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCredentialsWoVersion")
    def client_credentials_wo_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @client_credentials_wo_version.setter
    def client_credentials_wo_version(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientIdWo")
    def client_id_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id_wo.setter
    def client_id_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecretWo")
    def client_secret_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret_wo.setter
    def client_secret_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthDiscoveries")
    def oauth_discoveries(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscoveryArgs
                ]
            ]
        ]
    ]: ...
    @oauth_discoveries.setter
    def oauth_discoveries(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscoveryArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscoveryArgsDict(
    TypedDict
):
    authorization_server_metadatas: pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgsDict
            ]
        ]
    ]
    discovery_url: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscoveryArgs:
    def __init__(
        __self__,
        *,
        authorization_server_metadatas: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
                ]
            ]
        ],
        discovery_url: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationServerMetadatas")
    def authorization_server_metadatas(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
            ]
        ]
    ]: ...
    @authorization_server_metadatas.setter
    def authorization_server_metadatas(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> pulumi.Input[_builtins.str]: ...
    @discovery_url.setter
    def discovery_url(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgsDict(
    TypedDict
):
    authorization_endpoint: pulumi.Input[_builtins.str]
    issuer: pulumi.Input[_builtins.str]
    response_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    token_endpoint: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigGoogleOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs:
    def __init__(
        __self__,
        *,
        authorization_endpoint: pulumi.Input[_builtins.str],
        issuer: pulumi.Input[_builtins.str],
        response_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        token_endpoint: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @authorization_endpoint.setter
    def authorization_endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]: ...
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="responseTypes")
    def response_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @response_types.setter
    def response_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigArgsDict(
    TypedDict
):
    client_credentials_wo_version: NotRequired[pulumi.Input[_builtins.int]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_id_wo: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_wo: NotRequired[pulumi.Input[_builtins.str]]
    oauth_discoveries: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscoveryArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigArgs:
    def __init__(
        __self__,
        *,
        client_credentials_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_id_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_discoveries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscoveryArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCredentialsWoVersion")
    def client_credentials_wo_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @client_credentials_wo_version.setter
    def client_credentials_wo_version(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientIdWo")
    def client_id_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id_wo.setter
    def client_id_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecretWo")
    def client_secret_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret_wo.setter
    def client_secret_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthDiscoveries")
    def oauth_discoveries(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscoveryArgs
                ]
            ]
        ]
    ]: ...
    @oauth_discoveries.setter
    def oauth_discoveries(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscoveryArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscoveryArgsDict(
    TypedDict
):
    authorization_server_metadatas: pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgsDict
            ]
        ]
    ]
    discovery_url: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscoveryArgs:
    def __init__(
        __self__,
        *,
        authorization_server_metadatas: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
                ]
            ]
        ],
        discovery_url: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationServerMetadatas")
    def authorization_server_metadatas(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
            ]
        ]
    ]: ...
    @authorization_server_metadatas.setter
    def authorization_server_metadatas(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> pulumi.Input[_builtins.str]: ...
    @discovery_url.setter
    def discovery_url(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgsDict(
    TypedDict
):
    authorization_endpoint: pulumi.Input[_builtins.str]
    issuer: pulumi.Input[_builtins.str]
    response_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    token_endpoint: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigMicrosoftOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs:
    def __init__(
        __self__,
        *,
        authorization_endpoint: pulumi.Input[_builtins.str],
        issuer: pulumi.Input[_builtins.str],
        response_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        token_endpoint: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @authorization_endpoint.setter
    def authorization_endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]: ...
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="responseTypes")
    def response_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @response_types.setter
    def response_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigArgsDict(
    TypedDict
):
    client_credentials_wo_version: NotRequired[pulumi.Input[_builtins.int]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_id_wo: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_wo: NotRequired[pulumi.Input[_builtins.str]]
    oauth_discoveries: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscoveryArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigArgs:
    def __init__(
        __self__,
        *,
        client_credentials_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_id_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_discoveries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscoveryArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCredentialsWoVersion")
    def client_credentials_wo_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @client_credentials_wo_version.setter
    def client_credentials_wo_version(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientIdWo")
    def client_id_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id_wo.setter
    def client_id_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecretWo")
    def client_secret_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret_wo.setter
    def client_secret_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthDiscoveries")
    def oauth_discoveries(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscoveryArgs
                ]
            ]
        ]
    ]: ...
    @oauth_discoveries.setter
    def oauth_discoveries(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscoveryArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscoveryArgsDict(
    TypedDict
):
    authorization_server_metadatas: pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgsDict
            ]
        ]
    ]
    discovery_url: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscoveryArgs:
    def __init__(
        __self__,
        *,
        authorization_server_metadatas: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
                ]
            ]
        ],
        discovery_url: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationServerMetadatas")
    def authorization_server_metadatas(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
            ]
        ]
    ]: ...
    @authorization_server_metadatas.setter
    def authorization_server_metadatas(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> pulumi.Input[_builtins.str]: ...
    @discovery_url.setter
    def discovery_url(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgsDict(
    TypedDict
):
    authorization_endpoint: pulumi.Input[_builtins.str]
    issuer: pulumi.Input[_builtins.str]
    response_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    token_endpoint: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSalesforceOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs:
    def __init__(
        __self__,
        *,
        authorization_endpoint: pulumi.Input[_builtins.str],
        issuer: pulumi.Input[_builtins.str],
        response_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        token_endpoint: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @authorization_endpoint.setter
    def authorization_endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]: ...
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="responseTypes")
    def response_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @response_types.setter
    def response_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigArgsDict(
    TypedDict
):
    client_credentials_wo_version: NotRequired[pulumi.Input[_builtins.int]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_id_wo: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_wo: NotRequired[pulumi.Input[_builtins.str]]
    oauth_discoveries: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscoveryArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigArgs:
    def __init__(
        __self__,
        *,
        client_credentials_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_id_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_discoveries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscoveryArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCredentialsWoVersion")
    def client_credentials_wo_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @client_credentials_wo_version.setter
    def client_credentials_wo_version(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientIdWo")
    def client_id_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id_wo.setter
    def client_id_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecretWo")
    def client_secret_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret_wo.setter
    def client_secret_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthDiscoveries")
    def oauth_discoveries(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscoveryArgs
                ]
            ]
        ]
    ]: ...
    @oauth_discoveries.setter
    def oauth_discoveries(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscoveryArgs
                    ]
                ]
            ]
        ],
    ): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscoveryArgsDict(
    TypedDict
):
    authorization_server_metadatas: pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgsDict
            ]
        ]
    ]
    discovery_url: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscoveryArgs:
    def __init__(
        __self__,
        *,
        authorization_server_metadatas: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
                ]
            ]
        ],
        discovery_url: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationServerMetadatas")
    def authorization_server_metadatas(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
            ]
        ]
    ]: ...
    @authorization_server_metadatas.setter
    def authorization_server_metadatas(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> pulumi.Input[_builtins.str]: ...
    @discovery_url.setter
    def discovery_url(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgsDict(
    TypedDict
):
    authorization_endpoint: pulumi.Input[_builtins.str]
    issuer: pulumi.Input[_builtins.str]
    response_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    token_endpoint: pulumi.Input[_builtins.str]

@pulumi.input_type
class AgentcoreOauth2CredentialProviderOauth2ProviderConfigSlackOauth2ProviderConfigOauthDiscoveryAuthorizationServerMetadataArgs:
    def __init__(
        __self__,
        *,
        authorization_endpoint: pulumi.Input[_builtins.str],
        issuer: pulumi.Input[_builtins.str],
        response_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        token_endpoint: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @authorization_endpoint.setter
    def authorization_endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]: ...
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="responseTypes")
    def response_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @response_types.setter
    def response_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): ...

class AgentcoreTokenVaultCmkKmsConfigurationArgsDict(TypedDict):
    key_type: pulumi.Input[_builtins.str]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AgentcoreTokenVaultCmkKmsConfigurationArgs:
    def __init__(
        __self__,
        *,
        key_type: pulumi.Input[_builtins.str],
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> pulumi.Input[_builtins.str]: ...
    @key_type.setter
    def key_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CustomModelOutputDataConfigArgsDict(TypedDict):
    s3_uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class CustomModelOutputDataConfigArgs:
    def __init__(__self__, *, s3_uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]: ...
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): ...

class CustomModelTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CustomModelTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CustomModelTrainingDataConfigArgsDict(TypedDict):
    s3_uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class CustomModelTrainingDataConfigArgs:
    def __init__(__self__, *, s3_uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]: ...
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): ...

class CustomModelTrainingMetricArgsDict(TypedDict):
    training_loss: pulumi.Input[_builtins.float]

@pulumi.input_type
class CustomModelTrainingMetricArgs:
    def __init__(__self__, *, training_loss: pulumi.Input[_builtins.float]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="trainingLoss")
    def training_loss(self) -> pulumi.Input[_builtins.float]: ...
    @training_loss.setter
    def training_loss(self, value: pulumi.Input[_builtins.float]): ...

class CustomModelValidationDataConfigArgsDict(TypedDict):
    validators: pulumi.Input[
        Sequence[pulumi.Input[CustomModelValidationDataConfigValidatorArgsDict]]
    ]

@pulumi.input_type
class CustomModelValidationDataConfigArgs:
    def __init__(
        __self__,
        *,
        validators: pulumi.Input[
            Sequence[pulumi.Input[CustomModelValidationDataConfigValidatorArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validators(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[CustomModelValidationDataConfigValidatorArgs]]
    ]: ...
    @validators.setter
    def validators(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[CustomModelValidationDataConfigValidatorArgs]]
        ],
    ): ...

class CustomModelValidationDataConfigValidatorArgsDict(TypedDict):
    s3_uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class CustomModelValidationDataConfigValidatorArgs:
    def __init__(__self__, *, s3_uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Uri")
    def s3_uri(self) -> pulumi.Input[_builtins.str]: ...
    @s3_uri.setter
    def s3_uri(self, value: pulumi.Input[_builtins.str]): ...

class CustomModelValidationMetricArgsDict(TypedDict):
    validation_loss: pulumi.Input[_builtins.float]

@pulumi.input_type
class CustomModelValidationMetricArgs:
    def __init__(
        __self__, *, validation_loss: pulumi.Input[_builtins.float]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="validationLoss")
    def validation_loss(self) -> pulumi.Input[_builtins.float]: ...
    @validation_loss.setter
    def validation_loss(self, value: pulumi.Input[_builtins.float]): ...

class CustomModelVpcConfigArgsDict(TypedDict):
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class CustomModelVpcConfigArgs:
    def __init__(
        __self__,
        *,
        security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class GuardrailContentPolicyConfigArgsDict(TypedDict):
    filters_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[GuardrailContentPolicyConfigFiltersConfigArgsDict]]
        ]
    ]
    tier_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[GuardrailContentPolicyConfigTierConfigArgsDict]]
        ]
    ]

@pulumi.input_type
class GuardrailContentPolicyConfigArgs:
    def __init__(
        __self__,
        *,
        filters_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GuardrailContentPolicyConfigFiltersConfigArgs]]
            ]
        ] = ...,
        tier_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GuardrailContentPolicyConfigTierConfigArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filtersConfigs")
    def filters_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[GuardrailContentPolicyConfigFiltersConfigArgs]]
        ]
    ]: ...
    @filters_configs.setter
    def filters_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GuardrailContentPolicyConfigFiltersConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tierConfigs")
    def tier_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GuardrailContentPolicyConfigTierConfigArgs]]]
    ]: ...
    @tier_configs.setter
    def tier_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GuardrailContentPolicyConfigTierConfigArgs]]
            ]
        ],
    ): ...

class GuardrailContentPolicyConfigFiltersConfigArgsDict(TypedDict):
    input_strength: pulumi.Input[_builtins.str]
    output_strength: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    input_action: NotRequired[pulumi.Input[_builtins.str]]
    input_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    input_modalities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    output_action: NotRequired[pulumi.Input[_builtins.str]]
    output_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    output_modalities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class GuardrailContentPolicyConfigFiltersConfigArgs:
    def __init__(
        __self__,
        *,
        input_strength: pulumi.Input[_builtins.str],
        output_strength: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        input_action: Optional[pulumi.Input[_builtins.str]] = ...,
        input_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        input_modalities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        output_action: Optional[pulumi.Input[_builtins.str]] = ...,
        output_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        output_modalities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputStrength")
    def input_strength(self) -> pulumi.Input[_builtins.str]: ...
    @input_strength.setter
    def input_strength(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="outputStrength")
    def output_strength(self) -> pulumi.Input[_builtins.str]: ...
    @output_strength.setter
    def output_strength(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="inputAction")
    def input_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_action.setter
    def input_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputEnabled")
    def input_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @input_enabled.setter
    def input_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="inputModalities")
    def input_modalities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @input_modalities.setter
    def input_modalities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputAction")
    def output_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_action.setter
    def output_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputEnabled")
    def output_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @output_enabled.setter
    def output_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="outputModalities")
    def output_modalities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @output_modalities.setter
    def output_modalities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class GuardrailContentPolicyConfigTierConfigArgsDict(TypedDict):
    tier_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class GuardrailContentPolicyConfigTierConfigArgs:
    def __init__(__self__, *, tier_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tierName")
    def tier_name(self) -> pulumi.Input[_builtins.str]: ...
    @tier_name.setter
    def tier_name(self, value: pulumi.Input[_builtins.str]): ...

class GuardrailContextualGroundingPolicyConfigArgsDict(TypedDict):
    filters_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    GuardrailContextualGroundingPolicyConfigFiltersConfigArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class GuardrailContextualGroundingPolicyConfigArgs:
    def __init__(
        __self__,
        *,
        filters_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        GuardrailContextualGroundingPolicyConfigFiltersConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filtersConfigs")
    def filters_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[GuardrailContextualGroundingPolicyConfigFiltersConfigArgs]
            ]
        ]
    ]: ...
    @filters_configs.setter
    def filters_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        GuardrailContextualGroundingPolicyConfigFiltersConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class GuardrailContextualGroundingPolicyConfigFiltersConfigArgsDict(TypedDict):
    threshold: pulumi.Input[_builtins.float]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class GuardrailContextualGroundingPolicyConfigFiltersConfigArgs:
    def __init__(
        __self__,
        *,
        threshold: pulumi.Input[_builtins.float],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[_builtins.float]: ...
    @threshold.setter
    def threshold(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class GuardrailCrossRegionConfigArgsDict(TypedDict):
    guardrail_profile_identifier: pulumi.Input[_builtins.str]

@pulumi.input_type
class GuardrailCrossRegionConfigArgs:
    def __init__(
        __self__, *, guardrail_profile_identifier: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="guardrailProfileIdentifier")
    def guardrail_profile_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @guardrail_profile_identifier.setter
    def guardrail_profile_identifier(self, value: pulumi.Input[_builtins.str]): ...

class GuardrailSensitiveInformationPolicyConfigArgsDict(TypedDict):
    pii_entities_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    GuardrailSensitiveInformationPolicyConfigPiiEntitiesConfigArgsDict
                ]
            ]
        ]
    ]
    regexes_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    GuardrailSensitiveInformationPolicyConfigRegexesConfigArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class GuardrailSensitiveInformationPolicyConfigArgs:
    def __init__(
        __self__,
        *,
        pii_entities_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        GuardrailSensitiveInformationPolicyConfigPiiEntitiesConfigArgs
                    ]
                ]
            ]
        ] = ...,
        regexes_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        GuardrailSensitiveInformationPolicyConfigRegexesConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="piiEntitiesConfigs")
    def pii_entities_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    GuardrailSensitiveInformationPolicyConfigPiiEntitiesConfigArgs
                ]
            ]
        ]
    ]: ...
    @pii_entities_configs.setter
    def pii_entities_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        GuardrailSensitiveInformationPolicyConfigPiiEntitiesConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="regexesConfigs")
    def regexes_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[GuardrailSensitiveInformationPolicyConfigRegexesConfigArgs]
            ]
        ]
    ]: ...
    @regexes_configs.setter
    def regexes_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        GuardrailSensitiveInformationPolicyConfigRegexesConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class GuardrailSensitiveInformationPolicyConfigPiiEntitiesConfigArgsDict(TypedDict):
    action: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    input_action: NotRequired[pulumi.Input[_builtins.str]]
    input_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    output_action: NotRequired[pulumi.Input[_builtins.str]]
    output_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class GuardrailSensitiveInformationPolicyConfigPiiEntitiesConfigArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        input_action: Optional[pulumi.Input[_builtins.str]] = ...,
        input_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        output_action: Optional[pulumi.Input[_builtins.str]] = ...,
        output_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]: ...
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="inputAction")
    def input_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_action.setter
    def input_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputEnabled")
    def input_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @input_enabled.setter
    def input_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="outputAction")
    def output_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_action.setter
    def output_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputEnabled")
    def output_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @output_enabled.setter
    def output_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class GuardrailSensitiveInformationPolicyConfigRegexesConfigArgsDict(TypedDict):
    action: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    pattern: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    input_action: NotRequired[pulumi.Input[_builtins.str]]
    input_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    output_action: NotRequired[pulumi.Input[_builtins.str]]
    output_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class GuardrailSensitiveInformationPolicyConfigRegexesConfigArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        pattern: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        input_action: Optional[pulumi.Input[_builtins.str]] = ...,
        input_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        output_action: Optional[pulumi.Input[_builtins.str]] = ...,
        output_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]: ...
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> pulumi.Input[_builtins.str]: ...
    @pattern.setter
    def pattern(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputAction")
    def input_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_action.setter
    def input_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputEnabled")
    def input_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @input_enabled.setter
    def input_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="outputAction")
    def output_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_action.setter
    def output_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputEnabled")
    def output_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @output_enabled.setter
    def output_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class GuardrailTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GuardrailTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuardrailTopicPolicyConfigArgsDict(TypedDict):
    tier_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[GuardrailTopicPolicyConfigTierConfigArgsDict]]
        ]
    ]
    topics_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[GuardrailTopicPolicyConfigTopicsConfigArgsDict]]
        ]
    ]

@pulumi.input_type
class GuardrailTopicPolicyConfigArgs:
    def __init__(
        __self__,
        *,
        tier_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GuardrailTopicPolicyConfigTierConfigArgs]]
            ]
        ] = ...,
        topics_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GuardrailTopicPolicyConfigTopicsConfigArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tierConfigs")
    def tier_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GuardrailTopicPolicyConfigTierConfigArgs]]]
    ]: ...
    @tier_configs.setter
    def tier_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GuardrailTopicPolicyConfigTierConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="topicsConfigs")
    def topics_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GuardrailTopicPolicyConfigTopicsConfigArgs]]]
    ]: ...
    @topics_configs.setter
    def topics_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GuardrailTopicPolicyConfigTopicsConfigArgs]]
            ]
        ],
    ): ...

class GuardrailTopicPolicyConfigTierConfigArgsDict(TypedDict):
    tier_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class GuardrailTopicPolicyConfigTierConfigArgs:
    def __init__(__self__, *, tier_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tierName")
    def tier_name(self) -> pulumi.Input[_builtins.str]: ...
    @tier_name.setter
    def tier_name(self, value: pulumi.Input[_builtins.str]): ...

class GuardrailTopicPolicyConfigTopicsConfigArgsDict(TypedDict):
    definition: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    examples: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class GuardrailTopicPolicyConfigTopicsConfigArgs:
    def __init__(
        __self__,
        *,
        definition: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        examples: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def definition(self) -> pulumi.Input[_builtins.str]: ...
    @definition.setter
    def definition(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def examples(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @examples.setter
    def examples(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class GuardrailVersionTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GuardrailVersionTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuardrailWordPolicyConfigArgsDict(TypedDict):
    managed_word_lists_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[GuardrailWordPolicyConfigManagedWordListsConfigArgsDict]
            ]
        ]
    ]
    words_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[GuardrailWordPolicyConfigWordsConfigArgsDict]]
        ]
    ]

@pulumi.input_type
class GuardrailWordPolicyConfigArgs:
    def __init__(
        __self__,
        *,
        managed_word_lists_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[GuardrailWordPolicyConfigManagedWordListsConfigArgs]
                ]
            ]
        ] = ...,
        words_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GuardrailWordPolicyConfigWordsConfigArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedWordListsConfigs")
    def managed_word_lists_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[GuardrailWordPolicyConfigManagedWordListsConfigArgs]]
        ]
    ]: ...
    @managed_word_lists_configs.setter
    def managed_word_lists_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[GuardrailWordPolicyConfigManagedWordListsConfigArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="wordsConfigs")
    def words_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GuardrailWordPolicyConfigWordsConfigArgs]]]
    ]: ...
    @words_configs.setter
    def words_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GuardrailWordPolicyConfigWordsConfigArgs]]
            ]
        ],
    ): ...

class GuardrailWordPolicyConfigManagedWordListsConfigArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    input_action: NotRequired[pulumi.Input[_builtins.str]]
    input_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    output_action: NotRequired[pulumi.Input[_builtins.str]]
    output_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class GuardrailWordPolicyConfigManagedWordListsConfigArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        input_action: Optional[pulumi.Input[_builtins.str]] = ...,
        input_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        output_action: Optional[pulumi.Input[_builtins.str]] = ...,
        output_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="inputAction")
    def input_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_action.setter
    def input_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputEnabled")
    def input_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @input_enabled.setter
    def input_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="outputAction")
    def output_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_action.setter
    def output_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputEnabled")
    def output_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @output_enabled.setter
    def output_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class GuardrailWordPolicyConfigWordsConfigArgsDict(TypedDict):
    text: pulumi.Input[_builtins.str]
    input_action: NotRequired[pulumi.Input[_builtins.str]]
    input_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    output_action: NotRequired[pulumi.Input[_builtins.str]]
    output_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class GuardrailWordPolicyConfigWordsConfigArgs:
    def __init__(
        __self__,
        *,
        text: pulumi.Input[_builtins.str],
        input_action: Optional[pulumi.Input[_builtins.str]] = ...,
        input_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        output_action: Optional[pulumi.Input[_builtins.str]] = ...,
        output_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> pulumi.Input[_builtins.str]: ...
    @text.setter
    def text(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="inputAction")
    def input_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_action.setter
    def input_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputEnabled")
    def input_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @input_enabled.setter
    def input_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="outputAction")
    def output_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_action.setter
    def output_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputEnabled")
    def output_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @output_enabled.setter
    def output_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class InferenceProfileModelArgsDict(TypedDict):
    model_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class InferenceProfileModelArgs:
    def __init__(__self__, *, model_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelArn")
    def model_arn(self) -> pulumi.Input[_builtins.str]: ...
    @model_arn.setter
    def model_arn(self, value: pulumi.Input[_builtins.str]): ...

class InferenceProfileModelSourceArgsDict(TypedDict):
    copy_from: pulumi.Input[_builtins.str]

@pulumi.input_type
class InferenceProfileModelSourceArgs:
    def __init__(__self__, *, copy_from: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="copyFrom")
    def copy_from(self) -> pulumi.Input[_builtins.str]: ...
    @copy_from.setter
    def copy_from(self, value: pulumi.Input[_builtins.str]): ...

class InferenceProfileTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InferenceProfileTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProvisionedModelThroughputTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProvisionedModelThroughputTimeoutsArgs:
    def __init__(
        __self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GetAgentAgentVersionsAgentVersionSummaryArgsDict(TypedDict):
    agent_name: _builtins.str
    agent_status: _builtins.str
    agent_version: _builtins.str
    created_at: _builtins.str
    description: _builtins.str
    updated_at: _builtins.str
    guardrail_configurations: NotRequired[
        Sequence[GetAgentAgentVersionsAgentVersionSummaryGuardrailConfigurationArgsDict]
    ]

@pulumi.input_type
class GetAgentAgentVersionsAgentVersionSummaryArgs:
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
            Sequence[GetAgentAgentVersionsAgentVersionSummaryGuardrailConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentName")
    def agent_name(self) -> _builtins.str: ...
    @agent_name.setter
    def agent_name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="agentStatus")
    def agent_status(self) -> _builtins.str: ...
    @agent_status.setter
    def agent_status(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> _builtins.str: ...
    @agent_version.setter
    def agent_version(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @created_at.setter
    def created_at(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @description.setter
    def description(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str: ...
    @updated_at.setter
    def updated_at(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="guardrailConfigurations")
    def guardrail_configurations(
        self,
    ) -> Optional[
        Sequence[GetAgentAgentVersionsAgentVersionSummaryGuardrailConfigurationArgs]
    ]: ...
    @guardrail_configurations.setter
    def guardrail_configurations(
        self,
        value: Optional[
            Sequence[GetAgentAgentVersionsAgentVersionSummaryGuardrailConfigurationArgs]
        ],
    ): ...

class GetAgentAgentVersionsAgentVersionSummaryGuardrailConfigurationArgsDict(TypedDict):
    guardrail_identifier: _builtins.str
    guardrail_version: _builtins.str

@pulumi.input_type
class GetAgentAgentVersionsAgentVersionSummaryGuardrailConfigurationArgs:
    def __init__(
        __self__,
        *,
        guardrail_identifier: _builtins.str,
        guardrail_version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="guardrailIdentifier")
    def guardrail_identifier(self) -> _builtins.str: ...
    @guardrail_identifier.setter
    def guardrail_identifier(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="guardrailVersion")
    def guardrail_version(self) -> _builtins.str: ...
    @guardrail_version.setter
    def guardrail_version(self, value: _builtins.str): ...
