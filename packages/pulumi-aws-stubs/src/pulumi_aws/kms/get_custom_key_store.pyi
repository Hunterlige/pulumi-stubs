

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCustomKeyStoreResult', 'AwaitableGetCustomKeyStoreResult', 'get_custom_key_store', 'get_custom_key_store_output']
@pulumi.output_type
class GetCustomKeyStoreResult:
    
    def __init__(__self__, cloud_hsm_cluster_id=..., connection_state=..., creation_date=..., custom_key_store_id=..., custom_key_store_name=..., id=..., region=..., trust_anchor_certificate=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudHsmClusterId")
    def cloud_hsm_cluster_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionState")
    def connection_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customKeyStoreId")
    def custom_key_store_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customKeyStoreName")
    def custom_key_store_name(self) -> _builtins.str:
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
    @pulumi.getter(name="trustAnchorCertificate")
    def trust_anchor_certificate(self) -> _builtins.str:
        
        ...
    


class AwaitableGetCustomKeyStoreResult(GetCustomKeyStoreResult):
    def __await__(self): # -> Generator[Never, Any, GetCustomKeyStoreResult]:
        ...
    


def get_custom_key_store(custom_key_store_id: Optional[_builtins.str] = ..., custom_key_store_name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCustomKeyStoreResult:
    
    ...

def get_custom_key_store_output(custom_key_store_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., custom_key_store_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCustomKeyStoreResult]:
    
    ...

