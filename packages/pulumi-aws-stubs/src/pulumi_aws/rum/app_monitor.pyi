import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AppMonitorArgs", "AppMonitor"]

@pulumi.input_type
class AppMonitorArgs:
    def __init__(
        __self__,
        *,
        app_monitor_configuration: Optional[
            pulumi.Input[AppMonitorAppMonitorConfigurationArgs]
        ] = ...,
        custom_events: Optional[pulumi.Input[AppMonitorCustomEventsArgs]] = ...,
        cw_log_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appMonitorConfiguration")
    def app_monitor_configuration(
        self,
    ) -> Optional[pulumi.Input[AppMonitorAppMonitorConfigurationArgs]]: ...
    @app_monitor_configuration.setter
    def app_monitor_configuration(
        self, value: Optional[pulumi.Input[AppMonitorAppMonitorConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customEvents")
    def custom_events(self) -> Optional[pulumi.Input[AppMonitorCustomEventsArgs]]: ...
    @custom_events.setter
    def custom_events(
        self, value: Optional[pulumi.Input[AppMonitorCustomEventsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cwLogEnabled")
    def cw_log_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cw_log_enabled.setter
    def cw_log_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainLists")
    def domain_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @domain_lists.setter
    def domain_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _AppMonitorState:
    def __init__(
        __self__,
        *,
        app_monitor_configuration: Optional[
            pulumi.Input[AppMonitorAppMonitorConfigurationArgs]
        ] = ...,
        app_monitor_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_events: Optional[pulumi.Input[AppMonitorCustomEventsArgs]] = ...,
        cw_log_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        cw_log_group: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appMonitorConfiguration")
    def app_monitor_configuration(
        self,
    ) -> Optional[pulumi.Input[AppMonitorAppMonitorConfigurationArgs]]: ...
    @app_monitor_configuration.setter
    def app_monitor_configuration(
        self, value: Optional[pulumi.Input[AppMonitorAppMonitorConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="appMonitorId")
    def app_monitor_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_monitor_id.setter
    def app_monitor_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customEvents")
    def custom_events(self) -> Optional[pulumi.Input[AppMonitorCustomEventsArgs]]: ...
    @custom_events.setter
    def custom_events(
        self, value: Optional[pulumi.Input[AppMonitorCustomEventsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cwLogEnabled")
    def cw_log_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cw_log_enabled.setter
    def cw_log_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="cwLogGroup")
    def cw_log_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cw_log_group.setter
    def cw_log_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainLists")
    def domain_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @domain_lists.setter
    def domain_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:rum/appMonitor:AppMonitor")
class AppMonitor(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_monitor_configuration: Optional[
            pulumi.Input[
                Union[
                    AppMonitorAppMonitorConfigurationArgs,
                    AppMonitorAppMonitorConfigurationArgsDict,
                ]
            ]
        ] = ...,
        custom_events: Optional[
            pulumi.Input[
                Union[AppMonitorCustomEventsArgs, AppMonitorCustomEventsArgsDict]
            ]
        ] = ...,
        cw_log_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[AppMonitorArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_monitor_configuration: Optional[
            pulumi.Input[
                Union[
                    AppMonitorAppMonitorConfigurationArgs,
                    AppMonitorAppMonitorConfigurationArgsDict,
                ]
            ]
        ] = ...,
        app_monitor_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_events: Optional[
            pulumi.Input[
                Union[AppMonitorCustomEventsArgs, AppMonitorCustomEventsArgsDict]
            ]
        ] = ...,
        cw_log_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        cw_log_group: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> AppMonitor: ...
    @_builtins.property
    @pulumi.getter(name="appMonitorConfiguration")
    def app_monitor_configuration(
        self,
    ) -> pulumi.Output[outputs.AppMonitorAppMonitorConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="appMonitorId")
    def app_monitor_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customEvents")
    def custom_events(self) -> pulumi.Output[outputs.AppMonitorCustomEvents]: ...
    @_builtins.property
    @pulumi.getter(name="cwLogEnabled")
    def cw_log_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="cwLogGroup")
    def cw_log_group(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="domainLists")
    def domain_lists(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
