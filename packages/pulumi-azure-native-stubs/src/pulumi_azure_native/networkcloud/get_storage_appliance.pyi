

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetStorageApplianceResult', 'AwaitableGetStorageApplianceResult', 'get_storage_appliance', 'get_storage_appliance_output']
@pulumi.output_type
class GetStorageApplianceResult:
    def __init__(__self__, administrator_credentials=..., azure_api_version=..., capacity=..., capacity_used=..., cluster_id=..., detailed_status=..., detailed_status_message=..., etag=..., extended_location=..., id=..., location=..., management_ipv4_address=..., manufacturer=..., model=..., name=..., provisioning_state=..., rack_id=..., rack_slot=..., remote_vendor_management_feature=..., remote_vendor_management_status=..., secret_rotation_status=..., serial_number=..., storage_appliance_sku_id=..., system_data=..., tags=..., type=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorCredentials")
    def administrator_credentials(self) -> outputs.AdministrativeCredentialsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityUsed")
    def capacity_used(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementIpv4Address")
    def management_ipv4_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def manufacturer(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> _builtins.str:
        
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
    @pulumi.getter(name="rackId")
    def rack_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rackSlot")
    def rack_slot(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteVendorManagementFeature")
    def remote_vendor_management_feature(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteVendorManagementStatus")
    def remote_vendor_management_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretRotationStatus")
    def secret_rotation_status(self) -> Sequence[outputs.SecretRotationStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageApplianceSkuId")
    def storage_appliance_sku_id(self) -> _builtins.str:
        
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
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


class AwaitableGetStorageApplianceResult(GetStorageApplianceResult):
    def __await__(self): # -> Generator[Never, Any, GetStorageApplianceResult]:
        ...
    


def get_storage_appliance(resource_group_name: Optional[_builtins.str] = ..., storage_appliance_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetStorageApplianceResult:
    
    ...

def get_storage_appliance_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_appliance_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetStorageApplianceResult]:
    
    ...

