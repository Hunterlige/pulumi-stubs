import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInstanceTemplateResult",
    "AwaitableGetInstanceTemplateResult",
    "get_instance_template",
    "get_instance_template_output",
]

@pulumi.output_type
class GetInstanceTemplateResult:
    def __init__(
        __self__,
        advanced_machine_features=...,
        can_ip_forward=...,
        confidential_instance_configs=...,
        creation_timestamp=...,
        description=...,
        disks=...,
        effective_labels=...,
        enable_display=...,
        filter=...,
        guest_accelerators=...,
        id=...,
        instance_description=...,
        key_revocation_action_type=...,
        labels=...,
        machine_type=...,
        metadata=...,
        metadata_fingerprint=...,
        metadata_startup_script=...,
        min_cpu_platform=...,
        most_recent=...,
        name=...,
        name_prefix=...,
        network_interfaces=...,
        network_performance_configs=...,
        numeric_id=...,
        partner_metadata=...,
        project=...,
        pulumi_labels=...,
        region=...,
        reservation_affinities=...,
        resource_manager_tags=...,
        resource_policies=...,
        schedulings=...,
        self_link=...,
        self_link_unique=...,
        service_accounts=...,
        shielded_instance_configs=...,
        tags=...,
        tags_fingerprint=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(
        self,
    ) -> Sequence[outputs.GetInstanceTemplateAdvancedMachineFeatureResult]: ...
    @_builtins.property
    @pulumi.getter(name="canIpForward")
    def can_ip_forward(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceConfigs")
    def confidential_instance_configs(
        self,
    ) -> Sequence[outputs.GetInstanceTemplateConfidentialInstanceConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Sequence[outputs.GetInstanceTemplateDiskResult]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableDisplay")
    def enable_display(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(
        self,
    ) -> Sequence[outputs.GetInstanceTemplateGuestAcceleratorResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceDescription")
    def instance_description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyRevocationActionType")
    def key_revocation_action_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metadataFingerprint")
    def metadata_fingerprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metadataStartupScript")
    def metadata_startup_script(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> Sequence[outputs.GetInstanceTemplateNetworkInterfaceResult]: ...
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfigs")
    def network_performance_configs(
        self,
    ) -> Sequence[outputs.GetInstanceTemplateNetworkPerformanceConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="numericId")
    def numeric_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="partnerMetadata")
    def partner_metadata(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinities")
    def reservation_affinities(
        self,
    ) -> Sequence[outputs.GetInstanceTemplateReservationAffinityResult]: ...
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def schedulings(self) -> Sequence[outputs.GetInstanceTemplateSchedulingResult]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selfLinkUnique")
    def self_link_unique(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccounts")
    def service_accounts(
        self,
    ) -> Sequence[outputs.GetInstanceTemplateServiceAccountResult]: ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfigs")
    def shielded_instance_configs(
        self,
    ) -> Sequence[outputs.GetInstanceTemplateShieldedInstanceConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tagsFingerprint")
    def tags_fingerprint(self) -> _builtins.str: ...

class AwaitableGetInstanceTemplateResult(GetInstanceTemplateResult):
    def __await__(self): ...

def get_instance_template(
    filter: Optional[_builtins.str] = ...,
    most_recent: Optional[_builtins.bool] = ...,
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    self_link_unique: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInstanceTemplateResult: ...
def get_instance_template_output(
    filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    most_recent: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    self_link_unique: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInstanceTemplateResult]: ...
