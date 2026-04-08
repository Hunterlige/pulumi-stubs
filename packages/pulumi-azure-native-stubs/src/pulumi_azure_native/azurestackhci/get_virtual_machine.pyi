import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualMachineResult",
    "AwaitableGetVirtualMachineResult",
    "get_virtual_machine",
    "get_virtual_machine_output",
]

@pulumi.output_type
class GetVirtualMachineResult:
    def __init__(
        __self__,
        azure_api_version=...,
        extended_location=...,
        guest_agent_profile=...,
        hardware_profile=...,
        id=...,
        identity=...,
        location=...,
        name=...,
        network_profile=...,
        os_profile=...,
        provisioning_state=...,
        security_profile=...,
        status=...,
        storage_profile=...,
        system_data=...,
        tags=...,
        type=...,
        vm_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="guestAgentProfile")
    def guest_agent_profile(self) -> Optional[outputs.GuestAgentProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(
        self,
    ) -> Optional[outputs.VirtualMachinePropertiesResponseHardwareProfile]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.IdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(
        self,
    ) -> Optional[outputs.VirtualMachinePropertiesResponseNetworkProfile]: ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(
        self,
    ) -> Optional[outputs.VirtualMachinePropertiesResponseOsProfile]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(
        self,
    ) -> Optional[outputs.VirtualMachinePropertiesResponseSecurityProfile]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.VirtualMachineStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(
        self,
    ) -> Optional[outputs.VirtualMachinePropertiesResponseStorageProfile]: ...
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
    @pulumi.getter(name="vmId")
    def vm_id(self) -> _builtins.str: ...

class AwaitableGetVirtualMachineResult(GetVirtualMachineResult):
    def __await__(self): ...

def get_virtual_machine(
    resource_group_name: Optional[_builtins.str] = ...,
    virtual_machine_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualMachineResult: ...
def get_virtual_machine_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    virtual_machine_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualMachineResult]: ...
