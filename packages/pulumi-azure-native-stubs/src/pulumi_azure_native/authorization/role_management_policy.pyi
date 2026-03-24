

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RoleManagementPolicyArgs', 'RoleManagementPolicy']
@pulumi.input_type
class RoleManagementPolicyArgs:
    def __init__(__self__, *, scope: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., is_organization_default: Optional[pulumi.Input[_builtins.bool]] = ..., role_management_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RoleManagementPolicyApprovalRuleArgs, RoleManagementPolicyAuthenticationContextRuleArgs, RoleManagementPolicyEnablementRuleArgs, RoleManagementPolicyExpirationRuleArgs, RoleManagementPolicyNotificationRuleArgs, RoleManagementPolicyPimOnlyModeRuleArgs]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOrganizationDefault")
    def is_organization_default(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_organization_default.setter
    def is_organization_default(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleManagementPolicyName")
    def role_management_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_management_policy_name.setter
    def role_management_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[RoleManagementPolicyApprovalRuleArgs, RoleManagementPolicyAuthenticationContextRuleArgs, RoleManagementPolicyEnablementRuleArgs, RoleManagementPolicyExpirationRuleArgs, RoleManagementPolicyNotificationRuleArgs, RoleManagementPolicyPimOnlyModeRuleArgs]]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RoleManagementPolicyApprovalRuleArgs, RoleManagementPolicyAuthenticationContextRuleArgs, RoleManagementPolicyEnablementRuleArgs, RoleManagementPolicyExpirationRuleArgs, RoleManagementPolicyNotificationRuleArgs, RoleManagementPolicyPimOnlyModeRuleArgs]]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:authorization:RoleManagementPolicy")
class RoleManagementPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., is_organization_default: Optional[pulumi.Input[_builtins.bool]] = ..., role_management_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[Union[RoleManagementPolicyApprovalRuleArgs, RoleManagementPolicyApprovalRuleArgsDict], Union[RoleManagementPolicyAuthenticationContextRuleArgs, RoleManagementPolicyAuthenticationContextRuleArgsDict], Union[RoleManagementPolicyEnablementRuleArgs, RoleManagementPolicyEnablementRuleArgsDict], Union[RoleManagementPolicyExpirationRuleArgs, RoleManagementPolicyExpirationRuleArgsDict], Union[RoleManagementPolicyNotificationRuleArgs, RoleManagementPolicyNotificationRuleArgsDict], Union[RoleManagementPolicyPimOnlyModeRuleArgs, RoleManagementPolicyPimOnlyModeRuleArgsDict]]]]]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RoleManagementPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> RoleManagementPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveRules")
    def effective_rules(self) -> pulumi.Output[Sequence[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOrganizationDefault")
    def is_organization_default(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output[outputs.PrincipalResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedDateTime")
    def last_modified_date_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyProperties")
    def policy_properties(self) -> pulumi.Output[outputs.PolicyPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


