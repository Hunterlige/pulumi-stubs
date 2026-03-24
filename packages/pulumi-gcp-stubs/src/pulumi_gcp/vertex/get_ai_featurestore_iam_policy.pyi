

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAiFeaturestoreIamPolicyResult', 'AwaitableGetAiFeaturestoreIamPolicyResult', 'get_ai_featurestore_iam_policy', 'get_ai_featurestore_iam_policy_output']
@pulumi.output_type
class GetAiFeaturestoreIamPolicyResult:
    
    def __init__(__self__, etag=..., featurestore=..., id=..., policy_data=..., project=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def featurestore(self) -> _builtins.str:
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
    


class AwaitableGetAiFeaturestoreIamPolicyResult(GetAiFeaturestoreIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetAiFeaturestoreIamPolicyResult]:
        ...
    


def get_ai_featurestore_iam_policy(featurestore: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAiFeaturestoreIamPolicyResult:
    
    ...

def get_ai_featurestore_iam_policy_output(featurestore: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAiFeaturestoreIamPolicyResult]:
    
    ...

