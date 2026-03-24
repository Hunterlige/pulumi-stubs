

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIntegrationAccountAgreementResult', 'AwaitableGetIntegrationAccountAgreementResult', 'get_integration_account_agreement', 'get_integration_account_agreement_output']
@pulumi.output_type
class GetIntegrationAccountAgreementResult:
    
    def __init__(__self__, agreement_type=..., azure_api_version=..., changed_time=..., content=..., created_time=..., guest_identity=..., guest_partner=..., host_identity=..., host_partner=..., id=..., location=..., metadata=..., name=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agreementType")
    def agreement_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> outputs.AgreementContentResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestIdentity")
    def guest_identity(self) -> outputs.BusinessIdentityResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestPartner")
    def guest_partner(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostIdentity")
    def host_identity(self) -> outputs.BusinessIdentityResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostPartner")
    def host_partner(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetIntegrationAccountAgreementResult(GetIntegrationAccountAgreementResult):
    def __await__(self): # -> Generator[Never, Any, GetIntegrationAccountAgreementResult]:
        ...
    


def get_integration_account_agreement(agreement_name: Optional[_builtins.str] = ..., integration_account_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIntegrationAccountAgreementResult:
    
    ...

def get_integration_account_agreement_output(agreement_name: Optional[pulumi.Input[_builtins.str]] = ..., integration_account_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIntegrationAccountAgreementResult]:
    
    ...

