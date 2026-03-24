

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSecretVersionResult', 'AwaitableGetSecretVersionResult', 'get_secret_version', 'get_secret_version_output']
@pulumi.output_type
class GetSecretVersionResult:
    
    def __init__(__self__, arn=..., created_date=..., id=..., region=..., secret_binary=..., secret_id=..., secret_string=..., version_id=..., version_stage=..., version_stages=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretBinary")
    def secret_binary(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretString")
    def secret_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionStage")
    def version_stage(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionStages")
    def version_stages(self) -> Sequence[_builtins.str]:
        ...
    


class AwaitableGetSecretVersionResult(GetSecretVersionResult):
    def __await__(self): # -> Generator[Never, Any, GetSecretVersionResult]:
        ...
    


def get_secret_version(region: Optional[_builtins.str] = ..., secret_id: Optional[_builtins.str] = ..., version_id: Optional[_builtins.str] = ..., version_stage: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSecretVersionResult:
    
    ...

def get_secret_version_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., secret_id: Optional[pulumi.Input[_builtins.str]] = ..., version_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., version_stage: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSecretVersionResult]:
    
    ...

