

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServerResult', 'AwaitableGetServerResult', 'get_server', 'get_server_output']
@pulumi.output_type
class GetServerResult:
    
    def __init__(__self__, arn=..., certificate=..., domain=..., endpoint=..., endpoint_type=..., id=..., identity_provider_type=..., invocation_role=..., logging_role=..., protocols=..., region=..., security_policy_name=..., server_id=..., structured_log_destinations=..., tags=..., url=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityProviderType")
    def identity_provider_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invocationRole")
    def invocation_role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingRole")
    def logging_role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityPolicyName")
    def security_policy_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverId")
    def server_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="structuredLogDestinations")
    def structured_log_destinations(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        
        ...
    


class AwaitableGetServerResult(GetServerResult):
    def __await__(self): # -> Generator[Never, Any, GetServerResult]:
        ...
    


def get_server(region: Optional[_builtins.str] = ..., server_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServerResult:
    
    ...

def get_server_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., server_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServerResult]:
    
    ...

