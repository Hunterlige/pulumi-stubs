

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIcebergNamespaceIamPolicyResult', 'AwaitableGetIcebergNamespaceIamPolicyResult', 'get_iceberg_namespace_iam_policy', 'get_iceberg_namespace_iam_policy_output']
@pulumi.output_type
class GetIcebergNamespaceIamPolicyResult:
    
    def __init__(__self__, catalog=..., etag=..., id=..., namespace_id=..., policy_data=..., project=...) -> None:
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
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    


class AwaitableGetIcebergNamespaceIamPolicyResult(GetIcebergNamespaceIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetIcebergNamespaceIamPolicyResult]:
        ...
    


def get_iceberg_namespace_iam_policy(catalog: Optional[_builtins.str] = ..., namespace_id: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIcebergNamespaceIamPolicyResult:
    
    ...

def get_iceberg_namespace_iam_policy_output(catalog: Optional[pulumi.Input[_builtins.str]] = ..., namespace_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIcebergNamespaceIamPolicyResult]:
    
    ...

