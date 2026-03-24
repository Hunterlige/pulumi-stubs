

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIcebergTableIamPolicyResult', 'AwaitableGetIcebergTableIamPolicyResult', 'get_iceberg_table_iam_policy', 'get_iceberg_table_iam_policy_output']
@pulumi.output_type
class GetIcebergTableIamPolicyResult:
    
    def __init__(__self__, catalog=..., etag=..., id=..., name=..., namespace=..., policy_data=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def catalog(self) -> _builtins.str:
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
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    


class AwaitableGetIcebergTableIamPolicyResult(GetIcebergTableIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetIcebergTableIamPolicyResult]:
        ...
    


def get_iceberg_table_iam_policy(catalog: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., namespace: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIcebergTableIamPolicyResult:
    
    ...

def get_iceberg_table_iam_policy_output(catalog: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., namespace: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIcebergTableIamPolicyResult]:
    
    ...

