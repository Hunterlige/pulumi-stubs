

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMetastoreFederationIamPolicyResult', 'AwaitableGetMetastoreFederationIamPolicyResult', 'get_metastore_federation_iam_policy', 'get_metastore_federation_iam_policy_output']
@pulumi.output_type
class GetMetastoreFederationIamPolicyResult:
    
    def __init__(__self__, etag=..., federation_id=..., id=..., location=..., policy_data=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="federationId")
    def federation_id(self) -> _builtins.str:
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
    


class AwaitableGetMetastoreFederationIamPolicyResult(GetMetastoreFederationIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetMetastoreFederationIamPolicyResult]:
        ...
    


def get_metastore_federation_iam_policy(federation_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMetastoreFederationIamPolicyResult:
    
    ...

def get_metastore_federation_iam_policy_output(federation_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMetastoreFederationIamPolicyResult]:
    
    ...

