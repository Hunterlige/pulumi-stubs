

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMetastoreTableIamPolicyResult', 'AwaitableGetMetastoreTableIamPolicyResult', 'get_metastore_table_iam_policy', 'get_metastore_table_iam_policy_output']
@pulumi.output_type
class GetMetastoreTableIamPolicyResult:
    
    def __init__(__self__, database_id=..., etag=..., id=..., location=..., policy_data=..., project=..., service_id=..., table=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> _builtins.str:
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
    @pulumi.getter(name="serviceId")
    def service_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str:
        ...
    


class AwaitableGetMetastoreTableIamPolicyResult(GetMetastoreTableIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetMetastoreTableIamPolicyResult]:
        ...
    


def get_metastore_table_iam_policy(database_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., service_id: Optional[_builtins.str] = ..., table: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMetastoreTableIamPolicyResult:
    
    ...

def get_metastore_table_iam_policy_output(database_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., service_id: Optional[pulumi.Input[_builtins.str]] = ..., table: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMetastoreTableIamPolicyResult]:
    
    ...

