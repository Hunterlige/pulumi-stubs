

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTestBaseAccountResult', 'AwaitableGetTestBaseAccountResult', 'get_test_base_account', 'get_test_base_account_output']
@pulumi.output_type
class GetTestBaseAccountResult:
    
    def __init__(__self__, access_level=..., azure_api_version=..., id=..., identity=..., location=..., name=..., provisioning_state=..., sku=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> _builtins.str:
        
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
    def identity(self) -> Optional[outputs.SystemAssignedServiceIdentityResponse]:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.TestBaseAccountSKUResponse:
        
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
    


class AwaitableGetTestBaseAccountResult(GetTestBaseAccountResult):
    def __await__(self): # -> Generator[Never, Any, GetTestBaseAccountResult]:
        ...
    


def get_test_base_account(resource_group_name: Optional[_builtins.str] = ..., test_base_account_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTestBaseAccountResult:
    
    ...

def get_test_base_account_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., test_base_account_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTestBaseAccountResult]:
    
    ...

