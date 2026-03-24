import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RecordArgs", "Record"]

@pulumi.input_type
class RecordArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[Union[_builtins.str, RecordType]],
        zone_id: pulumi.Input[_builtins.str],
        aliases: Optional[pulumi.Input[Sequence[pulumi.Input[RecordAliasArgs]]]] = ...,
        allow_overwrite: Optional[pulumi.Input[_builtins.bool]] = ...,
        cidr_routing_policy: Optional[pulumi.Input[RecordCidrRoutingPolicyArgs]] = ...,
        failover_routing_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecordFailoverRoutingPolicyArgs]]]
        ] = ...,
        geolocation_routing_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecordGeolocationRoutingPolicyArgs]]]
        ] = ...,
        geoproximity_routing_policy: Optional[
            pulumi.Input[RecordGeoproximityRoutingPolicyArgs]
        ] = ...,
        health_check_id: Optional[pulumi.Input[_builtins.str]] = ...,
        latency_routing_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecordLatencyRoutingPolicyArgs]]]
        ] = ...,
        multivalue_answer_routing_policy: Optional[pulumi.Input[_builtins.bool]] = ...,
        records: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        set_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        weighted_routing_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecordWeightedRoutingPolicyArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, RecordType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, RecordType]]): ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[_builtins.str]: ...
    @zone_id.setter
    def zone_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def aliases(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RecordAliasArgs]]]]: ...
    @aliases.setter
    def aliases(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RecordAliasArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowOverwrite")
    def allow_overwrite(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_overwrite.setter
    def allow_overwrite(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="cidrRoutingPolicy")
    def cidr_routing_policy(
        self,
    ) -> Optional[pulumi.Input[RecordCidrRoutingPolicyArgs]]: ...
    @cidr_routing_policy.setter
    def cidr_routing_policy(
        self, value: Optional[pulumi.Input[RecordCidrRoutingPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failoverRoutingPolicies")
    def failover_routing_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RecordFailoverRoutingPolicyArgs]]]
    ]: ...
    @failover_routing_policies.setter
    def failover_routing_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecordFailoverRoutingPolicyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="geolocationRoutingPolicies")
    def geolocation_routing_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RecordGeolocationRoutingPolicyArgs]]]
    ]: ...
    @geolocation_routing_policies.setter
    def geolocation_routing_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecordGeolocationRoutingPolicyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="geoproximityRoutingPolicy")
    def geoproximity_routing_policy(
        self,
    ) -> Optional[pulumi.Input[RecordGeoproximityRoutingPolicyArgs]]: ...
    @geoproximity_routing_policy.setter
    def geoproximity_routing_policy(
        self, value: Optional[pulumi.Input[RecordGeoproximityRoutingPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckId")
    def health_check_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_check_id.setter
    def health_check_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="latencyRoutingPolicies")
    def latency_routing_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RecordLatencyRoutingPolicyArgs]]]
    ]: ...
    @latency_routing_policies.setter
    def latency_routing_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecordLatencyRoutingPolicyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="multivalueAnswerRoutingPolicy")
    def multivalue_answer_routing_policy(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multivalue_answer_routing_policy.setter
    def multivalue_answer_routing_policy(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def records(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @records.setter
    def records(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="setIdentifier")
    def set_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @set_identifier.setter
    def set_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="weightedRoutingPolicies")
    def weighted_routing_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RecordWeightedRoutingPolicyArgs]]]
    ]: ...
    @weighted_routing_policies.setter
    def weighted_routing_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecordWeightedRoutingPolicyArgs]]]
        ],
    ): ...

@pulumi.input_type
class _RecordState:
    def __init__(
        __self__,
        *,
        aliases: Optional[pulumi.Input[Sequence[pulumi.Input[RecordAliasArgs]]]] = ...,
        allow_overwrite: Optional[pulumi.Input[_builtins.bool]] = ...,
        cidr_routing_policy: Optional[pulumi.Input[RecordCidrRoutingPolicyArgs]] = ...,
        failover_routing_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecordFailoverRoutingPolicyArgs]]]
        ] = ...,
        fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        geolocation_routing_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecordGeolocationRoutingPolicyArgs]]]
        ] = ...,
        geoproximity_routing_policy: Optional[
            pulumi.Input[RecordGeoproximityRoutingPolicyArgs]
        ] = ...,
        health_check_id: Optional[pulumi.Input[_builtins.str]] = ...,
        latency_routing_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecordLatencyRoutingPolicyArgs]]]
        ] = ...,
        multivalue_answer_routing_policy: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        records: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        set_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, RecordType]]] = ...,
        weighted_routing_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecordWeightedRoutingPolicyArgs]]]
        ] = ...,
        zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def aliases(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RecordAliasArgs]]]]: ...
    @aliases.setter
    def aliases(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RecordAliasArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowOverwrite")
    def allow_overwrite(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_overwrite.setter
    def allow_overwrite(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="cidrRoutingPolicy")
    def cidr_routing_policy(
        self,
    ) -> Optional[pulumi.Input[RecordCidrRoutingPolicyArgs]]: ...
    @cidr_routing_policy.setter
    def cidr_routing_policy(
        self, value: Optional[pulumi.Input[RecordCidrRoutingPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failoverRoutingPolicies")
    def failover_routing_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RecordFailoverRoutingPolicyArgs]]]
    ]: ...
    @failover_routing_policies.setter
    def failover_routing_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecordFailoverRoutingPolicyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="geolocationRoutingPolicies")
    def geolocation_routing_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RecordGeolocationRoutingPolicyArgs]]]
    ]: ...
    @geolocation_routing_policies.setter
    def geolocation_routing_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecordGeolocationRoutingPolicyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="geoproximityRoutingPolicy")
    def geoproximity_routing_policy(
        self,
    ) -> Optional[pulumi.Input[RecordGeoproximityRoutingPolicyArgs]]: ...
    @geoproximity_routing_policy.setter
    def geoproximity_routing_policy(
        self, value: Optional[pulumi.Input[RecordGeoproximityRoutingPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckId")
    def health_check_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_check_id.setter
    def health_check_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="latencyRoutingPolicies")
    def latency_routing_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RecordLatencyRoutingPolicyArgs]]]
    ]: ...
    @latency_routing_policies.setter
    def latency_routing_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecordLatencyRoutingPolicyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="multivalueAnswerRoutingPolicy")
    def multivalue_answer_routing_policy(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multivalue_answer_routing_policy.setter
    def multivalue_answer_routing_policy(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def records(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @records.setter
    def records(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="setIdentifier")
    def set_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @set_identifier.setter
    def set_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, RecordType]]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, RecordType]]]): ...
    @_builtins.property
    @pulumi.getter(name="weightedRoutingPolicies")
    def weighted_routing_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RecordWeightedRoutingPolicyArgs]]]
    ]: ...
    @weighted_routing_policies.setter
    def weighted_routing_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RecordWeightedRoutingPolicyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:route53/record:Record")
class Record(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        aliases: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[RecordAliasArgs, RecordAliasArgsDict]]]
            ]
        ] = ...,
        allow_overwrite: Optional[pulumi.Input[_builtins.bool]] = ...,
        cidr_routing_policy: Optional[
            pulumi.Input[
                Union[RecordCidrRoutingPolicyArgs, RecordCidrRoutingPolicyArgsDict]
            ]
        ] = ...,
        failover_routing_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RecordFailoverRoutingPolicyArgs,
                            RecordFailoverRoutingPolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        geolocation_routing_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RecordGeolocationRoutingPolicyArgs,
                            RecordGeolocationRoutingPolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        geoproximity_routing_policy: Optional[
            pulumi.Input[
                Union[
                    RecordGeoproximityRoutingPolicyArgs,
                    RecordGeoproximityRoutingPolicyArgsDict,
                ]
            ]
        ] = ...,
        health_check_id: Optional[pulumi.Input[_builtins.str]] = ...,
        latency_routing_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RecordLatencyRoutingPolicyArgs,
                            RecordLatencyRoutingPolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        multivalue_answer_routing_policy: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        records: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        set_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, RecordType]]] = ...,
        weighted_routing_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RecordWeightedRoutingPolicyArgs,
                            RecordWeightedRoutingPolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RecordArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        aliases: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[RecordAliasArgs, RecordAliasArgsDict]]]
            ]
        ] = ...,
        allow_overwrite: Optional[pulumi.Input[_builtins.bool]] = ...,
        cidr_routing_policy: Optional[
            pulumi.Input[
                Union[RecordCidrRoutingPolicyArgs, RecordCidrRoutingPolicyArgsDict]
            ]
        ] = ...,
        failover_routing_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RecordFailoverRoutingPolicyArgs,
                            RecordFailoverRoutingPolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        geolocation_routing_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RecordGeolocationRoutingPolicyArgs,
                            RecordGeolocationRoutingPolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        geoproximity_routing_policy: Optional[
            pulumi.Input[
                Union[
                    RecordGeoproximityRoutingPolicyArgs,
                    RecordGeoproximityRoutingPolicyArgsDict,
                ]
            ]
        ] = ...,
        health_check_id: Optional[pulumi.Input[_builtins.str]] = ...,
        latency_routing_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RecordLatencyRoutingPolicyArgs,
                            RecordLatencyRoutingPolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        multivalue_answer_routing_policy: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        records: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        set_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, RecordType]]] = ...,
        weighted_routing_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RecordWeightedRoutingPolicyArgs,
                            RecordWeightedRoutingPolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Record: ...
    @_builtins.property
    @pulumi.getter
    def aliases(self) -> pulumi.Output[Optional[Sequence[outputs.RecordAlias]]]: ...
    @_builtins.property
    @pulumi.getter(name="allowOverwrite")
    def allow_overwrite(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="cidrRoutingPolicy")
    def cidr_routing_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.RecordCidrRoutingPolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="failoverRoutingPolicies")
    def failover_routing_policies(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.RecordFailoverRoutingPolicy]]]: ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="geolocationRoutingPolicies")
    def geolocation_routing_policies(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.RecordGeolocationRoutingPolicy]]]: ...
    @_builtins.property
    @pulumi.getter(name="geoproximityRoutingPolicy")
    def geoproximity_routing_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.RecordGeoproximityRoutingPolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckId")
    def health_check_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="latencyRoutingPolicies")
    def latency_routing_policies(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.RecordLatencyRoutingPolicy]]]: ...
    @_builtins.property
    @pulumi.getter(name="multivalueAnswerRoutingPolicy")
    def multivalue_answer_routing_policy(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def records(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="setIdentifier")
    def set_identifier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="weightedRoutingPolicies")
    def weighted_routing_policies(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.RecordWeightedRoutingPolicy]]]: ...
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[_builtins.str]: ...
