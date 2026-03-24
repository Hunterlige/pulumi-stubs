import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInstanceTypeResult",
    "AwaitableGetInstanceTypeResult",
    "get_instance_type",
    "get_instance_type_output",
]

@pulumi.output_type
class GetInstanceTypeResult:
    def __init__(
        __self__,
        auto_recovery_supported=...,
        bandwidth_weightings=...,
        bare_metal=...,
        boot_modes=...,
        burstable_performance_supported=...,
        current_generation=...,
        dedicated_hosts_supported=...,
        default_cores=...,
        default_network_card_index=...,
        default_threads_per_core=...,
        default_vcpus=...,
        ebs_encryption_support=...,
        ebs_nvme_support=...,
        ebs_optimized_support=...,
        ebs_performance_baseline_bandwidth=...,
        ebs_performance_baseline_iops=...,
        ebs_performance_baseline_throughput=...,
        ebs_performance_maximum_bandwidth=...,
        ebs_performance_maximum_iops=...,
        ebs_performance_maximum_throughput=...,
        efa_maximum_interfaces=...,
        efa_supported=...,
        ena_srd_supported=...,
        ena_support=...,
        encryption_in_transit_supported=...,
        fpgas=...,
        free_tier_eligible=...,
        gpuses=...,
        hibernation_supported=...,
        hypervisor=...,
        id=...,
        inference_accelerators=...,
        instance_disks=...,
        instance_storage_supported=...,
        instance_type=...,
        ipv6_supported=...,
        maximum_ipv4_addresses_per_interface=...,
        maximum_ipv6_addresses_per_interface=...,
        maximum_network_cards=...,
        maximum_network_interfaces=...,
        media_accelerators=...,
        memory_size=...,
        network_cards=...,
        network_performance=...,
        neuron_devices=...,
        nitro_enclaves_support=...,
        nitro_tpm_support=...,
        nitro_tpm_supported_versions=...,
        phc_support=...,
        region=...,
        supported_architectures=...,
        supported_cpu_features=...,
        supported_placement_strategies=...,
        supported_root_device_types=...,
        supported_usages_classes=...,
        supported_virtualization_types=...,
        sustained_clock_speed=...,
        total_fpga_memory=...,
        total_gpu_memory=...,
        total_inference_memory=...,
        total_instance_storage=...,
        total_media_memory=...,
        total_neuron_device_memory=...,
        valid_cores=...,
        valid_threads_per_cores=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRecoverySupported")
    def auto_recovery_supported(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="bandwidthWeightings")
    def bandwidth_weightings(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bareMetal")
    def bare_metal(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="bootModes")
    def boot_modes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="burstablePerformanceSupported")
    def burstable_performance_supported(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="currentGeneration")
    def current_generation(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedHostsSupported")
    def dedicated_hosts_supported(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="defaultCores")
    def default_cores(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="defaultNetworkCardIndex")
    def default_network_card_index(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="defaultThreadsPerCore")
    def default_threads_per_core(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="defaultVcpus")
    def default_vcpus(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ebsEncryptionSupport")
    def ebs_encryption_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ebsNvmeSupport")
    def ebs_nvme_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ebsOptimizedSupport")
    def ebs_optimized_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ebsPerformanceBaselineBandwidth")
    def ebs_performance_baseline_bandwidth(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ebsPerformanceBaselineIops")
    def ebs_performance_baseline_iops(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ebsPerformanceBaselineThroughput")
    def ebs_performance_baseline_throughput(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="ebsPerformanceMaximumBandwidth")
    def ebs_performance_maximum_bandwidth(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ebsPerformanceMaximumIops")
    def ebs_performance_maximum_iops(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ebsPerformanceMaximumThroughput")
    def ebs_performance_maximum_throughput(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="efaMaximumInterfaces")
    def efa_maximum_interfaces(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="efaSupported")
    def efa_supported(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enaSrdSupported")
    def ena_srd_supported(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enaSupport")
    def ena_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptionInTransitSupported")
    def encryption_in_transit_supported(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def fpgas(self) -> Sequence[outputs.GetInstanceTypeFpgaResult]: ...
    @_builtins.property
    @pulumi.getter(name="freeTierEligible")
    def free_tier_eligible(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def gpuses(self) -> Sequence[outputs.GetInstanceTypeGpusResult]: ...
    @_builtins.property
    @pulumi.getter(name="hibernationSupported")
    def hibernation_supported(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def hypervisor(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inferenceAccelerators")
    def inference_accelerators(
        self,
    ) -> Sequence[outputs.GetInstanceTypeInferenceAcceleratorResult]: ...
    @_builtins.property
    @pulumi.getter(name="instanceDisks")
    def instance_disks(self) -> Sequence[outputs.GetInstanceTypeInstanceDiskResult]: ...
    @_builtins.property
    @pulumi.getter(name="instanceStorageSupported")
    def instance_storage_supported(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv6Supported")
    def ipv6_supported(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="maximumIpv4AddressesPerInterface")
    def maximum_ipv4_addresses_per_interface(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maximumIpv6AddressesPerInterface")
    def maximum_ipv6_addresses_per_interface(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maximumNetworkCards")
    def maximum_network_cards(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maximumNetworkInterfaces")
    def maximum_network_interfaces(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="mediaAccelerators")
    def media_accelerators(
        self,
    ) -> Sequence[outputs.GetInstanceTypeMediaAcceleratorResult]: ...
    @_builtins.property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="networkCards")
    def network_cards(self) -> Sequence[outputs.GetInstanceTypeNetworkCardResult]: ...
    @_builtins.property
    @pulumi.getter(name="networkPerformance")
    def network_performance(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="neuronDevices")
    def neuron_devices(self) -> Sequence[outputs.GetInstanceTypeNeuronDeviceResult]: ...
    @_builtins.property
    @pulumi.getter(name="nitroEnclavesSupport")
    def nitro_enclaves_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nitroTpmSupport")
    def nitro_tpm_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nitroTpmSupportedVersions")
    def nitro_tpm_supported_versions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="phcSupport")
    def phc_support(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportedArchitectures")
    def supported_architectures(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportedCpuFeatures")
    def supported_cpu_features(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportedPlacementStrategies")
    def supported_placement_strategies(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportedRootDeviceTypes")
    def supported_root_device_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportedUsagesClasses")
    def supported_usages_classes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportedVirtualizationTypes")
    def supported_virtualization_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sustainedClockSpeed")
    def sustained_clock_speed(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="totalFpgaMemory")
    def total_fpga_memory(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="totalGpuMemory")
    def total_gpu_memory(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="totalInferenceMemory")
    def total_inference_memory(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="totalInstanceStorage")
    def total_instance_storage(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="totalMediaMemory")
    def total_media_memory(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="totalNeuronDeviceMemory")
    def total_neuron_device_memory(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="validCores")
    def valid_cores(self) -> Sequence[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="validThreadsPerCores")
    def valid_threads_per_cores(self) -> Sequence[_builtins.int]: ...

class AwaitableGetInstanceTypeResult(GetInstanceTypeResult):
    def __await__(self): ...

def get_instance_type(
    instance_type: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInstanceTypeResult: ...
def get_instance_type_output(
    instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInstanceTypeResult]: ...
