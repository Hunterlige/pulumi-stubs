

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOrganizationPolicyResult', 'AwaitableGetOrganizationPolicyResult', 'get_organization_policy', 'get_organization_policy_output']
@pulumi.output_type
class GetOrganizationPolicyResult:
    
    def __init__(__self__, boolean_policies=..., constraint=..., etag=..., folder=..., id=..., list_policies=..., restore_policies=..., update_time=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanPolicies")
    def boolean_policies(self) -> Sequence[outputs.GetOrganizationPolicyBooleanPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def constraint(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listPolicies")
    def list_policies(self) -> Sequence[outputs.GetOrganizationPolicyListPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePolicies")
    def restore_policies(self) -> Sequence[outputs.GetOrganizationPolicyRestorePolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.int:
        ...
    


class AwaitableGetOrganizationPolicyResult(GetOrganizationPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetOrganizationPolicyResult]:
        ...
    


def get_organization_policy(constraint: Optional[_builtins.str] = ..., folder: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOrganizationPolicyResult:
    
    ...

def get_organization_policy_output(constraint: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOrganizationPolicyResult]:
    
    ...

