import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ProfilesAssociationTimeouts",
    "ProfilesProfileTimeouts",
    "ProfilesResourceAssociationTimeouts",
    "RecordAlias",
    "RecordCidrRoutingPolicy",
    "RecordFailoverRoutingPolicy",
    "RecordGeolocationRoutingPolicy",
    "RecordGeoproximityRoutingPolicy",
    "RecordGeoproximityRoutingPolicyCoordinate",
    "RecordLatencyRoutingPolicy",
    "RecordWeightedRoutingPolicy",
    "RecordsExclusiveResourceRecordSet",
    "RecordsExclusiveResourceRecordSetAliasTarget",
    "RecordsExclusiveResourceRecordSetCidrRoutingConfig",
    "RecordsExclusiveResourceRecordSetGeolocation",
    ...,
    ...,
    "RecordsExclusiveResourceRecordSetResourceRecord",
    "RecordsExclusiveTimeouts",
    "ResolverEndpointIpAddress",
    "ResolverRuleTargetIp",
    "ZoneVpc",
    "GetProfilesProfilesProfileResult",
    "GetQueryLogConfigFilterResult",
    "GetRecordsResourceRecordSetResult",
    "GetRecordsResourceRecordSetAliasTargetResult",
    "GetRecordsResourceRecordSetCidrRoutingConfigResult",
    "GetRecordsResourceRecordSetGeolocationResult",
    ...,
    ...,
    "GetRecordsResourceRecordSetResourceRecordResult",
    "GetResolverEndpointFilterResult",
    "GetResolverFirewallRulesFirewallRuleResult",
    "GetResolverRuleTargetIpResult",
    "GetTrafficPolicyDocumentEndpointResult",
    "GetTrafficPolicyDocumentRuleResult",
    ...,
    "GetTrafficPolicyDocumentRuleItemResult",
    "GetTrafficPolicyDocumentRuleLocationResult",
    "GetTrafficPolicyDocumentRulePrimaryResult",
    "GetTrafficPolicyDocumentRuleRegionResult",
    "GetTrafficPolicyDocumentRuleSecondaryResult",
]

@pulumi.output_type
class ProfilesAssociationTimeouts(dict):
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
class ProfilesProfileTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        read: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def read(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProfilesResourceAssociationTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        read: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def read(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RecordAlias(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        evaluate_target_health: _builtins.bool,
        name: _builtins.str,
        zone_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> _builtins.str: ...

@pulumi.output_type
class RecordCidrRoutingPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, collection_id: _builtins.str, location_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="locationName")
    def location_name(self) -> _builtins.str: ...

@pulumi.output_type
class RecordFailoverRoutingPolicy(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class RecordGeolocationRoutingPolicy(dict):
    def __init__(
        __self__,
        *,
        continent: Optional[_builtins.str] = ...,
        country: Optional[_builtins.str] = ...,
        subdivision: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def continent(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subdivision(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RecordGeoproximityRoutingPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aws_region: Optional[_builtins.str] = ...,
        bias: Optional[_builtins.int] = ...,
        coordinates: Optional[
            Sequence[outputs.RecordGeoproximityRoutingPolicyCoordinate]
        ] = ...,
        local_zone_group: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def bias(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def coordinates(
        self,
    ) -> Optional[Sequence[outputs.RecordGeoproximityRoutingPolicyCoordinate]]: ...
    @_builtins.property
    @pulumi.getter(name="localZoneGroup")
    def local_zone_group(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RecordGeoproximityRoutingPolicyCoordinate(dict):
    def __init__(
        __self__, *, latitude: _builtins.str, longitude: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def latitude(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def longitude(self) -> _builtins.str: ...

@pulumi.output_type
class RecordLatencyRoutingPolicy(dict):
    def __init__(__self__, *, region: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

@pulumi.output_type
class RecordWeightedRoutingPolicy(dict):
    def __init__(__self__, *, weight: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int: ...

@pulumi.output_type
class RecordsExclusiveResourceRecordSet(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        alias_target: Optional[
            outputs.RecordsExclusiveResourceRecordSetAliasTarget
        ] = ...,
        cidr_routing_config: Optional[
            outputs.RecordsExclusiveResourceRecordSetCidrRoutingConfig
        ] = ...,
        failover: Optional[_builtins.str] = ...,
        geolocation: Optional[
            outputs.RecordsExclusiveResourceRecordSetGeolocation
        ] = ...,
        geoproximity_location: Optional[
            outputs.RecordsExclusiveResourceRecordSetGeoproximityLocation
        ] = ...,
        health_check_id: Optional[_builtins.str] = ...,
        multi_value_answer: Optional[_builtins.bool] = ...,
        region: Optional[_builtins.str] = ...,
        resource_records: Optional[
            Sequence[outputs.RecordsExclusiveResourceRecordSetResourceRecord]
        ] = ...,
        set_identifier: Optional[_builtins.str] = ...,
        traffic_policy_instance_id: Optional[_builtins.str] = ...,
        ttl: Optional[_builtins.int] = ...,
        type: Optional[_builtins.str] = ...,
        weight: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="aliasTarget")
    def alias_target(
        self,
    ) -> Optional[outputs.RecordsExclusiveResourceRecordSetAliasTarget]: ...
    @_builtins.property
    @pulumi.getter(name="cidrRoutingConfig")
    def cidr_routing_config(
        self,
    ) -> Optional[outputs.RecordsExclusiveResourceRecordSetCidrRoutingConfig]: ...
    @_builtins.property
    @pulumi.getter
    def failover(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def geolocation(
        self,
    ) -> Optional[outputs.RecordsExclusiveResourceRecordSetGeolocation]: ...
    @_builtins.property
    @pulumi.getter(name="geoproximityLocation")
    def geoproximity_location(
        self,
    ) -> Optional[outputs.RecordsExclusiveResourceRecordSetGeoproximityLocation]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckId")
    def health_check_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="multiValueAnswer")
    def multi_value_answer(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceRecords")
    def resource_records(
        self,
    ) -> Optional[
        Sequence[outputs.RecordsExclusiveResourceRecordSetResourceRecord]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="setIdentifier")
    def set_identifier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trafficPolicyInstanceId")
    def traffic_policy_instance_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class RecordsExclusiveResourceRecordSetAliasTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_name: _builtins.str,
        evaluate_target_health: _builtins.bool,
        hosted_zone_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> _builtins.str: ...

@pulumi.output_type
class RecordsExclusiveResourceRecordSetCidrRoutingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, collection_id: _builtins.str, location_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="locationName")
    def location_name(self) -> _builtins.str: ...

@pulumi.output_type
class RecordsExclusiveResourceRecordSetGeolocation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        continent_code: Optional[_builtins.str] = ...,
        country_code: Optional[_builtins.str] = ...,
        subdivision_code: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="continentCode")
    def continent_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subdivisionCode")
    def subdivision_code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RecordsExclusiveResourceRecordSetGeoproximityLocation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aws_region: Optional[_builtins.str] = ...,
        bias: Optional[_builtins.int] = ...,
        coordinates: Optional[
            outputs.RecordsExclusiveResourceRecordSetGeoproximityLocationCoordinates
        ] = ...,
        local_zone_group: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def bias(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def coordinates(
        self,
    ) -> Optional[
        outputs.RecordsExclusiveResourceRecordSetGeoproximityLocationCoordinates
    ]: ...
    @_builtins.property
    @pulumi.getter(name="localZoneGroup")
    def local_zone_group(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RecordsExclusiveResourceRecordSetGeoproximityLocationCoordinates(dict):
    def __init__(
        __self__, *, latitude: _builtins.str, longitude: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def latitude(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def longitude(self) -> _builtins.str: ...

@pulumi.output_type
class RecordsExclusiveResourceRecordSetResourceRecord(dict):
    def __init__(__self__, *, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class RecordsExclusiveTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResolverEndpointIpAddress(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        subnet_id: _builtins.str,
        ip: Optional[_builtins.str] = ...,
        ip_id: Optional[_builtins.str] = ...,
        ipv6: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipId")
    def ip_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ipv6(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResolverRuleTargetIp(dict):
    def __init__(
        __self__,
        *,
        ip: Optional[_builtins.str] = ...,
        ipv6: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        protocol: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ipv6(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ZoneVpc(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, vpc_id: _builtins.str, vpc_region: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcRegion")
    def vpc_region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetProfilesProfilesProfileResult(dict):
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        id: _builtins.str,
        name: _builtins.str,
        share_status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shareStatus")
    def share_status(self) -> _builtins.str: ...

@pulumi.output_type
class GetQueryLogConfigFilterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetRecordsResourceRecordSetResult(dict):
    def __init__(
        __self__,
        *,
        alias_target: outputs.GetRecordsResourceRecordSetAliasTargetResult,
        cidr_routing_config: outputs.GetRecordsResourceRecordSetCidrRoutingConfigResult,
        failover: _builtins.str,
        geolocation: outputs.GetRecordsResourceRecordSetGeolocationResult,
        geoproximity_location: outputs.GetRecordsResourceRecordSetGeoproximityLocationResult,
        health_check_id: _builtins.str,
        multi_value_answer: _builtins.bool,
        name: _builtins.str,
        region: _builtins.str,
        resource_records: Sequence[
            outputs.GetRecordsResourceRecordSetResourceRecordResult
        ],
        set_identifier: _builtins.str,
        traffic_policy_instance_id: _builtins.str,
        ttl: _builtins.int,
        type: _builtins.str,
        weight: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aliasTarget")
    def alias_target(self) -> outputs.GetRecordsResourceRecordSetAliasTargetResult: ...
    @_builtins.property
    @pulumi.getter(name="cidrRoutingConfig")
    def cidr_routing_config(
        self,
    ) -> outputs.GetRecordsResourceRecordSetCidrRoutingConfigResult: ...
    @_builtins.property
    @pulumi.getter
    def failover(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def geolocation(self) -> outputs.GetRecordsResourceRecordSetGeolocationResult: ...
    @_builtins.property
    @pulumi.getter(name="geoproximityLocation")
    def geoproximity_location(
        self,
    ) -> outputs.GetRecordsResourceRecordSetGeoproximityLocationResult: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckId")
    def health_check_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="multiValueAnswer")
    def multi_value_answer(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceRecords")
    def resource_records(
        self,
    ) -> Sequence[outputs.GetRecordsResourceRecordSetResourceRecordResult]: ...
    @_builtins.property
    @pulumi.getter(name="setIdentifier")
    def set_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="trafficPolicyInstanceId")
    def traffic_policy_instance_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int: ...

@pulumi.output_type
class GetRecordsResourceRecordSetAliasTargetResult(dict):
    def __init__(
        __self__,
        *,
        dns_name: _builtins.str,
        evaluate_target_health: _builtins.bool,
        hosted_zone_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetRecordsResourceRecordSetCidrRoutingConfigResult(dict):
    def __init__(
        __self__, *, collection_id: _builtins.str, location_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="locationName")
    def location_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetRecordsResourceRecordSetGeolocationResult(dict):
    def __init__(
        __self__,
        *,
        continent_code: _builtins.str,
        country_code: _builtins.str,
        subdivision_code: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="continentCode")
    def continent_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subdivisionCode")
    def subdivision_code(self) -> _builtins.str: ...

@pulumi.output_type
class GetRecordsResourceRecordSetGeoproximityLocationResult(dict):
    def __init__(
        __self__,
        *,
        aws_region: _builtins.str,
        bias: _builtins.int,
        coordinates: outputs.GetRecordsResourceRecordSetGeoproximityLocationCoordinatesResult,
        local_zone_group: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def bias(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def coordinates(
        self,
    ) -> outputs.GetRecordsResourceRecordSetGeoproximityLocationCoordinatesResult: ...
    @_builtins.property
    @pulumi.getter(name="localZoneGroup")
    def local_zone_group(self) -> _builtins.str: ...

@pulumi.output_type
class GetRecordsResourceRecordSetGeoproximityLocationCoordinatesResult(dict):
    def __init__(
        __self__, *, latitude: _builtins.str, longitude: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def latitude(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def longitude(self) -> _builtins.str: ...

@pulumi.output_type
class GetRecordsResourceRecordSetResourceRecordResult(dict):
    def __init__(__self__, *, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetResolverEndpointFilterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetResolverFirewallRulesFirewallRuleResult(dict):
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        block_override_dns_type: _builtins.str,
        block_override_domain: _builtins.str,
        block_override_ttl: _builtins.int,
        block_response: _builtins.str,
        confidence_threshold: _builtins.str,
        creation_time: _builtins.str,
        creator_request_id: _builtins.str,
        dns_threat_protection: _builtins.str,
        firewall_domain_list_id: _builtins.str,
        firewall_domain_redirection_action: _builtins.str,
        firewall_rule_group_id: _builtins.str,
        firewall_threat_protection_id: _builtins.str,
        modification_time: _builtins.str,
        name: _builtins.str,
        priority: _builtins.int,
        q_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="blockOverrideDnsType")
    def block_override_dns_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="blockOverrideDomain")
    def block_override_domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="blockOverrideTtl")
    def block_override_ttl(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="blockResponse")
    def block_response(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="confidenceThreshold")
    def confidence_threshold(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creatorRequestId")
    def creator_request_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsThreatProtection")
    def dns_threat_protection(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="firewallDomainListId")
    def firewall_domain_list_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="firewallDomainRedirectionAction")
    def firewall_domain_redirection_action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="firewallRuleGroupId")
    def firewall_rule_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="firewallThreatProtectionId")
    def firewall_threat_protection_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modificationTime")
    def modification_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="qType")
    def q_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetResolverRuleTargetIpResult(dict):
    def __init__(
        __self__,
        *,
        ip: _builtins.str,
        ipv6: _builtins.str,
        port: _builtins.int,
        protocol: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ipv6(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...

@pulumi.output_type
class GetTrafficPolicyDocumentEndpointResult(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        region: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetTrafficPolicyDocumentRuleResult(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        geo_proximity_locations: Optional[
            Sequence[outputs.GetTrafficPolicyDocumentRuleGeoProximityLocationResult]
        ] = ...,
        items: Optional[Sequence[outputs.GetTrafficPolicyDocumentRuleItemResult]] = ...,
        locations: Optional[
            Sequence[outputs.GetTrafficPolicyDocumentRuleLocationResult]
        ] = ...,
        primary: Optional[outputs.GetTrafficPolicyDocumentRulePrimaryResult] = ...,
        regions: Optional[
            Sequence[outputs.GetTrafficPolicyDocumentRuleRegionResult]
        ] = ...,
        secondary: Optional[outputs.GetTrafficPolicyDocumentRuleSecondaryResult] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="geoProximityLocations")
    def geo_proximity_locations(
        self,
    ) -> Optional[
        Sequence[outputs.GetTrafficPolicyDocumentRuleGeoProximityLocationResult]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[Sequence[outputs.GetTrafficPolicyDocumentRuleItemResult]]: ...
    @_builtins.property
    @pulumi.getter
    def locations(
        self,
    ) -> Optional[Sequence[outputs.GetTrafficPolicyDocumentRuleLocationResult]]: ...
    @_builtins.property
    @pulumi.getter
    def primary(
        self,
    ) -> Optional[outputs.GetTrafficPolicyDocumentRulePrimaryResult]: ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[Sequence[outputs.GetTrafficPolicyDocumentRuleRegionResult]]: ...
    @_builtins.property
    @pulumi.getter
    def secondary(
        self,
    ) -> Optional[outputs.GetTrafficPolicyDocumentRuleSecondaryResult]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetTrafficPolicyDocumentRuleGeoProximityLocationResult(dict):
    def __init__(
        __self__,
        *,
        bias: Optional[_builtins.str] = ...,
        endpoint_reference: Optional[_builtins.str] = ...,
        evaluate_target_health: Optional[_builtins.bool] = ...,
        health_check: Optional[_builtins.str] = ...,
        latitude: Optional[_builtins.str] = ...,
        longitude: Optional[_builtins.str] = ...,
        region: Optional[_builtins.str] = ...,
        rule_reference: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointReference")
    def endpoint_reference(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def latitude(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def longitude(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleReference")
    def rule_reference(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetTrafficPolicyDocumentRuleItemResult(dict):
    def __init__(
        __self__,
        *,
        endpoint_reference: Optional[_builtins.str] = ...,
        health_check: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointReference")
    def endpoint_reference(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetTrafficPolicyDocumentRuleLocationResult(dict):
    def __init__(
        __self__,
        *,
        continent: Optional[_builtins.str] = ...,
        country: Optional[_builtins.str] = ...,
        endpoint_reference: Optional[_builtins.str] = ...,
        evaluate_target_health: Optional[_builtins.bool] = ...,
        health_check: Optional[_builtins.str] = ...,
        is_default: Optional[_builtins.bool] = ...,
        rule_reference: Optional[_builtins.str] = ...,
        subdivision: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def continent(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointReference")
    def endpoint_reference(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ruleReference")
    def rule_reference(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subdivision(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetTrafficPolicyDocumentRulePrimaryResult(dict):
    def __init__(
        __self__,
        *,
        endpoint_reference: Optional[_builtins.str] = ...,
        evaluate_target_health: Optional[_builtins.bool] = ...,
        health_check: Optional[_builtins.str] = ...,
        rule_reference: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointReference")
    def endpoint_reference(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleReference")
    def rule_reference(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetTrafficPolicyDocumentRuleRegionResult(dict):
    def __init__(
        __self__,
        *,
        endpoint_reference: Optional[_builtins.str] = ...,
        evaluate_target_health: Optional[_builtins.bool] = ...,
        health_check: Optional[_builtins.str] = ...,
        region: Optional[_builtins.str] = ...,
        rule_reference: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointReference")
    def endpoint_reference(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleReference")
    def rule_reference(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetTrafficPolicyDocumentRuleSecondaryResult(dict):
    def __init__(
        __self__,
        *,
        endpoint_reference: Optional[_builtins.str] = ...,
        evaluate_target_health: Optional[_builtins.bool] = ...,
        health_check: Optional[_builtins.str] = ...,
        rule_reference: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointReference")
    def endpoint_reference(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleReference")
    def rule_reference(self) -> Optional[_builtins.str]: ...
