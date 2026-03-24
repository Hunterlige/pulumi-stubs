import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SavedQueryArgs", "SavedQuery"]

@pulumi.input_type
class SavedQueryArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        parent: pulumi.Input[_builtins.str],
        visibility: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_query: Optional[pulumi.Input[SavedQueryLoggingQueryArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ops_analytics_query: Optional[
            pulumi.Input[SavedQueryOpsAnalyticsQueryArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]: ...
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> pulumi.Input[_builtins.str]: ...
    @visibility.setter
    def visibility(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingQuery")
    def logging_query(self) -> Optional[pulumi.Input[SavedQueryLoggingQueryArgs]]: ...
    @logging_query.setter
    def logging_query(
        self, value: Optional[pulumi.Input[SavedQueryLoggingQueryArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="opsAnalyticsQuery")
    def ops_analytics_query(
        self,
    ) -> Optional[pulumi.Input[SavedQueryOpsAnalyticsQueryArgs]]: ...
    @ops_analytics_query.setter
    def ops_analytics_query(
        self, value: Optional[pulumi.Input[SavedQueryOpsAnalyticsQueryArgs]]
    ): ...

@pulumi.input_type
class _SavedQueryState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_query: Optional[pulumi.Input[SavedQueryLoggingQueryArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ops_analytics_query: Optional[
            pulumi.Input[SavedQueryOpsAnalyticsQueryArgs]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingQuery")
    def logging_query(self) -> Optional[pulumi.Input[SavedQueryLoggingQueryArgs]]: ...
    @logging_query.setter
    def logging_query(
        self, value: Optional[pulumi.Input[SavedQueryLoggingQueryArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="opsAnalyticsQuery")
    def ops_analytics_query(
        self,
    ) -> Optional[pulumi.Input[SavedQueryOpsAnalyticsQueryArgs]]: ...
    @ops_analytics_query.setter
    def ops_analytics_query(
        self, value: Optional[pulumi.Input[SavedQueryOpsAnalyticsQueryArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:logging/savedQuery:SavedQuery")
class SavedQuery(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_query: Optional[
            pulumi.Input[
                Union[SavedQueryLoggingQueryArgs, SavedQueryLoggingQueryArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ops_analytics_query: Optional[
            pulumi.Input[
                Union[
                    SavedQueryOpsAnalyticsQueryArgs, SavedQueryOpsAnalyticsQueryArgsDict
                ]
            ]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SavedQueryArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_query: Optional[
            pulumi.Input[
                Union[SavedQueryLoggingQueryArgs, SavedQueryLoggingQueryArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ops_analytics_query: Optional[
            pulumi.Input[
                Union[
                    SavedQueryOpsAnalyticsQueryArgs, SavedQueryOpsAnalyticsQueryArgsDict
                ]
            ]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SavedQuery: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loggingQuery")
    def logging_query(
        self,
    ) -> pulumi.Output[Optional[outputs.SavedQueryLoggingQuery]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="opsAnalyticsQuery")
    def ops_analytics_query(
        self,
    ) -> pulumi.Output[Optional[outputs.SavedQueryOpsAnalyticsQuery]]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> pulumi.Output[_builtins.str]: ...
