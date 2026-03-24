

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDnssecConfigResult', 'AwaitableGetDnssecConfigResult', 'get_dnssec_config', 'get_dnssec_config_output']
@pulumi.output_type
class GetDnssecConfigResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., name=..., provisioning_state=..., signing_keys=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="signingKeys")
    def signing_keys(self) -> Sequence[outputs.SigningKeyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDnssecConfigResult(GetDnssecConfigResult):
    def __await__(self): # -> Generator[Never, Any, GetDnssecConfigResult]:
        ...
    


def get_dnssec_config(resource_group_name: Optional[_builtins.str] = ..., zone_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDnssecConfigResult:
    
    ...

def get_dnssec_config_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., zone_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDnssecConfigResult]:
    
    ...

