

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InstanceArgs', 'Instance']
@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *, ami: Optional[pulumi.Input[_builtins.str]] = ..., associate_public_ip_address: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., capacity_reservation_specification: Optional[pulumi.Input[InstanceCapacityReservationSpecificationArgs]] = ..., cpu_options: Optional[pulumi.Input[InstanceCpuOptionsArgs]] = ..., credit_specification: Optional[pulumi.Input[InstanceCreditSpecificationArgs]] = ..., disable_api_stop: Optional[pulumi.Input[_builtins.bool]] = ..., disable_api_termination: Optional[pulumi.Input[_builtins.bool]] = ..., ebs_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEbsBlockDeviceArgs]]]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., enable_primary_ipv6: Optional[pulumi.Input[_builtins.bool]] = ..., enclave_options: Optional[pulumi.Input[InstanceEnclaveOptionsArgs]] = ..., ephemeral_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEphemeralBlockDeviceArgs]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., get_password_data: Optional[pulumi.Input[_builtins.bool]] = ..., hibernation: Optional[pulumi.Input[_builtins.bool]] = ..., host_id: Optional[pulumi.Input[_builtins.str]] = ..., host_resource_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ..., instance_initiated_shutdown_behavior: Optional[pulumi.Input[_builtins.str]] = ..., instance_market_options: Optional[pulumi.Input[InstanceInstanceMarketOptionsArgs]] = ..., instance_type: Optional[pulumi.Input[Union[_builtins.str, InstanceType]]] = ..., ipv6_address_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., key_name: Optional[pulumi.Input[_builtins.str]] = ..., launch_template: Optional[pulumi.Input[InstanceLaunchTemplateArgs]] = ..., maintenance_options: Optional[pulumi.Input[InstanceMaintenanceOptionsArgs]] = ..., metadata_options: Optional[pulumi.Input[InstanceMetadataOptionsArgs]] = ..., monitoring: Optional[pulumi.Input[_builtins.bool]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceNetworkInterfaceArgs]]]] = ..., placement_group: Optional[pulumi.Input[_builtins.str]] = ..., placement_group_id: Optional[pulumi.Input[_builtins.str]] = ..., placement_partition_number: Optional[pulumi.Input[_builtins.int]] = ..., primary_network_interface: Optional[pulumi.Input[InstancePrimaryNetworkInterfaceArgs]] = ..., private_dns_name_options: Optional[pulumi.Input[InstancePrivateDnsNameOptionsArgs]] = ..., private_ip: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_block_device: Optional[pulumi.Input[InstanceRootBlockDeviceArgs]] = ..., secondary_network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceSecondaryNetworkInterfaceArgs]]]] = ..., secondary_private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_dest_check: Optional[pulumi.Input[_builtins.bool]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenancy: Optional[pulumi.Input[Union[_builtins.str, Tenancy]]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., user_data_base64: Optional[pulumi.Input[_builtins.str]] = ..., user_data_replace_on_change: Optional[pulumi.Input[_builtins.bool]] = ..., volume_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ami(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ami.setter
    def ami(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @associate_public_ip_address.setter
    def associate_public_ip_address(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationSpecification")
    def capacity_reservation_specification(self) -> Optional[pulumi.Input[InstanceCapacityReservationSpecificationArgs]]:
        
        ...
    
    @capacity_reservation_specification.setter
    def capacity_reservation_specification(self, value: Optional[pulumi.Input[InstanceCapacityReservationSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuOptions")
    def cpu_options(self) -> Optional[pulumi.Input[InstanceCpuOptionsArgs]]:
        
        ...
    
    @cpu_options.setter
    def cpu_options(self, value: Optional[pulumi.Input[InstanceCpuOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creditSpecification")
    def credit_specification(self) -> Optional[pulumi.Input[InstanceCreditSpecificationArgs]]:
        
        ...
    
    @credit_specification.setter
    def credit_specification(self, value: Optional[pulumi.Input[InstanceCreditSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableApiStop")
    def disable_api_stop(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_api_stop.setter
    def disable_api_stop(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableApiTermination")
    def disable_api_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_api_termination.setter
    def disable_api_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsBlockDevices")
    def ebs_block_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEbsBlockDeviceArgs]]]]:
        
        ...
    
    @ebs_block_devices.setter
    def ebs_block_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEbsBlockDeviceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ebs_optimized.setter
    def ebs_optimized(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrimaryIpv6")
    def enable_primary_ipv6(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_primary_ipv6.setter
    def enable_primary_ipv6(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enclaveOptions")
    def enclave_options(self) -> Optional[pulumi.Input[InstanceEnclaveOptionsArgs]]:
        
        ...
    
    @enclave_options.setter
    def enclave_options(self, value: Optional[pulumi.Input[InstanceEnclaveOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralBlockDevices")
    def ephemeral_block_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEphemeralBlockDeviceArgs]]]]:
        
        ...
    
    @ephemeral_block_devices.setter
    def ephemeral_block_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEphemeralBlockDeviceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="getPasswordData")
    def get_password_data(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @get_password_data.setter
    def get_password_data(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hibernation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @hibernation.setter
    def hibernation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host_id.setter
    def host_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostResourceGroupArn")
    def host_resource_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host_resource_group_arn.setter
    def host_resource_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_instance_profile.setter
    def iam_instance_profile(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceInitiatedShutdownBehavior")
    def instance_initiated_shutdown_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_initiated_shutdown_behavior.setter
    def instance_initiated_shutdown_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMarketOptions")
    def instance_market_options(self) -> Optional[pulumi.Input[InstanceInstanceMarketOptionsArgs]]:
        
        ...
    
    @instance_market_options.setter
    def instance_market_options(self, value: Optional[pulumi.Input[InstanceInstanceMarketOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[Union[_builtins.str, InstanceType]]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[Union[_builtins.str, InstanceType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressCount")
    def ipv6_address_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ipv6_address_count.setter
    def ipv6_address_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_addresses.setter
    def ipv6_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplate")
    def launch_template(self) -> Optional[pulumi.Input[InstanceLaunchTemplateArgs]]:
        
        ...
    
    @launch_template.setter
    def launch_template(self, value: Optional[pulumi.Input[InstanceLaunchTemplateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceOptions")
    def maintenance_options(self) -> Optional[pulumi.Input[InstanceMaintenanceOptionsArgs]]:
        
        ...
    
    @maintenance_options.setter
    def maintenance_options(self, value: Optional[pulumi.Input[InstanceMaintenanceOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataOptions")
    def metadata_options(self) -> Optional[pulumi.Input[InstanceMetadataOptionsArgs]]:
        
        ...
    
    @metadata_options.setter
    def metadata_options(self, value: Optional[pulumi.Input[InstanceMetadataOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @monitoring.setter
    def monitoring(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    @_utilities.deprecated(...)
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceNetworkInterfaceArgs]]]]:
        
        ...
    
    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceNetworkInterfaceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroup")
    def placement_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @placement_group.setter
    def placement_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroupId")
    def placement_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @placement_group_id.setter
    def placement_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementPartitionNumber")
    def placement_partition_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @placement_partition_number.setter
    def placement_partition_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryNetworkInterface")
    def primary_network_interface(self) -> Optional[pulumi.Input[InstancePrimaryNetworkInterfaceArgs]]:
        
        ...
    
    @primary_network_interface.setter
    def primary_network_interface(self, value: Optional[pulumi.Input[InstancePrimaryNetworkInterfaceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsNameOptions")
    def private_dns_name_options(self) -> Optional[pulumi.Input[InstancePrivateDnsNameOptionsArgs]]:
        
        ...
    
    @private_dns_name_options.setter
    def private_dns_name_options(self, value: Optional[pulumi.Input[InstancePrivateDnsNameOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ip.setter
    def private_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootBlockDevice")
    def root_block_device(self) -> Optional[pulumi.Input[InstanceRootBlockDeviceArgs]]:
        
        ...
    
    @root_block_device.setter
    def root_block_device(self, value: Optional[pulumi.Input[InstanceRootBlockDeviceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryNetworkInterfaces")
    def secondary_network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceSecondaryNetworkInterfaceArgs]]]]:
        
        ...
    
    @secondary_network_interfaces.setter
    def secondary_network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceSecondaryNetworkInterfaceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryPrivateIps")
    def secondary_private_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @secondary_private_ips.setter
    def secondary_private_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    @_utilities.deprecated(...)
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDestCheck")
    def source_dest_check(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @source_dest_check.setter
    def source_dest_check(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def tenancy(self) -> Optional[pulumi.Input[Union[_builtins.str, Tenancy]]]:
        
        ...
    
    @tenancy.setter
    def tenancy(self, value: Optional[pulumi.Input[Union[_builtins.str, Tenancy]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_data.setter
    def user_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDataBase64")
    def user_data_base64(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_data_base64.setter
    def user_data_base64(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDataReplaceOnChange")
    def user_data_replace_on_change(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @user_data_replace_on_change.setter
    def user_data_replace_on_change(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeTags")
    def volume_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @volume_tags.setter
    def volume_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _InstanceState:
    def __init__(__self__, *, ami: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., associate_public_ip_address: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., capacity_reservation_specification: Optional[pulumi.Input[InstanceCapacityReservationSpecificationArgs]] = ..., cpu_options: Optional[pulumi.Input[InstanceCpuOptionsArgs]] = ..., credit_specification: Optional[pulumi.Input[InstanceCreditSpecificationArgs]] = ..., disable_api_stop: Optional[pulumi.Input[_builtins.bool]] = ..., disable_api_termination: Optional[pulumi.Input[_builtins.bool]] = ..., ebs_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEbsBlockDeviceArgs]]]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., enable_primary_ipv6: Optional[pulumi.Input[_builtins.bool]] = ..., enclave_options: Optional[pulumi.Input[InstanceEnclaveOptionsArgs]] = ..., ephemeral_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEphemeralBlockDeviceArgs]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., get_password_data: Optional[pulumi.Input[_builtins.bool]] = ..., hibernation: Optional[pulumi.Input[_builtins.bool]] = ..., host_id: Optional[pulumi.Input[_builtins.str]] = ..., host_resource_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ..., instance_initiated_shutdown_behavior: Optional[pulumi.Input[_builtins.str]] = ..., instance_lifecycle: Optional[pulumi.Input[_builtins.str]] = ..., instance_market_options: Optional[pulumi.Input[InstanceInstanceMarketOptionsArgs]] = ..., instance_state: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[Union[_builtins.str, InstanceType]]] = ..., ipv6_address_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., key_name: Optional[pulumi.Input[_builtins.str]] = ..., launch_template: Optional[pulumi.Input[InstanceLaunchTemplateArgs]] = ..., maintenance_options: Optional[pulumi.Input[InstanceMaintenanceOptionsArgs]] = ..., metadata_options: Optional[pulumi.Input[InstanceMetadataOptionsArgs]] = ..., monitoring: Optional[pulumi.Input[_builtins.bool]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceNetworkInterfaceArgs]]]] = ..., outpost_arn: Optional[pulumi.Input[_builtins.str]] = ..., password_data: Optional[pulumi.Input[_builtins.str]] = ..., placement_group: Optional[pulumi.Input[_builtins.str]] = ..., placement_group_id: Optional[pulumi.Input[_builtins.str]] = ..., placement_partition_number: Optional[pulumi.Input[_builtins.int]] = ..., primary_network_interface: Optional[pulumi.Input[InstancePrimaryNetworkInterfaceArgs]] = ..., primary_network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., private_dns: Optional[pulumi.Input[_builtins.str]] = ..., private_dns_name_options: Optional[pulumi.Input[InstancePrivateDnsNameOptionsArgs]] = ..., private_ip: Optional[pulumi.Input[_builtins.str]] = ..., public_dns: Optional[pulumi.Input[_builtins.str]] = ..., public_ip: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_block_device: Optional[pulumi.Input[InstanceRootBlockDeviceArgs]] = ..., secondary_network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceSecondaryNetworkInterfaceArgs]]]] = ..., secondary_private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_dest_check: Optional[pulumi.Input[_builtins.bool]] = ..., spot_instance_request_id: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenancy: Optional[pulumi.Input[Union[_builtins.str, Tenancy]]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., user_data_base64: Optional[pulumi.Input[_builtins.str]] = ..., user_data_replace_on_change: Optional[pulumi.Input[_builtins.bool]] = ..., volume_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ami(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ami.setter
    def ami(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @associate_public_ip_address.setter
    def associate_public_ip_address(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationSpecification")
    def capacity_reservation_specification(self) -> Optional[pulumi.Input[InstanceCapacityReservationSpecificationArgs]]:
        
        ...
    
    @capacity_reservation_specification.setter
    def capacity_reservation_specification(self, value: Optional[pulumi.Input[InstanceCapacityReservationSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuOptions")
    def cpu_options(self) -> Optional[pulumi.Input[InstanceCpuOptionsArgs]]:
        
        ...
    
    @cpu_options.setter
    def cpu_options(self, value: Optional[pulumi.Input[InstanceCpuOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creditSpecification")
    def credit_specification(self) -> Optional[pulumi.Input[InstanceCreditSpecificationArgs]]:
        
        ...
    
    @credit_specification.setter
    def credit_specification(self, value: Optional[pulumi.Input[InstanceCreditSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableApiStop")
    def disable_api_stop(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_api_stop.setter
    def disable_api_stop(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableApiTermination")
    def disable_api_termination(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_api_termination.setter
    def disable_api_termination(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsBlockDevices")
    def ebs_block_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEbsBlockDeviceArgs]]]]:
        
        ...
    
    @ebs_block_devices.setter
    def ebs_block_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEbsBlockDeviceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ebs_optimized.setter
    def ebs_optimized(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrimaryIpv6")
    def enable_primary_ipv6(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_primary_ipv6.setter
    def enable_primary_ipv6(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enclaveOptions")
    def enclave_options(self) -> Optional[pulumi.Input[InstanceEnclaveOptionsArgs]]:
        
        ...
    
    @enclave_options.setter
    def enclave_options(self, value: Optional[pulumi.Input[InstanceEnclaveOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralBlockDevices")
    def ephemeral_block_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEphemeralBlockDeviceArgs]]]]:
        
        ...
    
    @ephemeral_block_devices.setter
    def ephemeral_block_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEphemeralBlockDeviceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="getPasswordData")
    def get_password_data(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @get_password_data.setter
    def get_password_data(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hibernation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @hibernation.setter
    def hibernation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host_id.setter
    def host_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostResourceGroupArn")
    def host_resource_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host_resource_group_arn.setter
    def host_resource_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_instance_profile.setter
    def iam_instance_profile(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceInitiatedShutdownBehavior")
    def instance_initiated_shutdown_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_initiated_shutdown_behavior.setter
    def instance_initiated_shutdown_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceLifecycle")
    def instance_lifecycle(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_lifecycle.setter
    def instance_lifecycle(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMarketOptions")
    def instance_market_options(self) -> Optional[pulumi.Input[InstanceInstanceMarketOptionsArgs]]:
        
        ...
    
    @instance_market_options.setter
    def instance_market_options(self, value: Optional[pulumi.Input[InstanceInstanceMarketOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceState")
    def instance_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_state.setter
    def instance_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[Union[_builtins.str, InstanceType]]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[Union[_builtins.str, InstanceType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressCount")
    def ipv6_address_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ipv6_address_count.setter
    def ipv6_address_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_addresses.setter
    def ipv6_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplate")
    def launch_template(self) -> Optional[pulumi.Input[InstanceLaunchTemplateArgs]]:
        
        ...
    
    @launch_template.setter
    def launch_template(self, value: Optional[pulumi.Input[InstanceLaunchTemplateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceOptions")
    def maintenance_options(self) -> Optional[pulumi.Input[InstanceMaintenanceOptionsArgs]]:
        
        ...
    
    @maintenance_options.setter
    def maintenance_options(self, value: Optional[pulumi.Input[InstanceMaintenanceOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataOptions")
    def metadata_options(self) -> Optional[pulumi.Input[InstanceMetadataOptionsArgs]]:
        
        ...
    
    @metadata_options.setter
    def metadata_options(self, value: Optional[pulumi.Input[InstanceMetadataOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @monitoring.setter
    def monitoring(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    @_utilities.deprecated(...)
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceNetworkInterfaceArgs]]]]:
        
        ...
    
    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceNetworkInterfaceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @outpost_arn.setter
    def outpost_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordData")
    def password_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password_data.setter
    def password_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroup")
    def placement_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @placement_group.setter
    def placement_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroupId")
    def placement_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @placement_group_id.setter
    def placement_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementPartitionNumber")
    def placement_partition_number(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @placement_partition_number.setter
    def placement_partition_number(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryNetworkInterface")
    def primary_network_interface(self) -> Optional[pulumi.Input[InstancePrimaryNetworkInterfaceArgs]]:
        
        ...
    
    @primary_network_interface.setter
    def primary_network_interface(self, value: Optional[pulumi.Input[InstancePrimaryNetworkInterfaceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryNetworkInterfaceId")
    def primary_network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_network_interface_id.setter
    def primary_network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDns")
    def private_dns(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_dns.setter
    def private_dns(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsNameOptions")
    def private_dns_name_options(self) -> Optional[pulumi.Input[InstancePrivateDnsNameOptionsArgs]]:
        
        ...
    
    @private_dns_name_options.setter
    def private_dns_name_options(self, value: Optional[pulumi.Input[InstancePrivateDnsNameOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ip.setter
    def private_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicDns")
    def public_dns(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_dns.setter
    def public_dns(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_ip.setter
    def public_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootBlockDevice")
    def root_block_device(self) -> Optional[pulumi.Input[InstanceRootBlockDeviceArgs]]:
        
        ...
    
    @root_block_device.setter
    def root_block_device(self, value: Optional[pulumi.Input[InstanceRootBlockDeviceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryNetworkInterfaces")
    def secondary_network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceSecondaryNetworkInterfaceArgs]]]]:
        
        ...
    
    @secondary_network_interfaces.setter
    def secondary_network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceSecondaryNetworkInterfaceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryPrivateIps")
    def secondary_private_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @secondary_private_ips.setter
    def secondary_private_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    @_utilities.deprecated(...)
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDestCheck")
    def source_dest_check(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @source_dest_check.setter
    def source_dest_check(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotInstanceRequestId")
    def spot_instance_request_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @spot_instance_request_id.setter
    def spot_instance_request_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def tenancy(self) -> Optional[pulumi.Input[Union[_builtins.str, Tenancy]]]:
        
        ...
    
    @tenancy.setter
    def tenancy(self, value: Optional[pulumi.Input[Union[_builtins.str, Tenancy]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_data.setter
    def user_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDataBase64")
    def user_data_base64(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_data_base64.setter
    def user_data_base64(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDataReplaceOnChange")
    def user_data_replace_on_change(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @user_data_replace_on_change.setter
    def user_data_replace_on_change(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeTags")
    def volume_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @volume_tags.setter
    def volume_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:ec2/instance:Instance")
class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., ami: Optional[pulumi.Input[_builtins.str]] = ..., associate_public_ip_address: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., capacity_reservation_specification: Optional[pulumi.Input[Union[InstanceCapacityReservationSpecificationArgs, InstanceCapacityReservationSpecificationArgsDict]]] = ..., cpu_options: Optional[pulumi.Input[Union[InstanceCpuOptionsArgs, InstanceCpuOptionsArgsDict]]] = ..., credit_specification: Optional[pulumi.Input[Union[InstanceCreditSpecificationArgs, InstanceCreditSpecificationArgsDict]]] = ..., disable_api_stop: Optional[pulumi.Input[_builtins.bool]] = ..., disable_api_termination: Optional[pulumi.Input[_builtins.bool]] = ..., ebs_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceEbsBlockDeviceArgs, InstanceEbsBlockDeviceArgsDict]]]]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., enable_primary_ipv6: Optional[pulumi.Input[_builtins.bool]] = ..., enclave_options: Optional[pulumi.Input[Union[InstanceEnclaveOptionsArgs, InstanceEnclaveOptionsArgsDict]]] = ..., ephemeral_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceEphemeralBlockDeviceArgs, InstanceEphemeralBlockDeviceArgsDict]]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., get_password_data: Optional[pulumi.Input[_builtins.bool]] = ..., hibernation: Optional[pulumi.Input[_builtins.bool]] = ..., host_id: Optional[pulumi.Input[_builtins.str]] = ..., host_resource_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ..., instance_initiated_shutdown_behavior: Optional[pulumi.Input[_builtins.str]] = ..., instance_market_options: Optional[pulumi.Input[Union[InstanceInstanceMarketOptionsArgs, InstanceInstanceMarketOptionsArgsDict]]] = ..., instance_type: Optional[pulumi.Input[Union[_builtins.str, InstanceType]]] = ..., ipv6_address_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., key_name: Optional[pulumi.Input[_builtins.str]] = ..., launch_template: Optional[pulumi.Input[Union[InstanceLaunchTemplateArgs, InstanceLaunchTemplateArgsDict]]] = ..., maintenance_options: Optional[pulumi.Input[Union[InstanceMaintenanceOptionsArgs, InstanceMaintenanceOptionsArgsDict]]] = ..., metadata_options: Optional[pulumi.Input[Union[InstanceMetadataOptionsArgs, InstanceMetadataOptionsArgsDict]]] = ..., monitoring: Optional[pulumi.Input[_builtins.bool]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceNetworkInterfaceArgs, InstanceNetworkInterfaceArgsDict]]]]] = ..., placement_group: Optional[pulumi.Input[_builtins.str]] = ..., placement_group_id: Optional[pulumi.Input[_builtins.str]] = ..., placement_partition_number: Optional[pulumi.Input[_builtins.int]] = ..., primary_network_interface: Optional[pulumi.Input[Union[InstancePrimaryNetworkInterfaceArgs, InstancePrimaryNetworkInterfaceArgsDict]]] = ..., private_dns_name_options: Optional[pulumi.Input[Union[InstancePrivateDnsNameOptionsArgs, InstancePrivateDnsNameOptionsArgsDict]]] = ..., private_ip: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_block_device: Optional[pulumi.Input[Union[InstanceRootBlockDeviceArgs, InstanceRootBlockDeviceArgsDict]]] = ..., secondary_network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceSecondaryNetworkInterfaceArgs, InstanceSecondaryNetworkInterfaceArgsDict]]]]] = ..., secondary_private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_dest_check: Optional[pulumi.Input[_builtins.bool]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenancy: Optional[pulumi.Input[Union[_builtins.str, Tenancy]]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., user_data_base64: Optional[pulumi.Input[_builtins.str]] = ..., user_data_replace_on_change: Optional[pulumi.Input[_builtins.bool]] = ..., volume_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[InstanceArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., ami: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., associate_public_ip_address: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., capacity_reservation_specification: Optional[pulumi.Input[Union[InstanceCapacityReservationSpecificationArgs, InstanceCapacityReservationSpecificationArgsDict]]] = ..., cpu_options: Optional[pulumi.Input[Union[InstanceCpuOptionsArgs, InstanceCpuOptionsArgsDict]]] = ..., credit_specification: Optional[pulumi.Input[Union[InstanceCreditSpecificationArgs, InstanceCreditSpecificationArgsDict]]] = ..., disable_api_stop: Optional[pulumi.Input[_builtins.bool]] = ..., disable_api_termination: Optional[pulumi.Input[_builtins.bool]] = ..., ebs_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceEbsBlockDeviceArgs, InstanceEbsBlockDeviceArgsDict]]]]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., enable_primary_ipv6: Optional[pulumi.Input[_builtins.bool]] = ..., enclave_options: Optional[pulumi.Input[Union[InstanceEnclaveOptionsArgs, InstanceEnclaveOptionsArgsDict]]] = ..., ephemeral_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceEphemeralBlockDeviceArgs, InstanceEphemeralBlockDeviceArgsDict]]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., get_password_data: Optional[pulumi.Input[_builtins.bool]] = ..., hibernation: Optional[pulumi.Input[_builtins.bool]] = ..., host_id: Optional[pulumi.Input[_builtins.str]] = ..., host_resource_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ..., instance_initiated_shutdown_behavior: Optional[pulumi.Input[_builtins.str]] = ..., instance_lifecycle: Optional[pulumi.Input[_builtins.str]] = ..., instance_market_options: Optional[pulumi.Input[Union[InstanceInstanceMarketOptionsArgs, InstanceInstanceMarketOptionsArgsDict]]] = ..., instance_state: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[Union[_builtins.str, InstanceType]]] = ..., ipv6_address_count: Optional[pulumi.Input[_builtins.int]] = ..., ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., key_name: Optional[pulumi.Input[_builtins.str]] = ..., launch_template: Optional[pulumi.Input[Union[InstanceLaunchTemplateArgs, InstanceLaunchTemplateArgsDict]]] = ..., maintenance_options: Optional[pulumi.Input[Union[InstanceMaintenanceOptionsArgs, InstanceMaintenanceOptionsArgsDict]]] = ..., metadata_options: Optional[pulumi.Input[Union[InstanceMetadataOptionsArgs, InstanceMetadataOptionsArgsDict]]] = ..., monitoring: Optional[pulumi.Input[_builtins.bool]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceNetworkInterfaceArgs, InstanceNetworkInterfaceArgsDict]]]]] = ..., outpost_arn: Optional[pulumi.Input[_builtins.str]] = ..., password_data: Optional[pulumi.Input[_builtins.str]] = ..., placement_group: Optional[pulumi.Input[_builtins.str]] = ..., placement_group_id: Optional[pulumi.Input[_builtins.str]] = ..., placement_partition_number: Optional[pulumi.Input[_builtins.int]] = ..., primary_network_interface: Optional[pulumi.Input[Union[InstancePrimaryNetworkInterfaceArgs, InstancePrimaryNetworkInterfaceArgsDict]]] = ..., primary_network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., private_dns: Optional[pulumi.Input[_builtins.str]] = ..., private_dns_name_options: Optional[pulumi.Input[Union[InstancePrivateDnsNameOptionsArgs, InstancePrivateDnsNameOptionsArgsDict]]] = ..., private_ip: Optional[pulumi.Input[_builtins.str]] = ..., public_dns: Optional[pulumi.Input[_builtins.str]] = ..., public_ip: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_block_device: Optional[pulumi.Input[Union[InstanceRootBlockDeviceArgs, InstanceRootBlockDeviceArgsDict]]] = ..., secondary_network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceSecondaryNetworkInterfaceArgs, InstanceSecondaryNetworkInterfaceArgsDict]]]]] = ..., secondary_private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_dest_check: Optional[pulumi.Input[_builtins.bool]] = ..., spot_instance_request_id: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenancy: Optional[pulumi.Input[Union[_builtins.str, Tenancy]]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., user_data_base64: Optional[pulumi.Input[_builtins.str]] = ..., user_data_replace_on_change: Optional[pulumi.Input[_builtins.bool]] = ..., volume_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> Instance:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ami(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationSpecification")
    def capacity_reservation_specification(self) -> pulumi.Output[outputs.InstanceCapacityReservationSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuOptions")
    def cpu_options(self) -> pulumi.Output[outputs.InstanceCpuOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creditSpecification")
    def credit_specification(self) -> pulumi.Output[Optional[outputs.InstanceCreditSpecification]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableApiStop")
    def disable_api_stop(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableApiTermination")
    def disable_api_termination(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsBlockDevices")
    def ebs_block_devices(self) -> pulumi.Output[Sequence[outputs.InstanceEbsBlockDevice]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrimaryIpv6")
    def enable_primary_ipv6(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enclaveOptions")
    def enclave_options(self) -> pulumi.Output[outputs.InstanceEnclaveOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralBlockDevices")
    def ephemeral_block_devices(self) -> pulumi.Output[Sequence[outputs.InstanceEphemeralBlockDevice]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="getPasswordData")
    def get_password_data(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hibernation(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostResourceGroupArn")
    def host_resource_group_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceInitiatedShutdownBehavior")
    def instance_initiated_shutdown_behavior(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceLifecycle")
    def instance_lifecycle(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMarketOptions")
    def instance_market_options(self) -> pulumi.Output[outputs.InstanceInstanceMarketOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceState")
    def instance_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AddressCount")
    def ipv6_address_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplate")
    def launch_template(self) -> pulumi.Output[Optional[outputs.InstanceLaunchTemplate]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceOptions")
    def maintenance_options(self) -> pulumi.Output[outputs.InstanceMaintenanceOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataOptions")
    def metadata_options(self) -> pulumi.Output[outputs.InstanceMetadataOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    @_utilities.deprecated(...)
    def network_interfaces(self) -> pulumi.Output[Sequence[outputs.InstanceNetworkInterface]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordData")
    def password_data(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroup")
    def placement_group(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroupId")
    def placement_group_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementPartitionNumber")
    def placement_partition_number(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryNetworkInterface")
    def primary_network_interface(self) -> pulumi.Output[outputs.InstancePrimaryNetworkInterface]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryNetworkInterfaceId")
    def primary_network_interface_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDns")
    def private_dns(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsNameOptions")
    def private_dns_name_options(self) -> pulumi.Output[outputs.InstancePrivateDnsNameOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicDns")
    def public_dns(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootBlockDevice")
    def root_block_device(self) -> pulumi.Output[outputs.InstanceRootBlockDevice]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryNetworkInterfaces")
    def secondary_network_interfaces(self) -> pulumi.Output[Sequence[outputs.InstanceSecondaryNetworkInterface]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryPrivateIps")
    def secondary_private_ips(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    @_utilities.deprecated(...)
    def security_groups(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDestCheck")
    def source_dest_check(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotInstanceRequestId")
    def spot_instance_request_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[_builtins.str]:
        
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
    def tenancy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDataBase64")
    def user_data_base64(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDataReplaceOnChange")
    def user_data_replace_on_change(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeTags")
    def volume_tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    


