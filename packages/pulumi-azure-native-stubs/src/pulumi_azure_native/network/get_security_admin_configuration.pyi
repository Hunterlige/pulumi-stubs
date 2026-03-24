

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSecurityAdminConfigurationResult', 'AwaitableGetSecurityAdminConfigurationResult', 'get_security_admin_configuration', 'get_security_admin_configuration_output']
@pulumi.output_type
class GetSecurityAdminConfigurationResult:
    
    def __init__(__self__, apply_on_network_intent_policy_based_services=..., azure_api_version=..., description=..., etag=..., id=..., name=..., network_group_address_space_aggregation_option=..., provisioning_state=..., resource_guid=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyOnNetworkIntentPolicyBasedServices")
    def apply_on_network_intent_policy_based_services(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkGroupAddressSpaceAggregationOption")
    def network_group_address_space_aggregation_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSecurityAdminConfigurationResult(GetSecurityAdminConfigurationResult):
    def __await__(self): # -> Generator[Never, Any, GetSecurityAdminConfigurationResult]:
        ...
    


def get_security_admin_configuration(configuration_name: Optional[_builtins.str] = ..., network_manager_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSecurityAdminConfigurationResult:
    
    ...

def get_security_admin_configuration_output(configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., network_manager_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSecurityAdminConfigurationResult]:
    
    ...

