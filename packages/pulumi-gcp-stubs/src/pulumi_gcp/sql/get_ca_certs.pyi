

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCaCertsResult', 'AwaitableGetCaCertsResult', 'get_ca_certs', 'get_ca_certs_output']
@pulumi.output_type
class GetCaCertsResult:
    
    def __init__(__self__, active_version=..., certs=..., id=..., instance=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeVersion")
    def active_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certs(self) -> Sequence[outputs.GetCaCertsCertResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    


class AwaitableGetCaCertsResult(GetCaCertsResult):
    def __await__(self): # -> Generator[Never, Any, GetCaCertsResult]:
        ...
    


def get_ca_certs(instance: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCaCertsResult:
    
    ...

def get_ca_certs_output(instance: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCaCertsResult]:
    
    ...

