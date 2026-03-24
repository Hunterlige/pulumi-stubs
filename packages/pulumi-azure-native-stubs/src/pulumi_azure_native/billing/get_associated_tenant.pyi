

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAssociatedTenantResult', 'AwaitableGetAssociatedTenantResult', 'get_associated_tenant', 'get_associated_tenant_output']
@pulumi.output_type
class GetAssociatedTenantResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., properties=..., system_data=..., tags=..., type=...) -> None:
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
    @pulumi.getter
    def properties(self) -> outputs.AssociatedTenantPropertiesResponse:
        
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
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAssociatedTenantResult(GetAssociatedTenantResult):
    def __await__(self): # -> Generator[Never, Any, GetAssociatedTenantResult]:
        ...
    


def get_associated_tenant(associated_tenant_name: Optional[_builtins.str] = ..., billing_account_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAssociatedTenantResult:
    
    ...

def get_associated_tenant_output(associated_tenant_name: Optional[pulumi.Input[_builtins.str]] = ..., billing_account_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAssociatedTenantResult]:
    
    ...

