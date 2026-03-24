import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListenerDefaultAction",
    "ListenerDefaultActionFixedResponse",
    "ListenerDefaultActionForward",
    "ListenerDefaultActionForwardTargetGroup",
    "ListenerRuleAction",
    "ListenerRuleActionFixedResponse",
    "ListenerRuleActionForward",
    "ListenerRuleActionForwardTargetGroup",
    "ListenerRuleMatch",
    "ListenerRuleMatchHttpMatch",
    "ListenerRuleMatchHttpMatchHeaderMatch",
    "ListenerRuleMatchHttpMatchHeaderMatchMatch",
    "ListenerRuleMatchHttpMatchPathMatch",
    "ListenerRuleMatchHttpMatchPathMatchMatch",
    ...,
    ...,
    ...,
    ...,
    "ResourceConfigurationTimeouts",
    "ResourceGatewayTimeouts",
    "ServiceDnsEntry",
    "ServiceNetworkResourceAssociationDnsEntry",
    "ServiceNetworkResourceAssociationTimeouts",
    "ServiceNetworkServiceAssociationDnsEntry",
    "ServiceNetworkVpcAssociationDnsOptions",
    "TargetGroupAttachmentTarget",
    "TargetGroupConfig",
    "TargetGroupConfigHealthCheck",
    "TargetGroupConfigHealthCheckMatcher",
    "GetListenerDefaultActionResult",
    "GetListenerDefaultActionFixedResponseResult",
    "GetListenerDefaultActionForwardResult",
    "GetListenerDefaultActionForwardTargetGroupResult",
    "GetServiceDnsEntryResult",
]

@pulumi.output_type
class ListenerDefaultAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fixed_response: Optional[outputs.ListenerDefaultActionFixedResponse] = ...,
        forwards: Optional[Sequence[outputs.ListenerDefaultActionForward]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedResponse")
    def fixed_response(
        self,
    ) -> Optional[outputs.ListenerDefaultActionFixedResponse]: ...
    @_builtins.property
    @pulumi.getter
    def forwards(self) -> Optional[Sequence[outputs.ListenerDefaultActionForward]]: ...

@pulumi.output_type
class ListenerDefaultActionFixedResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, status_code: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.int: ...

@pulumi.output_type
class ListenerDefaultActionForward(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_groups: Optional[
            Sequence[outputs.ListenerDefaultActionForwardTargetGroup]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetGroups")
    def target_groups(
        self,
    ) -> Optional[Sequence[outputs.ListenerDefaultActionForwardTargetGroup]]: ...

@pulumi.output_type
class ListenerDefaultActionForwardTargetGroup(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_group_identifier: Optional[_builtins.str] = ...,
        weight: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetGroupIdentifier")
    def target_group_identifier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ListenerRuleAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fixed_response: Optional[outputs.ListenerRuleActionFixedResponse] = ...,
        forward: Optional[outputs.ListenerRuleActionForward] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedResponse")
    def fixed_response(self) -> Optional[outputs.ListenerRuleActionFixedResponse]: ...
    @_builtins.property
    @pulumi.getter
    def forward(self) -> Optional[outputs.ListenerRuleActionForward]: ...

@pulumi.output_type
class ListenerRuleActionFixedResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, status_code: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.int: ...

@pulumi.output_type
class ListenerRuleActionForward(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_groups: Sequence[outputs.ListenerRuleActionForwardTargetGroup],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetGroups")
    def target_groups(
        self,
    ) -> Sequence[outputs.ListenerRuleActionForwardTargetGroup]: ...

@pulumi.output_type
class ListenerRuleActionForwardTargetGroup(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_group_identifier: _builtins.str,
        weight: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetGroupIdentifier")
    def target_group_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ListenerRuleMatch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, http_match: outputs.ListenerRuleMatchHttpMatch
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpMatch")
    def http_match(self) -> outputs.ListenerRuleMatchHttpMatch: ...

@pulumi.output_type
class ListenerRuleMatchHttpMatch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        header_matches: Optional[
            Sequence[outputs.ListenerRuleMatchHttpMatchHeaderMatch]
        ] = ...,
        method: Optional[_builtins.str] = ...,
        path_match: Optional[outputs.ListenerRuleMatchHttpMatchPathMatch] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerMatches")
    def header_matches(
        self,
    ) -> Optional[Sequence[outputs.ListenerRuleMatchHttpMatchHeaderMatch]]: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pathMatch")
    def path_match(self) -> Optional[outputs.ListenerRuleMatchHttpMatchPathMatch]: ...

@pulumi.output_type
class ListenerRuleMatchHttpMatchHeaderMatch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        match: outputs.ListenerRuleMatchHttpMatchHeaderMatchMatch,
        name: _builtins.str,
        case_sensitive: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> outputs.ListenerRuleMatchHttpMatchHeaderMatchMatch: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="caseSensitive")
    def case_sensitive(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ListenerRuleMatchHttpMatchHeaderMatchMatch(dict):
    def __init__(
        __self__,
        *,
        contains: Optional[_builtins.str] = ...,
        exact: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def contains(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListenerRuleMatchHttpMatchPathMatch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        match: outputs.ListenerRuleMatchHttpMatchPathMatchMatch,
        case_sensitive: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> outputs.ListenerRuleMatchHttpMatchPathMatchMatch: ...
    @_builtins.property
    @pulumi.getter(name="caseSensitive")
    def case_sensitive(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ListenerRuleMatchHttpMatchPathMatchMatch(dict):
    def __init__(
        __self__,
        *,
        exact: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceConfigurationResourceConfigurationDefinition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn_resource: Optional[
            outputs.ResourceConfigurationResourceConfigurationDefinitionArnResource
        ] = ...,
        dns_resource: Optional[
            outputs.ResourceConfigurationResourceConfigurationDefinitionDnsResource
        ] = ...,
        ip_resource: Optional[
            outputs.ResourceConfigurationResourceConfigurationDefinitionIpResource
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="arnResource")
    def arn_resource(
        self,
    ) -> Optional[
        outputs.ResourceConfigurationResourceConfigurationDefinitionArnResource
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dnsResource")
    def dns_resource(
        self,
    ) -> Optional[
        outputs.ResourceConfigurationResourceConfigurationDefinitionDnsResource
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ipResource")
    def ip_resource(
        self,
    ) -> Optional[
        outputs.ResourceConfigurationResourceConfigurationDefinitionIpResource
    ]: ...

@pulumi.output_type
class ResourceConfigurationResourceConfigurationDefinitionArnResource(dict):
    def __init__(__self__, *, arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...

@pulumi.output_type
class ResourceConfigurationResourceConfigurationDefinitionDnsResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, domain_name: _builtins.str, ip_address_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> _builtins.str: ...

@pulumi.output_type
class ResourceConfigurationResourceConfigurationDefinitionIpResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, ip_address: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str: ...

@pulumi.output_type
class ResourceConfigurationTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceGatewayTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceDnsEntry(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain_name: Optional[_builtins.str] = ...,
        hosted_zone_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceNetworkResourceAssociationDnsEntry(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, domain_name: _builtins.str, hosted_zone_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> _builtins.str: ...

@pulumi.output_type
class ServiceNetworkResourceAssociationTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceNetworkServiceAssociationDnsEntry(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain_name: Optional[_builtins.str] = ...,
        hosted_zone_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceNetworkVpcAssociationDnsOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        private_dns_preference: Optional[_builtins.str] = ...,
        private_dns_specified_domains: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateDnsPreference")
    def private_dns_preference(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateDnsSpecifiedDomains")
    def private_dns_specified_domains(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class TargetGroupAttachmentTarget(dict):
    def __init__(
        __self__, *, id: _builtins.str, port: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TargetGroupConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        health_check: Optional[outputs.TargetGroupConfigHealthCheck] = ...,
        ip_address_type: Optional[_builtins.str] = ...,
        lambda_event_structure_version: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        protocol: Optional[_builtins.str] = ...,
        protocol_version: Optional[_builtins.str] = ...,
        vpc_identifier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[outputs.TargetGroupConfigHealthCheck]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaEventStructureVersion")
    def lambda_event_structure_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcIdentifier")
    def vpc_identifier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TargetGroupConfigHealthCheck(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        health_check_interval_seconds: Optional[_builtins.int] = ...,
        health_check_timeout_seconds: Optional[_builtins.int] = ...,
        healthy_threshold_count: Optional[_builtins.int] = ...,
        matcher: Optional[outputs.TargetGroupConfigHealthCheckMatcher] = ...,
        path: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        protocol: Optional[_builtins.str] = ...,
        protocol_version: Optional[_builtins.str] = ...,
        unhealthy_threshold_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckIntervalSeconds")
    def health_check_interval_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckTimeoutSeconds")
    def health_check_timeout_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="healthyThresholdCount")
    def healthy_threshold_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def matcher(self) -> Optional[outputs.TargetGroupConfigHealthCheckMatcher]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThresholdCount")
    def unhealthy_threshold_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TargetGroupConfigHealthCheckMatcher(dict):
    def __init__(__self__, *, value: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetListenerDefaultActionResult(dict):
    def __init__(
        __self__,
        *,
        fixed_responses: Sequence[outputs.GetListenerDefaultActionFixedResponseResult],
        forwards: Sequence[outputs.GetListenerDefaultActionForwardResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedResponses")
    def fixed_responses(
        self,
    ) -> Sequence[outputs.GetListenerDefaultActionFixedResponseResult]: ...
    @_builtins.property
    @pulumi.getter
    def forwards(self) -> Sequence[outputs.GetListenerDefaultActionForwardResult]: ...

@pulumi.output_type
class GetListenerDefaultActionFixedResponseResult(dict):
    def __init__(__self__, *, status_code: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.int: ...

@pulumi.output_type
class GetListenerDefaultActionForwardResult(dict):
    def __init__(
        __self__,
        *,
        target_groups: Sequence[
            outputs.GetListenerDefaultActionForwardTargetGroupResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetGroups")
    def target_groups(
        self,
    ) -> Sequence[outputs.GetListenerDefaultActionForwardTargetGroupResult]: ...

@pulumi.output_type
class GetListenerDefaultActionForwardTargetGroupResult(dict):
    def __init__(
        __self__, *, target_group_identifier: _builtins.str, weight: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetGroupIdentifier")
    def target_group_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int: ...

@pulumi.output_type
class GetServiceDnsEntryResult(dict):
    def __init__(
        __self__, *, domain_name: _builtins.str, hosted_zone_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> _builtins.str: ...
