

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetImageIamPolicyResult', 'AwaitableGetImageIamPolicyResult', 'get_image_iam_policy', 'get_image_iam_policy_output']
@pulumi.output_type
class GetImageIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., image=..., policy_data=..., project=...) -> None:
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
    def image(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    


class AwaitableGetImageIamPolicyResult(GetImageIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetImageIamPolicyResult]:
        ...
    


def get_image_iam_policy(image: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetImageIamPolicyResult:
    
    ...

def get_image_iam_policy_output(image: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetImageIamPolicyResult]:
    
    ...

