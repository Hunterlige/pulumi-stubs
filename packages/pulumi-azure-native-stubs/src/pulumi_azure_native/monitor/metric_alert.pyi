import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MetricAlertArgs", "MetricAlert"]

@pulumi.input_type
class MetricAlertArgs:
    def __init__(
        __self__,
        *,
        criteria: pulumi.Input[
            Union[
                MetricAlertMultipleResourceMultipleMetricCriteriaArgs,
                MetricAlertSingleResourceMultipleMetricCriteriaArgs,
                WebtestLocationAvailabilityCriteriaArgs,
            ]
        ],
        enabled: pulumi.Input[_builtins.bool],
        evaluation_frequency: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        scopes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        severity: pulumi.Input[_builtins.int],
        window_size: pulumi.Input[_builtins.str],
        actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricAlertActionArgs]]]
        ] = ...,
        auto_mitigate: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_resource_region: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def criteria(
        self,
    ) -> pulumi.Input[
        Union[
            MetricAlertMultipleResourceMultipleMetricCriteriaArgs,
            MetricAlertSingleResourceMultipleMetricCriteriaArgs,
            WebtestLocationAvailabilityCriteriaArgs,
        ]
    ]: ...
    @criteria.setter
    def criteria(
        self,
        value: pulumi.Input[
            Union[
                MetricAlertMultipleResourceMultipleMetricCriteriaArgs,
                MetricAlertSingleResourceMultipleMetricCriteriaArgs,
                WebtestLocationAvailabilityCriteriaArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> pulumi.Input[_builtins.str]: ...
    @evaluation_frequency.setter
    def evaluation_frequency(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @scopes.setter
    def scopes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Input[_builtins.int]: ...
    @severity.setter
    def severity(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="windowSize")
    def window_size(self) -> pulumi.Input[_builtins.str]: ...
    @window_size.setter
    def window_size(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[MetricAlertActionArgs]]]]: ...
    @actions.setter
    def actions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[MetricAlertActionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoMitigate")
    def auto_mitigate(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_mitigate.setter
    def auto_mitigate(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="targetResourceRegion")
    def target_resource_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_region.setter
    def target_resource_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceType")
    def target_resource_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_type.setter
    def target_resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:monitor:MetricAlert")
class MetricAlert(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[MetricAlertActionArgs, MetricAlertActionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        auto_mitigate: Optional[pulumi.Input[_builtins.bool]] = ...,
        criteria: Optional[
            pulumi.Input[
                Union[
                    Union[
                        MetricAlertMultipleResourceMultipleMetricCriteriaArgs,
                        MetricAlertMultipleResourceMultipleMetricCriteriaArgsDict,
                    ],
                    Union[
                        MetricAlertSingleResourceMultipleMetricCriteriaArgs,
                        MetricAlertSingleResourceMultipleMetricCriteriaArgsDict,
                    ],
                    Union[
                        WebtestLocationAvailabilityCriteriaArgs,
                        WebtestLocationAvailabilityCriteriaArgsDict,
                    ],
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        evaluation_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        severity: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_resource_region: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        window_size: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MetricAlertArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> MetricAlert: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.MetricAlertActionResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="autoMitigate")
    def auto_mitigate(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def criteria(self) -> pulumi.Output[Any]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isMigrated")
    def is_migrated(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceRegion")
    def target_resource_region(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceType")
    def target_resource_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="windowSize")
    def window_size(self) -> pulumi.Output[_builtins.str]: ...
