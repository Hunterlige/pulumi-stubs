

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetListenerResult', 'AwaitableGetListenerResult', 'get_listener', 'get_listener_output']
@pulumi.output_type
class GetListenerResult:
    
    def __init__(__self__, alpn_policy=..., arn=..., certificate_arn=..., default_actions=..., id=..., load_balancer_arn=..., mutual_authentications=..., port=..., protocol=..., region=..., ssl_policy=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alpnPolicy")
    def alpn_policy(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultActions")
    def default_actions(self) -> Sequence[outputs.GetListenerDefaultActionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerArn")
    def load_balancer_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mutualAuthentications")
    def mutual_authentications(self) -> Sequence[outputs.GetListenerMutualAuthenticationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetListenerResult(GetListenerResult):
    def __await__(self): # -> Generator[Never, Any, GetListenerResult]:
        ...
    


def get_listener(arn: Optional[_builtins.str] = ..., load_balancer_arn: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetListenerResult:
    
    ...

def get_listener_output(arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., load_balancer_arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., port: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetListenerResult]:
    
    ...

