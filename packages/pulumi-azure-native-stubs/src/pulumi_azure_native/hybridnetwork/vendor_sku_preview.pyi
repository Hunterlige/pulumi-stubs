

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VendorSkuPreviewArgs', 'VendorSkuPreview']
@pulumi.input_type
class VendorSkuPreviewArgs:
    def __init__(__self__, *, sku_name: pulumi.Input[_builtins.str], vendor_name: pulumi.Input[_builtins.str], preview_subscription: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sku_name.setter
    def sku_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vendorName")
    def vendor_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vendor_name.setter
    def vendor_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="previewSubscription")
    def preview_subscription(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preview_subscription.setter
    def preview_subscription(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:hybridnetwork:VendorSkuPreview")
class VendorSkuPreview(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., preview_subscription: Optional[pulumi.Input[_builtins.str]] = ..., sku_name: Optional[pulumi.Input[_builtins.str]] = ..., vendor_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VendorSkuPreviewArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> VendorSkuPreview:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


