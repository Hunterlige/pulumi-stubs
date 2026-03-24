

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebBackendServiceIamPolicyResult', 'AwaitableGetWebBackendServiceIamPolicyResult', 'get_web_backend_service_iam_policy', 'get_web_backend_service_iam_policy_output']
@pulumi.output_type
class GetWebBackendServiceIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., policy_data=..., project=..., web_backend_service=...) -> None:
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
    @pulumi.getter(name="webBackendService")
    def web_backend_service(self) -> _builtins.str:
        ...
    


class AwaitableGetWebBackendServiceIamPolicyResult(GetWebBackendServiceIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetWebBackendServiceIamPolicyResult]:
        ...
    


def get_web_backend_service_iam_policy(project: Optional[_builtins.str] = ..., web_backend_service: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebBackendServiceIamPolicyResult:
    
    ...

def get_web_backend_service_iam_policy_output(project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., web_backend_service: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebBackendServiceIamPolicyResult]:
    
    ...

