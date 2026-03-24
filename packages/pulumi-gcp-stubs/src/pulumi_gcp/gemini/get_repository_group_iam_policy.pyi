

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRepositoryGroupIamPolicyResult', 'AwaitableGetRepositoryGroupIamPolicyResult', 'get_repository_group_iam_policy', 'get_repository_group_iam_policy_output']
@pulumi.output_type
class GetRepositoryGroupIamPolicyResult:
    
    def __init__(__self__, code_repository_index=..., etag=..., id=..., location=..., policy_data=..., project=..., repository_group_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeRepositoryIndex")
    def code_repository_index(self) -> _builtins.str:
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
    @pulumi.getter(name="repositoryGroupId")
    def repository_group_id(self) -> _builtins.str:
        ...
    


class AwaitableGetRepositoryGroupIamPolicyResult(GetRepositoryGroupIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetRepositoryGroupIamPolicyResult]:
        ...
    


def get_repository_group_iam_policy(code_repository_index: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., repository_group_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRepositoryGroupIamPolicyResult:
    
    ...

def get_repository_group_iam_policy_output(code_repository_index: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., repository_group_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRepositoryGroupIamPolicyResult]:
    
    ...

