import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RecordSetArgs", "RecordSet"]

@pulumi.input_type
class RecordSetArgs:
    def __init__(
        __self__,
        *,
        managed_zone: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_policy: Optional[pulumi.Input[RecordSetRoutingPolicyArgs]] = ...,
        rrdatas: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        ttl: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedZone")
    def managed_zone(self) -> pulumi.Input[_builtins.str]: ...
    @managed_zone.setter
    def managed_zone(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingPolicy")
    def routing_policy(self) -> Optional[pulumi.Input[RecordSetRoutingPolicyArgs]]: ...
    @routing_policy.setter
    def routing_policy(
        self, value: Optional[pulumi.Input[RecordSetRoutingPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def rrdatas(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @rrdatas.setter
    def rrdatas(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.input_type
class _RecordSetState:
    def __init__(
        __self__,
        *,
        managed_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_policy: Optional[pulumi.Input[RecordSetRoutingPolicyArgs]] = ...,
        rrdatas: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedZone")
    def managed_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_zone.setter
    def managed_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingPolicy")
    def routing_policy(self) -> Optional[pulumi.Input[RecordSetRoutingPolicyArgs]]: ...
    @routing_policy.setter
    def routing_policy(
        self, value: Optional[pulumi.Input[RecordSetRoutingPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def rrdatas(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @rrdatas.setter
    def rrdatas(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
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

@pulumi.type_token("gcp:dns/recordSet:RecordSet")
class RecordSet(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        managed_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_policy: Optional[
            pulumi.Input[
                Union[RecordSetRoutingPolicyArgs, RecordSetRoutingPolicyArgsDict]
            ]
        ] = ...,
        rrdatas: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RecordSetArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        managed_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_policy: Optional[
            pulumi.Input[
                Union[RecordSetRoutingPolicyArgs, RecordSetRoutingPolicyArgsDict]
            ]
        ] = ...,
        rrdatas: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        ttl: Optional[pulumi.Input[_builtins.int]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> RecordSet: ...
    @_builtins.property
    @pulumi.getter(name="managedZone")
    def managed_zone(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingPolicy")
    def routing_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.RecordSetRoutingPolicy]]: ...
    @_builtins.property
    @pulumi.getter
    def rrdatas(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
