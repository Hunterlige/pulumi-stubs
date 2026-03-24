

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLabResult', 'AwaitableGetLabResult', 'get_lab', 'get_lab_output']
@pulumi.output_type
class GetLabResult:
    
    def __init__(__self__, auto_shutdown_profile=..., azure_api_version=..., connection_profile=..., description=..., id=..., lab_plan_id=..., location=..., name=..., network_profile=..., provisioning_state=..., resource_operation_error=..., roster_profile=..., security_profile=..., state=..., system_data=..., tags=..., title=..., type=..., virtual_machine_profile=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoShutdownProfile")
    def auto_shutdown_profile(self) -> outputs.AutoShutdownProfileResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionProfile")
    def connection_profile(self) -> outputs.ConnectionProfileResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labPlanId")
    def lab_plan_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[outputs.LabNetworkProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceOperationError")
    def resource_operation_error(self) -> outputs.ResourceOperationErrorResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rosterProfile")
    def roster_profile(self) -> Optional[outputs.RosterProfileResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> outputs.SecurityProfileResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineProfile")
    def virtual_machine_profile(self) -> outputs.VirtualMachineProfileResponse:
        
        ...
    


class AwaitableGetLabResult(GetLabResult):
    def __await__(self): # -> Generator[Never, Any, GetLabResult]:
        ...
    


def get_lab(lab_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLabResult:
    
    ...

def get_lab_output(lab_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLabResult]:
    
    ...

