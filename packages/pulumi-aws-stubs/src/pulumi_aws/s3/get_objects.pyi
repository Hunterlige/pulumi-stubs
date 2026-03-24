

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetObjectsResult', 'AwaitableGetObjectsResult', 'get_objects', 'get_objects_output']
@pulumi.output_type
class GetObjectsResult:
    
    def __init__(__self__, bucket=..., common_prefixes=..., delimiter=..., encoding_type=..., fetch_owner=..., id=..., keys=..., max_keys=..., owners=..., prefix=..., region=..., request_charged=..., request_payer=..., start_after=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonPrefixes")
    def common_prefixes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encodingType")
    def encoding_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fetchOwner")
    def fetch_owner(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxKeys")
    def max_keys(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def owners(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestCharged")
    def request_charged(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestPayer")
    def request_payer(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAfter")
    def start_after(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetObjectsResult(GetObjectsResult):
    def __await__(self): # -> Generator[Never, Any, GetObjectsResult]:
        ...
    


def get_objects(bucket: Optional[_builtins.str] = ..., delimiter: Optional[_builtins.str] = ..., encoding_type: Optional[_builtins.str] = ..., fetch_owner: Optional[_builtins.bool] = ..., max_keys: Optional[_builtins.int] = ..., prefix: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., request_payer: Optional[_builtins.str] = ..., start_after: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetObjectsResult:
    
    ...

def get_objects_output(bucket: Optional[pulumi.Input[_builtins.str]] = ..., delimiter: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., encoding_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., fetch_owner: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., max_keys: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., request_payer: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., start_after: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetObjectsResult]:
    
    ...

