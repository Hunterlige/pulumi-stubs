

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRecoveryPointAccessTokenResult', 'AwaitableGetRecoveryPointAccessTokenResult', 'get_recovery_point_access_token', 'get_recovery_point_access_token_output']
@pulumi.output_type
class GetRecoveryPointAccessTokenResult:
    def __init__(__self__, e_tag=..., id=..., location=..., name=..., properties=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.WorkloadCrrAccessTokenResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetRecoveryPointAccessTokenResult(GetRecoveryPointAccessTokenResult):
    def __await__(self): # -> Generator[Never, Any, GetRecoveryPointAccessTokenResult]:
        ...
    


def get_recovery_point_access_token(container_name: Optional[_builtins.str] = ..., e_tag: Optional[_builtins.str] = ..., fabric_name: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., properties: Optional[Union[AADProperties, AADPropertiesDict]] = ..., protected_item_name: Optional[_builtins.str] = ..., recovery_point_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., vault_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRecoveryPointAccessTokenResult:
    
    ...

def get_recovery_point_access_token_output(container_name: Optional[pulumi.Input[_builtins.str]] = ..., e_tag: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., fabric_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., properties: Optional[pulumi.Input[Optional[Union[AADProperties, AADPropertiesDict]]]] = ..., protected_item_name: Optional[pulumi.Input[_builtins.str]] = ..., recovery_point_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., vault_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRecoveryPointAccessTokenResult]:
    
    ...

