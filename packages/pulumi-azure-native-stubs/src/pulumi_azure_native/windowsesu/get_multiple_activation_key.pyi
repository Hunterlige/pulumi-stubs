

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMultipleActivationKeyResult', 'AwaitableGetMultipleActivationKeyResult', 'get_multiple_activation_key', 'get_multiple_activation_key_output']
@pulumi.output_type
class GetMultipleActivationKeyResult:
    
    def __init__(__self__, agreement_number=..., azure_api_version=..., expiration_date=..., id=..., installed_server_number=..., is_eligible=..., location=..., multiple_activation_key=..., name=..., os_type=..., provisioning_state=..., support_type=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agreementNumber")
    def agreement_number(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="installedServerNumber")
    def installed_server_number(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEligible")
    def is_eligible(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multipleActivationKey")
    def multiple_activation_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportType")
    def support_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetMultipleActivationKeyResult(GetMultipleActivationKeyResult):
    def __await__(self): # -> Generator[Never, Any, GetMultipleActivationKeyResult]:
        ...
    


def get_multiple_activation_key(multiple_activation_key_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMultipleActivationKeyResult:
    
    ...

def get_multiple_activation_key_output(multiple_activation_key_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMultipleActivationKeyResult]:
    
    ...

