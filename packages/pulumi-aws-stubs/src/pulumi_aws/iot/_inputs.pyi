import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BillingGroupMetadataArgs",
    "BillingGroupMetadataArgsDict",
    "BillingGroupPropertiesArgs",
    "BillingGroupPropertiesArgsDict",
    "CaCertificateRegistrationConfigArgs",
    "CaCertificateRegistrationConfigArgsDict",
    "CaCertificateValidityArgs",
    "CaCertificateValidityArgsDict",
    "DomainConfigurationAuthorizerConfigArgs",
    "DomainConfigurationAuthorizerConfigArgsDict",
    "DomainConfigurationTlsConfigArgs",
    "DomainConfigurationTlsConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ProvisioningTemplatePreProvisioningHookArgs",
    "ProvisioningTemplatePreProvisioningHookArgsDict",
    "ThingGroupMetadataArgs",
    "ThingGroupMetadataArgsDict",
    "ThingGroupMetadataRootToParentGroupArgs",
    "ThingGroupMetadataRootToParentGroupArgsDict",
    "ThingGroupPropertiesArgs",
    "ThingGroupPropertiesArgsDict",
    "ThingGroupPropertiesAttributePayloadArgs",
    "ThingGroupPropertiesAttributePayloadArgsDict",
    "ThingTypePropertiesArgs",
    "ThingTypePropertiesArgsDict",
    "TopicRuleCloudwatchAlarmArgs",
    "TopicRuleCloudwatchAlarmArgsDict",
    "TopicRuleCloudwatchLogArgs",
    "TopicRuleCloudwatchLogArgsDict",
    "TopicRuleCloudwatchMetricArgs",
    "TopicRuleCloudwatchMetricArgsDict",
    "TopicRuleDestinationVpcConfigurationArgs",
    "TopicRuleDestinationVpcConfigurationArgsDict",
    "TopicRuleDynamodbArgs",
    "TopicRuleDynamodbArgsDict",
    "TopicRuleDynamodbv2Args",
    "TopicRuleDynamodbv2ArgsDict",
    "TopicRuleDynamodbv2PutItemArgs",
    "TopicRuleDynamodbv2PutItemArgsDict",
    "TopicRuleElasticsearchArgs",
    "TopicRuleElasticsearchArgsDict",
    "TopicRuleErrorActionArgs",
    "TopicRuleErrorActionArgsDict",
    "TopicRuleErrorActionCloudwatchAlarmArgs",
    "TopicRuleErrorActionCloudwatchAlarmArgsDict",
    "TopicRuleErrorActionCloudwatchLogsArgs",
    "TopicRuleErrorActionCloudwatchLogsArgsDict",
    "TopicRuleErrorActionCloudwatchMetricArgs",
    "TopicRuleErrorActionCloudwatchMetricArgsDict",
    "TopicRuleErrorActionDynamodbArgs",
    "TopicRuleErrorActionDynamodbArgsDict",
    "TopicRuleErrorActionDynamodbv2Args",
    "TopicRuleErrorActionDynamodbv2ArgsDict",
    "TopicRuleErrorActionDynamodbv2PutItemArgs",
    "TopicRuleErrorActionDynamodbv2PutItemArgsDict",
    "TopicRuleErrorActionElasticsearchArgs",
    "TopicRuleErrorActionElasticsearchArgsDict",
    "TopicRuleErrorActionFirehoseArgs",
    "TopicRuleErrorActionFirehoseArgsDict",
    "TopicRuleErrorActionHttpArgs",
    "TopicRuleErrorActionHttpArgsDict",
    "TopicRuleErrorActionHttpHttpHeaderArgs",
    "TopicRuleErrorActionHttpHttpHeaderArgsDict",
    "TopicRuleErrorActionIotAnalyticsArgs",
    "TopicRuleErrorActionIotAnalyticsArgsDict",
    "TopicRuleErrorActionIotEventsArgs",
    "TopicRuleErrorActionIotEventsArgsDict",
    "TopicRuleErrorActionKafkaArgs",
    "TopicRuleErrorActionKafkaArgsDict",
    "TopicRuleErrorActionKafkaHeaderArgs",
    "TopicRuleErrorActionKafkaHeaderArgsDict",
    "TopicRuleErrorActionKinesisArgs",
    "TopicRuleErrorActionKinesisArgsDict",
    "TopicRuleErrorActionLambdaArgs",
    "TopicRuleErrorActionLambdaArgsDict",
    "TopicRuleErrorActionRepublishArgs",
    "TopicRuleErrorActionRepublishArgsDict",
    "TopicRuleErrorActionS3Args",
    "TopicRuleErrorActionS3ArgsDict",
    "TopicRuleErrorActionSnsArgs",
    "TopicRuleErrorActionSnsArgsDict",
    "TopicRuleErrorActionSqsArgs",
    "TopicRuleErrorActionSqsArgsDict",
    "TopicRuleErrorActionStepFunctionsArgs",
    "TopicRuleErrorActionStepFunctionsArgsDict",
    "TopicRuleErrorActionTimestreamArgs",
    "TopicRuleErrorActionTimestreamArgsDict",
    "TopicRuleErrorActionTimestreamDimensionArgs",
    "TopicRuleErrorActionTimestreamDimensionArgsDict",
    "TopicRuleErrorActionTimestreamTimestampArgs",
    "TopicRuleErrorActionTimestreamTimestampArgsDict",
    "TopicRuleFirehoseArgs",
    "TopicRuleFirehoseArgsDict",
    "TopicRuleHttpArgs",
    "TopicRuleHttpArgsDict",
    "TopicRuleHttpHttpHeaderArgs",
    "TopicRuleHttpHttpHeaderArgsDict",
    "TopicRuleIotAnalyticArgs",
    "TopicRuleIotAnalyticArgsDict",
    "TopicRuleIotEventArgs",
    "TopicRuleIotEventArgsDict",
    "TopicRuleKafkaArgs",
    "TopicRuleKafkaArgsDict",
    "TopicRuleKafkaHeaderArgs",
    "TopicRuleKafkaHeaderArgsDict",
    "TopicRuleKinesisArgs",
    "TopicRuleKinesisArgsDict",
    "TopicRuleLambdaArgs",
    "TopicRuleLambdaArgsDict",
    "TopicRuleRepublishArgs",
    "TopicRuleRepublishArgsDict",
    "TopicRuleS3Args",
    "TopicRuleS3ArgsDict",
    "TopicRuleSnsArgs",
    "TopicRuleSnsArgsDict",
    "TopicRuleSqsArgs",
    "TopicRuleSqsArgsDict",
    "TopicRuleStepFunctionArgs",
    "TopicRuleStepFunctionArgsDict",
    "TopicRuleTimestreamArgs",
    "TopicRuleTimestreamArgsDict",
    "TopicRuleTimestreamDimensionArgs",
    "TopicRuleTimestreamDimensionArgsDict",
    "TopicRuleTimestreamTimestampArgs",
    "TopicRuleTimestreamTimestampArgsDict",
]

class BillingGroupMetadataArgsDict(TypedDict):
    creation_date: pulumi.Input[_builtins.str]

@pulumi.input_type
class BillingGroupMetadataArgs:
    def __init__(__self__, *, creation_date: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Input[_builtins.str]: ...
    @creation_date.setter
    def creation_date(self, value: pulumi.Input[_builtins.str]): ...

class BillingGroupPropertiesArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BillingGroupPropertiesArgs:
    def __init__(
        __self__, *, description: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CaCertificateRegistrationConfigArgsDict(TypedDict):
    role_arn: NotRequired[pulumi.Input[_builtins.str]]
    template_body: NotRequired[pulumi.Input[_builtins.str]]
    template_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CaCertificateRegistrationConfigArgs:
    def __init__(
        __self__,
        *,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        template_body: Optional[pulumi.Input[_builtins.str]] = ...,
        template_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="templateBody")
    def template_body(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_body.setter
    def template_body(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_name.setter
    def template_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CaCertificateValidityArgsDict(TypedDict):
    not_after: NotRequired[pulumi.Input[_builtins.str]]
    not_before: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CaCertificateValidityArgs:
    def __init__(
        __self__,
        *,
        not_after: Optional[pulumi.Input[_builtins.str]] = ...,
        not_before: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="notAfter")
    def not_after(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @not_after.setter
    def not_after(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @not_before.setter
    def not_before(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainConfigurationAuthorizerConfigArgsDict(TypedDict):
    allow_authorizer_override: NotRequired[pulumi.Input[_builtins.bool]]
    default_authorizer_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DomainConfigurationAuthorizerConfigArgs:
    def __init__(
        __self__,
        *,
        allow_authorizer_override: Optional[pulumi.Input[_builtins.bool]] = ...,
        default_authorizer_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowAuthorizerOverride")
    def allow_authorizer_override(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_authorizer_override.setter
    def allow_authorizer_override(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultAuthorizerName")
    def default_authorizer_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_authorizer_name.setter
    def default_authorizer_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainConfigurationTlsConfigArgsDict(TypedDict):
    security_policy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DomainConfigurationTlsConfigArgs:
    def __init__(
        __self__, *, security_policy: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_policy.setter
    def security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IndexingConfigurationThingGroupIndexingConfigurationArgsDict(TypedDict):
    thing_group_indexing_mode: pulumi.Input[_builtins.str]
    custom_fields: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    IndexingConfigurationThingGroupIndexingConfigurationCustomFieldArgsDict
                ]
            ]
        ]
    ]
    managed_fields: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    IndexingConfigurationThingGroupIndexingConfigurationManagedFieldArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class IndexingConfigurationThingGroupIndexingConfigurationArgs:
    def __init__(
        __self__,
        *,
        thing_group_indexing_mode: pulumi.Input[_builtins.str],
        custom_fields: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        IndexingConfigurationThingGroupIndexingConfigurationCustomFieldArgs
                    ]
                ]
            ]
        ] = ...,
        managed_fields: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        IndexingConfigurationThingGroupIndexingConfigurationManagedFieldArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="thingGroupIndexingMode")
    def thing_group_indexing_mode(self) -> pulumi.Input[_builtins.str]: ...
    @thing_group_indexing_mode.setter
    def thing_group_indexing_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customFields")
    def custom_fields(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    IndexingConfigurationThingGroupIndexingConfigurationCustomFieldArgs
                ]
            ]
        ]
    ]: ...
    @custom_fields.setter
    def custom_fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        IndexingConfigurationThingGroupIndexingConfigurationCustomFieldArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedFields")
    def managed_fields(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    IndexingConfigurationThingGroupIndexingConfigurationManagedFieldArgs
                ]
            ]
        ]
    ]: ...
    @managed_fields.setter
    def managed_fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        IndexingConfigurationThingGroupIndexingConfigurationManagedFieldArgs
                    ]
                ]
            ]
        ],
    ): ...

class IndexingConfigurationThingGroupIndexingConfigurationCustomFieldArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IndexingConfigurationThingGroupIndexingConfigurationCustomFieldArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IndexingConfigurationThingGroupIndexingConfigurationManagedFieldArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IndexingConfigurationThingGroupIndexingConfigurationManagedFieldArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IndexingConfigurationThingIndexingConfigurationArgsDict(TypedDict):
    thing_indexing_mode: pulumi.Input[_builtins.str]
    custom_fields: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    IndexingConfigurationThingIndexingConfigurationCustomFieldArgsDict
                ]
            ]
        ]
    ]
    device_defender_indexing_mode: NotRequired[pulumi.Input[_builtins.str]]
    filter: NotRequired[
        pulumi.Input[IndexingConfigurationThingIndexingConfigurationFilterArgsDict]
    ]
    managed_fields: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    IndexingConfigurationThingIndexingConfigurationManagedFieldArgsDict
                ]
            ]
        ]
    ]
    named_shadow_indexing_mode: NotRequired[pulumi.Input[_builtins.str]]
    thing_connectivity_indexing_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IndexingConfigurationThingIndexingConfigurationArgs:
    def __init__(
        __self__,
        *,
        thing_indexing_mode: pulumi.Input[_builtins.str],
        custom_fields: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        IndexingConfigurationThingIndexingConfigurationCustomFieldArgs
                    ]
                ]
            ]
        ] = ...,
        device_defender_indexing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[
            pulumi.Input[IndexingConfigurationThingIndexingConfigurationFilterArgs]
        ] = ...,
        managed_fields: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        IndexingConfigurationThingIndexingConfigurationManagedFieldArgs
                    ]
                ]
            ]
        ] = ...,
        named_shadow_indexing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        thing_connectivity_indexing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="thingIndexingMode")
    def thing_indexing_mode(self) -> pulumi.Input[_builtins.str]: ...
    @thing_indexing_mode.setter
    def thing_indexing_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customFields")
    def custom_fields(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    IndexingConfigurationThingIndexingConfigurationCustomFieldArgs
                ]
            ]
        ]
    ]: ...
    @custom_fields.setter
    def custom_fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        IndexingConfigurationThingIndexingConfigurationCustomFieldArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deviceDefenderIndexingMode")
    def device_defender_indexing_mode(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @device_defender_indexing_mode.setter
    def device_defender_indexing_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(
        self,
    ) -> Optional[
        pulumi.Input[IndexingConfigurationThingIndexingConfigurationFilterArgs]
    ]: ...
    @filter.setter
    def filter(
        self,
        value: Optional[
            pulumi.Input[IndexingConfigurationThingIndexingConfigurationFilterArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedFields")
    def managed_fields(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    IndexingConfigurationThingIndexingConfigurationManagedFieldArgs
                ]
            ]
        ]
    ]: ...
    @managed_fields.setter
    def managed_fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        IndexingConfigurationThingIndexingConfigurationManagedFieldArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="namedShadowIndexingMode")
    def named_shadow_indexing_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @named_shadow_indexing_mode.setter
    def named_shadow_indexing_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="thingConnectivityIndexingMode")
    def thing_connectivity_indexing_mode(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @thing_connectivity_indexing_mode.setter
    def thing_connectivity_indexing_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class IndexingConfigurationThingIndexingConfigurationCustomFieldArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IndexingConfigurationThingIndexingConfigurationCustomFieldArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IndexingConfigurationThingIndexingConfigurationFilterArgsDict(TypedDict):
    named_shadow_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class IndexingConfigurationThingIndexingConfigurationFilterArgs:
    def __init__(
        __self__,
        *,
        named_shadow_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namedShadowNames")
    def named_shadow_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @named_shadow_names.setter
    def named_shadow_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class IndexingConfigurationThingIndexingConfigurationManagedFieldArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IndexingConfigurationThingIndexingConfigurationManagedFieldArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProvisioningTemplatePreProvisioningHookArgsDict(TypedDict):
    target_arn: pulumi.Input[_builtins.str]
    payload_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProvisioningTemplatePreProvisioningHookArgs:
    def __init__(
        __self__,
        *,
        target_arn: pulumi.Input[_builtins.str],
        payload_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Input[_builtins.str]: ...
    @target_arn.setter
    def target_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="payloadVersion")
    def payload_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @payload_version.setter
    def payload_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ThingGroupMetadataArgsDict(TypedDict):
    creation_date: NotRequired[pulumi.Input[_builtins.str]]
    parent_group_name: NotRequired[pulumi.Input[_builtins.str]]
    root_to_parent_groups: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ThingGroupMetadataRootToParentGroupArgsDict]]
        ]
    ]

@pulumi.input_type
class ThingGroupMetadataArgs:
    def __init__(
        __self__,
        *,
        creation_date: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        root_to_parent_groups: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ThingGroupMetadataRootToParentGroupArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_date.setter
    def creation_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parentGroupName")
    def parent_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_group_name.setter
    def parent_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootToParentGroups")
    def root_to_parent_groups(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ThingGroupMetadataRootToParentGroupArgs]]]
    ]: ...
    @root_to_parent_groups.setter
    def root_to_parent_groups(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ThingGroupMetadataRootToParentGroupArgs]]
            ]
        ],
    ): ...

class ThingGroupMetadataRootToParentGroupArgsDict(TypedDict):
    group_arn: NotRequired[pulumi.Input[_builtins.str]]
    group_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ThingGroupMetadataRootToParentGroupArgs:
    def __init__(
        __self__,
        *,
        group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupArn")
    def group_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_arn.setter
    def group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ThingGroupPropertiesArgsDict(TypedDict):
    attribute_payload: NotRequired[
        pulumi.Input[ThingGroupPropertiesAttributePayloadArgsDict]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ThingGroupPropertiesArgs:
    def __init__(
        __self__,
        *,
        attribute_payload: Optional[
            pulumi.Input[ThingGroupPropertiesAttributePayloadArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributePayload")
    def attribute_payload(
        self,
    ) -> Optional[pulumi.Input[ThingGroupPropertiesAttributePayloadArgs]]: ...
    @attribute_payload.setter
    def attribute_payload(
        self, value: Optional[pulumi.Input[ThingGroupPropertiesAttributePayloadArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ThingGroupPropertiesAttributePayloadArgsDict(TypedDict):
    attributes: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ThingGroupPropertiesAttributePayloadArgs:
    def __init__(
        __self__,
        *,
        attributes: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attributes(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @attributes.setter
    def attributes(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ThingTypePropertiesArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    searchable_attributes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ThingTypePropertiesArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        searchable_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="searchableAttributes")
    def searchable_attributes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @searchable_attributes.setter
    def searchable_attributes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class TopicRuleCloudwatchAlarmArgsDict(TypedDict):
    alarm_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    state_reason: pulumi.Input[_builtins.str]
    state_value: pulumi.Input[_builtins.str]

@pulumi.input_type
class TopicRuleCloudwatchAlarmArgs:
    def __init__(
        __self__,
        *,
        alarm_name: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        state_reason: pulumi.Input[_builtins.str],
        state_value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alarmName")
    def alarm_name(self) -> pulumi.Input[_builtins.str]: ...
    @alarm_name.setter
    def alarm_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> pulumi.Input[_builtins.str]: ...
    @state_reason.setter
    def state_reason(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="stateValue")
    def state_value(self) -> pulumi.Input[_builtins.str]: ...
    @state_value.setter
    def state_value(self, value: pulumi.Input[_builtins.str]): ...

class TopicRuleCloudwatchLogArgsDict(TypedDict):
    log_group_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    batch_mode: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class TopicRuleCloudwatchLogArgs:
    def __init__(
        __self__,
        *,
        log_group_name: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        batch_mode: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @log_group_name.setter
    def log_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="batchMode")
    def batch_mode(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @batch_mode.setter
    def batch_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TopicRuleCloudwatchMetricArgsDict(TypedDict):
    metric_name: pulumi.Input[_builtins.str]
    metric_namespace: pulumi.Input[_builtins.str]
    metric_unit: pulumi.Input[_builtins.str]
    metric_value: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    metric_timestamp: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleCloudwatchMetricArgs:
    def __init__(
        __self__,
        *,
        metric_name: pulumi.Input[_builtins.str],
        metric_namespace: pulumi.Input[_builtins.str],
        metric_unit: pulumi.Input[_builtins.str],
        metric_value: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        metric_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> pulumi.Input[_builtins.str]: ...
    @metric_namespace.setter
    def metric_namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricUnit")
    def metric_unit(self) -> pulumi.Input[_builtins.str]: ...
    @metric_unit.setter
    def metric_unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricValue")
    def metric_value(self) -> pulumi.Input[_builtins.str]: ...
    @metric_value.setter
    def metric_value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricTimestamp")
    def metric_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_timestamp.setter
    def metric_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleDestinationVpcConfigurationArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    vpc_id: pulumi.Input[_builtins.str]
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class TopicRuleDestinationVpcConfigurationArgs:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        vpc_id: pulumi.Input[_builtins.str],
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_groups.setter
    def security_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class TopicRuleDynamodbArgsDict(TypedDict):
    hash_key_field: pulumi.Input[_builtins.str]
    hash_key_value: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    table_name: pulumi.Input[_builtins.str]
    hash_key_type: NotRequired[pulumi.Input[_builtins.str]]
    operation: NotRequired[pulumi.Input[_builtins.str]]
    payload_field: NotRequired[pulumi.Input[_builtins.str]]
    range_key_field: NotRequired[pulumi.Input[_builtins.str]]
    range_key_type: NotRequired[pulumi.Input[_builtins.str]]
    range_key_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleDynamodbArgs:
    def __init__(
        __self__,
        *,
        hash_key_field: pulumi.Input[_builtins.str],
        hash_key_value: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        table_name: pulumi.Input[_builtins.str],
        hash_key_type: Optional[pulumi.Input[_builtins.str]] = ...,
        operation: Optional[pulumi.Input[_builtins.str]] = ...,
        payload_field: Optional[pulumi.Input[_builtins.str]] = ...,
        range_key_field: Optional[pulumi.Input[_builtins.str]] = ...,
        range_key_type: Optional[pulumi.Input[_builtins.str]] = ...,
        range_key_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hashKeyField")
    def hash_key_field(self) -> pulumi.Input[_builtins.str]: ...
    @hash_key_field.setter
    def hash_key_field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hashKeyValue")
    def hash_key_value(self) -> pulumi.Input[_builtins.str]: ...
    @hash_key_value.setter
    def hash_key_value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hashKeyType")
    def hash_key_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hash_key_type.setter
    def hash_key_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def operation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operation.setter
    def operation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="payloadField")
    def payload_field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @payload_field.setter
    def payload_field(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rangeKeyField")
    def range_key_field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @range_key_field.setter
    def range_key_field(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rangeKeyType")
    def range_key_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @range_key_type.setter
    def range_key_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rangeKeyValue")
    def range_key_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @range_key_value.setter
    def range_key_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleDynamodbv2ArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    put_item: NotRequired[pulumi.Input[TopicRuleDynamodbv2PutItemArgsDict]]

@pulumi.input_type
class TopicRuleDynamodbv2Args:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        put_item: Optional[pulumi.Input[TopicRuleDynamodbv2PutItemArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="putItem")
    def put_item(self) -> Optional[pulumi.Input[TopicRuleDynamodbv2PutItemArgs]]: ...
    @put_item.setter
    def put_item(
        self, value: Optional[pulumi.Input[TopicRuleDynamodbv2PutItemArgs]]
    ): ...

class TopicRuleDynamodbv2PutItemArgsDict(TypedDict):
    table_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class TopicRuleDynamodbv2PutItemArgs:
    def __init__(__self__, *, table_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...

class TopicRuleElasticsearchArgsDict(TypedDict):
    endpoint: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    index: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class TopicRuleElasticsearchArgs:
    def __init__(
        __self__,
        *,
        endpoint: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        index: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def index(self) -> pulumi.Input[_builtins.str]: ...
    @index.setter
    def index(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class TopicRuleErrorActionArgsDict(TypedDict):
    cloudwatch_alarm: NotRequired[
        pulumi.Input[TopicRuleErrorActionCloudwatchAlarmArgsDict]
    ]
    cloudwatch_logs: NotRequired[
        pulumi.Input[TopicRuleErrorActionCloudwatchLogsArgsDict]
    ]
    cloudwatch_metric: NotRequired[
        pulumi.Input[TopicRuleErrorActionCloudwatchMetricArgsDict]
    ]
    dynamodb: NotRequired[pulumi.Input[TopicRuleErrorActionDynamodbArgsDict]]
    dynamodbv2: NotRequired[pulumi.Input[TopicRuleErrorActionDynamodbv2ArgsDict]]
    elasticsearch: NotRequired[pulumi.Input[TopicRuleErrorActionElasticsearchArgsDict]]
    firehose: NotRequired[pulumi.Input[TopicRuleErrorActionFirehoseArgsDict]]
    http: NotRequired[pulumi.Input[TopicRuleErrorActionHttpArgsDict]]
    iot_analytics: NotRequired[pulumi.Input[TopicRuleErrorActionIotAnalyticsArgsDict]]
    iot_events: NotRequired[pulumi.Input[TopicRuleErrorActionIotEventsArgsDict]]
    kafka: NotRequired[pulumi.Input[TopicRuleErrorActionKafkaArgsDict]]
    kinesis: NotRequired[pulumi.Input[TopicRuleErrorActionKinesisArgsDict]]
    lambda_: NotRequired[pulumi.Input[TopicRuleErrorActionLambdaArgsDict]]
    republish: NotRequired[pulumi.Input[TopicRuleErrorActionRepublishArgsDict]]
    s3: NotRequired[pulumi.Input[TopicRuleErrorActionS3ArgsDict]]
    sns: NotRequired[pulumi.Input[TopicRuleErrorActionSnsArgsDict]]
    sqs: NotRequired[pulumi.Input[TopicRuleErrorActionSqsArgsDict]]
    step_functions: NotRequired[pulumi.Input[TopicRuleErrorActionStepFunctionsArgsDict]]
    timestream: NotRequired[pulumi.Input[TopicRuleErrorActionTimestreamArgsDict]]

@pulumi.input_type
class TopicRuleErrorActionArgs:
    def __init__(
        __self__,
        *,
        cloudwatch_alarm: Optional[
            pulumi.Input[TopicRuleErrorActionCloudwatchAlarmArgs]
        ] = ...,
        cloudwatch_logs: Optional[
            pulumi.Input[TopicRuleErrorActionCloudwatchLogsArgs]
        ] = ...,
        cloudwatch_metric: Optional[
            pulumi.Input[TopicRuleErrorActionCloudwatchMetricArgs]
        ] = ...,
        dynamodb: Optional[pulumi.Input[TopicRuleErrorActionDynamodbArgs]] = ...,
        dynamodbv2: Optional[pulumi.Input[TopicRuleErrorActionDynamodbv2Args]] = ...,
        elasticsearch: Optional[
            pulumi.Input[TopicRuleErrorActionElasticsearchArgs]
        ] = ...,
        firehose: Optional[pulumi.Input[TopicRuleErrorActionFirehoseArgs]] = ...,
        http: Optional[pulumi.Input[TopicRuleErrorActionHttpArgs]] = ...,
        iot_analytics: Optional[
            pulumi.Input[TopicRuleErrorActionIotAnalyticsArgs]
        ] = ...,
        iot_events: Optional[pulumi.Input[TopicRuleErrorActionIotEventsArgs]] = ...,
        kafka: Optional[pulumi.Input[TopicRuleErrorActionKafkaArgs]] = ...,
        kinesis: Optional[pulumi.Input[TopicRuleErrorActionKinesisArgs]] = ...,
        lambda_: Optional[pulumi.Input[TopicRuleErrorActionLambdaArgs]] = ...,
        republish: Optional[pulumi.Input[TopicRuleErrorActionRepublishArgs]] = ...,
        s3: Optional[pulumi.Input[TopicRuleErrorActionS3Args]] = ...,
        sns: Optional[pulumi.Input[TopicRuleErrorActionSnsArgs]] = ...,
        sqs: Optional[pulumi.Input[TopicRuleErrorActionSqsArgs]] = ...,
        step_functions: Optional[
            pulumi.Input[TopicRuleErrorActionStepFunctionsArgs]
        ] = ...,
        timestream: Optional[pulumi.Input[TopicRuleErrorActionTimestreamArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchAlarm")
    def cloudwatch_alarm(
        self,
    ) -> Optional[pulumi.Input[TopicRuleErrorActionCloudwatchAlarmArgs]]: ...
    @cloudwatch_alarm.setter
    def cloudwatch_alarm(
        self, value: Optional[pulumi.Input[TopicRuleErrorActionCloudwatchAlarmArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(
        self,
    ) -> Optional[pulumi.Input[TopicRuleErrorActionCloudwatchLogsArgs]]: ...
    @cloudwatch_logs.setter
    def cloudwatch_logs(
        self, value: Optional[pulumi.Input[TopicRuleErrorActionCloudwatchLogsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchMetric")
    def cloudwatch_metric(
        self,
    ) -> Optional[pulumi.Input[TopicRuleErrorActionCloudwatchMetricArgs]]: ...
    @cloudwatch_metric.setter
    def cloudwatch_metric(
        self, value: Optional[pulumi.Input[TopicRuleErrorActionCloudwatchMetricArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def dynamodb(self) -> Optional[pulumi.Input[TopicRuleErrorActionDynamodbArgs]]: ...
    @dynamodb.setter
    def dynamodb(
        self, value: Optional[pulumi.Input[TopicRuleErrorActionDynamodbArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def dynamodbv2(
        self,
    ) -> Optional[pulumi.Input[TopicRuleErrorActionDynamodbv2Args]]: ...
    @dynamodbv2.setter
    def dynamodbv2(
        self, value: Optional[pulumi.Input[TopicRuleErrorActionDynamodbv2Args]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def elasticsearch(
        self,
    ) -> Optional[pulumi.Input[TopicRuleErrorActionElasticsearchArgs]]: ...
    @elasticsearch.setter
    def elasticsearch(
        self, value: Optional[pulumi.Input[TopicRuleErrorActionElasticsearchArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def firehose(self) -> Optional[pulumi.Input[TopicRuleErrorActionFirehoseArgs]]: ...
    @firehose.setter
    def firehose(
        self, value: Optional[pulumi.Input[TopicRuleErrorActionFirehoseArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def http(self) -> Optional[pulumi.Input[TopicRuleErrorActionHttpArgs]]: ...
    @http.setter
    def http(self, value: Optional[pulumi.Input[TopicRuleErrorActionHttpArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="iotAnalytics")
    def iot_analytics(
        self,
    ) -> Optional[pulumi.Input[TopicRuleErrorActionIotAnalyticsArgs]]: ...
    @iot_analytics.setter
    def iot_analytics(
        self, value: Optional[pulumi.Input[TopicRuleErrorActionIotAnalyticsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="iotEvents")
    def iot_events(
        self,
    ) -> Optional[pulumi.Input[TopicRuleErrorActionIotEventsArgs]]: ...
    @iot_events.setter
    def iot_events(
        self, value: Optional[pulumi.Input[TopicRuleErrorActionIotEventsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def kafka(self) -> Optional[pulumi.Input[TopicRuleErrorActionKafkaArgs]]: ...
    @kafka.setter
    def kafka(self, value: Optional[pulumi.Input[TopicRuleErrorActionKafkaArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def kinesis(self) -> Optional[pulumi.Input[TopicRuleErrorActionKinesisArgs]]: ...
    @kinesis.setter
    def kinesis(
        self, value: Optional[pulumi.Input[TopicRuleErrorActionKinesisArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> Optional[pulumi.Input[TopicRuleErrorActionLambdaArgs]]: ...
    @lambda_.setter
    def lambda_(
        self, value: Optional[pulumi.Input[TopicRuleErrorActionLambdaArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def republish(
        self,
    ) -> Optional[pulumi.Input[TopicRuleErrorActionRepublishArgs]]: ...
    @republish.setter
    def republish(
        self, value: Optional[pulumi.Input[TopicRuleErrorActionRepublishArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input[TopicRuleErrorActionS3Args]]: ...
    @s3.setter
    def s3(self, value: Optional[pulumi.Input[TopicRuleErrorActionS3Args]]): ...
    @_builtins.property
    @pulumi.getter
    def sns(self) -> Optional[pulumi.Input[TopicRuleErrorActionSnsArgs]]: ...
    @sns.setter
    def sns(self, value: Optional[pulumi.Input[TopicRuleErrorActionSnsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def sqs(self) -> Optional[pulumi.Input[TopicRuleErrorActionSqsArgs]]: ...
    @sqs.setter
    def sqs(self, value: Optional[pulumi.Input[TopicRuleErrorActionSqsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="stepFunctions")
    def step_functions(
        self,
    ) -> Optional[pulumi.Input[TopicRuleErrorActionStepFunctionsArgs]]: ...
    @step_functions.setter
    def step_functions(
        self, value: Optional[pulumi.Input[TopicRuleErrorActionStepFunctionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timestream(
        self,
    ) -> Optional[pulumi.Input[TopicRuleErrorActionTimestreamArgs]]: ...
    @timestream.setter
    def timestream(
        self, value: Optional[pulumi.Input[TopicRuleErrorActionTimestreamArgs]]
    ): ...

class TopicRuleErrorActionCloudwatchAlarmArgsDict(TypedDict):
    alarm_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    state_reason: pulumi.Input[_builtins.str]
    state_value: pulumi.Input[_builtins.str]

@pulumi.input_type
class TopicRuleErrorActionCloudwatchAlarmArgs:
    def __init__(
        __self__,
        *,
        alarm_name: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        state_reason: pulumi.Input[_builtins.str],
        state_value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alarmName")
    def alarm_name(self) -> pulumi.Input[_builtins.str]: ...
    @alarm_name.setter
    def alarm_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> pulumi.Input[_builtins.str]: ...
    @state_reason.setter
    def state_reason(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="stateValue")
    def state_value(self) -> pulumi.Input[_builtins.str]: ...
    @state_value.setter
    def state_value(self, value: pulumi.Input[_builtins.str]): ...

class TopicRuleErrorActionCloudwatchLogsArgsDict(TypedDict):
    log_group_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    batch_mode: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class TopicRuleErrorActionCloudwatchLogsArgs:
    def __init__(
        __self__,
        *,
        log_group_name: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        batch_mode: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @log_group_name.setter
    def log_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="batchMode")
    def batch_mode(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @batch_mode.setter
    def batch_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TopicRuleErrorActionCloudwatchMetricArgsDict(TypedDict):
    metric_name: pulumi.Input[_builtins.str]
    metric_namespace: pulumi.Input[_builtins.str]
    metric_unit: pulumi.Input[_builtins.str]
    metric_value: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    metric_timestamp: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleErrorActionCloudwatchMetricArgs:
    def __init__(
        __self__,
        *,
        metric_name: pulumi.Input[_builtins.str],
        metric_namespace: pulumi.Input[_builtins.str],
        metric_unit: pulumi.Input[_builtins.str],
        metric_value: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        metric_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> pulumi.Input[_builtins.str]: ...
    @metric_namespace.setter
    def metric_namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricUnit")
    def metric_unit(self) -> pulumi.Input[_builtins.str]: ...
    @metric_unit.setter
    def metric_unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricValue")
    def metric_value(self) -> pulumi.Input[_builtins.str]: ...
    @metric_value.setter
    def metric_value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricTimestamp")
    def metric_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_timestamp.setter
    def metric_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleErrorActionDynamodbArgsDict(TypedDict):
    hash_key_field: pulumi.Input[_builtins.str]
    hash_key_value: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    table_name: pulumi.Input[_builtins.str]
    hash_key_type: NotRequired[pulumi.Input[_builtins.str]]
    operation: NotRequired[pulumi.Input[_builtins.str]]
    payload_field: NotRequired[pulumi.Input[_builtins.str]]
    range_key_field: NotRequired[pulumi.Input[_builtins.str]]
    range_key_type: NotRequired[pulumi.Input[_builtins.str]]
    range_key_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleErrorActionDynamodbArgs:
    def __init__(
        __self__,
        *,
        hash_key_field: pulumi.Input[_builtins.str],
        hash_key_value: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        table_name: pulumi.Input[_builtins.str],
        hash_key_type: Optional[pulumi.Input[_builtins.str]] = ...,
        operation: Optional[pulumi.Input[_builtins.str]] = ...,
        payload_field: Optional[pulumi.Input[_builtins.str]] = ...,
        range_key_field: Optional[pulumi.Input[_builtins.str]] = ...,
        range_key_type: Optional[pulumi.Input[_builtins.str]] = ...,
        range_key_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hashKeyField")
    def hash_key_field(self) -> pulumi.Input[_builtins.str]: ...
    @hash_key_field.setter
    def hash_key_field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hashKeyValue")
    def hash_key_value(self) -> pulumi.Input[_builtins.str]: ...
    @hash_key_value.setter
    def hash_key_value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hashKeyType")
    def hash_key_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hash_key_type.setter
    def hash_key_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def operation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operation.setter
    def operation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="payloadField")
    def payload_field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @payload_field.setter
    def payload_field(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rangeKeyField")
    def range_key_field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @range_key_field.setter
    def range_key_field(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rangeKeyType")
    def range_key_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @range_key_type.setter
    def range_key_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rangeKeyValue")
    def range_key_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @range_key_value.setter
    def range_key_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleErrorActionDynamodbv2ArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    put_item: NotRequired[pulumi.Input[TopicRuleErrorActionDynamodbv2PutItemArgsDict]]

@pulumi.input_type
class TopicRuleErrorActionDynamodbv2Args:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        put_item: Optional[
            pulumi.Input[TopicRuleErrorActionDynamodbv2PutItemArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="putItem")
    def put_item(
        self,
    ) -> Optional[pulumi.Input[TopicRuleErrorActionDynamodbv2PutItemArgs]]: ...
    @put_item.setter
    def put_item(
        self, value: Optional[pulumi.Input[TopicRuleErrorActionDynamodbv2PutItemArgs]]
    ): ...

class TopicRuleErrorActionDynamodbv2PutItemArgsDict(TypedDict):
    table_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class TopicRuleErrorActionDynamodbv2PutItemArgs:
    def __init__(__self__, *, table_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...

class TopicRuleErrorActionElasticsearchArgsDict(TypedDict):
    endpoint: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    index: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class TopicRuleErrorActionElasticsearchArgs:
    def __init__(
        __self__,
        *,
        endpoint: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        index: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def index(self) -> pulumi.Input[_builtins.str]: ...
    @index.setter
    def index(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class TopicRuleErrorActionFirehoseArgsDict(TypedDict):
    delivery_stream_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    batch_mode: NotRequired[pulumi.Input[_builtins.bool]]
    separator: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleErrorActionFirehoseArgs:
    def __init__(
        __self__,
        *,
        delivery_stream_name: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        batch_mode: Optional[pulumi.Input[_builtins.bool]] = ...,
        separator: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deliveryStreamName")
    def delivery_stream_name(self) -> pulumi.Input[_builtins.str]: ...
    @delivery_stream_name.setter
    def delivery_stream_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="batchMode")
    def batch_mode(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @batch_mode.setter
    def batch_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def separator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @separator.setter
    def separator(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleErrorActionHttpArgsDict(TypedDict):
    url: pulumi.Input[_builtins.str]
    confirmation_url: NotRequired[pulumi.Input[_builtins.str]]
    http_headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TopicRuleErrorActionHttpHttpHeaderArgsDict]]]
    ]

@pulumi.input_type
class TopicRuleErrorActionHttpArgs:
    def __init__(
        __self__,
        *,
        url: pulumi.Input[_builtins.str],
        confirmation_url: Optional[pulumi.Input[_builtins.str]] = ...,
        http_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[TopicRuleErrorActionHttpHttpHeaderArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="confirmationUrl")
    def confirmation_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @confirmation_url.setter
    def confirmation_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TopicRuleErrorActionHttpHttpHeaderArgs]]]
    ]: ...
    @http_headers.setter
    def http_headers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TopicRuleErrorActionHttpHttpHeaderArgs]]]
        ],
    ): ...

class TopicRuleErrorActionHttpHttpHeaderArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class TopicRuleErrorActionHttpHttpHeaderArgs:
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

class TopicRuleErrorActionIotAnalyticsArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    batch_mode: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class TopicRuleErrorActionIotAnalyticsArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        batch_mode: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="batchMode")
    def batch_mode(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @batch_mode.setter
    def batch_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TopicRuleErrorActionIotEventsArgsDict(TypedDict):
    input_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    batch_mode: NotRequired[pulumi.Input[_builtins.bool]]
    message_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleErrorActionIotEventsArgs:
    def __init__(
        __self__,
        *,
        input_name: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        batch_mode: Optional[pulumi.Input[_builtins.bool]] = ...,
        message_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputName")
    def input_name(self) -> pulumi.Input[_builtins.str]: ...
    @input_name.setter
    def input_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="batchMode")
    def batch_mode(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @batch_mode.setter
    def batch_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_id.setter
    def message_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleErrorActionKafkaArgsDict(TypedDict):
    client_properties: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    destination_arn: pulumi.Input[_builtins.str]
    topic: pulumi.Input[_builtins.str]
    headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TopicRuleErrorActionKafkaHeaderArgsDict]]]
    ]
    key: NotRequired[pulumi.Input[_builtins.str]]
    partition: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleErrorActionKafkaArgs:
    def __init__(
        __self__,
        *,
        client_properties: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        destination_arn: pulumi.Input[_builtins.str],
        topic: pulumi.Input[_builtins.str],
        headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[TopicRuleErrorActionKafkaHeaderArgs]]]
        ] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        partition: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientProperties")
    def client_properties(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @client_properties.setter
    def client_properties(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> pulumi.Input[_builtins.str]: ...
    @destination_arn.setter
    def destination_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]: ...
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TopicRuleErrorActionKafkaHeaderArgs]]]
    ]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TopicRuleErrorActionKafkaHeaderArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def partition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partition.setter
    def partition(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleErrorActionKafkaHeaderArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class TopicRuleErrorActionKafkaHeaderArgs:
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

class TopicRuleErrorActionKinesisArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    stream_name: pulumi.Input[_builtins.str]
    partition_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleErrorActionKinesisArgs:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        stream_name: pulumi.Input[_builtins.str],
        partition_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> pulumi.Input[_builtins.str]: ...
    @stream_name.setter
    def stream_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partition_key.setter
    def partition_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleErrorActionLambdaArgsDict(TypedDict):
    function_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class TopicRuleErrorActionLambdaArgs:
    def __init__(__self__, *, function_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> pulumi.Input[_builtins.str]: ...
    @function_arn.setter
    def function_arn(self, value: pulumi.Input[_builtins.str]): ...

class TopicRuleErrorActionRepublishArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    topic: pulumi.Input[_builtins.str]
    qos: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class TopicRuleErrorActionRepublishArgs:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        topic: pulumi.Input[_builtins.str],
        qos: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]: ...
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def qos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @qos.setter
    def qos(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TopicRuleErrorActionS3ArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    canned_acl: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleErrorActionS3Args:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        canned_acl: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cannedAcl")
    def canned_acl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @canned_acl.setter
    def canned_acl(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleErrorActionSnsArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    target_arn: pulumi.Input[_builtins.str]
    message_format: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleErrorActionSnsArgs:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        target_arn: pulumi.Input[_builtins.str],
        message_format: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Input[_builtins.str]: ...
    @target_arn.setter
    def target_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_format.setter
    def message_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleErrorActionSqsArgsDict(TypedDict):
    queue_url: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    use_base64: pulumi.Input[_builtins.bool]

@pulumi.input_type
class TopicRuleErrorActionSqsArgs:
    def __init__(
        __self__,
        *,
        queue_url: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        use_base64: pulumi.Input[_builtins.bool],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queueUrl")
    def queue_url(self) -> pulumi.Input[_builtins.str]: ...
    @queue_url.setter
    def queue_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="useBase64")
    def use_base64(self) -> pulumi.Input[_builtins.bool]: ...
    @use_base64.setter
    def use_base64(self, value: pulumi.Input[_builtins.bool]): ...

class TopicRuleErrorActionStepFunctionsArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    state_machine_name: pulumi.Input[_builtins.str]
    execution_name_prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleErrorActionStepFunctionsArgs:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        state_machine_name: pulumi.Input[_builtins.str],
        execution_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="stateMachineName")
    def state_machine_name(self) -> pulumi.Input[_builtins.str]: ...
    @state_machine_name.setter
    def state_machine_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="executionNamePrefix")
    def execution_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_name_prefix.setter
    def execution_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleErrorActionTimestreamArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    dimensions: pulumi.Input[
        Sequence[pulumi.Input[TopicRuleErrorActionTimestreamDimensionArgsDict]]
    ]
    role_arn: pulumi.Input[_builtins.str]
    table_name: pulumi.Input[_builtins.str]
    timestamp: NotRequired[
        pulumi.Input[TopicRuleErrorActionTimestreamTimestampArgsDict]
    ]

@pulumi.input_type
class TopicRuleErrorActionTimestreamArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        dimensions: pulumi.Input[
            Sequence[pulumi.Input[TopicRuleErrorActionTimestreamDimensionArgs]]
        ],
        role_arn: pulumi.Input[_builtins.str],
        table_name: pulumi.Input[_builtins.str],
        timestamp: Optional[
            pulumi.Input[TopicRuleErrorActionTimestreamTimestampArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[TopicRuleErrorActionTimestreamDimensionArgs]]
    ]: ...
    @dimensions.setter
    def dimensions(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[TopicRuleErrorActionTimestreamDimensionArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def timestamp(
        self,
    ) -> Optional[pulumi.Input[TopicRuleErrorActionTimestreamTimestampArgs]]: ...
    @timestamp.setter
    def timestamp(
        self, value: Optional[pulumi.Input[TopicRuleErrorActionTimestreamTimestampArgs]]
    ): ...

class TopicRuleErrorActionTimestreamDimensionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class TopicRuleErrorActionTimestreamDimensionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class TopicRuleErrorActionTimestreamTimestampArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class TopicRuleErrorActionTimestreamTimestampArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class TopicRuleFirehoseArgsDict(TypedDict):
    delivery_stream_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    batch_mode: NotRequired[pulumi.Input[_builtins.bool]]
    separator: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleFirehoseArgs:
    def __init__(
        __self__,
        *,
        delivery_stream_name: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        batch_mode: Optional[pulumi.Input[_builtins.bool]] = ...,
        separator: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deliveryStreamName")
    def delivery_stream_name(self) -> pulumi.Input[_builtins.str]: ...
    @delivery_stream_name.setter
    def delivery_stream_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="batchMode")
    def batch_mode(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @batch_mode.setter
    def batch_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def separator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @separator.setter
    def separator(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleHttpArgsDict(TypedDict):
    url: pulumi.Input[_builtins.str]
    confirmation_url: NotRequired[pulumi.Input[_builtins.str]]
    http_headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TopicRuleHttpHttpHeaderArgsDict]]]
    ]

@pulumi.input_type
class TopicRuleHttpArgs:
    def __init__(
        __self__,
        *,
        url: pulumi.Input[_builtins.str],
        confirmation_url: Optional[pulumi.Input[_builtins.str]] = ...,
        http_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[TopicRuleHttpHttpHeaderArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="confirmationUrl")
    def confirmation_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @confirmation_url.setter
    def confirmation_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TopicRuleHttpHttpHeaderArgs]]]
    ]: ...
    @http_headers.setter
    def http_headers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TopicRuleHttpHttpHeaderArgs]]]
        ],
    ): ...

class TopicRuleHttpHttpHeaderArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class TopicRuleHttpHttpHeaderArgs:
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

class TopicRuleIotAnalyticArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    batch_mode: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class TopicRuleIotAnalyticArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        batch_mode: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="batchMode")
    def batch_mode(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @batch_mode.setter
    def batch_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TopicRuleIotEventArgsDict(TypedDict):
    input_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    batch_mode: NotRequired[pulumi.Input[_builtins.bool]]
    message_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleIotEventArgs:
    def __init__(
        __self__,
        *,
        input_name: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        batch_mode: Optional[pulumi.Input[_builtins.bool]] = ...,
        message_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputName")
    def input_name(self) -> pulumi.Input[_builtins.str]: ...
    @input_name.setter
    def input_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="batchMode")
    def batch_mode(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @batch_mode.setter
    def batch_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_id.setter
    def message_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleKafkaArgsDict(TypedDict):
    client_properties: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    destination_arn: pulumi.Input[_builtins.str]
    topic: pulumi.Input[_builtins.str]
    headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TopicRuleKafkaHeaderArgsDict]]]
    ]
    key: NotRequired[pulumi.Input[_builtins.str]]
    partition: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleKafkaArgs:
    def __init__(
        __self__,
        *,
        client_properties: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        destination_arn: pulumi.Input[_builtins.str],
        topic: pulumi.Input[_builtins.str],
        headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[TopicRuleKafkaHeaderArgs]]]
        ] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        partition: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientProperties")
    def client_properties(
        self,
    ) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @client_properties.setter
    def client_properties(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> pulumi.Input[_builtins.str]: ...
    @destination_arn.setter
    def destination_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]: ...
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleKafkaHeaderArgs]]]]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[TopicRuleKafkaHeaderArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def partition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partition.setter
    def partition(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleKafkaHeaderArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class TopicRuleKafkaHeaderArgs:
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

class TopicRuleKinesisArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    stream_name: pulumi.Input[_builtins.str]
    partition_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleKinesisArgs:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        stream_name: pulumi.Input[_builtins.str],
        partition_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> pulumi.Input[_builtins.str]: ...
    @stream_name.setter
    def stream_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partition_key.setter
    def partition_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleLambdaArgsDict(TypedDict):
    function_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class TopicRuleLambdaArgs:
    def __init__(__self__, *, function_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> pulumi.Input[_builtins.str]: ...
    @function_arn.setter
    def function_arn(self, value: pulumi.Input[_builtins.str]): ...

class TopicRuleRepublishArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    topic: pulumi.Input[_builtins.str]
    qos: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class TopicRuleRepublishArgs:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        topic: pulumi.Input[_builtins.str],
        qos: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]: ...
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def qos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @qos.setter
    def qos(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TopicRuleS3ArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    canned_acl: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleS3Args:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        canned_acl: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cannedAcl")
    def canned_acl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @canned_acl.setter
    def canned_acl(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleSnsArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    target_arn: pulumi.Input[_builtins.str]
    message_format: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleSnsArgs:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        target_arn: pulumi.Input[_builtins.str],
        message_format: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Input[_builtins.str]: ...
    @target_arn.setter
    def target_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_format.setter
    def message_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleSqsArgsDict(TypedDict):
    queue_url: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    use_base64: pulumi.Input[_builtins.bool]

@pulumi.input_type
class TopicRuleSqsArgs:
    def __init__(
        __self__,
        *,
        queue_url: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        use_base64: pulumi.Input[_builtins.bool],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queueUrl")
    def queue_url(self) -> pulumi.Input[_builtins.str]: ...
    @queue_url.setter
    def queue_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="useBase64")
    def use_base64(self) -> pulumi.Input[_builtins.bool]: ...
    @use_base64.setter
    def use_base64(self, value: pulumi.Input[_builtins.bool]): ...

class TopicRuleStepFunctionArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    state_machine_name: pulumi.Input[_builtins.str]
    execution_name_prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TopicRuleStepFunctionArgs:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        state_machine_name: pulumi.Input[_builtins.str],
        execution_name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="stateMachineName")
    def state_machine_name(self) -> pulumi.Input[_builtins.str]: ...
    @state_machine_name.setter
    def state_machine_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="executionNamePrefix")
    def execution_name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_name_prefix.setter
    def execution_name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopicRuleTimestreamArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    dimensions: pulumi.Input[
        Sequence[pulumi.Input[TopicRuleTimestreamDimensionArgsDict]]
    ]
    role_arn: pulumi.Input[_builtins.str]
    table_name: pulumi.Input[_builtins.str]
    timestamp: NotRequired[pulumi.Input[TopicRuleTimestreamTimestampArgsDict]]

@pulumi.input_type
class TopicRuleTimestreamArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        dimensions: pulumi.Input[
            Sequence[pulumi.Input[TopicRuleTimestreamDimensionArgs]]
        ],
        role_arn: pulumi.Input[_builtins.str],
        table_name: pulumi.Input[_builtins.str],
        timestamp: Optional[pulumi.Input[TopicRuleTimestreamTimestampArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[TopicRuleTimestreamDimensionArgs]]]: ...
    @dimensions.setter
    def dimensions(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[TopicRuleTimestreamDimensionArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> Optional[pulumi.Input[TopicRuleTimestreamTimestampArgs]]: ...
    @timestamp.setter
    def timestamp(
        self, value: Optional[pulumi.Input[TopicRuleTimestreamTimestampArgs]]
    ): ...

class TopicRuleTimestreamDimensionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class TopicRuleTimestreamDimensionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class TopicRuleTimestreamTimestampArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class TopicRuleTimestreamTimestampArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
