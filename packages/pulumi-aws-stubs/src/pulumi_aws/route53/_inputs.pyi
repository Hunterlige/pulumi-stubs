import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ProfilesAssociationTimeoutsArgs",
    "ProfilesAssociationTimeoutsArgsDict",
    "ProfilesProfileTimeoutsArgs",
    "ProfilesProfileTimeoutsArgsDict",
    "ProfilesResourceAssociationTimeoutsArgs",
    "ProfilesResourceAssociationTimeoutsArgsDict",
    "RecordAliasArgs",
    "RecordAliasArgsDict",
    "RecordCidrRoutingPolicyArgs",
    "RecordCidrRoutingPolicyArgsDict",
    "RecordFailoverRoutingPolicyArgs",
    "RecordFailoverRoutingPolicyArgsDict",
    "RecordGeolocationRoutingPolicyArgs",
    "RecordGeolocationRoutingPolicyArgsDict",
    "RecordGeoproximityRoutingPolicyArgs",
    "RecordGeoproximityRoutingPolicyArgsDict",
    "RecordGeoproximityRoutingPolicyCoordinateArgs",
    "RecordGeoproximityRoutingPolicyCoordinateArgsDict",
    "RecordLatencyRoutingPolicyArgs",
    "RecordLatencyRoutingPolicyArgsDict",
    "RecordWeightedRoutingPolicyArgs",
    "RecordWeightedRoutingPolicyArgsDict",
    "RecordsExclusiveResourceRecordSetArgs",
    "RecordsExclusiveResourceRecordSetArgsDict",
    "RecordsExclusiveResourceRecordSetAliasTargetArgs",
    ...,
    ...,
    ...,
    "RecordsExclusiveResourceRecordSetGeolocationArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "RecordsExclusiveTimeoutsArgs",
    "RecordsExclusiveTimeoutsArgsDict",
    "ResolverEndpointIpAddressArgs",
    "ResolverEndpointIpAddressArgsDict",
    "ResolverRuleTargetIpArgs",
    "ResolverRuleTargetIpArgsDict",
    "ZoneVpcArgs",
    "ZoneVpcArgsDict",
    "GetQueryLogConfigFilterArgs",
    "GetQueryLogConfigFilterArgsDict",
    "GetResolverEndpointFilterArgs",
    "GetResolverEndpointFilterArgsDict",
    "GetTrafficPolicyDocumentEndpointArgs",
    "GetTrafficPolicyDocumentEndpointArgsDict",
    "GetTrafficPolicyDocumentRuleArgs",
    "GetTrafficPolicyDocumentRuleArgsDict",
    ...,
    ...,
    "GetTrafficPolicyDocumentRuleItemArgs",
    "GetTrafficPolicyDocumentRuleItemArgsDict",
    "GetTrafficPolicyDocumentRuleLocationArgs",
    "GetTrafficPolicyDocumentRuleLocationArgsDict",
    "GetTrafficPolicyDocumentRulePrimaryArgs",
    "GetTrafficPolicyDocumentRulePrimaryArgsDict",
    "GetTrafficPolicyDocumentRuleRegionArgs",
    "GetTrafficPolicyDocumentRuleRegionArgsDict",
    "GetTrafficPolicyDocumentRuleSecondaryArgs",
    "GetTrafficPolicyDocumentRuleSecondaryArgsDict",
]

class ProfilesAssociationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ProfilesAssociationTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProfilesProfileTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    read: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ProfilesProfileTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        read: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def read(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @read.setter
    def read(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProfilesResourceAssociationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    read: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ProfilesResourceAssociationTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        read: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def read(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @read.setter
    def read(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RecordAliasArgsDict(TypedDict):
    evaluate_target_health: pulumi.Input[_builtins.bool]
    name: pulumi.Input[_builtins.str]
    zone_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RecordAliasArgs:
    def __init__(
        __self__,
        *,
        evaluate_target_health: pulumi.Input[_builtins.bool],
        name: pulumi.Input[_builtins.str],
        zone_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> pulumi.Input[_builtins.bool]: ...
    @evaluate_target_health.setter
    def evaluate_target_health(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[_builtins.str]: ...
    @zone_id.setter
    def zone_id(self, value: pulumi.Input[_builtins.str]): ...

class RecordCidrRoutingPolicyArgsDict(TypedDict):
    collection_id: pulumi.Input[_builtins.str]
    location_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RecordCidrRoutingPolicyArgs:
    def __init__(
        __self__,
        *,
        collection_id: pulumi.Input[_builtins.str],
        location_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Input[_builtins.str]: ...
    @collection_id.setter
    def collection_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="locationName")
    def location_name(self) -> pulumi.Input[_builtins.str]: ...
    @location_name.setter
    def location_name(self, value: pulumi.Input[_builtins.str]): ...

class RecordFailoverRoutingPolicyArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RecordFailoverRoutingPolicyArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class RecordGeolocationRoutingPolicyArgsDict(TypedDict):
    continent: NotRequired[pulumi.Input[_builtins.str]]
    country: NotRequired[pulumi.Input[_builtins.str]]
    subdivision: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RecordGeolocationRoutingPolicyArgs:
    def __init__(
        __self__,
        *,
        continent: Optional[pulumi.Input[_builtins.str]] = ...,
        country: Optional[pulumi.Input[_builtins.str]] = ...,
        subdivision: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def continent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @continent.setter
    def continent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @country.setter
    def country(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subdivision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subdivision.setter
    def subdivision(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RecordGeoproximityRoutingPolicyArgsDict(TypedDict):
    aws_region: NotRequired[pulumi.Input[_builtins.str]]
    bias: NotRequired[pulumi.Input[_builtins.int]]
    coordinates: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[RecordGeoproximityRoutingPolicyCoordinateArgsDict]]
        ]
    ]
    local_zone_group: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RecordGeoproximityRoutingPolicyArgs:
    def __init__(
        __self__,
        *,
        aws_region: Optional[pulumi.Input[_builtins.str]] = ...,
        bias: Optional[pulumi.Input[_builtins.int]] = ...,
        coordinates: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RecordGeoproximityRoutingPolicyCoordinateArgs]]
            ]
        ] = ...,
        local_zone_group: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_region.setter
    def aws_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def bias(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @bias.setter
    def bias(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def coordinates(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[RecordGeoproximityRoutingPolicyCoordinateArgs]]
        ]
    ]: ...
    @coordinates.setter
    def coordinates(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RecordGeoproximityRoutingPolicyCoordinateArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localZoneGroup")
    def local_zone_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_zone_group.setter
    def local_zone_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RecordGeoproximityRoutingPolicyCoordinateArgsDict(TypedDict):
    latitude: pulumi.Input[_builtins.str]
    longitude: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RecordGeoproximityRoutingPolicyCoordinateArgs:
    def __init__(
        __self__,
        *,
        latitude: pulumi.Input[_builtins.str],
        longitude: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def latitude(self) -> pulumi.Input[_builtins.str]: ...
    @latitude.setter
    def latitude(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def longitude(self) -> pulumi.Input[_builtins.str]: ...
    @longitude.setter
    def longitude(self, value: pulumi.Input[_builtins.str]): ...

class RecordLatencyRoutingPolicyArgsDict(TypedDict):
    region: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RecordLatencyRoutingPolicyArgs:
    def __init__(__self__, *, region: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...

class RecordWeightedRoutingPolicyArgsDict(TypedDict):
    weight: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class RecordWeightedRoutingPolicyArgs:
    def __init__(__self__, *, weight: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> pulumi.Input[_builtins.int]: ...
    @weight.setter
    def weight(self, value: pulumi.Input[_builtins.int]): ...

class RecordsExclusiveResourceRecordSetArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    alias_target: NotRequired[
        pulumi.Input[RecordsExclusiveResourceRecordSetAliasTargetArgsDict]
    ]
    cidr_routing_config: NotRequired[
        pulumi.Input[RecordsExclusiveResourceRecordSetCidrRoutingConfigArgsDict]
    ]
    failover: NotRequired[pulumi.Input[_builtins.str]]
    geolocation: NotRequired[
        pulumi.Input[RecordsExclusiveResourceRecordSetGeolocationArgsDict]
    ]
    geoproximity_location: NotRequired[
        pulumi.Input[RecordsExclusiveResourceRecordSetGeoproximityLocationArgsDict]
    ]
    health_check_id: NotRequired[pulumi.Input[_builtins.str]]
    multi_value_answer: NotRequired[pulumi.Input[_builtins.bool]]
    region: NotRequired[pulumi.Input[_builtins.str]]
    resource_records: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[RecordsExclusiveResourceRecordSetResourceRecordArgsDict]
            ]
        ]
    ]
    set_identifier: NotRequired[pulumi.Input[_builtins.str]]
    traffic_policy_instance_id: NotRequired[pulumi.Input[_builtins.str]]
    ttl: NotRequired[pulumi.Input[_builtins.int]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    weight: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class RecordsExclusiveResourceRecordSetArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        alias_target: Optional[
            pulumi.Input[RecordsExclusiveResourceRecordSetAliasTargetArgs]
        ] = ...,
        cidr_routing_config: Optional[
            pulumi.Input[RecordsExclusiveResourceRecordSetCidrRoutingConfigArgs]
        ] = ...,
        failover: Optional[pulumi.Input[_builtins.str]] = ...,
        geolocation: Optional[
            pulumi.Input[RecordsExclusiveResourceRecordSetGeolocationArgs]
        ] = ...,
        geoproximity_location: Optional[
            pulumi.Input[RecordsExclusiveResourceRecordSetGeoproximityLocationArgs]
        ] = ...,
        health_check_id: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_value_answer: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_records: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[RecordsExclusiveResourceRecordSetResourceRecordArgs]
                ]
            ]
        ] = ...,
        set_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        traffic_policy_instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="aliasTarget")
    def alias_target(
        self,
    ) -> Optional[pulumi.Input[RecordsExclusiveResourceRecordSetAliasTargetArgs]]: ...
    @alias_target.setter
    def alias_target(
        self,
        value: Optional[pulumi.Input[RecordsExclusiveResourceRecordSetAliasTargetArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cidrRoutingConfig")
    def cidr_routing_config(
        self,
    ) -> Optional[
        pulumi.Input[RecordsExclusiveResourceRecordSetCidrRoutingConfigArgs]
    ]: ...
    @cidr_routing_config.setter
    def cidr_routing_config(
        self,
        value: Optional[
            pulumi.Input[RecordsExclusiveResourceRecordSetCidrRoutingConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def failover(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failover.setter
    def failover(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def geolocation(
        self,
    ) -> Optional[pulumi.Input[RecordsExclusiveResourceRecordSetGeolocationArgs]]: ...
    @geolocation.setter
    def geolocation(
        self,
        value: Optional[pulumi.Input[RecordsExclusiveResourceRecordSetGeolocationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="geoproximityLocation")
    def geoproximity_location(
        self,
    ) -> Optional[
        pulumi.Input[RecordsExclusiveResourceRecordSetGeoproximityLocationArgs]
    ]: ...
    @geoproximity_location.setter
    def geoproximity_location(
        self,
        value: Optional[
            pulumi.Input[RecordsExclusiveResourceRecordSetGeoproximityLocationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckId")
    def health_check_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_check_id.setter
    def health_check_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiValueAnswer")
    def multi_value_answer(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_value_answer.setter
    def multi_value_answer(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceRecords")
    def resource_records(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[RecordsExclusiveResourceRecordSetResourceRecordArgs]]
        ]
    ]: ...
    @resource_records.setter
    def resource_records(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[RecordsExclusiveResourceRecordSetResourceRecordArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="setIdentifier")
    def set_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @set_identifier.setter
    def set_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trafficPolicyInstanceId")
    def traffic_policy_instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @traffic_policy_instance_id.setter
    def traffic_policy_instance_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class RecordsExclusiveResourceRecordSetAliasTargetArgsDict(TypedDict):
    dns_name: pulumi.Input[_builtins.str]
    evaluate_target_health: pulumi.Input[_builtins.bool]
    hosted_zone_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RecordsExclusiveResourceRecordSetAliasTargetArgs:
    def __init__(
        __self__,
        *,
        dns_name: pulumi.Input[_builtins.str],
        evaluate_target_health: pulumi.Input[_builtins.bool],
        hosted_zone_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Input[_builtins.str]: ...
    @dns_name.setter
    def dns_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> pulumi.Input[_builtins.bool]: ...
    @evaluate_target_health.setter
    def evaluate_target_health(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Input[_builtins.str]: ...
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: pulumi.Input[_builtins.str]): ...

class RecordsExclusiveResourceRecordSetCidrRoutingConfigArgsDict(TypedDict):
    collection_id: pulumi.Input[_builtins.str]
    location_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RecordsExclusiveResourceRecordSetCidrRoutingConfigArgs:
    def __init__(
        __self__,
        *,
        collection_id: pulumi.Input[_builtins.str],
        location_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Input[_builtins.str]: ...
    @collection_id.setter
    def collection_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="locationName")
    def location_name(self) -> pulumi.Input[_builtins.str]: ...
    @location_name.setter
    def location_name(self, value: pulumi.Input[_builtins.str]): ...

class RecordsExclusiveResourceRecordSetGeolocationArgsDict(TypedDict):
    continent_code: NotRequired[pulumi.Input[_builtins.str]]
    country_code: NotRequired[pulumi.Input[_builtins.str]]
    subdivision_code: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RecordsExclusiveResourceRecordSetGeolocationArgs:
    def __init__(
        __self__,
        *,
        continent_code: Optional[pulumi.Input[_builtins.str]] = ...,
        country_code: Optional[pulumi.Input[_builtins.str]] = ...,
        subdivision_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="continentCode")
    def continent_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @continent_code.setter
    def continent_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subdivisionCode")
    def subdivision_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subdivision_code.setter
    def subdivision_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RecordsExclusiveResourceRecordSetGeoproximityLocationArgsDict(TypedDict):
    aws_region: NotRequired[pulumi.Input[_builtins.str]]
    bias: NotRequired[pulumi.Input[_builtins.int]]
    coordinates: NotRequired[
        pulumi.Input[
            RecordsExclusiveResourceRecordSetGeoproximityLocationCoordinatesArgsDict
        ]
    ]
    local_zone_group: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RecordsExclusiveResourceRecordSetGeoproximityLocationArgs:
    def __init__(
        __self__,
        *,
        aws_region: Optional[pulumi.Input[_builtins.str]] = ...,
        bias: Optional[pulumi.Input[_builtins.int]] = ...,
        coordinates: Optional[
            pulumi.Input[
                RecordsExclusiveResourceRecordSetGeoproximityLocationCoordinatesArgs
            ]
        ] = ...,
        local_zone_group: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_region.setter
    def aws_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def bias(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @bias.setter
    def bias(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def coordinates(
        self,
    ) -> Optional[
        pulumi.Input[
            RecordsExclusiveResourceRecordSetGeoproximityLocationCoordinatesArgs
        ]
    ]: ...
    @coordinates.setter
    def coordinates(
        self,
        value: Optional[
            pulumi.Input[
                RecordsExclusiveResourceRecordSetGeoproximityLocationCoordinatesArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localZoneGroup")
    def local_zone_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_zone_group.setter
    def local_zone_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RecordsExclusiveResourceRecordSetGeoproximityLocationCoordinatesArgsDict(
    TypedDict
):
    latitude: pulumi.Input[_builtins.str]
    longitude: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RecordsExclusiveResourceRecordSetGeoproximityLocationCoordinatesArgs:
    def __init__(
        __self__,
        *,
        latitude: pulumi.Input[_builtins.str],
        longitude: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def latitude(self) -> pulumi.Input[_builtins.str]: ...
    @latitude.setter
    def latitude(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def longitude(self) -> pulumi.Input[_builtins.str]: ...
    @longitude.setter
    def longitude(self, value: pulumi.Input[_builtins.str]): ...

class RecordsExclusiveResourceRecordSetResourceRecordArgsDict(TypedDict):
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RecordsExclusiveResourceRecordSetResourceRecordArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class RecordsExclusiveTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RecordsExclusiveTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResolverEndpointIpAddressArgsDict(TypedDict):
    subnet_id: pulumi.Input[_builtins.str]
    ip: NotRequired[pulumi.Input[_builtins.str]]
    ip_id: NotRequired[pulumi.Input[_builtins.str]]
    ipv6: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ResolverEndpointIpAddressArgs:
    def __init__(
        __self__,
        *,
        subnet_id: pulumi.Input[_builtins.str],
        ip: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip.setter
    def ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipId")
    def ip_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_id.setter
    def ip_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ipv6(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6.setter
    def ipv6(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResolverRuleTargetIpArgsDict(TypedDict):
    ip: NotRequired[pulumi.Input[_builtins.str]]
    ipv6: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ResolverRuleTargetIpArgs:
    def __init__(
        __self__,
        *,
        ip: Optional[pulumi.Input[_builtins.str]] = ...,
        ipv6: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip.setter
    def ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ipv6(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv6.setter
    def ipv6(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ZoneVpcArgsDict(TypedDict):
    vpc_id: pulumi.Input[_builtins.str]
    vpc_region: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ZoneVpcArgs:
    def __init__(
        __self__,
        *,
        vpc_id: pulumi.Input[_builtins.str],
        vpc_region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vpcRegion")
    def vpc_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_region.setter
    def vpc_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GetQueryLogConfigFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]
    ...

@pulumi.input_type
class GetQueryLogConfigFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

class GetResolverEndpointFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]
    ...

@pulumi.input_type
class GetResolverEndpointFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...

class GetTrafficPolicyDocumentEndpointArgsDict(TypedDict):
    id: _builtins.str
    region: NotRequired[_builtins.str]
    type: NotRequired[_builtins.str]
    value: NotRequired[_builtins.str]
    ...

@pulumi.input_type
class GetTrafficPolicyDocumentEndpointArgs:
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
    @id.setter
    def id(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @region.setter
    def region(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @type.setter
    def type(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...
    @value.setter
    def value(self, value: Optional[_builtins.str]): ...

class GetTrafficPolicyDocumentRuleArgsDict(TypedDict):
    id: _builtins.str
    geo_proximity_locations: NotRequired[
        Sequence[GetTrafficPolicyDocumentRuleGeoProximityLocationArgsDict]
    ]
    items: NotRequired[Sequence[GetTrafficPolicyDocumentRuleItemArgsDict]]
    locations: NotRequired[Sequence[GetTrafficPolicyDocumentRuleLocationArgsDict]]
    primary: NotRequired[GetTrafficPolicyDocumentRulePrimaryArgsDict]
    regions: NotRequired[Sequence[GetTrafficPolicyDocumentRuleRegionArgsDict]]
    secondary: NotRequired[GetTrafficPolicyDocumentRuleSecondaryArgsDict]
    type: NotRequired[_builtins.str]
    ...

@pulumi.input_type
class GetTrafficPolicyDocumentRuleArgs:
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        geo_proximity_locations: Optional[
            Sequence[GetTrafficPolicyDocumentRuleGeoProximityLocationArgs]
        ] = ...,
        items: Optional[Sequence[GetTrafficPolicyDocumentRuleItemArgs]] = ...,
        locations: Optional[Sequence[GetTrafficPolicyDocumentRuleLocationArgs]] = ...,
        primary: Optional[GetTrafficPolicyDocumentRulePrimaryArgs] = ...,
        regions: Optional[Sequence[GetTrafficPolicyDocumentRuleRegionArgs]] = ...,
        secondary: Optional[GetTrafficPolicyDocumentRuleSecondaryArgs] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @id.setter
    def id(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="geoProximityLocations")
    def geo_proximity_locations(
        self,
    ) -> Optional[Sequence[GetTrafficPolicyDocumentRuleGeoProximityLocationArgs]]: ...
    @geo_proximity_locations.setter
    def geo_proximity_locations(
        self,
        value: Optional[Sequence[GetTrafficPolicyDocumentRuleGeoProximityLocationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[GetTrafficPolicyDocumentRuleItemArgs]]: ...
    @items.setter
    def items(
        self, value: Optional[Sequence[GetTrafficPolicyDocumentRuleItemArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def locations(
        self,
    ) -> Optional[Sequence[GetTrafficPolicyDocumentRuleLocationArgs]]: ...
    @locations.setter
    def locations(
        self, value: Optional[Sequence[GetTrafficPolicyDocumentRuleLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def primary(self) -> Optional[GetTrafficPolicyDocumentRulePrimaryArgs]: ...
    @primary.setter
    def primary(self, value: Optional[GetTrafficPolicyDocumentRulePrimaryArgs]): ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[GetTrafficPolicyDocumentRuleRegionArgs]]: ...
    @regions.setter
    def regions(
        self, value: Optional[Sequence[GetTrafficPolicyDocumentRuleRegionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def secondary(self) -> Optional[GetTrafficPolicyDocumentRuleSecondaryArgs]: ...
    @secondary.setter
    def secondary(self, value: Optional[GetTrafficPolicyDocumentRuleSecondaryArgs]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @type.setter
    def type(self, value: Optional[_builtins.str]): ...

class GetTrafficPolicyDocumentRuleGeoProximityLocationArgsDict(TypedDict):
    bias: NotRequired[_builtins.str]
    endpoint_reference: NotRequired[_builtins.str]
    evaluate_target_health: NotRequired[_builtins.bool]
    health_check: NotRequired[_builtins.str]
    latitude: NotRequired[_builtins.str]
    longitude: NotRequired[_builtins.str]
    region: NotRequired[_builtins.str]
    rule_reference: NotRequired[_builtins.str]
    ...

@pulumi.input_type
class GetTrafficPolicyDocumentRuleGeoProximityLocationArgs:
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
    @bias.setter
    def bias(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointReference")
    def endpoint_reference(self) -> Optional[_builtins.str]: ...
    @endpoint_reference.setter
    def endpoint_reference(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> Optional[_builtins.bool]: ...
    @evaluate_target_health.setter
    def evaluate_target_health(self, value: Optional[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[_builtins.str]: ...
    @health_check.setter
    def health_check(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def latitude(self) -> Optional[_builtins.str]: ...
    @latitude.setter
    def latitude(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def longitude(self) -> Optional[_builtins.str]: ...
    @longitude.setter
    def longitude(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @region.setter
    def region(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ruleReference")
    def rule_reference(self) -> Optional[_builtins.str]: ...
    @rule_reference.setter
    def rule_reference(self, value: Optional[_builtins.str]): ...

class GetTrafficPolicyDocumentRuleItemArgsDict(TypedDict):
    endpoint_reference: NotRequired[_builtins.str]
    health_check: NotRequired[_builtins.str]
    ...

@pulumi.input_type
class GetTrafficPolicyDocumentRuleItemArgs:
    def __init__(
        __self__,
        *,
        endpoint_reference: Optional[_builtins.str] = ...,
        health_check: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointReference")
    def endpoint_reference(self) -> Optional[_builtins.str]: ...
    @endpoint_reference.setter
    def endpoint_reference(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[_builtins.str]: ...
    @health_check.setter
    def health_check(self, value: Optional[_builtins.str]): ...

class GetTrafficPolicyDocumentRuleLocationArgsDict(TypedDict):
    continent: NotRequired[_builtins.str]
    country: NotRequired[_builtins.str]
    endpoint_reference: NotRequired[_builtins.str]
    evaluate_target_health: NotRequired[_builtins.bool]
    health_check: NotRequired[_builtins.str]
    is_default: NotRequired[_builtins.bool]
    rule_reference: NotRequired[_builtins.str]
    subdivision: NotRequired[_builtins.str]
    ...

@pulumi.input_type
class GetTrafficPolicyDocumentRuleLocationArgs:
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
    @continent.setter
    def continent(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[_builtins.str]: ...
    @country.setter
    def country(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endpointReference")
    def endpoint_reference(self) -> Optional[_builtins.str]: ...
    @endpoint_reference.setter
    def endpoint_reference(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> Optional[_builtins.bool]: ...
    @evaluate_target_health.setter
    def evaluate_target_health(self, value: Optional[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[_builtins.str]: ...
    @health_check.setter
    def health_check(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[_builtins.bool]: ...
    @is_default.setter
    def is_default(self, value: Optional[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="ruleReference")
    def rule_reference(self) -> Optional[_builtins.str]: ...
    @rule_reference.setter
    def rule_reference(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def subdivision(self) -> Optional[_builtins.str]: ...
    @subdivision.setter
    def subdivision(self, value: Optional[_builtins.str]): ...

class GetTrafficPolicyDocumentRulePrimaryArgsDict(TypedDict):
    endpoint_reference: NotRequired[_builtins.str]
    evaluate_target_health: NotRequired[_builtins.bool]
    health_check: NotRequired[_builtins.str]
    rule_reference: NotRequired[_builtins.str]
    ...

@pulumi.input_type
class GetTrafficPolicyDocumentRulePrimaryArgs:
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
    @endpoint_reference.setter
    def endpoint_reference(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> Optional[_builtins.bool]: ...
    @evaluate_target_health.setter
    def evaluate_target_health(self, value: Optional[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[_builtins.str]: ...
    @health_check.setter
    def health_check(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ruleReference")
    def rule_reference(self) -> Optional[_builtins.str]: ...
    @rule_reference.setter
    def rule_reference(self, value: Optional[_builtins.str]): ...

class GetTrafficPolicyDocumentRuleRegionArgsDict(TypedDict):
    endpoint_reference: NotRequired[_builtins.str]
    evaluate_target_health: NotRequired[_builtins.bool]
    health_check: NotRequired[_builtins.str]
    region: NotRequired[_builtins.str]
    rule_reference: NotRequired[_builtins.str]
    ...

@pulumi.input_type
class GetTrafficPolicyDocumentRuleRegionArgs:
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
    @endpoint_reference.setter
    def endpoint_reference(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> Optional[_builtins.bool]: ...
    @evaluate_target_health.setter
    def evaluate_target_health(self, value: Optional[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[_builtins.str]: ...
    @health_check.setter
    def health_check(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @region.setter
    def region(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ruleReference")
    def rule_reference(self) -> Optional[_builtins.str]: ...
    @rule_reference.setter
    def rule_reference(self, value: Optional[_builtins.str]): ...

class GetTrafficPolicyDocumentRuleSecondaryArgsDict(TypedDict):
    endpoint_reference: NotRequired[_builtins.str]
    evaluate_target_health: NotRequired[_builtins.bool]
    health_check: NotRequired[_builtins.str]
    rule_reference: NotRequired[_builtins.str]
    ...

@pulumi.input_type
class GetTrafficPolicyDocumentRuleSecondaryArgs:
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
    @endpoint_reference.setter
    def endpoint_reference(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> Optional[_builtins.bool]: ...
    @evaluate_target_health.setter
    def evaluate_target_health(self, value: Optional[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[_builtins.str]: ...
    @health_check.setter
    def health_check(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ruleReference")
    def rule_reference(self) -> Optional[_builtins.str]: ...
    @rule_reference.setter
    def rule_reference(self, value: Optional[_builtins.str]): ...
