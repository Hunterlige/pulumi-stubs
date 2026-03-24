

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
__all__ = ['LaunchTemplateArgs', 'LaunchTemplate']
@pulumi.input_type
class LaunchTemplateArgs:
    def __init__(__self__, *, block_device_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateBlockDeviceMappingArgs]]]] = ..., capacity_reservation_specification: Optional[pulumi.Input[LaunchTemplateCapacityReservationSpecificationArgs]] = ..., cpu_options: Optional[pulumi.Input[LaunchTemplateCpuOptionsArgs]] = ..., credit_specification: Optional[pulumi.Input[LaunchTemplateCreditSpecificationArgs]] = ..., default_version: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disable_api_stop: Optional[pulumi.Input[_builtins.bool]] = ..., disable_api_termination: Optional[pulumi.Input[_builtins.bool]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.str]] = ..., enclave_options: Optional[pulumi.Input[LaunchTemplateEnclaveOptionsArgs]] = ..., hibernation_options: Optional[pulumi.Input[LaunchTemplateHibernationOptionsArgs]] = ..., iam_instance_profile: Optional[pulumi.Input[LaunchTemplateIamInstanceProfileArgs]] = ..., image_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_initiated_shutdown_behavior: Optional[pulumi.Input[_builtins.str]] = ..., instance_market_options: Optional[pulumi.Input[LaunchTemplateInstanceMarketOptionsArgs]] = ..., instance_requirements: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsArgs]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., kernel_id: Optional[pulumi.Input[_builtins.str]] = ..., key_name: Optional[pulumi.Input[_builtins.str]] = ..., license_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateLicenseSpecificationArgs]]]] = ..., maintenance_options: Optional[pulumi.Input[LaunchTemplateMaintenanceOptionsArgs]] = ..., metadata_options: Optional[pulumi.Input[LaunchTemplateMetadataOptionsArgs]] = ..., monitoring: Optional[pulumi.Input[LaunchTemplateMonitoringArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateNetworkInterfaceArgs]]]] = ..., network_performance_options: Optional[pulumi.Input[LaunchTemplateNetworkPerformanceOptionsArgs]] = ..., placement: Optional[pulumi.Input[LaunchTemplatePlacementArgs]] = ..., private_dns_name_options: Optional[pulumi.Input[LaunchTemplatePrivateDnsNameOptionsArgs]] = ..., ram_disk_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secondary_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateSecondaryInterfaceArgs]]]] = ..., security_group_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateTagSpecificationArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., update_default_version: Optional[pulumi.Input[_builtins.bool]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockDeviceMappings")
    def block_device_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateBlockDeviceMappingArgs]]]]:
        
        ...
    
    @block_device_mappings.setter
    def block_device_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateBlockDeviceMappingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationSpecification")
    def capacity_reservation_specification(self) -> Optional[pulumi.Input[LaunchTemplateCapacityReservationSpecificationArgs]]:
        
        ...
    
    @capacity_reservation_specification.setter
    def capacity_reservation_specification(self, value: Optional[pulumi.Input[LaunchTemplateCapacityReservationSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuOptions")
    def cpu_options(self) -> Optional[pulumi.Input[LaunchTemplateCpuOptionsArgs]]:
        
        ...
    
    @cpu_options.setter
    def cpu_options(self, value: Optional[pulumi.Input[LaunchTemplateCpuOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creditSpecification")
    def credit_specification(self) -> Optional[pulumi.Input[LaunchTemplateCreditSpecificationArgs]]:
        
        ...
    
    @credit_specification.setter
    def credit_specification(self, value: Optional[pulumi.Input[LaunchTemplateCreditSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultVersion")
    def default_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_version.setter
    def default_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ebs_optimized.setter
    def ebs_optimized(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enclaveOptions")
    def enclave_options(self) -> Optional[pulumi.Input[LaunchTemplateEnclaveOptionsArgs]]:
        
        ...
    
    @enclave_options.setter
    def enclave_options(self, value: Optional[pulumi.Input[LaunchTemplateEnclaveOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hibernationOptions")
    def hibernation_options(self) -> Optional[pulumi.Input[LaunchTemplateHibernationOptionsArgs]]:
        
        ...
    
    @hibernation_options.setter
    def hibernation_options(self, value: Optional[pulumi.Input[LaunchTemplateHibernationOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> Optional[pulumi.Input[LaunchTemplateIamInstanceProfileArgs]]:
        
        ...
    
    @iam_instance_profile.setter
    def iam_instance_profile(self, value: Optional[pulumi.Input[LaunchTemplateIamInstanceProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_id.setter
    def image_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def instance_market_options(self) -> Optional[pulumi.Input[LaunchTemplateInstanceMarketOptionsArgs]]:
        
        ...
    
    @instance_market_options.setter
    def instance_market_options(self, value: Optional[pulumi.Input[LaunchTemplateInstanceMarketOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRequirements")
    def instance_requirements(self) -> Optional[pulumi.Input[LaunchTemplateInstanceRequirementsArgs]]:
        
        ...
    
    @instance_requirements.setter
    def instance_requirements(self, value: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kernelId")
    def kernel_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kernel_id.setter
    def kernel_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseSpecifications")
    def license_specifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateLicenseSpecificationArgs]]]]:
        
        ...
    
    @license_specifications.setter
    def license_specifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateLicenseSpecificationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceOptions")
    def maintenance_options(self) -> Optional[pulumi.Input[LaunchTemplateMaintenanceOptionsArgs]]:
        
        ...
    
    @maintenance_options.setter
    def maintenance_options(self, value: Optional[pulumi.Input[LaunchTemplateMaintenanceOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataOptions")
    def metadata_options(self) -> Optional[pulumi.Input[LaunchTemplateMetadataOptionsArgs]]:
        
        ...
    
    @metadata_options.setter
    def metadata_options(self, value: Optional[pulumi.Input[LaunchTemplateMetadataOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> Optional[pulumi.Input[LaunchTemplateMonitoringArgs]]:
        
        ...
    
    @monitoring.setter
    def monitoring(self, value: Optional[pulumi.Input[LaunchTemplateMonitoringArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateNetworkInterfaceArgs]]]]:
        
        ...
    
    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateNetworkInterfaceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPerformanceOptions")
    def network_performance_options(self) -> Optional[pulumi.Input[LaunchTemplateNetworkPerformanceOptionsArgs]]:
        ...
    
    @network_performance_options.setter
    def network_performance_options(self, value: Optional[pulumi.Input[LaunchTemplateNetworkPerformanceOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def placement(self) -> Optional[pulumi.Input[LaunchTemplatePlacementArgs]]:
        
        ...
    
    @placement.setter
    def placement(self, value: Optional[pulumi.Input[LaunchTemplatePlacementArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsNameOptions")
    def private_dns_name_options(self) -> Optional[pulumi.Input[LaunchTemplatePrivateDnsNameOptionsArgs]]:
        
        ...
    
    @private_dns_name_options.setter
    def private_dns_name_options(self, value: Optional[pulumi.Input[LaunchTemplatePrivateDnsNameOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ramDiskId")
    def ram_disk_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ram_disk_id.setter
    def ram_disk_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryInterfaces")
    def secondary_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateSecondaryInterfaceArgs]]]]:
        
        ...
    
    @secondary_interfaces.setter
    def secondary_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateSecondaryInterfaceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupNames")
    def security_group_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_names.setter
    def security_group_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagSpecifications")
    def tag_specifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateTagSpecificationArgs]]]]:
        
        ...
    
    @tag_specifications.setter
    def tag_specifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateTagSpecificationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateDefaultVersion")
    def update_default_version(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @update_default_version.setter
    def update_default_version(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_data.setter
    def user_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _LaunchTemplateState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., block_device_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateBlockDeviceMappingArgs]]]] = ..., capacity_reservation_specification: Optional[pulumi.Input[LaunchTemplateCapacityReservationSpecificationArgs]] = ..., cpu_options: Optional[pulumi.Input[LaunchTemplateCpuOptionsArgs]] = ..., credit_specification: Optional[pulumi.Input[LaunchTemplateCreditSpecificationArgs]] = ..., default_version: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disable_api_stop: Optional[pulumi.Input[_builtins.bool]] = ..., disable_api_termination: Optional[pulumi.Input[_builtins.bool]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.str]] = ..., enclave_options: Optional[pulumi.Input[LaunchTemplateEnclaveOptionsArgs]] = ..., hibernation_options: Optional[pulumi.Input[LaunchTemplateHibernationOptionsArgs]] = ..., iam_instance_profile: Optional[pulumi.Input[LaunchTemplateIamInstanceProfileArgs]] = ..., image_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_initiated_shutdown_behavior: Optional[pulumi.Input[_builtins.str]] = ..., instance_market_options: Optional[pulumi.Input[LaunchTemplateInstanceMarketOptionsArgs]] = ..., instance_requirements: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsArgs]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., kernel_id: Optional[pulumi.Input[_builtins.str]] = ..., key_name: Optional[pulumi.Input[_builtins.str]] = ..., latest_version: Optional[pulumi.Input[_builtins.int]] = ..., license_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateLicenseSpecificationArgs]]]] = ..., maintenance_options: Optional[pulumi.Input[LaunchTemplateMaintenanceOptionsArgs]] = ..., metadata_options: Optional[pulumi.Input[LaunchTemplateMetadataOptionsArgs]] = ..., monitoring: Optional[pulumi.Input[LaunchTemplateMonitoringArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateNetworkInterfaceArgs]]]] = ..., network_performance_options: Optional[pulumi.Input[LaunchTemplateNetworkPerformanceOptionsArgs]] = ..., placement: Optional[pulumi.Input[LaunchTemplatePlacementArgs]] = ..., private_dns_name_options: Optional[pulumi.Input[LaunchTemplatePrivateDnsNameOptionsArgs]] = ..., ram_disk_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secondary_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateSecondaryInterfaceArgs]]]] = ..., security_group_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateTagSpecificationArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., update_default_version: Optional[pulumi.Input[_builtins.bool]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockDeviceMappings")
    def block_device_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateBlockDeviceMappingArgs]]]]:
        
        ...
    
    @block_device_mappings.setter
    def block_device_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateBlockDeviceMappingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationSpecification")
    def capacity_reservation_specification(self) -> Optional[pulumi.Input[LaunchTemplateCapacityReservationSpecificationArgs]]:
        
        ...
    
    @capacity_reservation_specification.setter
    def capacity_reservation_specification(self, value: Optional[pulumi.Input[LaunchTemplateCapacityReservationSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuOptions")
    def cpu_options(self) -> Optional[pulumi.Input[LaunchTemplateCpuOptionsArgs]]:
        
        ...
    
    @cpu_options.setter
    def cpu_options(self, value: Optional[pulumi.Input[LaunchTemplateCpuOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creditSpecification")
    def credit_specification(self) -> Optional[pulumi.Input[LaunchTemplateCreditSpecificationArgs]]:
        
        ...
    
    @credit_specification.setter
    def credit_specification(self, value: Optional[pulumi.Input[LaunchTemplateCreditSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultVersion")
    def default_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_version.setter
    def default_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ebs_optimized.setter
    def ebs_optimized(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enclaveOptions")
    def enclave_options(self) -> Optional[pulumi.Input[LaunchTemplateEnclaveOptionsArgs]]:
        
        ...
    
    @enclave_options.setter
    def enclave_options(self, value: Optional[pulumi.Input[LaunchTemplateEnclaveOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hibernationOptions")
    def hibernation_options(self) -> Optional[pulumi.Input[LaunchTemplateHibernationOptionsArgs]]:
        
        ...
    
    @hibernation_options.setter
    def hibernation_options(self, value: Optional[pulumi.Input[LaunchTemplateHibernationOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> Optional[pulumi.Input[LaunchTemplateIamInstanceProfileArgs]]:
        
        ...
    
    @iam_instance_profile.setter
    def iam_instance_profile(self, value: Optional[pulumi.Input[LaunchTemplateIamInstanceProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_id.setter
    def image_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def instance_market_options(self) -> Optional[pulumi.Input[LaunchTemplateInstanceMarketOptionsArgs]]:
        
        ...
    
    @instance_market_options.setter
    def instance_market_options(self, value: Optional[pulumi.Input[LaunchTemplateInstanceMarketOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRequirements")
    def instance_requirements(self) -> Optional[pulumi.Input[LaunchTemplateInstanceRequirementsArgs]]:
        
        ...
    
    @instance_requirements.setter
    def instance_requirements(self, value: Optional[pulumi.Input[LaunchTemplateInstanceRequirementsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kernelId")
    def kernel_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kernel_id.setter
    def kernel_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestVersion")
    def latest_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @latest_version.setter
    def latest_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseSpecifications")
    def license_specifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateLicenseSpecificationArgs]]]]:
        
        ...
    
    @license_specifications.setter
    def license_specifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateLicenseSpecificationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceOptions")
    def maintenance_options(self) -> Optional[pulumi.Input[LaunchTemplateMaintenanceOptionsArgs]]:
        
        ...
    
    @maintenance_options.setter
    def maintenance_options(self, value: Optional[pulumi.Input[LaunchTemplateMaintenanceOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataOptions")
    def metadata_options(self) -> Optional[pulumi.Input[LaunchTemplateMetadataOptionsArgs]]:
        
        ...
    
    @metadata_options.setter
    def metadata_options(self, value: Optional[pulumi.Input[LaunchTemplateMetadataOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> Optional[pulumi.Input[LaunchTemplateMonitoringArgs]]:
        
        ...
    
    @monitoring.setter
    def monitoring(self, value: Optional[pulumi.Input[LaunchTemplateMonitoringArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateNetworkInterfaceArgs]]]]:
        
        ...
    
    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateNetworkInterfaceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPerformanceOptions")
    def network_performance_options(self) -> Optional[pulumi.Input[LaunchTemplateNetworkPerformanceOptionsArgs]]:
        ...
    
    @network_performance_options.setter
    def network_performance_options(self, value: Optional[pulumi.Input[LaunchTemplateNetworkPerformanceOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def placement(self) -> Optional[pulumi.Input[LaunchTemplatePlacementArgs]]:
        
        ...
    
    @placement.setter
    def placement(self, value: Optional[pulumi.Input[LaunchTemplatePlacementArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsNameOptions")
    def private_dns_name_options(self) -> Optional[pulumi.Input[LaunchTemplatePrivateDnsNameOptionsArgs]]:
        
        ...
    
    @private_dns_name_options.setter
    def private_dns_name_options(self, value: Optional[pulumi.Input[LaunchTemplatePrivateDnsNameOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ramDiskId")
    def ram_disk_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ram_disk_id.setter
    def ram_disk_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryInterfaces")
    def secondary_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateSecondaryInterfaceArgs]]]]:
        
        ...
    
    @secondary_interfaces.setter
    def secondary_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateSecondaryInterfaceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupNames")
    def security_group_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_names.setter
    def security_group_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagSpecifications")
    def tag_specifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateTagSpecificationArgs]]]]:
        
        ...
    
    @tag_specifications.setter
    def tag_specifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchTemplateTagSpecificationArgs]]]]): # -> None:
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
    @pulumi.getter(name="updateDefaultVersion")
    def update_default_version(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @update_default_version.setter
    def update_default_version(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_data.setter
    def user_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:ec2/launchTemplate:LaunchTemplate")
class LaunchTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., block_device_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LaunchTemplateBlockDeviceMappingArgs, LaunchTemplateBlockDeviceMappingArgsDict]]]]] = ..., capacity_reservation_specification: Optional[pulumi.Input[Union[LaunchTemplateCapacityReservationSpecificationArgs, LaunchTemplateCapacityReservationSpecificationArgsDict]]] = ..., cpu_options: Optional[pulumi.Input[Union[LaunchTemplateCpuOptionsArgs, LaunchTemplateCpuOptionsArgsDict]]] = ..., credit_specification: Optional[pulumi.Input[Union[LaunchTemplateCreditSpecificationArgs, LaunchTemplateCreditSpecificationArgsDict]]] = ..., default_version: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disable_api_stop: Optional[pulumi.Input[_builtins.bool]] = ..., disable_api_termination: Optional[pulumi.Input[_builtins.bool]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.str]] = ..., enclave_options: Optional[pulumi.Input[Union[LaunchTemplateEnclaveOptionsArgs, LaunchTemplateEnclaveOptionsArgsDict]]] = ..., hibernation_options: Optional[pulumi.Input[Union[LaunchTemplateHibernationOptionsArgs, LaunchTemplateHibernationOptionsArgsDict]]] = ..., iam_instance_profile: Optional[pulumi.Input[Union[LaunchTemplateIamInstanceProfileArgs, LaunchTemplateIamInstanceProfileArgsDict]]] = ..., image_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_initiated_shutdown_behavior: Optional[pulumi.Input[_builtins.str]] = ..., instance_market_options: Optional[pulumi.Input[Union[LaunchTemplateInstanceMarketOptionsArgs, LaunchTemplateInstanceMarketOptionsArgsDict]]] = ..., instance_requirements: Optional[pulumi.Input[Union[LaunchTemplateInstanceRequirementsArgs, LaunchTemplateInstanceRequirementsArgsDict]]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., kernel_id: Optional[pulumi.Input[_builtins.str]] = ..., key_name: Optional[pulumi.Input[_builtins.str]] = ..., license_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LaunchTemplateLicenseSpecificationArgs, LaunchTemplateLicenseSpecificationArgsDict]]]]] = ..., maintenance_options: Optional[pulumi.Input[Union[LaunchTemplateMaintenanceOptionsArgs, LaunchTemplateMaintenanceOptionsArgsDict]]] = ..., metadata_options: Optional[pulumi.Input[Union[LaunchTemplateMetadataOptionsArgs, LaunchTemplateMetadataOptionsArgsDict]]] = ..., monitoring: Optional[pulumi.Input[Union[LaunchTemplateMonitoringArgs, LaunchTemplateMonitoringArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LaunchTemplateNetworkInterfaceArgs, LaunchTemplateNetworkInterfaceArgsDict]]]]] = ..., network_performance_options: Optional[pulumi.Input[Union[LaunchTemplateNetworkPerformanceOptionsArgs, LaunchTemplateNetworkPerformanceOptionsArgsDict]]] = ..., placement: Optional[pulumi.Input[Union[LaunchTemplatePlacementArgs, LaunchTemplatePlacementArgsDict]]] = ..., private_dns_name_options: Optional[pulumi.Input[Union[LaunchTemplatePrivateDnsNameOptionsArgs, LaunchTemplatePrivateDnsNameOptionsArgsDict]]] = ..., ram_disk_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secondary_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LaunchTemplateSecondaryInterfaceArgs, LaunchTemplateSecondaryInterfaceArgsDict]]]]] = ..., security_group_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LaunchTemplateTagSpecificationArgs, LaunchTemplateTagSpecificationArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., update_default_version: Optional[pulumi.Input[_builtins.bool]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[LaunchTemplateArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., block_device_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LaunchTemplateBlockDeviceMappingArgs, LaunchTemplateBlockDeviceMappingArgsDict]]]]] = ..., capacity_reservation_specification: Optional[pulumi.Input[Union[LaunchTemplateCapacityReservationSpecificationArgs, LaunchTemplateCapacityReservationSpecificationArgsDict]]] = ..., cpu_options: Optional[pulumi.Input[Union[LaunchTemplateCpuOptionsArgs, LaunchTemplateCpuOptionsArgsDict]]] = ..., credit_specification: Optional[pulumi.Input[Union[LaunchTemplateCreditSpecificationArgs, LaunchTemplateCreditSpecificationArgsDict]]] = ..., default_version: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disable_api_stop: Optional[pulumi.Input[_builtins.bool]] = ..., disable_api_termination: Optional[pulumi.Input[_builtins.bool]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.str]] = ..., enclave_options: Optional[pulumi.Input[Union[LaunchTemplateEnclaveOptionsArgs, LaunchTemplateEnclaveOptionsArgsDict]]] = ..., hibernation_options: Optional[pulumi.Input[Union[LaunchTemplateHibernationOptionsArgs, LaunchTemplateHibernationOptionsArgsDict]]] = ..., iam_instance_profile: Optional[pulumi.Input[Union[LaunchTemplateIamInstanceProfileArgs, LaunchTemplateIamInstanceProfileArgsDict]]] = ..., image_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_initiated_shutdown_behavior: Optional[pulumi.Input[_builtins.str]] = ..., instance_market_options: Optional[pulumi.Input[Union[LaunchTemplateInstanceMarketOptionsArgs, LaunchTemplateInstanceMarketOptionsArgsDict]]] = ..., instance_requirements: Optional[pulumi.Input[Union[LaunchTemplateInstanceRequirementsArgs, LaunchTemplateInstanceRequirementsArgsDict]]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., kernel_id: Optional[pulumi.Input[_builtins.str]] = ..., key_name: Optional[pulumi.Input[_builtins.str]] = ..., latest_version: Optional[pulumi.Input[_builtins.int]] = ..., license_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LaunchTemplateLicenseSpecificationArgs, LaunchTemplateLicenseSpecificationArgsDict]]]]] = ..., maintenance_options: Optional[pulumi.Input[Union[LaunchTemplateMaintenanceOptionsArgs, LaunchTemplateMaintenanceOptionsArgsDict]]] = ..., metadata_options: Optional[pulumi.Input[Union[LaunchTemplateMetadataOptionsArgs, LaunchTemplateMetadataOptionsArgsDict]]] = ..., monitoring: Optional[pulumi.Input[Union[LaunchTemplateMonitoringArgs, LaunchTemplateMonitoringArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LaunchTemplateNetworkInterfaceArgs, LaunchTemplateNetworkInterfaceArgsDict]]]]] = ..., network_performance_options: Optional[pulumi.Input[Union[LaunchTemplateNetworkPerformanceOptionsArgs, LaunchTemplateNetworkPerformanceOptionsArgsDict]]] = ..., placement: Optional[pulumi.Input[Union[LaunchTemplatePlacementArgs, LaunchTemplatePlacementArgsDict]]] = ..., private_dns_name_options: Optional[pulumi.Input[Union[LaunchTemplatePrivateDnsNameOptionsArgs, LaunchTemplatePrivateDnsNameOptionsArgsDict]]] = ..., ram_disk_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secondary_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LaunchTemplateSecondaryInterfaceArgs, LaunchTemplateSecondaryInterfaceArgsDict]]]]] = ..., security_group_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LaunchTemplateTagSpecificationArgs, LaunchTemplateTagSpecificationArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., update_default_version: Optional[pulumi.Input[_builtins.bool]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> LaunchTemplate:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockDeviceMappings")
    def block_device_mappings(self) -> pulumi.Output[Optional[Sequence[outputs.LaunchTemplateBlockDeviceMapping]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationSpecification")
    def capacity_reservation_specification(self) -> pulumi.Output[Optional[outputs.LaunchTemplateCapacityReservationSpecification]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuOptions")
    def cpu_options(self) -> pulumi.Output[Optional[outputs.LaunchTemplateCpuOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creditSpecification")
    def credit_specification(self) -> pulumi.Output[Optional[outputs.LaunchTemplateCreditSpecification]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultVersion")
    def default_version(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableApiStop")
    def disable_api_stop(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableApiTermination")
    def disable_api_termination(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enclaveOptions")
    def enclave_options(self) -> pulumi.Output[Optional[outputs.LaunchTemplateEnclaveOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hibernationOptions")
    def hibernation_options(self) -> pulumi.Output[Optional[outputs.LaunchTemplateHibernationOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> pulumi.Output[Optional[outputs.LaunchTemplateIamInstanceProfile]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceInitiatedShutdownBehavior")
    def instance_initiated_shutdown_behavior(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMarketOptions")
    def instance_market_options(self) -> pulumi.Output[Optional[outputs.LaunchTemplateInstanceMarketOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRequirements")
    def instance_requirements(self) -> pulumi.Output[Optional[outputs.LaunchTemplateInstanceRequirements]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kernelId")
    def kernel_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestVersion")
    def latest_version(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseSpecifications")
    def license_specifications(self) -> pulumi.Output[Optional[Sequence[outputs.LaunchTemplateLicenseSpecification]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceOptions")
    def maintenance_options(self) -> pulumi.Output[Optional[outputs.LaunchTemplateMaintenanceOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataOptions")
    def metadata_options(self) -> pulumi.Output[outputs.LaunchTemplateMetadataOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> pulumi.Output[Optional[outputs.LaunchTemplateMonitoring]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> pulumi.Output[Optional[Sequence[outputs.LaunchTemplateNetworkInterface]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPerformanceOptions")
    def network_performance_options(self) -> pulumi.Output[Optional[outputs.LaunchTemplateNetworkPerformanceOptions]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def placement(self) -> pulumi.Output[Optional[outputs.LaunchTemplatePlacement]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsNameOptions")
    def private_dns_name_options(self) -> pulumi.Output[Optional[outputs.LaunchTemplatePrivateDnsNameOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ramDiskId")
    def ram_disk_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryInterfaces")
    def secondary_interfaces(self) -> pulumi.Output[Optional[Sequence[outputs.LaunchTemplateSecondaryInterface]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupNames")
    def security_group_names(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagSpecifications")
    def tag_specifications(self) -> pulumi.Output[Optional[Sequence[outputs.LaunchTemplateTagSpecification]]]:
        
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
    @pulumi.getter(name="updateDefaultVersion")
    def update_default_version(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    


