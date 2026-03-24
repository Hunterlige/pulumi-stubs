

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRegionalSecretIamPolicyResult', 'AwaitableGetRegionalSecretIamPolicyResult', 'get_regional_secret_iam_policy', 'get_regional_secret_iam_policy_output']
@pulumi.output_type
class GetRegionalSecretIamPolicyResult:
    
    def __init__(__self__, etag=..., id=..., location=..., policy_data=..., project=..., secret_id=...) -> None:
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
    @pulumi.getter(name="secretId")
    def secret_id(self) -> _builtins.str:
        ...
    


class AwaitableGetRegionalSecretIamPolicyResult(GetRegionalSecretIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetRegionalSecretIamPolicyResult]:
        ...
    


def get_regional_secret_iam_policy(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., secret_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRegionalSecretIamPolicyResult:
    
    ...

def get_regional_secret_iam_policy_output(location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., secret_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRegionalSecretIamPolicyResult]:
    
    ...

