

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVirtualMachineInstanceResult', 'AwaitableGetVirtualMachineInstanceResult', 'get_virtual_machine_instance', 'get_virtual_machine_instance_output']
@pulumi.output_type
class GetVirtualMachineInstanceResult:
    
    def __init__(__self__, azure_api_version=..., create_from_local=..., extended_location=..., guest_agent_install_status=..., hardware_profile=..., http_proxy_config=..., id=..., identity=..., instance_view=..., name=..., network_profile=..., os_profile=..., provisioning_state=..., resource_uid=..., security_profile=..., status=..., storage_profile=..., system_data=..., type=..., vm_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createFromLocal")
    def create_from_local(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestAgentInstallStatus")
    def guest_agent_install_status(self) -> Optional[outputs.GuestAgentInstallStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[outputs.VirtualMachineInstancePropertiesHardwareProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpProxyConfig")
    def http_proxy_config(self) -> Optional[outputs.HttpProxyConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> outputs.VirtualMachineInstanceViewResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[outputs.VirtualMachineInstancePropertiesNetworkProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[outputs.VirtualMachineInstancePropertiesOsProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceUid")
    def resource_uid(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[outputs.VirtualMachineInstancePropertiesSecurityProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.VirtualMachineInstanceStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[outputs.VirtualMachineInstancePropertiesStorageProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetVirtualMachineInstanceResult(GetVirtualMachineInstanceResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualMachineInstanceResult]:
        ...
    


def get_virtual_machine_instance(resource_uri: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualMachineInstanceResult:
    
    ...

def get_virtual_machine_instance_output(resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualMachineInstanceResult]:
    
    ...

