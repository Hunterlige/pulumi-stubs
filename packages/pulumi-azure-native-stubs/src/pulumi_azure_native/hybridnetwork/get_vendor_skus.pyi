

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVendorSkusResult', 'AwaitableGetVendorSkusResult', 'get_vendor_skus', 'get_vendor_skus_output']
@pulumi.output_type
class GetVendorSkusResult:
    
    def __init__(__self__, azure_api_version=..., deployment_mode=..., id=..., managed_application_parameters=..., managed_application_template=..., name=..., network_function_template=..., network_function_type=..., preview=..., provisioning_state=..., sku_type=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedApplicationParameters")
    def managed_application_parameters(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedApplicationTemplate")
    def managed_application_template(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkFunctionTemplate")
    def network_function_template(self) -> Optional[outputs.NetworkFunctionTemplateResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkFunctionType")
    def network_function_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def preview(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skuType")
    def sku_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetVendorSkusResult(GetVendorSkusResult):
    def __await__(self): # -> Generator[Never, Any, GetVendorSkusResult]:
        ...
    


def get_vendor_skus(sku_name: Optional[_builtins.str] = ..., vendor_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVendorSkusResult:
    
    ...

def get_vendor_skus_output(sku_name: Optional[pulumi.Input[_builtins.str]] = ..., vendor_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVendorSkusResult]:
    
    ...

