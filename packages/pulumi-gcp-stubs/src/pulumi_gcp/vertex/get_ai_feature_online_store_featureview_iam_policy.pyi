

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAiFeatureOnlineStoreFeatureviewIamPolicyResult', ..., 'get_ai_feature_online_store_featureview_iam_policy', ...]
@pulumi.output_type
class GetAiFeatureOnlineStoreFeatureviewIamPolicyResult:
    
    def __init__(__self__, etag=..., feature_online_store=..., feature_view=..., id=..., policy_data=..., project=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureOnlineStore")
    def feature_online_store(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureView")
    def feature_view(self) -> _builtins.str:
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
    


class AwaitableGetAiFeatureOnlineStoreFeatureviewIamPolicyResult(GetAiFeatureOnlineStoreFeatureviewIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetAiFeatureOnlineStoreFeatureviewIamPolicyResult]:
        ...
    


def get_ai_feature_online_store_featureview_iam_policy(feature_online_store: Optional[_builtins.str] = ..., feature_view: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAiFeatureOnlineStoreFeatureviewIamPolicyResult:
    
    ...

def get_ai_feature_online_store_featureview_iam_policy_output(feature_online_store: Optional[pulumi.Input[_builtins.str]] = ..., feature_view: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAiFeatureOnlineStoreFeatureviewIamPolicyResult]:
    
    ...

