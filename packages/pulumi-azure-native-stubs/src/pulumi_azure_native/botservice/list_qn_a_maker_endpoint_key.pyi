

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListQnAMakerEndpointKeyResult', 'AwaitableListQnAMakerEndpointKeyResult', 'list_qn_a_maker_endpoint_key', 'list_qn_a_maker_endpoint_key_output']
@pulumi.output_type
class ListQnAMakerEndpointKeyResult:
    
    def __init__(__self__, installed_version=..., last_stable_version=..., primary_endpoint_key=..., secondary_endpoint_key=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="installedVersion")
    def installed_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastStableVersion")
    def last_stable_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryEndpointKey")
    def primary_endpoint_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryEndpointKey")
    def secondary_endpoint_key(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableListQnAMakerEndpointKeyResult(ListQnAMakerEndpointKeyResult):
    def __await__(self): # -> Generator[Never, Any, ListQnAMakerEndpointKeyResult]:
        ...
    


def list_qn_a_maker_endpoint_key(authkey: Optional[_builtins.str] = ..., hostname: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListQnAMakerEndpointKeyResult:
    
    ...

def list_qn_a_maker_endpoint_key_output(authkey: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., hostname: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListQnAMakerEndpointKeyResult]:
    
    ...

