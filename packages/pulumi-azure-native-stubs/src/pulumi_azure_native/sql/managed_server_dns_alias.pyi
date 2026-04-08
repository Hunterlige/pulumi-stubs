import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ManagedServerDnsAliasArgs", "ManagedServerDnsAlias"]

@pulumi.input_type
class ManagedServerDnsAliasArgs:
    def __init__(
        __self__,
        *,
        managed_instance_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        create_dns_record: Optional[pulumi.Input[_builtins.bool]] = ...,
        dns_alias_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedInstanceName")
    def managed_instance_name(self) -> pulumi.Input[_builtins.str]: ...
    @managed_instance_name.setter
    def managed_instance_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="createDnsRecord")
    def create_dns_record(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_dns_record.setter
    def create_dns_record(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsAliasName")
    def dns_alias_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_alias_name.setter
    def dns_alias_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:sql:ManagedServerDnsAlias")
class ManagedServerDnsAlias(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_dns_record: Optional[pulumi.Input[_builtins.bool]] = ...,
        dns_alias_name: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ManagedServerDnsAliasArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ManagedServerDnsAlias: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureDnsRecord")
    def azure_dns_record(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicAzureDnsRecord")
    def public_azure_dns_record(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
