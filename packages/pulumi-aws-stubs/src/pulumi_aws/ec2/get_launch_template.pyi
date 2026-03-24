

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLaunchTemplateResult', 'AwaitableGetLaunchTemplateResult', 'get_launch_template', 'get_launch_template_output']
@pulumi.output_type
class GetLaunchTemplateResult:
    
    def __init__(__self__, arn=..., block_device_mappings=..., capacity_reservation_specifications=..., cpu_options=..., credit_specifications=..., default_version=..., description=..., disable_api_stop=..., disable_api_termination=..., ebs_optimized=..., enclave_options=..., filters=..., hibernation_options=..., iam_instance_profiles=..., id=..., image_id=..., instance_initiated_shutdown_behavior=..., instance_market_options=..., instance_requirements=..., instance_type=..., kernel_id=..., key_name=..., latest_version=..., license_specifications=..., maintenance_options=..., metadata_options=..., monitorings=..., name=..., network_interfaces=..., network_performance_options=..., placements=..., private_dns_name_options=..., ram_disk_id=..., region=..., secondary_interfaces=..., security_group_names=..., tag_specifications=..., tags=..., user_data=..., vpc_security_group_ids=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockDeviceMappings")
    def block_device_mappings(self) -> Sequence[outputs.GetLaunchTemplateBlockDeviceMappingResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservationSpecifications")
    def capacity_reservation_specifications(self) -> Sequence[outputs.GetLaunchTemplateCapacityReservationSpecificationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuOptions")
    def cpu_options(self) -> Sequence[outputs.GetLaunchTemplateCpuOptionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creditSpecifications")
    def credit_specifications(self) -> Sequence[outputs.GetLaunchTemplateCreditSpecificationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultVersion")
    def default_version(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableApiStop")
    def disable_api_stop(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableApiTermination")
    def disable_api_termination(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enclaveOptions")
    def enclave_options(self) -> Sequence[outputs.GetLaunchTemplateEnclaveOptionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetLaunchTemplateFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hibernationOptions")
    def hibernation_options(self) -> Sequence[outputs.GetLaunchTemplateHibernationOptionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfiles")
    def iam_instance_profiles(self) -> Sequence[outputs.GetLaunchTemplateIamInstanceProfileResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceInitiatedShutdownBehavior")
    def instance_initiated_shutdown_behavior(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMarketOptions")
    def instance_market_options(self) -> Sequence[outputs.GetLaunchTemplateInstanceMarketOptionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRequirements")
    def instance_requirements(self) -> Sequence[outputs.GetLaunchTemplateInstanceRequirementResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kernelId")
    def kernel_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestVersion")
    def latest_version(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseSpecifications")
    def license_specifications(self) -> Sequence[outputs.GetLaunchTemplateLicenseSpecificationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceOptions")
    def maintenance_options(self) -> Sequence[outputs.GetLaunchTemplateMaintenanceOptionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataOptions")
    def metadata_options(self) -> Sequence[outputs.GetLaunchTemplateMetadataOptionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitorings(self) -> Sequence[outputs.GetLaunchTemplateMonitoringResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Sequence[outputs.GetLaunchTemplateNetworkInterfaceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPerformanceOptions")
    def network_performance_options(self) -> Sequence[outputs.GetLaunchTemplateNetworkPerformanceOptionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def placements(self) -> Sequence[outputs.GetLaunchTemplatePlacementResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsNameOptions")
    def private_dns_name_options(self) -> Sequence[outputs.GetLaunchTemplatePrivateDnsNameOptionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ramDiskId")
    def ram_disk_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryInterfaces")
    def secondary_interfaces(self) -> Sequence[outputs.GetLaunchTemplateSecondaryInterfaceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupNames")
    def security_group_names(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagSpecifications")
    def tag_specifications(self) -> Sequence[outputs.GetLaunchTemplateTagSpecificationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Sequence[_builtins.str]:
        ...
    


class AwaitableGetLaunchTemplateResult(GetLaunchTemplateResult):
    def __await__(self): # -> Generator[Never, Any, GetLaunchTemplateResult]:
        ...
    


def get_launch_template(filters: Optional[Sequence[Union[GetLaunchTemplateFilterArgs, GetLaunchTemplateFilterArgsDict]]] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLaunchTemplateResult:
    
    ...

def get_launch_template_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetLaunchTemplateFilterArgs, GetLaunchTemplateFilterArgsDict]]]]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLaunchTemplateResult]:
    
    ...

