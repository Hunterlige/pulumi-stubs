

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSapVirtualInstanceInvokeSapSupportedSkuResult', ..., 'get_sap_virtual_instance_invoke_sap_supported_sku', ...]
@pulumi.output_type
class GetSapVirtualInstanceInvokeSapSupportedSkuResult:
    
    def __init__(__self__, supported_skus=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedSkus")
    def supported_skus(self) -> Optional[Sequence[outputs.SAPSupportedSkuResponse]]:
        
        ...
    


class AwaitableGetSapVirtualInstanceInvokeSapSupportedSkuResult(GetSapVirtualInstanceInvokeSapSupportedSkuResult):
    def __await__(self): # -> Generator[Never, Any, GetSapVirtualInstanceInvokeSapSupportedSkuResult]:
        ...
    


def get_sap_virtual_instance_invoke_sap_supported_sku(app_location: Optional[_builtins.str] = ..., database_type: Optional[Union[_builtins.str, SAPDatabaseType]] = ..., deployment_type: Optional[Union[_builtins.str, SAPDeploymentType]] = ..., environment: Optional[Union[_builtins.str, SAPEnvironmentType]] = ..., high_availability_type: Optional[Union[_builtins.str, SAPHighAvailabilityType]] = ..., location: Optional[_builtins.str] = ..., sap_product: Optional[Union[_builtins.str, SAPProductType]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSapVirtualInstanceInvokeSapSupportedSkuResult:
    
    ...

def get_sap_virtual_instance_invoke_sap_supported_sku_output(app_location: Optional[pulumi.Input[_builtins.str]] = ..., database_type: Optional[pulumi.Input[Union[_builtins.str, SAPDatabaseType]]] = ..., deployment_type: Optional[pulumi.Input[Union[_builtins.str, SAPDeploymentType]]] = ..., environment: Optional[pulumi.Input[Union[_builtins.str, SAPEnvironmentType]]] = ..., high_availability_type: Optional[pulumi.Input[Optional[Union[_builtins.str, SAPHighAvailabilityType]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., sap_product: Optional[pulumi.Input[Union[_builtins.str, SAPProductType]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSapVirtualInstanceInvokeSapSupportedSkuResult]:
    
    ...

