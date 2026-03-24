

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTunnelIamPolicyResult', 'AwaitableGetTunnelIamPolicyResult', 'get_tunnel_iam_policy', 'get_tunnel_iam_policy_output']
@pulumi.output_type
class GetTunnelIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., policy_data=..., project=...) -> None:
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
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    


class AwaitableGetTunnelIamPolicyResult(GetTunnelIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetTunnelIamPolicyResult]:
        ...
    


def get_tunnel_iam_policy(project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTunnelIamPolicyResult:
    
    ...

def get_tunnel_iam_policy_output(project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTunnelIamPolicyResult]:
    
    ...

