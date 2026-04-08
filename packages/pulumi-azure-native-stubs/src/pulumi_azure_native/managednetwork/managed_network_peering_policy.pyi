import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ManagedNetworkPeeringPolicyArgs", "ManagedNetworkPeeringPolicy"]

@pulumi.input_type
class ManagedNetworkPeeringPolicyArgs:
    def __init__(
        __self__,
        *,
        managed_network_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_network_peering_policy_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        properties: Optional[
            pulumi.Input[ManagedNetworkPeeringPolicyPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedNetworkName")
    def managed_network_name(self) -> pulumi.Input[_builtins.str]: ...
    @managed_network_name.setter
    def managed_network_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedNetworkPeeringPolicyName")
    def managed_network_peering_policy_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_network_peering_policy_name.setter
    def managed_network_peering_policy_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[ManagedNetworkPeeringPolicyPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[ManagedNetworkPeeringPolicyPropertiesArgs]]
    ): ...

@pulumi.type_token(...)
class ManagedNetworkPeeringPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_network_name: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_network_peering_policy_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    ManagedNetworkPeeringPolicyPropertiesArgs,
                    ManagedNetworkPeeringPolicyPropertiesArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ManagedNetworkPeeringPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ManagedNetworkPeeringPolicy: ...
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
    def properties(
        self,
    ) -> pulumi.Output[outputs.ManagedNetworkPeeringPolicyPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
