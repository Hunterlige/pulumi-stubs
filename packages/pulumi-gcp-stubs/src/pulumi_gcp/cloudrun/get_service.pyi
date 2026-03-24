

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServiceResult', 'AwaitableGetServiceResult', 'get_service', 'get_service_output']
@pulumi.output_type
class GetServiceResult:
    
    def __init__(__self__, autogenerate_revision_name=..., id=..., location=..., metadatas=..., name=..., project=..., statuses=..., templates=..., traffics=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autogenerateRevisionName")
    def autogenerate_revision_name(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadatas(self) -> Sequence[outputs.GetServiceMetadataResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Sequence[outputs.GetServiceStatusResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def templates(self) -> Sequence[outputs.GetServiceTemplateResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def traffics(self) -> Sequence[outputs.GetServiceTrafficResult]:
        ...
    


class AwaitableGetServiceResult(GetServiceResult):
    def __await__(self): # -> Generator[Never, Any, GetServiceResult]:
        ...
    


def get_service(location: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServiceResult:
    
    ...

def get_service_output(location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServiceResult]:
    
    ...

