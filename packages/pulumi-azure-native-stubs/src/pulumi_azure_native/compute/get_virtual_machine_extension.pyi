import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualMachineExtensionResult",
    "AwaitableGetVirtualMachineExtensionResult",
    "get_virtual_machine_extension",
    "get_virtual_machine_extension_output",
]

@pulumi.output_type
class GetVirtualMachineExtensionResult:
    def __init__(
        __self__,
        auto_upgrade_minor_version=...,
        azure_api_version=...,
        enable_automatic_upgrade=...,
        force_update_tag=...,
        id=...,
        instance_view=...,
        location=...,
        name=...,
        protected_settings=...,
        protected_settings_from_key_vault=...,
        provision_after_extensions=...,
        provisioning_state=...,
        publisher=...,
        settings=...,
        suppress_failures=...,
        system_data=...,
        tags=...,
        type=...,
        type_handler_version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(
        self,
    ) -> Optional[outputs.VirtualMachineExtensionInstanceViewResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="protectedSettingsFromKeyVault")
    def protected_settings_from_key_vault(
        self,
    ) -> Optional[outputs.KeyVaultSecretReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisionAfterExtensions")
    def provision_after_extensions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="suppressFailures")
    def suppress_failures(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[_builtins.str]: ...

class AwaitableGetVirtualMachineExtensionResult(GetVirtualMachineExtensionResult):
    def __await__(self): ...

def get_virtual_machine_extension(
    expand: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    vm_extension_name: Optional[_builtins.str] = ...,
    vm_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualMachineExtensionResult: ...
def get_virtual_machine_extension_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    vm_extension_name: Optional[pulumi.Input[_builtins.str]] = ...,
    vm_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualMachineExtensionResult]: ...
