import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["QueryArgs", "Query"]

@pulumi.input_type
class QueryArgs:
    def __init__(
        __self__,
        *,
        body: pulumi.Input[_builtins.str],
        display_name: pulumi.Input[_builtins.str],
        query_pack_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[Any] = ...,
        related: Optional[
            pulumi.Input[LogAnalyticsQueryPackQueryPropertiesRelatedArgs]
        ] = ...,
        tags: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def body(self) -> pulumi.Input[_builtins.str]: ...
    @body.setter
    def body(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="queryPackName")
    def query_pack_name(self) -> pulumi.Input[_builtins.str]: ...
    @query_pack_name.setter
    def query_pack_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Any]: ...
    @properties.setter
    def properties(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter
    def related(
        self,
    ) -> Optional[pulumi.Input[LogAnalyticsQueryPackQueryPropertiesRelatedArgs]]: ...
    @related.setter
    def related(
        self,
        value: Optional[pulumi.Input[LogAnalyticsQueryPackQueryPropertiesRelatedArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]
    ]: ...
    @tags.setter
    def tags(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
            ]
        ],
    ): ...

@pulumi.type_token("azure-native:operationalinsights:Query")
class Query(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        body: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[Any] = ...,
        query_pack_name: Optional[pulumi.Input[_builtins.str]] = ...,
        related: Optional[
            pulumi.Input[
                Union[
                    LogAnalyticsQueryPackQueryPropertiesRelatedArgs,
                    LogAnalyticsQueryPackQueryPropertiesRelatedArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: QueryArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Query: ...
    @_builtins.property
    @pulumi.getter
    def author(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def body(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]: ...
    @_builtins.property
    @pulumi.getter
    def related(
        self,
    ) -> pulumi.Output[
        Optional[outputs.LogAnalyticsQueryPackQueryPropertiesResponseRelated]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, Sequence[_builtins.str]]]]: ...
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
