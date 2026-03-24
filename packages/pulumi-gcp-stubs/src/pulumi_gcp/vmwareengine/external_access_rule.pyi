import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ExternalAccessRuleArgs", "ExternalAccessRule"]

@pulumi.input_type
class ExternalAccessRuleArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[_builtins.str],
        destination_ip_ranges: pulumi.Input[
            Sequence[pulumi.Input[ExternalAccessRuleDestinationIpRangeArgs]]
        ],
        destination_ports: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        ip_protocol: pulumi.Input[_builtins.str],
        parent: pulumi.Input[_builtins.str],
        priority: pulumi.Input[_builtins.int],
        source_ip_ranges: pulumi.Input[
            Sequence[pulumi.Input[ExternalAccessRuleSourceIpRangeArgs]]
        ],
        source_ports: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]: ...
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="destinationIpRanges")
    def destination_ip_ranges(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ExternalAccessRuleDestinationIpRangeArgs]]
    ]: ...
    @destination_ip_ranges.setter
    def destination_ip_ranges(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ExternalAccessRuleDestinationIpRangeArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationPorts")
    def destination_ports(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @destination_ports.setter
    def destination_ports(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Input[_builtins.str]: ...
    @ip_protocol.setter
    def ip_protocol(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]: ...
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ExternalAccessRuleSourceIpRangeArgs]]]: ...
    @source_ip_ranges.setter
    def source_ip_ranges(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ExternalAccessRuleSourceIpRangeArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourcePorts")
    def source_ports(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @source_ports.setter
    def source_ports(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ExternalAccessRuleState:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_ip_ranges: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ExternalAccessRuleDestinationIpRangeArgs]]
            ]
        ] = ...,
        destination_ports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ip_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        source_ip_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExternalAccessRuleSourceIpRangeArgs]]]
        ] = ...,
        source_ports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationIpRanges")
    def destination_ip_ranges(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ExternalAccessRuleDestinationIpRangeArgs]]]
    ]: ...
    @destination_ip_ranges.setter
    def destination_ip_ranges(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ExternalAccessRuleDestinationIpRangeArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationPorts")
    def destination_ports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @destination_ports.setter
    def destination_ports(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_protocol.setter
    def ip_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ExternalAccessRuleSourceIpRangeArgs]]]
    ]: ...
    @source_ip_ranges.setter
    def source_ip_ranges(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExternalAccessRuleSourceIpRangeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourcePorts")
    def source_ports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @source_ports.setter
    def source_ports(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ExternalAccessRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_ip_ranges: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ExternalAccessRuleDestinationIpRangeArgs,
                            ExternalAccessRuleDestinationIpRangeArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        destination_ports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ip_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        source_ip_ranges: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ExternalAccessRuleSourceIpRangeArgs,
                            ExternalAccessRuleSourceIpRangeArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        source_ports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ExternalAccessRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_ip_ranges: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ExternalAccessRuleDestinationIpRangeArgs,
                            ExternalAccessRuleDestinationIpRangeArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        destination_ports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ip_protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        source_ip_ranges: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ExternalAccessRuleSourceIpRangeArgs,
                            ExternalAccessRuleSourceIpRangeArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        source_ports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ExternalAccessRule: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationIpRanges")
    def destination_ip_ranges(
        self,
    ) -> pulumi.Output[Sequence[outputs.ExternalAccessRuleDestinationIpRange]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationPorts")
    def destination_ports(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(
        self,
    ) -> pulumi.Output[Sequence[outputs.ExternalAccessRuleSourceIpRange]]: ...
    @_builtins.property
    @pulumi.getter(name="sourcePorts")
    def source_ports(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
