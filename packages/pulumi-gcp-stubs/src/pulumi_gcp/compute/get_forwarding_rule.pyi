

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetForwardingRuleResult', 'AwaitableGetForwardingRuleResult', 'get_forwarding_rule', 'get_forwarding_rule_output']
@pulumi.output_type
class GetForwardingRuleResult:
    
    def __init__(__self__, all_ports=..., allow_global_access=..., allow_psc_global_access=..., backend_service=..., base_forwarding_rule=..., creation_timestamp=..., description=..., effective_labels=..., forwarding_rule_id=..., id=..., ip_address=..., ip_collection=..., ip_protocol=..., ip_version=..., is_mirroring_collector=..., label_fingerprint=..., labels=..., load_balancing_scheme=..., name=..., network=..., network_tier=..., no_automate_dns_zone=..., port_range=..., ports=..., project=..., psc_connection_id=..., psc_connection_status=..., pulumi_labels=..., recreate_closed_psc=..., region=..., self_link=..., service_directory_registrations=..., service_label=..., service_name=..., source_ip_ranges=..., subnetwork=..., target=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allPorts")
    def all_ports(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowGlobalAccess")
    def allow_global_access(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPscGlobalAccess")
    def allow_psc_global_access(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendService")
    def backend_service(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseForwardingRule")
    def base_forwarding_rule(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardingRuleId")
    def forwarding_rule_id(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipCollection")
    def ip_collection(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isMirroringCollector")
    def is_mirroring_collector(self) -> _builtins.bool:
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
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkTier")
    def network_tier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noAutomateDnsZone")
    def no_automate_dns_zone(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portRange")
    def port_range(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnectionStatus")
    def psc_connection_status(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recreateClosedPsc")
    def recreate_closed_psc(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryRegistrations")
    def service_directory_registrations(self) -> Sequence[outputs.GetForwardingRuleServiceDirectoryRegistrationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceLabel")
    def service_label(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str:
        ...
    


class AwaitableGetForwardingRuleResult(GetForwardingRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetForwardingRuleResult]:
        ...
    


def get_forwarding_rule(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetForwardingRuleResult:
    
    ...

def get_forwarding_rule_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetForwardingRuleResult]:
    
    ...

