

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDatabaseResult', 'AwaitableGetDatabaseResult', 'get_database', 'get_database_output']
@pulumi.output_type
class GetDatabaseResult:
    
    def __init__(__self__, charset=..., collation=..., deletion_policy=..., id=..., instance=..., name=..., project=..., self_link=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def charset(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def collation(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> _builtins.str:
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
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        ...
    


class AwaitableGetDatabaseResult(GetDatabaseResult):
    def __await__(self): # -> Generator[Never, Any, GetDatabaseResult]:
        ...
    


def get_database(instance: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDatabaseResult:
    
    ...

def get_database_output(instance: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDatabaseResult]:
    
    ...

