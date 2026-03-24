import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UptimeCheckConfigArgs", "UptimeCheckConfig"]

@pulumi.input_type
class UptimeCheckConfigArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        timeout: pulumi.Input[_builtins.str],
        checker_type: Optional[pulumi.Input[_builtins.str]] = ...,
        content_matchers: Optional[
            pulumi.Input[Sequence[pulumi.Input[UptimeCheckConfigContentMatcherArgs]]]
        ] = ...,
        http_check: Optional[pulumi.Input[UptimeCheckConfigHttpCheckArgs]] = ...,
        log_check_failures: Optional[pulumi.Input[_builtins.bool]] = ...,
        monitored_resource: Optional[
            pulumi.Input[UptimeCheckConfigMonitoredResourceArgs]
        ] = ...,
        period: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[
            pulumi.Input[UptimeCheckConfigResourceGroupArgs]
        ] = ...,
        selected_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        synthetic_monitor: Optional[
            pulumi.Input[UptimeCheckConfigSyntheticMonitorArgs]
        ] = ...,
        tcp_check: Optional[pulumi.Input[UptimeCheckConfigTcpCheckArgs]] = ...,
        user_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> pulumi.Input[_builtins.str]: ...
    @timeout.setter
    def timeout(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="checkerType")
    def checker_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @checker_type.setter
    def checker_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contentMatchers")
    def content_matchers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[UptimeCheckConfigContentMatcherArgs]]]
    ]: ...
    @content_matchers.setter
    def content_matchers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[UptimeCheckConfigContentMatcherArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpCheck")
    def http_check(self) -> Optional[pulumi.Input[UptimeCheckConfigHttpCheckArgs]]: ...
    @http_check.setter
    def http_check(
        self, value: Optional[pulumi.Input[UptimeCheckConfigHttpCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logCheckFailures")
    def log_check_failures(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @log_check_failures.setter
    def log_check_failures(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoredResource")
    def monitored_resource(
        self,
    ) -> Optional[pulumi.Input[UptimeCheckConfigMonitoredResourceArgs]]: ...
    @monitored_resource.setter
    def monitored_resource(
        self, value: Optional[pulumi.Input[UptimeCheckConfigMonitoredResourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @period.setter
    def period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(
        self,
    ) -> Optional[pulumi.Input[UptimeCheckConfigResourceGroupArgs]]: ...
    @resource_group.setter
    def resource_group(
        self, value: Optional[pulumi.Input[UptimeCheckConfigResourceGroupArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selectedRegions")
    def selected_regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @selected_regions.setter
    def selected_regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="syntheticMonitor")
    def synthetic_monitor(
        self,
    ) -> Optional[pulumi.Input[UptimeCheckConfigSyntheticMonitorArgs]]: ...
    @synthetic_monitor.setter
    def synthetic_monitor(
        self, value: Optional[pulumi.Input[UptimeCheckConfigSyntheticMonitorArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tcpCheck")
    def tcp_check(self) -> Optional[pulumi.Input[UptimeCheckConfigTcpCheckArgs]]: ...
    @tcp_check.setter
    def tcp_check(
        self, value: Optional[pulumi.Input[UptimeCheckConfigTcpCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @user_labels.setter
    def user_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _UptimeCheckConfigState:
    def __init__(
        __self__,
        *,
        checker_type: Optional[pulumi.Input[_builtins.str]] = ...,
        content_matchers: Optional[
            pulumi.Input[Sequence[pulumi.Input[UptimeCheckConfigContentMatcherArgs]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        http_check: Optional[pulumi.Input[UptimeCheckConfigHttpCheckArgs]] = ...,
        log_check_failures: Optional[pulumi.Input[_builtins.bool]] = ...,
        monitored_resource: Optional[
            pulumi.Input[UptimeCheckConfigMonitoredResourceArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        period: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[
            pulumi.Input[UptimeCheckConfigResourceGroupArgs]
        ] = ...,
        selected_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        synthetic_monitor: Optional[
            pulumi.Input[UptimeCheckConfigSyntheticMonitorArgs]
        ] = ...,
        tcp_check: Optional[pulumi.Input[UptimeCheckConfigTcpCheckArgs]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        uptime_check_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="checkerType")
    def checker_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @checker_type.setter
    def checker_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contentMatchers")
    def content_matchers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[UptimeCheckConfigContentMatcherArgs]]]
    ]: ...
    @content_matchers.setter
    def content_matchers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[UptimeCheckConfigContentMatcherArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpCheck")
    def http_check(self) -> Optional[pulumi.Input[UptimeCheckConfigHttpCheckArgs]]: ...
    @http_check.setter
    def http_check(
        self, value: Optional[pulumi.Input[UptimeCheckConfigHttpCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logCheckFailures")
    def log_check_failures(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @log_check_failures.setter
    def log_check_failures(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="monitoredResource")
    def monitored_resource(
        self,
    ) -> Optional[pulumi.Input[UptimeCheckConfigMonitoredResourceArgs]]: ...
    @monitored_resource.setter
    def monitored_resource(
        self, value: Optional[pulumi.Input[UptimeCheckConfigMonitoredResourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @period.setter
    def period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(
        self,
    ) -> Optional[pulumi.Input[UptimeCheckConfigResourceGroupArgs]]: ...
    @resource_group.setter
    def resource_group(
        self, value: Optional[pulumi.Input[UptimeCheckConfigResourceGroupArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selectedRegions")
    def selected_regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @selected_regions.setter
    def selected_regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="syntheticMonitor")
    def synthetic_monitor(
        self,
    ) -> Optional[pulumi.Input[UptimeCheckConfigSyntheticMonitorArgs]]: ...
    @synthetic_monitor.setter
    def synthetic_monitor(
        self, value: Optional[pulumi.Input[UptimeCheckConfigSyntheticMonitorArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tcpCheck")
    def tcp_check(self) -> Optional[pulumi.Input[UptimeCheckConfigTcpCheckArgs]]: ...
    @tcp_check.setter
    def tcp_check(
        self, value: Optional[pulumi.Input[UptimeCheckConfigTcpCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="uptimeCheckId")
    def uptime_check_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uptime_check_id.setter
    def uptime_check_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @user_labels.setter
    def user_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("gcp:monitoring/uptimeCheckConfig:UptimeCheckConfig")
class UptimeCheckConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        checker_type: Optional[pulumi.Input[_builtins.str]] = ...,
        content_matchers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            UptimeCheckConfigContentMatcherArgs,
                            UptimeCheckConfigContentMatcherArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        http_check: Optional[
            pulumi.Input[
                Union[
                    UptimeCheckConfigHttpCheckArgs, UptimeCheckConfigHttpCheckArgsDict
                ]
            ]
        ] = ...,
        log_check_failures: Optional[pulumi.Input[_builtins.bool]] = ...,
        monitored_resource: Optional[
            pulumi.Input[
                Union[
                    UptimeCheckConfigMonitoredResourceArgs,
                    UptimeCheckConfigMonitoredResourceArgsDict,
                ]
            ]
        ] = ...,
        period: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[
            pulumi.Input[
                Union[
                    UptimeCheckConfigResourceGroupArgs,
                    UptimeCheckConfigResourceGroupArgsDict,
                ]
            ]
        ] = ...,
        selected_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        synthetic_monitor: Optional[
            pulumi.Input[
                Union[
                    UptimeCheckConfigSyntheticMonitorArgs,
                    UptimeCheckConfigSyntheticMonitorArgsDict,
                ]
            ]
        ] = ...,
        tcp_check: Optional[
            pulumi.Input[
                Union[UptimeCheckConfigTcpCheckArgs, UptimeCheckConfigTcpCheckArgsDict]
            ]
        ] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        user_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: UptimeCheckConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        checker_type: Optional[pulumi.Input[_builtins.str]] = ...,
        content_matchers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            UptimeCheckConfigContentMatcherArgs,
                            UptimeCheckConfigContentMatcherArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        http_check: Optional[
            pulumi.Input[
                Union[
                    UptimeCheckConfigHttpCheckArgs, UptimeCheckConfigHttpCheckArgsDict
                ]
            ]
        ] = ...,
        log_check_failures: Optional[pulumi.Input[_builtins.bool]] = ...,
        monitored_resource: Optional[
            pulumi.Input[
                Union[
                    UptimeCheckConfigMonitoredResourceArgs,
                    UptimeCheckConfigMonitoredResourceArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        period: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group: Optional[
            pulumi.Input[
                Union[
                    UptimeCheckConfigResourceGroupArgs,
                    UptimeCheckConfigResourceGroupArgsDict,
                ]
            ]
        ] = ...,
        selected_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        synthetic_monitor: Optional[
            pulumi.Input[
                Union[
                    UptimeCheckConfigSyntheticMonitorArgs,
                    UptimeCheckConfigSyntheticMonitorArgsDict,
                ]
            ]
        ] = ...,
        tcp_check: Optional[
            pulumi.Input[
                Union[UptimeCheckConfigTcpCheckArgs, UptimeCheckConfigTcpCheckArgsDict]
            ]
        ] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        uptime_check_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> UptimeCheckConfig: ...
    @_builtins.property
    @pulumi.getter(name="checkerType")
    def checker_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentMatchers")
    def content_matchers(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.UptimeCheckConfigContentMatcher]]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpCheck")
    def http_check(
        self,
    ) -> pulumi.Output[Optional[outputs.UptimeCheckConfigHttpCheck]]: ...
    @_builtins.property
    @pulumi.getter(name="logCheckFailures")
    def log_check_failures(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="monitoredResource")
    def monitored_resource(
        self,
    ) -> pulumi.Output[Optional[outputs.UptimeCheckConfigMonitoredResource]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(
        self,
    ) -> pulumi.Output[Optional[outputs.UptimeCheckConfigResourceGroup]]: ...
    @_builtins.property
    @pulumi.getter(name="selectedRegions")
    def selected_regions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="syntheticMonitor")
    def synthetic_monitor(
        self,
    ) -> pulumi.Output[Optional[outputs.UptimeCheckConfigSyntheticMonitor]]: ...
    @_builtins.property
    @pulumi.getter(name="tcpCheck")
    def tcp_check(
        self,
    ) -> pulumi.Output[Optional[outputs.UptimeCheckConfigTcpCheck]]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="uptimeCheckId")
    def uptime_check_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
