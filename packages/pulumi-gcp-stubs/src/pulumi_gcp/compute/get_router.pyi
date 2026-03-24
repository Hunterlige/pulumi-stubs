

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRouterResult', 'AwaitableGetRouterResult', 'get_router', 'get_router_output']
@pulumi.output_type
class GetRouterResult:
    
    def __init__(__self__, bgps=..., creation_timestamp=..., description=..., encrypted_interconnect_router=..., id=..., md5_authentication_keys=..., name=..., ncc_gateway=..., network=..., params=..., project=..., region=..., self_link=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bgps(self) -> Sequence[outputs.GetRouterBgpResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedInterconnectRouter")
    def encrypted_interconnect_router(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="md5AuthenticationKeys")
    def md5_authentication_keys(self) -> Sequence[outputs.GetRouterMd5AuthenticationKeyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nccGateway")
    def ncc_gateway(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Sequence[outputs.GetRouterParamResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        ...
    


class AwaitableGetRouterResult(GetRouterResult):
    def __await__(self): # -> Generator[Never, Any, GetRouterResult]:
        ...
    


def get_router(name: Optional[_builtins.str] = ..., network: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRouterResult:
    
    ...

def get_router_output(name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRouterResult]:
    
    ...

