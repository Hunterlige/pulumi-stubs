

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSecretVersionsResult', 'AwaitableGetSecretVersionsResult', 'get_secret_versions', 'get_secret_versions_output']
@pulumi.output_type
class GetSecretVersionsResult:
    
    def __init__(__self__, arn=..., id=..., include_deprecated=..., name=..., region=..., secret_id=..., versions=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeDeprecated")
    def include_deprecated(self) -> Optional[_builtins.bool]:
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
    @pulumi.getter(name="secretId")
    def secret_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Sequence[outputs.GetSecretVersionsVersionResult]:
        
        ...
    


class AwaitableGetSecretVersionsResult(GetSecretVersionsResult):
    def __await__(self): # -> Generator[Never, Any, GetSecretVersionsResult]:
        ...
    


def get_secret_versions(include_deprecated: Optional[_builtins.bool] = ..., region: Optional[_builtins.str] = ..., secret_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSecretVersionsResult:
    
    ...

def get_secret_versions_output(include_deprecated: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., secret_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSecretVersionsResult]:
    
    ...

