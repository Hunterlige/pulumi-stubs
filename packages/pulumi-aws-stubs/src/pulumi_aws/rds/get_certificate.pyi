

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCertificateResult', 'AwaitableGetCertificateResult', 'get_certificate', 'get_certificate_output']
@pulumi.output_type
class GetCertificateResult:
    
    def __init__(__self__, arn=..., certificate_type=..., customer_override=..., customer_override_valid_till=..., default_for_new_launches=..., id=..., latest_valid_till=..., region=..., thumbprint=..., valid_from=..., valid_till=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateType")
    def certificate_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOverride")
    def customer_override(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOverrideValidTill")
    def customer_override_valid_till(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultForNewLaunches")
    def default_for_new_launches(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestValidTill")
    def latest_valid_till(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validFrom")
    def valid_from(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validTill")
    def valid_till(self) -> _builtins.str:
        
        ...
    


class AwaitableGetCertificateResult(GetCertificateResult):
    def __await__(self): # -> Generator[Never, Any, GetCertificateResult]:
        ...
    


def get_certificate(default_for_new_launches: Optional[_builtins.bool] = ..., id: Optional[_builtins.str] = ..., latest_valid_till: Optional[_builtins.bool] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCertificateResult:
    
    ...

def get_certificate_output(default_for_new_launches: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., latest_valid_till: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCertificateResult]:
    
    ...

