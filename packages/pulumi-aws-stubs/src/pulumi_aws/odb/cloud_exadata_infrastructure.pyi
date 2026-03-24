

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CloudExadataInfrastructureArgs', 'CloudExadataInfrastructure']
@pulumi.input_type
class CloudExadataInfrastructureArgs:
    def __init__(__self__, *, availability_zone_id: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], maintenance_window: pulumi.Input[CloudExadataInfrastructureMaintenanceWindowArgs], shape: pulumi.Input[_builtins.str], availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., compute_count: Optional[pulumi.Input[_builtins.int]] = ..., customer_contacts_to_send_to_ocis: Optional[pulumi.Input[Sequence[pulumi.Input[CloudExadataInfrastructureCustomerContactsToSendToOciArgs]]]] = ..., database_server_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., storage_count: Optional[pulumi.Input[_builtins.int]] = ..., storage_server_type: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[CloudExadataInfrastructureTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @availability_zone_id.setter
    def availability_zone_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Input[CloudExadataInfrastructureMaintenanceWindowArgs]:
        
        ...
    
    @maintenance_window.setter
    def maintenance_window(self, value: pulumi.Input[CloudExadataInfrastructureMaintenanceWindowArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @shape.setter
    def shape(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeCount")
    def compute_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @compute_count.setter
    def compute_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerContactsToSendToOcis")
    def customer_contacts_to_send_to_ocis(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CloudExadataInfrastructureCustomerContactsToSendToOciArgs]]]]:
        
        ...
    
    @customer_contacts_to_send_to_ocis.setter
    def customer_contacts_to_send_to_ocis(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CloudExadataInfrastructureCustomerContactsToSendToOciArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseServerType")
    def database_server_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_server_type.setter
    def database_server_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCount")
    def storage_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @storage_count.setter
    def storage_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageServerType")
    def storage_server_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_server_type.setter
    def storage_server_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[CloudExadataInfrastructureTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[CloudExadataInfrastructureTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _CloudExadataInfrastructureState:
    def __init__(__self__, *, activated_storage_count: Optional[pulumi.Input[_builtins.int]] = ..., additional_storage_count: Optional[pulumi.Input[_builtins.int]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., available_storage_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., compute_count: Optional[pulumi.Input[_builtins.int]] = ..., compute_model: Optional[pulumi.Input[_builtins.str]] = ..., cpu_count: Optional[pulumi.Input[_builtins.int]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., customer_contacts_to_send_to_ocis: Optional[pulumi.Input[Sequence[pulumi.Input[CloudExadataInfrastructureCustomerContactsToSendToOciArgs]]]] = ..., data_storage_size_in_tbs: Optional[pulumi.Input[_builtins.float]] = ..., database_server_type: Optional[pulumi.Input[_builtins.str]] = ..., db_node_storage_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., db_server_version: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., last_maintenance_run_id: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[CloudExadataInfrastructureMaintenanceWindowArgs]] = ..., max_cpu_count: Optional[pulumi.Input[_builtins.int]] = ..., max_data_storage_in_tbs: Optional[pulumi.Input[_builtins.float]] = ..., max_db_node_storage_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., max_memory_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., memory_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., monthly_db_server_version: Optional[pulumi.Input[_builtins.str]] = ..., monthly_storage_server_version: Optional[pulumi.Input[_builtins.str]] = ..., next_maintenance_run_id: Optional[pulumi.Input[_builtins.str]] = ..., oci_resource_anchor_name: Optional[pulumi.Input[_builtins.str]] = ..., oci_url: Optional[pulumi.Input[_builtins.str]] = ..., ocid: Optional[pulumi.Input[_builtins.str]] = ..., percent_progress: Optional[pulumi.Input[_builtins.float]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shape: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., status_reason: Optional[pulumi.Input[_builtins.str]] = ..., storage_count: Optional[pulumi.Input[_builtins.int]] = ..., storage_server_type: Optional[pulumi.Input[_builtins.str]] = ..., storage_server_version: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[CloudExadataInfrastructureTimeoutsArgs]] = ..., total_storage_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activatedStorageCount")
    def activated_storage_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @activated_storage_count.setter
    def activated_storage_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalStorageCount")
    def additional_storage_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @additional_storage_count.setter
    def additional_storage_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone_id.setter
    def availability_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableStorageSizeInGbs")
    def available_storage_size_in_gbs(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @available_storage_size_in_gbs.setter
    def available_storage_size_in_gbs(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeCount")
    def compute_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @compute_count.setter
    def compute_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeModel")
    def compute_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compute_model.setter
    def compute_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cpu_count.setter
    def cpu_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerContactsToSendToOcis")
    def customer_contacts_to_send_to_ocis(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CloudExadataInfrastructureCustomerContactsToSendToOciArgs]]]]:
        
        ...
    
    @customer_contacts_to_send_to_ocis.setter
    def customer_contacts_to_send_to_ocis(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CloudExadataInfrastructureCustomerContactsToSendToOciArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeInTbs")
    def data_storage_size_in_tbs(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseServerType")
    def database_server_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_server_type.setter
    def database_server_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeInGbs")
    def db_node_storage_size_in_gbs(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @db_node_storage_size_in_gbs.setter
    def db_node_storage_size_in_gbs(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbServerVersion")
    def db_server_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_server_version.setter
    def db_server_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastMaintenanceRunId")
    def last_maintenance_run_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_maintenance_run_id.setter
    def last_maintenance_run_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[CloudExadataInfrastructureMaintenanceWindowArgs]]:
        
        ...
    
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[CloudExadataInfrastructureMaintenanceWindowArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCpuCount")
    def max_cpu_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_cpu_count.setter
    def max_cpu_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDataStorageInTbs")
    def max_data_storage_in_tbs(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max_data_storage_in_tbs.setter
    def max_data_storage_in_tbs(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDbNodeStorageSizeInGbs")
    def max_db_node_storage_size_in_gbs(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_db_node_storage_size_in_gbs.setter
    def max_db_node_storage_size_in_gbs(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxMemoryInGbs")
    def max_memory_in_gbs(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_memory_in_gbs.setter
    def max_memory_in_gbs(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySizeInGbs")
    def memory_size_in_gbs(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @memory_size_in_gbs.setter
    def memory_size_in_gbs(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyDbServerVersion")
    def monthly_db_server_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @monthly_db_server_version.setter
    def monthly_db_server_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyStorageServerVersion")
    def monthly_storage_server_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @monthly_storage_server_version.setter
    def monthly_storage_server_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextMaintenanceRunId")
    def next_maintenance_run_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @next_maintenance_run_id.setter
    def next_maintenance_run_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociResourceAnchorName")
    def oci_resource_anchor_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @oci_resource_anchor_name.setter
    def oci_resource_anchor_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @oci_url.setter
    def oci_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ocid.setter
    def ocid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentProgress")
    def percent_progress(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @percent_progress.setter
    def percent_progress(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @shape.setter
    def shape(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status_reason.setter
    def status_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCount")
    def storage_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @storage_count.setter
    def storage_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageServerType")
    def storage_server_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_server_type.setter
    def storage_server_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageServerVersion")
    def storage_server_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_server_version.setter
    def storage_server_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[CloudExadataInfrastructureTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[CloudExadataInfrastructureTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalStorageSizeInGbs")
    def total_storage_size_in_gbs(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @total_storage_size_in_gbs.setter
    def total_storage_size_in_gbs(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token(...)
class CloudExadataInfrastructure(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., compute_count: Optional[pulumi.Input[_builtins.int]] = ..., customer_contacts_to_send_to_ocis: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CloudExadataInfrastructureCustomerContactsToSendToOciArgs, CloudExadataInfrastructureCustomerContactsToSendToOciArgsDict]]]]] = ..., database_server_type: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[Union[CloudExadataInfrastructureMaintenanceWindowArgs, CloudExadataInfrastructureMaintenanceWindowArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shape: Optional[pulumi.Input[_builtins.str]] = ..., storage_count: Optional[pulumi.Input[_builtins.int]] = ..., storage_server_type: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[CloudExadataInfrastructureTimeoutsArgs, CloudExadataInfrastructureTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CloudExadataInfrastructureArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., activated_storage_count: Optional[pulumi.Input[_builtins.int]] = ..., additional_storage_count: Optional[pulumi.Input[_builtins.int]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., available_storage_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., compute_count: Optional[pulumi.Input[_builtins.int]] = ..., compute_model: Optional[pulumi.Input[_builtins.str]] = ..., cpu_count: Optional[pulumi.Input[_builtins.int]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., customer_contacts_to_send_to_ocis: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CloudExadataInfrastructureCustomerContactsToSendToOciArgs, CloudExadataInfrastructureCustomerContactsToSendToOciArgsDict]]]]] = ..., data_storage_size_in_tbs: Optional[pulumi.Input[_builtins.float]] = ..., database_server_type: Optional[pulumi.Input[_builtins.str]] = ..., db_node_storage_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., db_server_version: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., last_maintenance_run_id: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[Union[CloudExadataInfrastructureMaintenanceWindowArgs, CloudExadataInfrastructureMaintenanceWindowArgsDict]]] = ..., max_cpu_count: Optional[pulumi.Input[_builtins.int]] = ..., max_data_storage_in_tbs: Optional[pulumi.Input[_builtins.float]] = ..., max_db_node_storage_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., max_memory_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., memory_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., monthly_db_server_version: Optional[pulumi.Input[_builtins.str]] = ..., monthly_storage_server_version: Optional[pulumi.Input[_builtins.str]] = ..., next_maintenance_run_id: Optional[pulumi.Input[_builtins.str]] = ..., oci_resource_anchor_name: Optional[pulumi.Input[_builtins.str]] = ..., oci_url: Optional[pulumi.Input[_builtins.str]] = ..., ocid: Optional[pulumi.Input[_builtins.str]] = ..., percent_progress: Optional[pulumi.Input[_builtins.float]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shape: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., status_reason: Optional[pulumi.Input[_builtins.str]] = ..., storage_count: Optional[pulumi.Input[_builtins.int]] = ..., storage_server_type: Optional[pulumi.Input[_builtins.str]] = ..., storage_server_version: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[CloudExadataInfrastructureTimeoutsArgs, CloudExadataInfrastructureTimeoutsArgsDict]]] = ..., total_storage_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ...) -> CloudExadataInfrastructure:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activatedStorageCount")
    def activated_storage_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalStorageCount")
    def additional_storage_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableStorageSizeInGbs")
    def available_storage_size_in_gbs(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeCount")
    def compute_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeModel")
    def compute_model(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerContactsToSendToOcis")
    def customer_contacts_to_send_to_ocis(self) -> pulumi.Output[Optional[Sequence[outputs.CloudExadataInfrastructureCustomerContactsToSendToOci]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeInTbs")
    def data_storage_size_in_tbs(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseServerType")
    def database_server_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeInGbs")
    def db_node_storage_size_in_gbs(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbServerVersion")
    def db_server_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastMaintenanceRunId")
    def last_maintenance_run_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output[outputs.CloudExadataInfrastructureMaintenanceWindow]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCpuCount")
    def max_cpu_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDataStorageInTbs")
    def max_data_storage_in_tbs(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDbNodeStorageSizeInGbs")
    def max_db_node_storage_size_in_gbs(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxMemoryInGbs")
    def max_memory_in_gbs(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySizeInGbs")
    def memory_size_in_gbs(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyDbServerVersion")
    def monthly_db_server_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyStorageServerVersion")
    def monthly_storage_server_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextMaintenanceRunId")
    def next_maintenance_run_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociResourceAnchorName")
    def oci_resource_anchor_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentProgress")
    def percent_progress(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCount")
    def storage_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageServerType")
    def storage_server_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageServerVersion")
    def storage_server_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.CloudExadataInfrastructureTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalStorageSizeInGbs")
    def total_storage_size_in_gbs(self) -> pulumi.Output[_builtins.int]:
        
        ...
    


