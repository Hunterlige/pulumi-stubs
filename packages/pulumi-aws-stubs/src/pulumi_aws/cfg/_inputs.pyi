

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., ..., ..., 'ConformancePackInputParameterArgs', 'ConformancePackInputParameterArgsDict', 'DeliveryChannelSnapshotDeliveryPropertiesArgs', 'DeliveryChannelSnapshotDeliveryPropertiesArgsDict', 'OrganizationConformancePackInputParameterArgs', 'OrganizationConformancePackInputParameterArgsDict', 'RecorderRecordingGroupArgs', 'RecorderRecordingGroupArgsDict', 'RecorderRecordingGroupExclusionByResourceTypeArgs', ..., 'RecorderRecordingGroupRecordingStrategyArgs', 'RecorderRecordingGroupRecordingStrategyArgsDict', 'RecorderRecordingModeArgs', 'RecorderRecordingModeArgsDict', 'RecorderRecordingModeRecordingModeOverrideArgs', 'RecorderRecordingModeRecordingModeOverrideArgsDict', 'RemediationConfigurationExecutionControlsArgs', 'RemediationConfigurationExecutionControlsArgsDict', ..., ..., 'RemediationConfigurationParameterArgs', 'RemediationConfigurationParameterArgsDict', 'RuleEvaluationModeArgs', 'RuleEvaluationModeArgsDict', 'RuleScopeArgs', 'RuleScopeArgsDict', 'RuleSourceArgs', 'RuleSourceArgsDict', 'RuleSourceCustomPolicyDetailsArgs', 'RuleSourceCustomPolicyDetailsArgsDict', 'RuleSourceSourceDetailArgs', 'RuleSourceSourceDetailArgsDict']
class ConfigurationAggregatorAccountAggregationSourceArgsDict(TypedDict):
    account_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    all_regions: NotRequired[pulumi.Input[_builtins.bool]]
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ConfigurationAggregatorAccountAggregationSourceArgs:
    def __init__(__self__, *, account_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], all_regions: Optional[pulumi.Input[_builtins.bool]] = ..., regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountIds")
    def account_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @account_ids.setter
    def account_ids(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allRegions")
    def all_regions(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @all_regions.setter
    def all_regions(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @regions.setter
    def regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ConfigurationAggregatorOrganizationAggregationSourceArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    all_regions: NotRequired[pulumi.Input[_builtins.bool]]
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ConfigurationAggregatorOrganizationAggregationSourceArgs:
    def __init__(__self__, *, role_arn: pulumi.Input[_builtins.str], all_regions: Optional[pulumi.Input[_builtins.bool]] = ..., regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allRegions")
    def all_regions(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @all_regions.setter
    def all_regions(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @regions.setter
    def regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ConformancePackInputParameterArgsDict(TypedDict):
    parameter_name: pulumi.Input[_builtins.str]
    parameter_value: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConformancePackInputParameterArgs:
    def __init__(__self__, *, parameter_name: pulumi.Input[_builtins.str], parameter_value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_name.setter
    def parameter_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_value.setter
    def parameter_value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DeliveryChannelSnapshotDeliveryPropertiesArgsDict(TypedDict):
    delivery_frequency: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DeliveryChannelSnapshotDeliveryPropertiesArgs:
    def __init__(__self__, *, delivery_frequency: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryFrequency")
    def delivery_frequency(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delivery_frequency.setter
    def delivery_frequency(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OrganizationConformancePackInputParameterArgsDict(TypedDict):
    parameter_name: pulumi.Input[_builtins.str]
    parameter_value: pulumi.Input[_builtins.str]


@pulumi.input_type
class OrganizationConformancePackInputParameterArgs:
    def __init__(__self__, *, parameter_name: pulumi.Input[_builtins.str], parameter_value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_name.setter
    def parameter_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parameter_value.setter
    def parameter_value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class RecorderRecordingGroupArgsDict(TypedDict):
    all_supported: NotRequired[pulumi.Input[_builtins.bool]]
    exclusion_by_resource_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[RecorderRecordingGroupExclusionByResourceTypeArgsDict]]]]
    include_global_resource_types: NotRequired[pulumi.Input[_builtins.bool]]
    recording_strategies: NotRequired[pulumi.Input[Sequence[pulumi.Input[RecorderRecordingGroupRecordingStrategyArgsDict]]]]
    resource_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class RecorderRecordingGroupArgs:
    def __init__(__self__, *, all_supported: Optional[pulumi.Input[_builtins.bool]] = ..., exclusion_by_resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[RecorderRecordingGroupExclusionByResourceTypeArgs]]]] = ..., include_global_resource_types: Optional[pulumi.Input[_builtins.bool]] = ..., recording_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[RecorderRecordingGroupRecordingStrategyArgs]]]] = ..., resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allSupported")
    def all_supported(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @all_supported.setter
    def all_supported(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exclusionByResourceTypes")
    def exclusion_by_resource_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RecorderRecordingGroupExclusionByResourceTypeArgs]]]]:
        
        ...
    
    @exclusion_by_resource_types.setter
    def exclusion_by_resource_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RecorderRecordingGroupExclusionByResourceTypeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeGlobalResourceTypes")
    def include_global_resource_types(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_global_resource_types.setter
    def include_global_resource_types(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordingStrategies")
    def recording_strategies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RecorderRecordingGroupRecordingStrategyArgs]]]]:
        
        ...
    
    @recording_strategies.setter
    def recording_strategies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RecorderRecordingGroupRecordingStrategyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_types.setter
    def resource_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RecorderRecordingGroupExclusionByResourceTypeArgsDict(TypedDict):
    resource_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class RecorderRecordingGroupExclusionByResourceTypeArgs:
    def __init__(__self__, *, resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_types.setter
    def resource_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RecorderRecordingGroupRecordingStrategyArgsDict(TypedDict):
    use_only: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RecorderRecordingGroupRecordingStrategyArgs:
    def __init__(__self__, *, use_only: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useOnly")
    def use_only(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @use_only.setter
    def use_only(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RecorderRecordingModeArgsDict(TypedDict):
    recording_frequency: NotRequired[pulumi.Input[_builtins.str]]
    recording_mode_override: NotRequired[pulumi.Input[RecorderRecordingModeRecordingModeOverrideArgsDict]]


@pulumi.input_type
class RecorderRecordingModeArgs:
    def __init__(__self__, *, recording_frequency: Optional[pulumi.Input[_builtins.str]] = ..., recording_mode_override: Optional[pulumi.Input[RecorderRecordingModeRecordingModeOverrideArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordingFrequency")
    def recording_frequency(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @recording_frequency.setter
    def recording_frequency(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordingModeOverride")
    def recording_mode_override(self) -> Optional[pulumi.Input[RecorderRecordingModeRecordingModeOverrideArgs]]:
        
        ...
    
    @recording_mode_override.setter
    def recording_mode_override(self, value: Optional[pulumi.Input[RecorderRecordingModeRecordingModeOverrideArgs]]): # -> None:
        ...
    


class RecorderRecordingModeRecordingModeOverrideArgsDict(TypedDict):
    recording_frequency: pulumi.Input[_builtins.str]
    resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RecorderRecordingModeRecordingModeOverrideArgs:
    def __init__(__self__, *, recording_frequency: pulumi.Input[_builtins.str], resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordingFrequency")
    def recording_frequency(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @recording_frequency.setter
    def recording_frequency(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @resource_types.setter
    def resource_types(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RemediationConfigurationExecutionControlsArgsDict(TypedDict):
    ssm_controls: NotRequired[pulumi.Input[RemediationConfigurationExecutionControlsSsmControlsArgsDict]]


@pulumi.input_type
class RemediationConfigurationExecutionControlsArgs:
    def __init__(__self__, *, ssm_controls: Optional[pulumi.Input[RemediationConfigurationExecutionControlsSsmControlsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmControls")
    def ssm_controls(self) -> Optional[pulumi.Input[RemediationConfigurationExecutionControlsSsmControlsArgs]]:
        
        ...
    
    @ssm_controls.setter
    def ssm_controls(self, value: Optional[pulumi.Input[RemediationConfigurationExecutionControlsSsmControlsArgs]]): # -> None:
        ...
    


class RemediationConfigurationExecutionControlsSsmControlsArgsDict(TypedDict):
    concurrent_execution_rate_percentage: NotRequired[pulumi.Input[_builtins.int]]
    error_percentage: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class RemediationConfigurationExecutionControlsSsmControlsArgs:
    def __init__(__self__, *, concurrent_execution_rate_percentage: Optional[pulumi.Input[_builtins.int]] = ..., error_percentage: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="concurrentExecutionRatePercentage")
    def concurrent_execution_rate_percentage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @concurrent_execution_rate_percentage.setter
    def concurrent_execution_rate_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorPercentage")
    def error_percentage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @error_percentage.setter
    def error_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class RemediationConfigurationParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    resource_value: NotRequired[pulumi.Input[_builtins.str]]
    static_value: NotRequired[pulumi.Input[_builtins.str]]
    static_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class RemediationConfigurationParameterArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], resource_value: Optional[pulumi.Input[_builtins.str]] = ..., static_value: Optional[pulumi.Input[_builtins.str]] = ..., static_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceValue")
    def resource_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_value.setter
    def resource_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticValue")
    def static_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @static_value.setter
    def static_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticValues")
    def static_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @static_values.setter
    def static_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RuleEvaluationModeArgsDict(TypedDict):
    mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RuleEvaluationModeArgs:
    def __init__(__self__, *, mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuleScopeArgsDict(TypedDict):
    compliance_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    compliance_resource_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    tag_key: NotRequired[pulumi.Input[_builtins.str]]
    tag_value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RuleScopeArgs:
    def __init__(__self__, *, compliance_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., compliance_resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tag_key: Optional[pulumi.Input[_builtins.str]] = ..., tag_value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceResourceId")
    def compliance_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compliance_resource_id.setter
    def compliance_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceResourceTypes")
    def compliance_resource_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @compliance_resource_types.setter
    def compliance_resource_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag_key.setter
    def tag_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagValue")
    def tag_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag_value.setter
    def tag_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuleSourceArgsDict(TypedDict):
    owner: pulumi.Input[_builtins.str]
    custom_policy_details: NotRequired[pulumi.Input[RuleSourceCustomPolicyDetailsArgsDict]]
    source_details: NotRequired[pulumi.Input[Sequence[pulumi.Input[RuleSourceSourceDetailArgsDict]]]]
    source_identifier: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RuleSourceArgs:
    def __init__(__self__, *, owner: pulumi.Input[_builtins.str], custom_policy_details: Optional[pulumi.Input[RuleSourceCustomPolicyDetailsArgs]] = ..., source_details: Optional[pulumi.Input[Sequence[pulumi.Input[RuleSourceSourceDetailArgs]]]] = ..., source_identifier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @owner.setter
    def owner(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPolicyDetails")
    def custom_policy_details(self) -> Optional[pulumi.Input[RuleSourceCustomPolicyDetailsArgs]]:
        
        ...
    
    @custom_policy_details.setter
    def custom_policy_details(self, value: Optional[pulumi.Input[RuleSourceCustomPolicyDetailsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDetails")
    def source_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RuleSourceSourceDetailArgs]]]]:
        
        ...
    
    @source_details.setter
    def source_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RuleSourceSourceDetailArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIdentifier")
    def source_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_identifier.setter
    def source_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuleSourceCustomPolicyDetailsArgsDict(TypedDict):
    policy_runtime: pulumi.Input[_builtins.str]
    policy_text: pulumi.Input[_builtins.str]
    enable_debug_log_delivery: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class RuleSourceCustomPolicyDetailsArgs:
    def __init__(__self__, *, policy_runtime: pulumi.Input[_builtins.str], policy_text: pulumi.Input[_builtins.str], enable_debug_log_delivery: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyRuntime")
    def policy_runtime(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_runtime.setter
    def policy_runtime(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyText")
    def policy_text(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_text.setter
    def policy_text(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDebugLogDelivery")
    def enable_debug_log_delivery(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_debug_log_delivery.setter
    def enable_debug_log_delivery(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class RuleSourceSourceDetailArgsDict(TypedDict):
    event_source: NotRequired[pulumi.Input[_builtins.str]]
    maximum_execution_frequency: NotRequired[pulumi.Input[_builtins.str]]
    message_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RuleSourceSourceDetailArgs:
    def __init__(__self__, *, event_source: Optional[pulumi.Input[_builtins.str]] = ..., maximum_execution_frequency: Optional[pulumi.Input[_builtins.str]] = ..., message_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventSource")
    def event_source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_source.setter
    def event_source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @maximum_execution_frequency.setter
    def maximum_execution_frequency(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageType")
    def message_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_type.setter
    def message_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


