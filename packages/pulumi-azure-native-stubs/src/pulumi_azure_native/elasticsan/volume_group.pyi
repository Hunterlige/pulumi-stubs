

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VolumeGroupArgs', 'VolumeGroup']
@pulumi.input_type
class VolumeGroupArgs:
    def __init__(__self__, *, elastic_san_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], encryption: Optional[pulumi.Input[Union[_builtins.str, EncryptionType]]] = ..., encryption_properties: Optional[pulumi.Input[EncryptionPropertiesArgs]] = ..., enforce_data_integrity_check_for_iscsi: Optional[pulumi.Input[_builtins.bool]] = ..., identity: Optional[pulumi.Input[IdentityArgs]] = ..., network_acls: Optional[pulumi.Input[NetworkRuleSetArgs]] = ..., protocol_type: Optional[pulumi.Input[Union[_builtins.str, StorageTargetType]]] = ..., volume_group_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticSanName")
    def elastic_san_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @elastic_san_name.setter
    def elastic_san_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[Union[_builtins.str, EncryptionType]]]:
        
        ...
    
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[Union[_builtins.str, EncryptionType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionProperties")
    def encryption_properties(self) -> Optional[pulumi.Input[EncryptionPropertiesArgs]]:
        
        ...
    
    @encryption_properties.setter
    def encryption_properties(self, value: Optional[pulumi.Input[EncryptionPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforceDataIntegrityCheckForIscsi")
    def enforce_data_integrity_check_for_iscsi(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enforce_data_integrity_check_for_iscsi.setter
    def enforce_data_integrity_check_for_iscsi(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> Optional[pulumi.Input[NetworkRuleSetArgs]]:
        
        ...
    
    @network_acls.setter
    def network_acls(self, value: Optional[pulumi.Input[NetworkRuleSetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> Optional[pulumi.Input[Union[_builtins.str, StorageTargetType]]]:
        
        ...
    
    @protocol_type.setter
    def protocol_type(self, value: Optional[pulumi.Input[Union[_builtins.str, StorageTargetType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeGroupName")
    def volume_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_group_name.setter
    def volume_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:elasticsan:VolumeGroup")
class VolumeGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., elastic_san_name: Optional[pulumi.Input[_builtins.str]] = ..., encryption: Optional[pulumi.Input[Union[_builtins.str, EncryptionType]]] = ..., encryption_properties: Optional[pulumi.Input[Union[EncryptionPropertiesArgs, EncryptionPropertiesArgsDict]]] = ..., enforce_data_integrity_check_for_iscsi: Optional[pulumi.Input[_builtins.bool]] = ..., identity: Optional[pulumi.Input[Union[IdentityArgs, IdentityArgsDict]]] = ..., network_acls: Optional[pulumi.Input[Union[NetworkRuleSetArgs, NetworkRuleSetArgsDict]]] = ..., protocol_type: Optional[pulumi.Input[Union[_builtins.str, StorageTargetType]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VolumeGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> VolumeGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionProperties")
    def encryption_properties(self) -> pulumi.Output[Optional[outputs.EncryptionPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforceDataIntegrityCheckForIscsi")
    def enforce_data_integrity_check_for_iscsi(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> pulumi.Output[Optional[outputs.NetworkRuleSetResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence[outputs.PrivateEndpointConnectionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    


