

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAiFeaturestoreEntitytypeIamPolicyResult', ..., 'get_ai_featurestore_entitytype_iam_policy', 'get_ai_featurestore_entitytype_iam_policy_output']
@pulumi.output_type
class GetAiFeaturestoreEntitytypeIamPolicyResult:
    
    def __init__(__self__, entitytype=..., etag=..., featurestore=..., id=..., policy_data=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def entitytype(self) -> _builtins.str:
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
    


class AwaitableGetAiFeaturestoreEntitytypeIamPolicyResult(GetAiFeaturestoreEntitytypeIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetAiFeaturestoreEntitytypeIamPolicyResult]:
        ...
    


def get_ai_featurestore_entitytype_iam_policy(entitytype: Optional[_builtins.str] = ..., featurestore: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAiFeaturestoreEntitytypeIamPolicyResult:
    
    ...

def get_ai_featurestore_entitytype_iam_policy_output(entitytype: Optional[pulumi.Input[_builtins.str]] = ..., featurestore: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAiFeaturestoreEntitytypeIamPolicyResult]:
    
    ...

