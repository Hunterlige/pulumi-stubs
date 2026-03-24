

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetInstanceResult', 'AwaitableGetInstanceResult', 'get_instance', 'get_instance_output']
@pulumi.output_type
class GetInstanceResult:
    
    def __init__(__self__, advanced_machine_features=..., allow_stopping_for_update=..., attached_disks=..., boot_disks=..., can_ip_forward=..., confidential_instance_configs=..., cpu_platform=..., creation_timestamp=..., current_status=..., deletion_protection=..., description=..., desired_status=..., effective_labels=..., enable_display=..., guest_accelerators=..., hostname=..., id=..., instance_encryption_keys=..., instance_id=..., key_revocation_action_type=..., label_fingerprint=..., labels=..., machine_type=..., metadata=..., metadata_fingerprint=..., metadata_startup_script=..., min_cpu_platform=..., name=..., network_interfaces=..., network_performance_configs=..., params=..., partner_metadata=..., project=..., pulumi_labels=..., reservation_affinities=..., resource_policies=..., schedulings=..., scratch_disks=..., self_link=..., service_accounts=..., shielded_instance_configs=..., tags=..., tags_fingerprint=..., zone=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(self) -> Sequence[outputs.GetInstanceAdvancedMachineFeatureResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowStoppingForUpdate")
    def allow_stopping_for_update(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachedDisks")
    def attached_disks(self) -> Sequence[outputs.GetInstanceAttachedDiskResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDisks")
    def boot_disks(self) -> Sequence[outputs.GetInstanceBootDiskResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canIpForward")
    def can_ip_forward(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceConfigs")
    def confidential_instance_configs(self) -> Sequence[outputs.GetInstanceConfidentialInstanceConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuPlatform")
    def cpu_platform(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentStatus")
    def current_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredStatus")
    def desired_status(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDisplay")
    def enable_display(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(self) -> Sequence[outputs.GetInstanceGuestAcceleratorResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceEncryptionKeys")
    def instance_encryption_keys(self) -> Sequence[outputs.GetInstanceInstanceEncryptionKeyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyRevocationActionType")
    def key_revocation_action_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataFingerprint")
    def metadata_fingerprint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataStartupScript")
    def metadata_startup_script(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Sequence[outputs.GetInstanceNetworkInterfaceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfigs")
    def network_performance_configs(self) -> Sequence[outputs.GetInstanceNetworkPerformanceConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Sequence[outputs.GetInstanceParamResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerMetadata")
    def partner_metadata(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservationAffinities")
    def reservation_affinities(self) -> Sequence[outputs.GetInstanceReservationAffinityResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedulings(self) -> Sequence[outputs.GetInstanceSchedulingResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scratchDisks")
    def scratch_disks(self) -> Sequence[outputs.GetInstanceScratchDiskResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccounts")
    def service_accounts(self) -> Sequence[outputs.GetInstanceServiceAccountResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfigs")
    def shielded_instance_configs(self) -> Sequence[outputs.GetInstanceShieldedInstanceConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsFingerprint")
    def tags_fingerprint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetInstanceResult(GetInstanceResult):
    def __await__(self): # -> Generator[Never, Any, GetInstanceResult]:
        ...
    


def get_instance(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., self_link: Optional[_builtins.str] = ..., zone: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInstanceResult:
    
    ...

def get_instance_output(name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., self_link: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInstanceResult]:
    
    ...

