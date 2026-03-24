

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPartnerConfigurationResult', 'AwaitableGetPartnerConfigurationResult', 'get_partner_configuration', 'get_partner_configuration_output']
@pulumi.output_type
class GetPartnerConfigurationResult:
    
    def __init__(__self__, azure_api_version=..., id=..., location=..., name=..., partner_authorization=..., provisioning_state=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
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
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerAuthorization")
    def partner_authorization(self) -> Optional[outputs.PartnerAuthorizationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetPartnerConfigurationResult(GetPartnerConfigurationResult):
    def __await__(self): # -> Generator[Never, Any, GetPartnerConfigurationResult]:
        ...
    


def get_partner_configuration(resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPartnerConfigurationResult:
    
    ...

def get_partner_configuration_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPartnerConfigurationResult]:
    
    ...

