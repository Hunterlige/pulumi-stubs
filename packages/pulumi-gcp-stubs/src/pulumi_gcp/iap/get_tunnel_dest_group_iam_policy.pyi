

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTunnelDestGroupIamPolicyResult', 'AwaitableGetTunnelDestGroupIamPolicyResult', 'get_tunnel_dest_group_iam_policy', 'get_tunnel_dest_group_iam_policy_output']
@pulumi.output_type
class GetTunnelDestGroupIamPolicyResult:
    
    def __init__(__self__, dest_group=..., etag=..., id=..., policy_data=..., project=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destGroup")
    def dest_group(self) -> _builtins.str:
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
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetTunnelDestGroupIamPolicyResult(GetTunnelDestGroupIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetTunnelDestGroupIamPolicyResult]:
        ...
    


def get_tunnel_dest_group_iam_policy(dest_group: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTunnelDestGroupIamPolicyResult:
    
    ...

def get_tunnel_dest_group_iam_policy_output(dest_group: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTunnelDestGroupIamPolicyResult]:
    
    ...

