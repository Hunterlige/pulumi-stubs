import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReplicationExtensionArgs", "ReplicationExtension"]

@pulumi.input_type
class ReplicationExtensionArgs:
    def __init__(
        __self__,
        *,
        properties: pulumi.Input[ReplicationExtensionModelPropertiesArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        vault_name: pulumi.Input[_builtins.str],
        replication_extension_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[ReplicationExtensionModelPropertiesArgs]: ...
    @properties.setter
    def properties(
        self, value: pulumi.Input[ReplicationExtensionModelPropertiesArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vaultName")
    def vault_name(self) -> pulumi.Input[_builtins.str]: ...
    @vault_name.setter
    def vault_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="replicationExtensionName")
    def replication_extension_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_extension_name.setter
    def replication_extension_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("azure-native:datareplication:ReplicationExtension")
class ReplicationExtension(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    ReplicationExtensionModelPropertiesArgs,
                    ReplicationExtensionModelPropertiesArgsDict,
                ]
            ]
        ] = ...,
        replication_extension_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        vault_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReplicationExtensionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ReplicationExtension: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Output[outputs.ReplicationExtensionModelPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(
        self,
    ) -> pulumi.Output[outputs.ReplicationExtensionModelResponseSystemData]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
