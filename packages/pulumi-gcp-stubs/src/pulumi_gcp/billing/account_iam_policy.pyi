

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccountIamPolicyArgs', 'AccountIamPolicy']
@pulumi.input_type
class AccountIamPolicyArgs:
    def __init__(__self__, *, billing_account_id: pulumi.Input[_builtins.str], policy_data: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingAccountId")
    def billing_account_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @billing_account_id.setter
    def billing_account_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_data.setter
    def policy_data(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _AccountIamPolicyState:
    def __init__(__self__, *, billing_account_id: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., policy_data: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingAccountId")
    def billing_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @billing_account_id.setter
    def billing_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_data.setter
    def policy_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:billing/accountIamPolicy:AccountIamPolicy")
class AccountIamPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., billing_account_id: Optional[pulumi.Input[_builtins.str]] = ..., policy_data: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AccountIamPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., billing_account_id: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., policy_data: Optional[pulumi.Input[_builtins.str]] = ...) -> AccountIamPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingAccountId")
    def billing_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


