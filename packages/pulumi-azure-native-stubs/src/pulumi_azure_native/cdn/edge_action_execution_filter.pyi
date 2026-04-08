import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EdgeActionExecutionFilterArgs", "EdgeActionExecutionFilter"]

@pulumi.input_type
class EdgeActionExecutionFilterArgs:
    def __init__(
        __self__,
        *,
        edge_action_name: pulumi.Input[_builtins.str],
        execution_filter_identifier_header_name: pulumi.Input[_builtins.str],
        execution_filter_identifier_header_value: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        version_id: pulumi.Input[_builtins.str],
        execution_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="edgeActionName")
    def edge_action_name(self) -> pulumi.Input[_builtins.str]: ...
    @edge_action_name.setter
    def edge_action_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="executionFilterIdentifierHeaderName")
    def execution_filter_identifier_header_name(
        self,
    ) -> pulumi.Input[_builtins.str]: ...
    @execution_filter_identifier_header_name.setter
    def execution_filter_identifier_header_name(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionFilterIdentifierHeaderValue")
    def execution_filter_identifier_header_value(
        self,
    ) -> pulumi.Input[_builtins.str]: ...
    @execution_filter_identifier_header_value.setter
    def execution_filter_identifier_header_value(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Input[_builtins.str]: ...
    @version_id.setter
    def version_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="executionFilter")
    def execution_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_filter.setter
    def execution_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:cdn:EdgeActionExecutionFilter")
class EdgeActionExecutionFilter(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        edge_action_name: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_filter_identifier_header_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        execution_filter_identifier_header_value: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EdgeActionExecutionFilterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> EdgeActionExecutionFilter: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="executionFilterIdentifierHeaderName")
    def execution_filter_identifier_header_name(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="executionFilterIdentifierHeaderValue")
    def execution_filter_identifier_header_value(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
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
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[_builtins.str]: ...
