

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRepositoryResult', 'AwaitableGetRepositoryResult', 'get_repository', 'get_repository_output']
@pulumi.output_type
class GetRepositoryResult:
    
    def __init__(__self__, create_ignore_already_exists=..., id=..., name=..., project=..., pubsub_configs=..., size=..., url=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createIgnoreAlreadyExists")
    def create_ignore_already_exists(self) -> _builtins.bool:
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
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubConfigs")
    def pubsub_configs(self) -> Sequence[outputs.GetRepositoryPubsubConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        ...
    


class AwaitableGetRepositoryResult(GetRepositoryResult):
    def __await__(self): # -> Generator[Never, Any, GetRepositoryResult]:
        ...
    


def get_repository(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRepositoryResult:
    
    ...

def get_repository_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRepositoryResult]:
    
    ...

