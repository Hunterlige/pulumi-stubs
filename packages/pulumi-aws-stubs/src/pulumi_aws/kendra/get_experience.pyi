

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetExperienceResult', 'AwaitableGetExperienceResult', 'get_experience', 'get_experience_output']
@pulumi.output_type
class GetExperienceResult:
    
    def __init__(__self__, arn=..., configurations=..., created_at=..., description=..., endpoints=..., error_message=..., experience_id=..., id=..., index_id=..., name=..., region=..., role_arn=..., status=..., updated_at=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Sequence[outputs.GetExperienceConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Sequence[outputs.GetExperienceEndpointResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="experienceId")
    def experience_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexId")
    def index_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str:
        
        ...
    


class AwaitableGetExperienceResult(GetExperienceResult):
    def __await__(self): # -> Generator[Never, Any, GetExperienceResult]:
        ...
    


def get_experience(experience_id: Optional[_builtins.str] = ..., index_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetExperienceResult:
    
    ...

def get_experience_output(experience_id: Optional[pulumi.Input[_builtins.str]] = ..., index_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetExperienceResult]:
    
    ...

