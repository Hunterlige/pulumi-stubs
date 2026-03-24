

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAiEndpointIamPolicyResult', 'AwaitableGetAiEndpointIamPolicyResult', 'get_ai_endpoint_iam_policy', 'get_ai_endpoint_iam_policy_output']
@pulumi.output_type
class GetAiEndpointIamPolicyResult:
    
    def __init__(__self__, endpoint=..., etag=..., id=..., location=..., policy_data=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
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
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    


class AwaitableGetAiEndpointIamPolicyResult(GetAiEndpointIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetAiEndpointIamPolicyResult]:
        ...
    


def get_ai_endpoint_iam_policy(endpoint: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAiEndpointIamPolicyResult:
    
    ...

def get_ai_endpoint_iam_policy_output(endpoint: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAiEndpointIamPolicyResult]:
    
    ...

