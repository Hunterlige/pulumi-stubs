

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProxyResult', 'AwaitableGetProxyResult', 'get_proxy', 'get_proxy_output']
@pulumi.output_type
class GetProxyResult:
    
    def __init__(__self__, arn=..., auths=..., debug_logging=..., default_auth_scheme=..., endpoint=..., endpoint_network_type=..., engine_family=..., id=..., idle_client_timeout=..., name=..., region=..., require_tls=..., role_arn=..., target_connection_network_type=..., vpc_id=..., vpc_security_group_ids=..., vpc_subnet_ids=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def auths(self) -> Sequence[outputs.GetProxyAuthResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="debugLogging")
    def debug_logging(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAuthScheme")
    def default_auth_scheme(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointNetworkType")
    def endpoint_network_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineFamily")
    def engine_family(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleClientTimeout")
    def idle_client_timeout(self) -> _builtins.int:
        
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
    @pulumi.getter(name="requireTls")
    def require_tls(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionNetworkType")
    def target_connection_network_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSubnetIds")
    def vpc_subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetProxyResult(GetProxyResult):
    def __await__(self): # -> Generator[Never, Any, GetProxyResult]:
        ...
    


def get_proxy(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProxyResult:
    
    ...

def get_proxy_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProxyResult]:
    
    ...

