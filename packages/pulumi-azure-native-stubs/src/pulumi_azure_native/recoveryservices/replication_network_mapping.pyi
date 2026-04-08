import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReplicationNetworkMappingArgs", "ReplicationNetworkMapping"]

@pulumi.input_type
class ReplicationNetworkMappingArgs:
    def __init__(
        __self__,
        *,
        fabric_name: pulumi.Input[_builtins.str],
        network_name: pulumi.Input[_builtins.str],
        properties: pulumi.Input[CreateNetworkMappingInputPropertiesArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        resource_name: pulumi.Input[_builtins.str],
        network_mapping_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fabricName")
    def fabric_name(self) -> pulumi.Input[_builtins.str]: ...
    @fabric_name.setter
    def fabric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="networkName")
    def network_name(self) -> pulumi.Input[_builtins.str]: ...
    @network_name.setter
    def network_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[CreateNetworkMappingInputPropertiesArgs]: ...
    @properties.setter
    def properties(
        self, value: pulumi.Input[CreateNetworkMappingInputPropertiesArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="networkMappingName")
    def network_mapping_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_mapping_name.setter
    def network_mapping_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ReplicationNetworkMapping(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        fabric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_mapping_name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    CreateNetworkMappingInputPropertiesArgs,
                    CreateNetworkMappingInputPropertiesArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_name_: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReplicationNetworkMappingArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ReplicationNetworkMapping: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.NetworkMappingPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
