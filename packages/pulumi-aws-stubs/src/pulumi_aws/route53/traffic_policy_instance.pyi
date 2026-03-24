import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TrafficPolicyInstanceArgs", "TrafficPolicyInstance"]

@pulumi.input_type
class TrafficPolicyInstanceArgs:
    def __init__(
        __self__,
        *,
        hosted_zone_id: pulumi.Input[_builtins.str],
        traffic_policy_id: pulumi.Input[_builtins.str],
        traffic_policy_version: pulumi.Input[_builtins.int],
        ttl: pulumi.Input[_builtins.int],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Input[_builtins.str]: ...
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trafficPolicyId")
    def traffic_policy_id(self) -> pulumi.Input[_builtins.str]: ...
    @traffic_policy_id.setter
    def traffic_policy_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trafficPolicyVersion")
    def traffic_policy_version(self) -> pulumi.Input[_builtins.int]: ...
    @traffic_policy_version.setter
    def traffic_policy_version(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> pulumi.Input[_builtins.int]: ...
    @ttl.setter
    def ttl(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _TrafficPolicyInstanceState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        traffic_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        traffic_policy_version: Optional[pulumi.Input[_builtins.int]] = ...,
        ttl: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trafficPolicyId")
    def traffic_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @traffic_policy_id.setter
    def traffic_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trafficPolicyVersion")
    def traffic_policy_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @traffic_policy_version.setter
    def traffic_policy_version(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token(...)
class TrafficPolicyInstance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        traffic_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        traffic_policy_version: Optional[pulumi.Input[_builtins.int]] = ...,
        ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TrafficPolicyInstanceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        traffic_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        traffic_policy_version: Optional[pulumi.Input[_builtins.int]] = ...,
        ttl: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> TrafficPolicyInstance: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trafficPolicyId")
    def traffic_policy_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trafficPolicyVersion")
    def traffic_policy_version(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[_builtins.int]: ...
