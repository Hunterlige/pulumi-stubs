

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIAMPolicyResult', 'AwaitableGetIAMPolicyResult', 'get_iam_policy', 'get_iam_policy_output']
@pulumi.output_type
class GetIAMPolicyResult:
    
    def __init__(__self__, audit_configs=..., bindings=..., id=..., policy_data=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="auditConfigs")
    def audit_configs(self) -> Optional[Sequence[outputs.GetIAMPolicyAuditConfigResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bindings(self) -> Optional[Sequence[outputs.GetIAMPolicyBindingResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    


class AwaitableGetIAMPolicyResult(GetIAMPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetIAMPolicyResult]:
        ...
    


def get_iam_policy(audit_configs: Optional[Sequence[Union[GetIAMPolicyAuditConfigArgs, GetIAMPolicyAuditConfigArgsDict]]] = ..., bindings: Optional[Sequence[Union[GetIAMPolicyBindingArgs, GetIAMPolicyBindingArgsDict]]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIAMPolicyResult:
    
    ...

def get_iam_policy_output(audit_configs: Optional[pulumi.Input[Optional[Sequence[Union[GetIAMPolicyAuditConfigArgs, GetIAMPolicyAuditConfigArgsDict]]]]] = ..., bindings: Optional[pulumi.Input[Optional[Sequence[Union[GetIAMPolicyBindingArgs, GetIAMPolicyBindingArgsDict]]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIAMPolicyResult]:
    
    ...

