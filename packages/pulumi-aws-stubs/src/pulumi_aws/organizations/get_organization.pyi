

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOrganizationResult', 'AwaitableGetOrganizationResult', 'get_organization', 'get_organization_output']
@pulumi.output_type
class GetOrganizationResult:
    
    def __init__(__self__, accounts=..., arn=..., aws_service_access_principals=..., enabled_policy_types=..., feature_set=..., id=..., master_account_arn=..., master_account_email=..., master_account_id=..., master_account_name=..., non_master_accounts=..., return_organization_only=..., roots=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Sequence[outputs.GetOrganizationAccountResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsServiceAccessPrincipals")
    def aws_service_access_principals(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledPolicyTypes")
    def enabled_policy_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureSet")
    def feature_set(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAccountArn")
    def master_account_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAccountEmail")
    def master_account_email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAccountId")
    def master_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAccountName")
    def master_account_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonMasterAccounts")
    def non_master_accounts(self) -> Sequence[outputs.GetOrganizationNonMasterAccountResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnOrganizationOnly")
    def return_organization_only(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def roots(self) -> Sequence[outputs.GetOrganizationRootResult]:
        
        ...
    


class AwaitableGetOrganizationResult(GetOrganizationResult):
    def __await__(self): # -> Generator[Never, Any, GetOrganizationResult]:
        ...
    


def get_organization(return_organization_only: Optional[_builtins.bool] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOrganizationResult:
    
    ...

def get_organization_output(return_organization_only: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOrganizationResult]:
    
    ...

