

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetReceivedLicenseResult', 'AwaitableGetReceivedLicenseResult', 'get_received_license', 'get_received_license_output']
@pulumi.output_type
class GetReceivedLicenseResult:
    
    def __init__(__self__, beneficiary=..., consumption_configurations=..., create_time=..., entitlements=..., home_region=..., id=..., issuers=..., license_arn=..., license_metadatas=..., license_name=..., product_name=..., product_sku=..., received_metadatas=..., region=..., status=..., validities=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def beneficiary(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumptionConfigurations")
    def consumption_configurations(self) -> Sequence[outputs.GetReceivedLicenseConsumptionConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def entitlements(self) -> Sequence[outputs.GetReceivedLicenseEntitlementResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="homeRegion")
    def home_region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuers(self) -> Sequence[outputs.GetReceivedLicenseIssuerResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseArn")
    def license_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseMetadatas")
    def license_metadatas(self) -> Sequence[outputs.GetReceivedLicenseLicenseMetadataResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseName")
    def license_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productName")
    def product_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productSku")
    def product_sku(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="receivedMetadatas")
    def received_metadatas(self) -> Sequence[outputs.GetReceivedLicenseReceivedMetadataResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def validities(self) -> Sequence[outputs.GetReceivedLicenseValidityResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


class AwaitableGetReceivedLicenseResult(GetReceivedLicenseResult):
    def __await__(self): # -> Generator[Never, Any, GetReceivedLicenseResult]:
        ...
    


def get_received_license(license_arn: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetReceivedLicenseResult:
    
    ...

def get_received_license_output(license_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetReceivedLicenseResult]:
    
    ...

