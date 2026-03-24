

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEnterprisePolicyResult', 'AwaitableGetEnterprisePolicyResult', 'get_enterprise_policy', 'get_enterprise_policy_output']
@pulumi.output_type
class GetEnterprisePolicyResult:
    
    def __init__(__self__, azure_api_version=..., encryption=..., health_status=..., id=..., identity=..., kind=..., location=..., lockbox=..., name=..., network_injection=..., system_data=..., system_id=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.PropertiesResponseEncryption]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.EnterprisePolicyIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lockbox(self) -> Optional[outputs.PropertiesResponseLockbox]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInjection")
    def network_injection(self) -> Optional[outputs.PropertiesResponseNetworkInjection]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemId")
    def system_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetEnterprisePolicyResult(GetEnterprisePolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetEnterprisePolicyResult]:
        ...
    


def get_enterprise_policy(enterprise_policy_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEnterprisePolicyResult:
    
    ...

def get_enterprise_policy_output(enterprise_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEnterprisePolicyResult]:
    
    ...

