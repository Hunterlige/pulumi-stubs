

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ExportConfigurationArgs', 'ExportConfiguration']
@pulumi.input_type
class ExportConfigurationArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], resource_name: pulumi.Input[_builtins.str], destination_account_id: Optional[pulumi.Input[_builtins.str]] = ..., destination_address: Optional[pulumi.Input[_builtins.str]] = ..., destination_storage_location_id: Optional[pulumi.Input[_builtins.str]] = ..., destination_storage_subscription_id: Optional[pulumi.Input[_builtins.str]] = ..., destination_type: Optional[pulumi.Input[_builtins.str]] = ..., export_id: Optional[pulumi.Input[_builtins.str]] = ..., is_enabled: Optional[pulumi.Input[_builtins.str]] = ..., notification_queue_enabled: Optional[pulumi.Input[_builtins.str]] = ..., notification_queue_uri: Optional[pulumi.Input[_builtins.str]] = ..., record_types: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAccountId")
    def destination_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_account_id.setter
    def destination_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAddress")
    def destination_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_address.setter
    def destination_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationStorageLocationId")
    def destination_storage_location_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_storage_location_id.setter
    def destination_storage_location_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationStorageSubscriptionId")
    def destination_storage_subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_storage_subscription_id.setter
    def destination_storage_subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_type.setter
    def destination_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportId")
    def export_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_id.setter
    def export_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationQueueEnabled")
    def notification_queue_enabled(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notification_queue_enabled.setter
    def notification_queue_enabled(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationQueueUri")
    def notification_queue_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notification_queue_uri.setter
    def notification_queue_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordTypes")
    def record_types(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @record_types.setter
    def record_types(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ExportConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., destination_account_id: Optional[pulumi.Input[_builtins.str]] = ..., destination_address: Optional[pulumi.Input[_builtins.str]] = ..., destination_storage_location_id: Optional[pulumi.Input[_builtins.str]] = ..., destination_storage_subscription_id: Optional[pulumi.Input[_builtins.str]] = ..., destination_type: Optional[pulumi.Input[_builtins.str]] = ..., export_id: Optional[pulumi.Input[_builtins.str]] = ..., is_enabled: Optional[pulumi.Input[_builtins.str]] = ..., notification_queue_enabled: Optional[pulumi.Input[_builtins.str]] = ..., notification_queue_uri: Optional[pulumi.Input[_builtins.str]] = ..., record_types: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name_: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ExportConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ExportConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationAccountId")
    def destination_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationStorageLocationId")
    def destination_storage_location_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationStorageSubscriptionId")
    def destination_storage_subscription_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportId")
    def export_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportStatus")
    def export_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instrumentationKey")
    def instrumentation_key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isUserEnabled")
    def is_user_enabled(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastGapTime")
    def last_gap_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessTime")
    def last_success_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUserUpdate")
    def last_user_update(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationQueueEnabled")
    def notification_queue_enabled(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="permanentErrorReason")
    def permanent_error_reason(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordTypes")
    def record_types(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageName")
    def storage_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


