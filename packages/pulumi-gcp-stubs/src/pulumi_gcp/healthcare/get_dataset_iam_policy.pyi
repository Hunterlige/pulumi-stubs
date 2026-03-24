

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDatasetIamPolicyResult', 'AwaitableGetDatasetIamPolicyResult', 'get_dataset_iam_policy', 'get_dataset_iam_policy_output']
@pulumi.output_type
class GetDatasetIamPolicyResult:
    
    def __init__(__self__, dataset_id=..., etag=..., id=..., policy_data=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str:
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
    


class AwaitableGetDatasetIamPolicyResult(GetDatasetIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetDatasetIamPolicyResult]:
        ...
    


def get_dataset_iam_policy(dataset_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDatasetIamPolicyResult:
    
    ...

def get_dataset_iam_policy_output(dataset_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDatasetIamPolicyResult]:
    
    ...

