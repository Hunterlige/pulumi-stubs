

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTrustedAccessRoleBindingResult', 'AwaitableGetTrustedAccessRoleBindingResult', 'get_trusted_access_role_binding', 'get_trusted_access_role_binding_output']
@pulumi.output_type
class GetTrustedAccessRoleBindingResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., provisioning_state=..., roles=..., source_resource_id=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetTrustedAccessRoleBindingResult(GetTrustedAccessRoleBindingResult):
    def __await__(self): # -> Generator[Never, Any, GetTrustedAccessRoleBindingResult]:
        ...
    


def get_trusted_access_role_binding(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., trusted_access_role_binding_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTrustedAccessRoleBindingResult:
    
    ...

def get_trusted_access_role_binding_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., trusted_access_role_binding_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTrustedAccessRoleBindingResult]:
    
    ...

