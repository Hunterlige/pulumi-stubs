import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SapLandscapeMonitorArgs", "SapLandscapeMonitor"]

@pulumi.input_type
class SapLandscapeMonitorArgs:
    def __init__(
        __self__,
        *,
        monitor_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        grouping: Optional[
            pulumi.Input[SapLandscapeMonitorPropertiesGroupingArgs]
        ] = ...,
        top_metrics_thresholds: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[SapLandscapeMonitorMetricThresholdsArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="monitorName")
    def monitor_name(self) -> pulumi.Input[_builtins.str]: ...
    @monitor_name.setter
    def monitor_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def grouping(
        self,
    ) -> Optional[pulumi.Input[SapLandscapeMonitorPropertiesGroupingArgs]]: ...
    @grouping.setter
    def grouping(
        self, value: Optional[pulumi.Input[SapLandscapeMonitorPropertiesGroupingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="topMetricsThresholds")
    def top_metrics_thresholds(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SapLandscapeMonitorMetricThresholdsArgs]]]
    ]: ...
    @top_metrics_thresholds.setter
    def top_metrics_thresholds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[SapLandscapeMonitorMetricThresholdsArgs]]
            ]
        ],
    ): ...

@pulumi.type_token("azure-native:workloads:SapLandscapeMonitor")
class SapLandscapeMonitor(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        grouping: Optional[
            pulumi.Input[
                Union[
                    SapLandscapeMonitorPropertiesGroupingArgs,
                    SapLandscapeMonitorPropertiesGroupingArgsDict,
                ]
            ]
        ] = ...,
        monitor_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        top_metrics_thresholds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            SapLandscapeMonitorMetricThresholdsArgs,
                            SapLandscapeMonitorMetricThresholdsArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SapLandscapeMonitorArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> SapLandscapeMonitor: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def grouping(
        self,
    ) -> pulumi.Output[
        Optional[outputs.SapLandscapeMonitorPropertiesGroupingResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="topMetricsThresholds")
    def top_metrics_thresholds(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.SapLandscapeMonitorMetricThresholdsResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
