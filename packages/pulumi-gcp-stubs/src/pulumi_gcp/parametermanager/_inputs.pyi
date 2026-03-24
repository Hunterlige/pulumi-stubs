

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ParameterPolicyMemberArgs', 'ParameterPolicyMemberArgsDict', 'RegionalParameterPolicyMemberArgs', 'RegionalParameterPolicyMemberArgsDict']
class ParameterPolicyMemberArgsDict(TypedDict):
    iam_policy_name_principal: NotRequired[pulumi.Input[_builtins.str]]
    iam_policy_uid_principal: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ParameterPolicyMemberArgs:
    def __init__(__self__, *, iam_policy_name_principal: Optional[pulumi.Input[_builtins.str]] = ..., iam_policy_uid_principal: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamPolicyNamePrincipal")
    def iam_policy_name_principal(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_policy_name_principal.setter
    def iam_policy_name_principal(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamPolicyUidPrincipal")
    def iam_policy_uid_principal(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_policy_uid_principal.setter
    def iam_policy_uid_principal(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RegionalParameterPolicyMemberArgsDict(TypedDict):
    iam_policy_name_principal: NotRequired[pulumi.Input[_builtins.str]]
    iam_policy_uid_principal: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegionalParameterPolicyMemberArgs:
    def __init__(__self__, *, iam_policy_name_principal: Optional[pulumi.Input[_builtins.str]] = ..., iam_policy_uid_principal: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamPolicyNamePrincipal")
    def iam_policy_name_principal(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_policy_name_principal.setter
    def iam_policy_name_principal(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamPolicyUidPrincipal")
    def iam_policy_uid_principal(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_policy_uid_principal.setter
    def iam_policy_uid_principal(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


