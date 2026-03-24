import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConfigurationAggregatorAccountAggregationSource",
    ...,
    "ConformancePackInputParameter",
    "DeliveryChannelSnapshotDeliveryProperties",
    "OrganizationConformancePackInputParameter",
    "RecorderRecordingGroup",
    "RecorderRecordingGroupExclusionByResourceType",
    "RecorderRecordingGroupRecordingStrategy",
    "RecorderRecordingMode",
    "RecorderRecordingModeRecordingModeOverride",
    "RemediationConfigurationExecutionControls",
    ...,
    "RemediationConfigurationParameter",
    "RuleEvaluationMode",
    "RuleScope",
    "RuleSource",
    "RuleSourceCustomPolicyDetails",
    "RuleSourceSourceDetail",
]

@pulumi.output_type
class ConfigurationAggregatorAccountAggregationSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_ids: Sequence[_builtins.str],
        all_regions: Optional[_builtins.bool] = ...,
        regions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountIds")
    def account_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allRegions")
    def all_regions(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ConfigurationAggregatorOrganizationAggregationSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        role_arn: _builtins.str,
        all_regions: Optional[_builtins.bool] = ...,
        regions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allRegions")
    def all_regions(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ConformancePackInputParameter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, parameter_name: _builtins.str, parameter_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> _builtins.str: ...

@pulumi.output_type
class DeliveryChannelSnapshotDeliveryProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, delivery_frequency: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deliveryFrequency")
    def delivery_frequency(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OrganizationConformancePackInputParameter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, parameter_name: _builtins.str, parameter_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parameterName")
    def parameter_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> _builtins.str: ...

@pulumi.output_type
class RecorderRecordingGroup(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        all_supported: Optional[_builtins.bool] = ...,
        exclusion_by_resource_types: Optional[
            Sequence[outputs.RecorderRecordingGroupExclusionByResourceType]
        ] = ...,
        include_global_resource_types: Optional[_builtins.bool] = ...,
        recording_strategies: Optional[
            Sequence[outputs.RecorderRecordingGroupRecordingStrategy]
        ] = ...,
        resource_types: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allSupported")
    def all_supported(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="exclusionByResourceTypes")
    def exclusion_by_resource_types(
        self,
    ) -> Optional[Sequence[outputs.RecorderRecordingGroupExclusionByResourceType]]: ...
    @_builtins.property
    @pulumi.getter(name="includeGlobalResourceTypes")
    def include_global_resource_types(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="recordingStrategies")
    def recording_strategies(
        self,
    ) -> Optional[Sequence[outputs.RecorderRecordingGroupRecordingStrategy]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RecorderRecordingGroupExclusionByResourceType(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, resource_types: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RecorderRecordingGroupRecordingStrategy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, use_only: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="useOnly")
    def use_only(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RecorderRecordingMode(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        recording_frequency: Optional[_builtins.str] = ...,
        recording_mode_override: Optional[
            outputs.RecorderRecordingModeRecordingModeOverride
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordingFrequency")
    def recording_frequency(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recordingModeOverride")
    def recording_mode_override(
        self,
    ) -> Optional[outputs.RecorderRecordingModeRecordingModeOverride]: ...

@pulumi.output_type
class RecorderRecordingModeRecordingModeOverride(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        recording_frequency: _builtins.str,
        resource_types: Sequence[_builtins.str],
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordingFrequency")
    def recording_frequency(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RemediationConfigurationExecutionControls(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ssm_controls: Optional[
            outputs.RemediationConfigurationExecutionControlsSsmControls
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ssmControls")
    def ssm_controls(
        self,
    ) -> Optional[outputs.RemediationConfigurationExecutionControlsSsmControls]: ...

@pulumi.output_type
class RemediationConfigurationExecutionControlsSsmControls(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        concurrent_execution_rate_percentage: Optional[_builtins.int] = ...,
        error_percentage: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="concurrentExecutionRatePercentage")
    def concurrent_execution_rate_percentage(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="errorPercentage")
    def error_percentage(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class RemediationConfigurationParameter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        resource_value: Optional[_builtins.str] = ...,
        static_value: Optional[_builtins.str] = ...,
        static_values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceValue")
    def resource_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="staticValue")
    def static_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="staticValues")
    def static_values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RuleEvaluationMode(dict):
    def __init__(__self__, *, mode: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RuleScope(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compliance_resource_id: Optional[_builtins.str] = ...,
        compliance_resource_types: Optional[Sequence[_builtins.str]] = ...,
        tag_key: Optional[_builtins.str] = ...,
        tag_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="complianceResourceId")
    def compliance_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="complianceResourceTypes")
    def compliance_resource_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tagValue")
    def tag_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RuleSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        owner: _builtins.str,
        custom_policy_details: Optional[outputs.RuleSourceCustomPolicyDetails] = ...,
        source_details: Optional[Sequence[outputs.RuleSourceSourceDetail]] = ...,
        source_identifier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customPolicyDetails")
    def custom_policy_details(
        self,
    ) -> Optional[outputs.RuleSourceCustomPolicyDetails]: ...
    @_builtins.property
    @pulumi.getter(name="sourceDetails")
    def source_details(self) -> Optional[Sequence[outputs.RuleSourceSourceDetail]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceIdentifier")
    def source_identifier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RuleSourceCustomPolicyDetails(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        policy_runtime: _builtins.str,
        policy_text: _builtins.str,
        enable_debug_log_delivery: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyRuntime")
    def policy_runtime(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyText")
    def policy_text(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enableDebugLogDelivery")
    def enable_debug_log_delivery(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class RuleSourceSourceDetail(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event_source: Optional[_builtins.str] = ...,
        maximum_execution_frequency: Optional[_builtins.str] = ...,
        message_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventSource")
    def event_source(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="messageType")
    def message_type(self) -> Optional[_builtins.str]: ...
