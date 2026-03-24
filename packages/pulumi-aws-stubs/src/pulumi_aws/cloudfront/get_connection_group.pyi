

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConnectionGroupResult', 'AwaitableGetConnectionGroupResult', 'get_connection_group', 'get_connection_group_output']
@pulumi.output_type
class GetConnectionGroupResult:
    
    def __init__(__self__, anycast_ip_list_id=..., arn=..., enabled=..., etag=..., id=..., ipv6_enabled=..., is_default=..., last_modified_time=..., name=..., routing_endpoint=..., status=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="anycastIpListId")
    def anycast_ip_list_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Enabled")
    def ipv6_enabled(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingEndpoint")
    def routing_endpoint(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetConnectionGroupResult(GetConnectionGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetConnectionGroupResult]:
        ...
    


def get_connection_group(id: Optional[_builtins.str] = ..., routing_endpoint: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConnectionGroupResult:
    
    ...

def get_connection_group_output(id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., routing_endpoint: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConnectionGroupResult]:
    
    ...

