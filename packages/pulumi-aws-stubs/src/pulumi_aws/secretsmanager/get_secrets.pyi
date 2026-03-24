

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSecretsResult', 'AwaitableGetSecretsResult', 'get_secrets', 'get_secrets_output']
@pulumi.output_type
class GetSecretsResult:
    
    def __init__(__self__, arns=..., filters=..., id=..., names=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetSecretsFilterResult]]:
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
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetSecretsResult(GetSecretsResult):
    def __await__(self): # -> Generator[Never, Any, GetSecretsResult]:
        ...
    


def get_secrets(filters: Optional[Sequence[Union[GetSecretsFilterArgs, GetSecretsFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSecretsResult:
    
    ...

def get_secrets_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetSecretsFilterArgs, GetSecretsFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSecretsResult]:
    
    ...

