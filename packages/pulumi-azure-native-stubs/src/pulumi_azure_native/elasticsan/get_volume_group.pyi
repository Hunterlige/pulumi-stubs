

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVolumeGroupResult', 'AwaitableGetVolumeGroupResult', 'get_volume_group', 'get_volume_group_output']
@pulumi.output_type
class GetVolumeGroupResult:
    
    def __init__(__self__, azure_api_version=..., encryption=..., encryption_properties=..., enforce_data_integrity_check_for_iscsi=..., id=..., identity=..., name=..., network_acls=..., private_endpoint_connections=..., protocol_type=..., provisioning_state=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionProperties")
    def encryption_properties(self) -> Optional[outputs.EncryptionPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforceDataIntegrityCheckForIscsi")
    def enforce_data_integrity_check_for_iscsi(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.IdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> Optional[outputs.NetworkRuleSetResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetVolumeGroupResult(GetVolumeGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetVolumeGroupResult]:
        ...
    


def get_volume_group(elastic_san_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., volume_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVolumeGroupResult:
    
    ...

def get_volume_group_output(elastic_san_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVolumeGroupResult]:
    
    ...

