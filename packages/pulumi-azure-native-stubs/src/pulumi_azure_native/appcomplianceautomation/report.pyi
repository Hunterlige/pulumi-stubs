

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
__all__ = ['ReportArgs', 'Report']
@pulumi.input_type
class ReportArgs:
    def __init__(__self__, *, resources: pulumi.Input[Sequence[pulumi.Input[ResourceMetadataArgs]]], time_zone: pulumi.Input[_builtins.str], trigger_time: pulumi.Input[_builtins.str], offer_guid: Optional[pulumi.Input[_builtins.str]] = ..., report_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_info: Optional[pulumi.Input[StorageInfoArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Input[Sequence[pulumi.Input[ResourceMetadataArgs]]]:
        
        ...
    
    @resources.setter
    def resources(self, value: pulumi.Input[Sequence[pulumi.Input[ResourceMetadataArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @time_zone.setter
    def time_zone(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerTime")
    def trigger_time(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @trigger_time.setter
    def trigger_time(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offerGuid")
    def offer_guid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @offer_guid.setter
    def offer_guid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportName")
    def report_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @report_name.setter
    def report_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageInfo")
    def storage_info(self) -> Optional[pulumi.Input[StorageInfoArgs]]:
        
        ...
    
    @storage_info.setter
    def storage_info(self, value: Optional[pulumi.Input[StorageInfoArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:appcomplianceautomation:Report")
class Report(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., offer_guid: Optional[pulumi.Input[_builtins.str]] = ..., report_name: Optional[pulumi.Input[_builtins.str]] = ..., resources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ResourceMetadataArgs, ResourceMetadataArgsDict]]]]] = ..., storage_info: Optional[pulumi.Input[Union[StorageInfoArgs, StorageInfoArgsDict]]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ..., trigger_time: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ReportArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Report:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certRecords")
    def cert_records(self) -> pulumi.Output[Sequence[outputs.CertSyncRecordResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceStatus")
    def compliance_status(self) -> pulumi.Output[outputs.ReportComplianceStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTriggerTime")
    def last_trigger_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextTriggerTime")
    def next_trigger_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offerGuid")
    def offer_guid(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Sequence[outputs.ResourceMetadataResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageInfo")
    def storage_info(self) -> pulumi.Output[Optional[outputs.StorageInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subscriptions(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerTime")
    def trigger_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


