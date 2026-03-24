

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BlobServicePropertiesArgs', 'BlobServiceProperties']
@pulumi.input_type
class BlobServicePropertiesArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], automatic_snapshot_policy_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., blob_services_name: Optional[pulumi.Input[_builtins.str]] = ..., change_feed: Optional[pulumi.Input[ChangeFeedArgs]] = ..., container_delete_retention_policy: Optional[pulumi.Input[DeleteRetentionPolicyArgs]] = ..., cors: Optional[pulumi.Input[CorsRulesArgs]] = ..., default_service_version: Optional[pulumi.Input[_builtins.str]] = ..., delete_retention_policy: Optional[pulumi.Input[DeleteRetentionPolicyArgs]] = ..., is_versioning_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., last_access_time_tracking_policy: Optional[pulumi.Input[LastAccessTimeTrackingPolicyArgs]] = ..., restore_policy: Optional[pulumi.Input[RestorePolicyPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticSnapshotPolicyEnabled")
    def automatic_snapshot_policy_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @automatic_snapshot_policy_enabled.setter
    def automatic_snapshot_policy_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobServicesName")
    def blob_services_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @blob_services_name.setter
    def blob_services_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="changeFeed")
    def change_feed(self) -> Optional[pulumi.Input[ChangeFeedArgs]]:
        
        ...
    
    @change_feed.setter
    def change_feed(self, value: Optional[pulumi.Input[ChangeFeedArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerDeleteRetentionPolicy")
    def container_delete_retention_policy(self) -> Optional[pulumi.Input[DeleteRetentionPolicyArgs]]:
        
        ...
    
    @container_delete_retention_policy.setter
    def container_delete_retention_policy(self, value: Optional[pulumi.Input[DeleteRetentionPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cors(self) -> Optional[pulumi.Input[CorsRulesArgs]]:
        
        ...
    
    @cors.setter
    def cors(self, value: Optional[pulumi.Input[CorsRulesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultServiceVersion")
    def default_service_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_service_version.setter
    def default_service_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteRetentionPolicy")
    def delete_retention_policy(self) -> Optional[pulumi.Input[DeleteRetentionPolicyArgs]]:
        
        ...
    
    @delete_retention_policy.setter
    def delete_retention_policy(self, value: Optional[pulumi.Input[DeleteRetentionPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isVersioningEnabled")
    def is_versioning_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_versioning_enabled.setter
    def is_versioning_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAccessTimeTrackingPolicy")
    def last_access_time_tracking_policy(self) -> Optional[pulumi.Input[LastAccessTimeTrackingPolicyArgs]]:
        
        ...
    
    @last_access_time_tracking_policy.setter
    def last_access_time_tracking_policy(self, value: Optional[pulumi.Input[LastAccessTimeTrackingPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePolicy")
    def restore_policy(self) -> Optional[pulumi.Input[RestorePolicyPropertiesArgs]]:
        
        ...
    
    @restore_policy.setter
    def restore_policy(self, value: Optional[pulumi.Input[RestorePolicyPropertiesArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:storage:BlobServiceProperties")
class BlobServiceProperties(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., automatic_snapshot_policy_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., blob_services_name: Optional[pulumi.Input[_builtins.str]] = ..., change_feed: Optional[pulumi.Input[Union[ChangeFeedArgs, ChangeFeedArgsDict]]] = ..., container_delete_retention_policy: Optional[pulumi.Input[Union[DeleteRetentionPolicyArgs, DeleteRetentionPolicyArgsDict]]] = ..., cors: Optional[pulumi.Input[Union[CorsRulesArgs, CorsRulesArgsDict]]] = ..., default_service_version: Optional[pulumi.Input[_builtins.str]] = ..., delete_retention_policy: Optional[pulumi.Input[Union[DeleteRetentionPolicyArgs, DeleteRetentionPolicyArgsDict]]] = ..., is_versioning_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., last_access_time_tracking_policy: Optional[pulumi.Input[Union[LastAccessTimeTrackingPolicyArgs, LastAccessTimeTrackingPolicyArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., restore_policy: Optional[pulumi.Input[Union[RestorePolicyPropertiesArgs, RestorePolicyPropertiesArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BlobServicePropertiesArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> BlobServiceProperties:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticSnapshotPolicyEnabled")
    def automatic_snapshot_policy_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="changeFeed")
    def change_feed(self) -> pulumi.Output[Optional[outputs.ChangeFeedResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerDeleteRetentionPolicy")
    def container_delete_retention_policy(self) -> pulumi.Output[Optional[outputs.DeleteRetentionPolicyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cors(self) -> pulumi.Output[Optional[outputs.CorsRulesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultServiceVersion")
    def default_service_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteRetentionPolicy")
    def delete_retention_policy(self) -> pulumi.Output[Optional[outputs.DeleteRetentionPolicyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isVersioningEnabled")
    def is_versioning_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAccessTimeTrackingPolicy")
    def last_access_time_tracking_policy(self) -> pulumi.Output[Optional[outputs.LastAccessTimeTrackingPolicyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePolicy")
    def restore_policy(self) -> pulumi.Output[Optional[outputs.RestorePolicyPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.SkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


