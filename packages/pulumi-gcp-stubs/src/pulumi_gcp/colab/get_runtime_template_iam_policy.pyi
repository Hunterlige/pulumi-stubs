

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRuntimeTemplateIamPolicyResult', 'AwaitableGetRuntimeTemplateIamPolicyResult', 'get_runtime_template_iam_policy', 'get_runtime_template_iam_policy_output']
@pulumi.output_type
class GetRuntimeTemplateIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., location=..., policy_data=..., project=..., runtime_template=...) -> None:
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
    
    @_builtins.property
    @pulumi.getter(name="runtimeTemplate")
    def runtime_template(self) -> _builtins.str:
        ...
    


class AwaitableGetRuntimeTemplateIamPolicyResult(GetRuntimeTemplateIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetRuntimeTemplateIamPolicyResult]:
        ...
    


def get_runtime_template_iam_policy(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., runtime_template: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRuntimeTemplateIamPolicyResult:
    
    ...

def get_runtime_template_iam_policy_output(location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., runtime_template: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRuntimeTemplateIamPolicyResult]:
    
    ...

