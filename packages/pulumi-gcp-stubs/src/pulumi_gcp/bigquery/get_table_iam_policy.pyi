

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTableIamPolicyResult', 'AwaitableGetTableIamPolicyResult', 'get_table_iam_policy', 'get_table_iam_policy_output']
@pulumi.output_type
class GetTableIamPolicyResult:
    
    def __init__(__self__, dataset_id=..., etag=..., id=..., policy_data=..., project=..., table_id=...) -> None:
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
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> _builtins.str:
        ...
    


class AwaitableGetTableIamPolicyResult(GetTableIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetTableIamPolicyResult]:
        ...
    


def get_table_iam_policy(dataset_id: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., table_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTableIamPolicyResult:
    
    ...

def get_table_iam_policy_output(dataset_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., table_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTableIamPolicyResult]:
    
    ...

