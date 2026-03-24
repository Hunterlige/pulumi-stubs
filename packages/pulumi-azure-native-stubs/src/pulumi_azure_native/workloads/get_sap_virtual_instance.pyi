

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSapVirtualInstanceResult', 'AwaitableGetSapVirtualInstanceResult', 'get_sap_virtual_instance', 'get_sap_virtual_instance_output']
@pulumi.output_type
class GetSapVirtualInstanceResult:
    
    def __init__(__self__, azure_api_version=..., configuration=..., environment=..., errors=..., health=..., id=..., identity=..., location=..., managed_resource_group_configuration=..., managed_resources_network_access_type=..., name=..., provisioning_state=..., sap_product=..., state=..., status=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> outputs.SAPVirtualInstanceErrorResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.SAPVirtualInstanceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(self) -> Optional[outputs.ManagedRGConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedResourcesNetworkAccessType")
    def managed_resources_network_access_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sapProduct")
    def sap_product(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
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
    


class AwaitableGetSapVirtualInstanceResult(GetSapVirtualInstanceResult):
    def __await__(self): # -> Generator[Never, Any, GetSapVirtualInstanceResult]:
        ...
    


def get_sap_virtual_instance(resource_group_name: Optional[_builtins.str] = ..., sap_virtual_instance_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSapVirtualInstanceResult:
    
    ...

def get_sap_virtual_instance_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sap_virtual_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSapVirtualInstanceResult]:
    
    ...

