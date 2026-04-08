import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VirtualMachineExtensionArgs", "VirtualMachineExtension"]

@pulumi.input_type
class VirtualMachineExtensionArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        vm_name: pulumi.Input[_builtins.str],
        auto_upgrade_minor_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_automatic_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        force_update_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_view: Optional[
            pulumi.Input[VirtualMachineExtensionInstanceViewArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_settings: Optional[Any] = ...,
        protected_settings_from_key_vault: Optional[
            pulumi.Input[KeyVaultSecretReferenceArgs]
        ] = ...,
        provision_after_extensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        publisher: Optional[pulumi.Input[_builtins.str]] = ...,
        settings: Optional[Any] = ...,
        suppress_failures: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        type_handler_version: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_extension_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vmName")
    def vm_name(self) -> pulumi.Input[_builtins.str]: ...
    @vm_name.setter
    def vm_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_upgrade_minor_version.setter
    def auto_upgrade_minor_version(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_automatic_upgrade.setter
    def enable_automatic_upgrade(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @force_update_tag.setter
    def force_update_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(
        self,
    ) -> Optional[pulumi.Input[VirtualMachineExtensionInstanceViewArgs]]: ...
    @instance_view.setter
    def instance_view(
        self, value: Optional[pulumi.Input[VirtualMachineExtensionInstanceViewArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> Optional[Any]: ...
    @protected_settings.setter
    def protected_settings(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="protectedSettingsFromKeyVault")
    def protected_settings_from_key_vault(
        self,
    ) -> Optional[pulumi.Input[KeyVaultSecretReferenceArgs]]: ...
    @protected_settings_from_key_vault.setter
    def protected_settings_from_key_vault(
        self, value: Optional[pulumi.Input[KeyVaultSecretReferenceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisionAfterExtensions")
    def provision_after_extensions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @provision_after_extensions.setter
    def provision_after_extensions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Any]: ...
    @settings.setter
    def settings(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="suppressFailures")
    def suppress_failures(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @suppress_failures.setter
    def suppress_failures(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_handler_version.setter
    def type_handler_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmExtensionName")
    def vm_extension_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_extension_name.setter
    def vm_extension_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:compute:VirtualMachineExtension")
class VirtualMachineExtension(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_upgrade_minor_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_automatic_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        force_update_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_view: Optional[
            pulumi.Input[
                Union[
                    VirtualMachineExtensionInstanceViewArgs,
                    VirtualMachineExtensionInstanceViewArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_settings: Optional[Any] = ...,
        protected_settings_from_key_vault: Optional[
            pulumi.Input[
                Union[KeyVaultSecretReferenceArgs, KeyVaultSecretReferenceArgsDict]
            ]
        ] = ...,
        provision_after_extensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        publisher: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        settings: Optional[Any] = ...,
        suppress_failures: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        type_handler_version: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_extension_name: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VirtualMachineExtensionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VirtualMachineExtension: ...
    @_builtins.property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(
        self,
    ) -> pulumi.Output[
        Optional[outputs.VirtualMachineExtensionInstanceViewResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="protectedSettingsFromKeyVault")
    def protected_settings_from_key_vault(
        self,
    ) -> pulumi.Output[Optional[outputs.KeyVaultSecretReferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisionAfterExtensions")
    def provision_after_extensions(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="suppressFailures")
    def suppress_failures(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
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
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
