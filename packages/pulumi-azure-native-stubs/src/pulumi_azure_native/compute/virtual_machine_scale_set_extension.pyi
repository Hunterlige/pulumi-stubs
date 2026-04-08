import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VirtualMachineScaleSetExtensionInitArgs", "VirtualMachineScaleSetExtension"]

@pulumi.input_type
class VirtualMachineScaleSetExtensionInitArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        vm_scale_set_name: pulumi.Input[_builtins.str],
        auto_upgrade_minor_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_automatic_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        force_update_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
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
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        type_handler_version: Optional[pulumi.Input[_builtins.str]] = ...,
        vmss_extension_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vmScaleSetName")
    def vm_scale_set_name(self) -> pulumi.Input[_builtins.str]: ...
    @vm_scale_set_name.setter
    def vm_scale_set_name(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_handler_version.setter
    def type_handler_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmssExtensionName")
    def vmss_extension_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vmss_extension_name.setter
    def vmss_extension_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class VirtualMachineScaleSetExtension(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_upgrade_minor_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_automatic_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        force_update_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
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
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        type_handler_version: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_scale_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        vmss_extension_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VirtualMachineScaleSetExtensionInitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VirtualMachineScaleSetExtension: ...
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
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
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
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
