import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FileServicePropertiesArgs", "FileServiceProperties"]

@pulumi.input_type
class FileServicePropertiesArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        cors: Optional[pulumi.Input[CorsRulesArgs]] = ...,
        file_services_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol_settings: Optional[pulumi.Input[ProtocolSettingsArgs]] = ...,
        share_delete_retention_policy: Optional[
            pulumi.Input[DeleteRetentionPolicyArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]: ...
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def cors(self) -> Optional[pulumi.Input[CorsRulesArgs]]: ...
    @cors.setter
    def cors(self, value: Optional[pulumi.Input[CorsRulesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="fileServicesName")
    def file_services_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_services_name.setter
    def file_services_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protocolSettings")
    def protocol_settings(self) -> Optional[pulumi.Input[ProtocolSettingsArgs]]: ...
    @protocol_settings.setter
    def protocol_settings(
        self, value: Optional[pulumi.Input[ProtocolSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="shareDeleteRetentionPolicy")
    def share_delete_retention_policy(
        self,
    ) -> Optional[pulumi.Input[DeleteRetentionPolicyArgs]]: ...
    @share_delete_retention_policy.setter
    def share_delete_retention_policy(
        self, value: Optional[pulumi.Input[DeleteRetentionPolicyArgs]]
    ): ...

@pulumi.type_token("azure-native:storage:FileServiceProperties")
class FileServiceProperties(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cors: Optional[pulumi.Input[Union[CorsRulesArgs, CorsRulesArgsDict]]] = ...,
        file_services_name: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol_settings: Optional[
            pulumi.Input[Union[ProtocolSettingsArgs, ProtocolSettingsArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        share_delete_retention_policy: Optional[
            pulumi.Input[
                Union[DeleteRetentionPolicyArgs, DeleteRetentionPolicyArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FileServicePropertiesArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> FileServiceProperties: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cors(self) -> pulumi.Output[Optional[outputs.CorsRulesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="protocolSettings")
    def protocol_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.ProtocolSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="shareDeleteRetentionPolicy")
    def share_delete_retention_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.DeleteRetentionPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.SkuResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
