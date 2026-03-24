

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAiFeatureGroupIamPolicyResult', 'AwaitableGetAiFeatureGroupIamPolicyResult', 'get_ai_feature_group_iam_policy', 'get_ai_feature_group_iam_policy_output']
@pulumi.output_type
class GetAiFeatureGroupIamPolicyResult:
    
    def __init__(__self__, etag=..., feature_group=..., id=..., policy_data=..., project=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureGroup")
    def feature_group(self) -> _builtins.str:
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
    


class AwaitableGetAiFeatureGroupIamPolicyResult(GetAiFeatureGroupIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetAiFeatureGroupIamPolicyResult]:
        ...
    


def get_ai_feature_group_iam_policy(feature_group: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAiFeatureGroupIamPolicyResult:
    
    ...

def get_ai_feature_group_iam_policy_output(feature_group: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAiFeatureGroupIamPolicyResult]:
    
    ...

