import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetExportConfigurationResult",
    "AwaitableGetExportConfigurationResult",
    "get_export_configuration",
    "get_export_configuration_output",
]

@pulumi.output_type
class GetExportConfigurationResult:
    def __init__(
        __self__,
        application_name=...,
        azure_api_version=...,
        container_name=...,
        destination_account_id=...,
        destination_storage_location_id=...,
        destination_storage_subscription_id=...,
        destination_type=...,
        export_id=...,
        export_status=...,
        instrumentation_key=...,
        is_user_enabled=...,
        last_gap_time=...,
        last_success_time=...,
        last_user_update=...,
        notification_queue_enabled=...,
        permanent_error_reason=...,
        record_types=...,
        resource_group=...,
        storage_name=...,
        subscription_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationAccountId")
    def destination_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationStorageLocationId")
    def destination_storage_location_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationStorageSubscriptionId")
    def destination_storage_subscription_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exportId")
    def export_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exportStatus")
    def export_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instrumentationKey")
    def instrumentation_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isUserEnabled")
    def is_user_enabled(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastGapTime")
    def last_gap_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastSuccessTime")
    def last_success_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUserUpdate")
    def last_user_update(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="notificationQueueEnabled")
    def notification_queue_enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="permanentErrorReason")
    def permanent_error_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="recordTypes")
    def record_types(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageName")
    def storage_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> _builtins.str: ...

class AwaitableGetExportConfigurationResult(GetExportConfigurationResult):
    def __await__(self): ...

def get_export_configuration(
    export_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetExportConfigurationResult: ...
def get_export_configuration_output(
    export_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetExportConfigurationResult]: ...
