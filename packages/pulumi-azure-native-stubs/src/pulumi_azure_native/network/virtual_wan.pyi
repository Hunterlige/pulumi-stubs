import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VirtualWanArgs", "VirtualWan"]

@pulumi.input_type
class VirtualWanArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        allow_branch_to_branch_traffic: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_vnet_to_vnet_traffic: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_vpn_encryption: Optional[pulumi.Input[_builtins.bool]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_wan_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowBranchToBranchTraffic")
    def allow_branch_to_branch_traffic(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_branch_to_branch_traffic.setter
    def allow_branch_to_branch_traffic(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowVnetToVnetTraffic")
    def allow_vnet_to_vnet_traffic(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_vnet_to_vnet_traffic.setter
    def allow_vnet_to_vnet_traffic(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableVpnEncryption")
    def disable_vpn_encryption(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_vpn_encryption.setter
    def disable_vpn_encryption(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualWANName")
    def virtual_wan_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_wan_name.setter
    def virtual_wan_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:network:VirtualWan")
class VirtualWan(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_branch_to_branch_traffic: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_vnet_to_vnet_traffic: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_vpn_encryption: Optional[pulumi.Input[_builtins.bool]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_wan_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VirtualWanArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VirtualWan: ...
    @_builtins.property
    @pulumi.getter(name="allowBranchToBranchTraffic")
    def allow_branch_to_branch_traffic(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="allowVnetToVnetTraffic")
    def allow_vnet_to_vnet_traffic(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableVpnEncryption")
    def disable_vpn_encryption(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="office365LocalBreakoutCategory")
    def office365_local_breakout_category(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualHubs")
    def virtual_hubs(self) -> pulumi.Output[Sequence[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="vpnSites")
    def vpn_sites(self) -> pulumi.Output[Sequence[outputs.SubResourceResponse]]: ...
