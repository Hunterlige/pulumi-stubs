

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['OrganizationArgs', 'Organization']
@pulumi.input_type
class OrganizationArgs:
    def __init__(__self__, *, aws_service_access_principals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enabled_policy_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., feature_set: Optional[pulumi.Input[_builtins.str]] = ..., return_organization_only: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsServiceAccessPrincipals")
    def aws_service_access_principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @aws_service_access_principals.setter
    def aws_service_access_principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledPolicyTypes")
    def enabled_policy_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @enabled_policy_types.setter
    def enabled_policy_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureSet")
    def feature_set(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @feature_set.setter
    def feature_set(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnOrganizationOnly")
    def return_organization_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @return_organization_only.setter
    def return_organization_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _OrganizationState:
    def __init__(__self__, *, accounts: Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationAccountArgs]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., aws_service_access_principals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enabled_policy_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., feature_set: Optional[pulumi.Input[_builtins.str]] = ..., master_account_arn: Optional[pulumi.Input[_builtins.str]] = ..., master_account_email: Optional[pulumi.Input[_builtins.str]] = ..., master_account_id: Optional[pulumi.Input[_builtins.str]] = ..., master_account_name: Optional[pulumi.Input[_builtins.str]] = ..., non_master_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationNonMasterAccountArgs]]]] = ..., return_organization_only: Optional[pulumi.Input[_builtins.bool]] = ..., roots: Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationRootArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationAccountArgs]]]]:
        
        ...
    
    @accounts.setter
    def accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationAccountArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsServiceAccessPrincipals")
    def aws_service_access_principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @aws_service_access_principals.setter
    def aws_service_access_principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledPolicyTypes")
    def enabled_policy_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @enabled_policy_types.setter
    def enabled_policy_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureSet")
    def feature_set(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @feature_set.setter
    def feature_set(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAccountArn")
    def master_account_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_account_arn.setter
    def master_account_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAccountEmail")
    def master_account_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_account_email.setter
    def master_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAccountId")
    def master_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_account_id.setter
    def master_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAccountName")
    def master_account_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_account_name.setter
    def master_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonMasterAccounts")
    def non_master_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationNonMasterAccountArgs]]]]:
        
        ...
    
    @non_master_accounts.setter
    def non_master_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationNonMasterAccountArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnOrganizationOnly")
    def return_organization_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @return_organization_only.setter
    def return_organization_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def roots(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationRootArgs]]]]:
        
        ...
    
    @roots.setter
    def roots(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationRootArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:organizations/organization:Organization")
class Organization(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aws_service_access_principals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enabled_policy_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., feature_set: Optional[pulumi.Input[_builtins.str]] = ..., return_organization_only: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[OrganizationArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., accounts: Optional[pulumi.Input[Sequence[pulumi.Input[Union[OrganizationAccountArgs, OrganizationAccountArgsDict]]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., aws_service_access_principals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enabled_policy_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., feature_set: Optional[pulumi.Input[_builtins.str]] = ..., master_account_arn: Optional[pulumi.Input[_builtins.str]] = ..., master_account_email: Optional[pulumi.Input[_builtins.str]] = ..., master_account_id: Optional[pulumi.Input[_builtins.str]] = ..., master_account_name: Optional[pulumi.Input[_builtins.str]] = ..., non_master_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[Union[OrganizationNonMasterAccountArgs, OrganizationNonMasterAccountArgsDict]]]]] = ..., return_organization_only: Optional[pulumi.Input[_builtins.bool]] = ..., roots: Optional[pulumi.Input[Sequence[pulumi.Input[Union[OrganizationRootArgs, OrganizationRootArgsDict]]]]] = ...) -> Organization:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> pulumi.Output[Sequence[outputs.OrganizationAccount]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsServiceAccessPrincipals")
    def aws_service_access_principals(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledPolicyTypes")
    def enabled_policy_types(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureSet")
    def feature_set(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAccountArn")
    def master_account_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAccountEmail")
    def master_account_email(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAccountId")
    def master_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAccountName")
    def master_account_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonMasterAccounts")
    def non_master_accounts(self) -> pulumi.Output[Sequence[outputs.OrganizationNonMasterAccount]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnOrganizationOnly")
    def return_organization_only(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def roots(self) -> pulumi.Output[Sequence[outputs.OrganizationRoot]]:
        
        ...
    


