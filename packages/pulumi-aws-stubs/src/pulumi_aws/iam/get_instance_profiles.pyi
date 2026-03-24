

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetInstanceProfilesResult', 'AwaitableGetInstanceProfilesResult', 'get_instance_profiles', 'get_instance_profiles_output']
@pulumi.output_type
class GetInstanceProfilesResult:
    
    def __init__(__self__, arns=..., id=..., names=..., paths=..., role_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> _builtins.str:
        ...
    


class AwaitableGetInstanceProfilesResult(GetInstanceProfilesResult):
    def __await__(self): # -> Generator[Never, Any, GetInstanceProfilesResult]:
        ...
    


def get_instance_profiles(role_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInstanceProfilesResult:
    
    ...

def get_instance_profiles_output(role_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInstanceProfilesResult]:
    
    ...

