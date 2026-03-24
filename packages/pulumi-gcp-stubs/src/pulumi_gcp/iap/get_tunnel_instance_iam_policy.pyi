

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTunnelInstanceIamPolicyResult', 'AwaitableGetTunnelInstanceIamPolicyResult', 'get_tunnel_instance_iam_policy', 'get_tunnel_instance_iam_policy_output']
@pulumi.output_type
class GetTunnelInstanceIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., instance=..., policy_data=..., project=..., zone=...) -> None:
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
    @pulumi.getter
    def instance(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        ...
    


class AwaitableGetTunnelInstanceIamPolicyResult(GetTunnelInstanceIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetTunnelInstanceIamPolicyResult]:
        ...
    


def get_tunnel_instance_iam_policy(instance: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., zone: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTunnelInstanceIamPolicyResult:
    
    ...

def get_tunnel_instance_iam_policy_output(instance: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTunnelInstanceIamPolicyResult]:
    
    ...

