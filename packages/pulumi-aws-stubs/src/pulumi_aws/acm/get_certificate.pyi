

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCertificateResult', 'AwaitableGetCertificateResult', 'get_certificate', 'get_certificate_output']
@pulumi.output_type
class GetCertificateResult:
    
    def __init__(__self__, arn=..., certificate=..., certificate_chain=..., domain=..., id=..., key_types=..., most_recent=..., region=..., status=..., statuses=..., tags=..., types=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyTypes")
    def key_types(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


class AwaitableGetCertificateResult(GetCertificateResult):
    def __await__(self): # -> Generator[Never, Any, GetCertificateResult]:
        ...
    


def get_certificate(domain: Optional[_builtins.str] = ..., key_types: Optional[Sequence[_builtins.str]] = ..., most_recent: Optional[_builtins.bool] = ..., region: Optional[_builtins.str] = ..., statuses: Optional[Sequence[_builtins.str]] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., types: Optional[Sequence[_builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCertificateResult:
    
    ...

def get_certificate_output(domain: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., key_types: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., most_recent: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., statuses: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., types: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCertificateResult]:
    
    ...

