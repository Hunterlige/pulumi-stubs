import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGlobalForwardingRuleResult",
    "AwaitableGetGlobalForwardingRuleResult",
    "get_global_forwarding_rule",
    "get_global_forwarding_rule_output",
]

@pulumi.output_type
class GetGlobalForwardingRuleResult:
    def __init__(
        __self__,
        allow_psc_global_access=...,
        base_forwarding_rule=...,
        description=...,
        effective_labels=...,
        external_managed_backend_bucket_migration_state=...,
        external_managed_backend_bucket_migration_testing_percentage=...,
        forwarding_rule_id=...,
        id=...,
        ip_address=...,
        ip_protocol=...,
        ip_version=...,
        label_fingerprint=...,
        labels=...,
        load_balancing_scheme=...,
        metadata_filters=...,
        name=...,
        network=...,
        network_tier=...,
        no_automate_dns_zone=...,
        port_range=...,
        project=...,
        psc_connection_id=...,
        psc_connection_status=...,
        pulumi_labels=...,
        self_link=...,
        service_directory_registrations=...,
        source_ip_ranges=...,
        subnetwork=...,
        target=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPscGlobalAccess")
    def allow_psc_global_access(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="baseForwardingRule")
    def base_forwarding_rule(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalManagedBackendBucketMigrationState")
    def external_managed_backend_bucket_migration_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def external_managed_backend_bucket_migration_testing_percentage(
        self,
    ) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="forwardingRuleId")
    def forwarding_rule_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metadataFilters")
    def metadata_filters(
        self,
    ) -> Sequence[outputs.GetGlobalForwardingRuleMetadataFilterResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="noAutomateDnsZone")
    def no_automate_dns_zone(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="portRange")
    def port_range(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionStatus")
    def psc_connection_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryRegistrations")
    def service_directory_registrations(
        self,
    ) -> Sequence[
        outputs.GetGlobalForwardingRuleServiceDirectoryRegistrationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...

class AwaitableGetGlobalForwardingRuleResult(GetGlobalForwardingRuleResult):
    def __await__(self): ...

def get_global_forwarding_rule(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGlobalForwardingRuleResult: ...
def get_global_forwarding_rule_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGlobalForwardingRuleResult]: ...
