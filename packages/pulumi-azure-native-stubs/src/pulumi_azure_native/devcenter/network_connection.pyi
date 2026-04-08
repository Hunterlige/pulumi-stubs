import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NetworkConnectionArgs", "NetworkConnection"]

@pulumi.input_type
class NetworkConnectionArgs:
    def __init__(
        __self__,
        *,
        domain_join_type: pulumi.Input[Union[_builtins.str, DomainJoinType]],
        resource_group_name: pulumi.Input[_builtins.str],
        subnet_id: pulumi.Input[_builtins.str],
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_password: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_username: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        networking_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainJoinType")
    def domain_join_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, DomainJoinType]]: ...
    @domain_join_type.setter
    def domain_join_type(
        self, value: pulumi.Input[Union[_builtins.str, DomainJoinType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainPassword")
    def domain_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_password.setter
    def domain_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainUsername")
    def domain_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_username.setter
    def domain_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkConnectionName")
    def network_connection_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_connection_name.setter
    def network_connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkingResourceGroupName")
    def networking_resource_group_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @networking_resource_group_name.setter
    def networking_resource_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="organizationUnit")
    def organization_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organization_unit.setter
    def organization_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:devcenter:NetworkConnection")
class NetworkConnection(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        domain_join_type: Optional[
            pulumi.Input[Union[_builtins.str, DomainJoinType]]
        ] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_password: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_username: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        networking_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NetworkConnectionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> NetworkConnection: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainJoinType")
    def domain_join_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="domainPassword")
    def domain_password(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="domainUsername")
    def domain_username(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckStatus")
    def health_check_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkingResourceGroupName")
    def networking_resource_group_name(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="organizationUnit")
    def organization_unit(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
