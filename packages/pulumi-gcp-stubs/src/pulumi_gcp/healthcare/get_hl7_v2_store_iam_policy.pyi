

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetHl7V2StoreIamPolicyResult', 'AwaitableGetHl7V2StoreIamPolicyResult', 'get_hl7_v2_store_iam_policy', 'get_hl7_v2_store_iam_policy_output']
@pulumi.output_type
class GetHl7V2StoreIamPolicyResult:
    
    def __init__(__self__, etag=..., hl7_v2_store_id=..., id=..., policy_data=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hl7V2StoreId")
    def hl7_v2_store_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    


class AwaitableGetHl7V2StoreIamPolicyResult(GetHl7V2StoreIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetHl7V2StoreIamPolicyResult]:
        ...
    


def get_hl7_v2_store_iam_policy(hl7_v2_store_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetHl7V2StoreIamPolicyResult:
    
    ...

def get_hl7_v2_store_iam_policy_output(hl7_v2_store_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetHl7V2StoreIamPolicyResult]:
    
    ...

