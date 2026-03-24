

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetKeyPairResult', 'AwaitableGetKeyPairResult', 'get_key_pair', 'get_key_pair_output']
@pulumi.output_type
class GetKeyPairResult:
    
    def __init__(__self__, arn=..., create_time=..., filters=..., fingerprint=..., id=..., include_public_key=..., key_name=..., key_pair_id=..., key_type=..., public_key=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetKeyPairFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includePublicKey")
    def include_public_key(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPairId")
    def key_pair_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetKeyPairResult(GetKeyPairResult):
    def __await__(self): # -> Generator[Never, Any, GetKeyPairResult]:
        ...
    


def get_key_pair(filters: Optional[Sequence[Union[GetKeyPairFilterArgs, GetKeyPairFilterArgsDict]]] = ..., include_public_key: Optional[_builtins.bool] = ..., key_name: Optional[_builtins.str] = ..., key_pair_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetKeyPairResult:
    
    ...

def get_key_pair_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetKeyPairFilterArgs, GetKeyPairFilterArgsDict]]]]] = ..., include_public_key: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., key_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., key_pair_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetKeyPairResult]:
    
    ...

