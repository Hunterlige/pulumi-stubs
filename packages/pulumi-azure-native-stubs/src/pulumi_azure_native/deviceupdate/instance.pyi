import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["InstanceArgs", "Instance"]

@pulumi.input_type
class InstanceArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        diagnostic_storage_properties: Optional[
            pulumi.Input[DiagnosticStoragePropertiesArgs]
        ] = ...,
        enable_diagnostics: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        iot_hubs: Optional[
            pulumi.Input[Sequence[pulumi.Input[IotHubSettingsArgs]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
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
    @pulumi.getter(name="diagnosticStorageProperties")
    def diagnostic_storage_properties(
        self,
    ) -> Optional[pulumi.Input[DiagnosticStoragePropertiesArgs]]: ...
    @diagnostic_storage_properties.setter
    def diagnostic_storage_properties(
        self, value: Optional[pulumi.Input[DiagnosticStoragePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableDiagnostics")
    def enable_diagnostics(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_diagnostics.setter
    def enable_diagnostics(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iotHubs")
    def iot_hubs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IotHubSettingsArgs]]]]: ...
    @iot_hubs.setter
    def iot_hubs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IotHubSettingsArgs]]]]
    ): ...
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

@pulumi.type_token("azure-native:deviceupdate:Instance")
class Instance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        diagnostic_storage_properties: Optional[
            pulumi.Input[
                Union[
                    DiagnosticStoragePropertiesArgs, DiagnosticStoragePropertiesArgsDict
                ]
            ]
        ] = ...,
        enable_diagnostics: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        iot_hubs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[IotHubSettingsArgs, IotHubSettingsArgsDict]]
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: InstanceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Instance: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diagnosticStorageProperties")
    def diagnostic_storage_properties(
        self,
    ) -> pulumi.Output[Optional[outputs.DiagnosticStoragePropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="enableDiagnostics")
    def enable_diagnostics(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="iotHubs")
    def iot_hubs(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.IotHubSettingsResponse]]]: ...
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
