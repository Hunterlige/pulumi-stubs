import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NetworkPolicyArgs", "NetworkPolicy"]

@pulumi.input_type
class NetworkPolicyArgs:
    def __init__(
        __self__,
        *,
        edge_services_cidr: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        vmware_engine_network: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        external_ip: Optional[pulumi.Input[NetworkPolicyExternalIpArgs]] = ...,
        internet_access: Optional[pulumi.Input[NetworkPolicyInternetAccessArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="edgeServicesCidr")
    def edge_services_cidr(self) -> pulumi.Input[_builtins.str]: ...
    @edge_services_cidr.setter
    def edge_services_cidr(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetwork")
    def vmware_engine_network(self) -> pulumi.Input[_builtins.str]: ...
    @vmware_engine_network.setter
    def vmware_engine_network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalIp")
    def external_ip(self) -> Optional[pulumi.Input[NetworkPolicyExternalIpArgs]]: ...
    @external_ip.setter
    def external_ip(
        self, value: Optional[pulumi.Input[NetworkPolicyExternalIpArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="internetAccess")
    def internet_access(
        self,
    ) -> Optional[pulumi.Input[NetworkPolicyInternetAccessArgs]]: ...
    @internet_access.setter
    def internet_access(
        self, value: Optional[pulumi.Input[NetworkPolicyInternetAccessArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _NetworkPolicyState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        edge_services_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        external_ip: Optional[pulumi.Input[NetworkPolicyExternalIpArgs]] = ...,
        internet_access: Optional[pulumi.Input[NetworkPolicyInternetAccessArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_engine_network: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_engine_network_canonical: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter(name="edgeServicesCidr")
    def edge_services_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @edge_services_cidr.setter
    def edge_services_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalIp")
    def external_ip(self) -> Optional[pulumi.Input[NetworkPolicyExternalIpArgs]]: ...
    @external_ip.setter
    def external_ip(
        self, value: Optional[pulumi.Input[NetworkPolicyExternalIpArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="internetAccess")
    def internet_access(
        self,
    ) -> Optional[pulumi.Input[NetworkPolicyInternetAccessArgs]]: ...
    @internet_access.setter
    def internet_access(
        self, value: Optional[pulumi.Input[NetworkPolicyInternetAccessArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetwork")
    def vmware_engine_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vmware_engine_network.setter
    def vmware_engine_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetworkCanonical")
    def vmware_engine_network_canonical(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vmware_engine_network_canonical.setter
    def vmware_engine_network_canonical(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("gcp:vmwareengine/networkPolicy:NetworkPolicy")
class NetworkPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        edge_services_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        external_ip: Optional[
            pulumi.Input[
                Union[NetworkPolicyExternalIpArgs, NetworkPolicyExternalIpArgsDict]
            ]
        ] = ...,
        internet_access: Optional[
            pulumi.Input[
                Union[
                    NetworkPolicyInternetAccessArgs, NetworkPolicyInternetAccessArgsDict
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_engine_network: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NetworkPolicyArgs,
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
        edge_services_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        external_ip: Optional[
            pulumi.Input[
                Union[NetworkPolicyExternalIpArgs, NetworkPolicyExternalIpArgsDict]
            ]
        ] = ...,
        internet_access: Optional[
            pulumi.Input[
                Union[
                    NetworkPolicyInternetAccessArgs, NetworkPolicyInternetAccessArgsDict
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_engine_network: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_engine_network_canonical: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> NetworkPolicy: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="edgeServicesCidr")
    def edge_services_cidr(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalIp")
    def external_ip(self) -> pulumi.Output[outputs.NetworkPolicyExternalIp]: ...
    @_builtins.property
    @pulumi.getter(name="internetAccess")
    def internet_access(self) -> pulumi.Output[outputs.NetworkPolicyInternetAccess]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetwork")
    def vmware_engine_network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmwareEngineNetworkCanonical")
    def vmware_engine_network_canonical(self) -> pulumi.Output[_builtins.str]: ...
