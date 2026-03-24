

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIntegrationAccountPartnerResult', 'AwaitableGetIntegrationAccountPartnerResult', 'get_integration_account_partner', 'get_integration_account_partner_output']
@pulumi.output_type
class GetIntegrationAccountPartnerResult:
    
    def __init__(__self__, azure_api_version=..., changed_time=..., content=..., created_time=..., id=..., location=..., metadata=..., name=..., partner_type=..., tags=..., type=...) -> None:
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
    def content(self) -> outputs.PartnerContentResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str:
        
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
    @pulumi.getter(name="partnerType")
    def partner_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetIntegrationAccountPartnerResult(GetIntegrationAccountPartnerResult):
    def __await__(self): # -> Generator[Never, Any, GetIntegrationAccountPartnerResult]:
        ...
    


def get_integration_account_partner(integration_account_name: Optional[_builtins.str] = ..., partner_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIntegrationAccountPartnerResult:
    
    ...

def get_integration_account_partner_output(integration_account_name: Optional[pulumi.Input[_builtins.str]] = ..., partner_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIntegrationAccountPartnerResult]:
    
    ...

