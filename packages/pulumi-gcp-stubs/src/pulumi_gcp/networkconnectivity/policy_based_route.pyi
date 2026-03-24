import builtins as _builtins
import warnings
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PolicyBasedRouteArgs", "PolicyBasedRoute"]

@pulumi.input_type
class PolicyBasedRouteArgs:
    def __init__(
        __self__,
        *,
        filter: pulumi.Input[PolicyBasedRouteFilterArgs],
        network: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        interconnect_attachment: Optional[
            pulumi.Input[PolicyBasedRouteInterconnectAttachmentArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_ilb_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_other_routes: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_machine: Optional[
            pulumi.Input[PolicyBasedRouteVirtualMachineArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[PolicyBasedRouteFilterArgs]: ...
    @filter.setter
    def filter(self, value: pulumi.Input[PolicyBasedRouteFilterArgs]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="interconnectAttachment")
    def interconnect_attachment(
        self,
    ) -> Optional[pulumi.Input[PolicyBasedRouteInterconnectAttachmentArgs]]: ...
    @interconnect_attachment.setter
    def interconnect_attachment(
        self, value: Optional[pulumi.Input[PolicyBasedRouteInterconnectAttachmentArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopIlbIp")
    def next_hop_ilb_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_ilb_ip.setter
    def next_hop_ilb_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopOtherRoutes")
    def next_hop_other_routes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_other_routes.setter
    def next_hop_other_routes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(
        self,
    ) -> Optional[pulumi.Input[PolicyBasedRouteVirtualMachineArgs]]: ...
    @virtual_machine.setter
    def virtual_machine(
        self, value: Optional[pulumi.Input[PolicyBasedRouteVirtualMachineArgs]]
    ): ...

@pulumi.input_type
class _PolicyBasedRouteState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        filter: Optional[pulumi.Input[PolicyBasedRouteFilterArgs]] = ...,
        interconnect_attachment: Optional[
            pulumi.Input[PolicyBasedRouteInterconnectAttachmentArgs]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_ilb_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_other_routes: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_machine: Optional[
            pulumi.Input[PolicyBasedRouteVirtualMachineArgs]
        ] = ...,
        warnings: Optional[
            pulumi.Input[Sequence[pulumi.Input[PolicyBasedRouteWarningArgs]]]
        ] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[PolicyBasedRouteFilterArgs]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[PolicyBasedRouteFilterArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="interconnectAttachment")
    def interconnect_attachment(
        self,
    ) -> Optional[pulumi.Input[PolicyBasedRouteInterconnectAttachmentArgs]]: ...
    @interconnect_attachment.setter
    def interconnect_attachment(
        self, value: Optional[pulumi.Input[PolicyBasedRouteInterconnectAttachmentArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopIlbIp")
    def next_hop_ilb_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_ilb_ip.setter
    def next_hop_ilb_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextHopOtherRoutes")
    def next_hop_other_routes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_hop_other_routes.setter
    def next_hop_other_routes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(
        self,
    ) -> Optional[pulumi.Input[PolicyBasedRouteVirtualMachineArgs]]: ...
    @virtual_machine.setter
    def virtual_machine(
        self, value: Optional[pulumi.Input[PolicyBasedRouteVirtualMachineArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def warnings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PolicyBasedRouteWarningArgs]]]
    ]: ...
    @warnings.setter
    def warnings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PolicyBasedRouteWarningArgs]]]
        ],
    ): ...

@pulumi.type_token(...)
class PolicyBasedRoute(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[
            pulumi.Input[
                Union[PolicyBasedRouteFilterArgs, PolicyBasedRouteFilterArgsDict]
            ]
        ] = ...,
        interconnect_attachment: Optional[
            pulumi.Input[
                Union[
                    PolicyBasedRouteInterconnectAttachmentArgs,
                    PolicyBasedRouteInterconnectAttachmentArgsDict,
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_ilb_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_other_routes: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_machine: Optional[
            pulumi.Input[
                Union[
                    PolicyBasedRouteVirtualMachineArgs,
                    PolicyBasedRouteVirtualMachineArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PolicyBasedRouteArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        filter: Optional[
            pulumi.Input[
                Union[PolicyBasedRouteFilterArgs, PolicyBasedRouteFilterArgsDict]
            ]
        ] = ...,
        interconnect_attachment: Optional[
            pulumi.Input[
                Union[
                    PolicyBasedRouteInterconnectAttachmentArgs,
                    PolicyBasedRouteInterconnectAttachmentArgsDict,
                ]
            ]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_ilb_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        next_hop_other_routes: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_machine: Optional[
            pulumi.Input[
                Union[
                    PolicyBasedRouteVirtualMachineArgs,
                    PolicyBasedRouteVirtualMachineArgsDict,
                ]
            ]
        ] = ...,
        warnings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PolicyBasedRouteWarningArgs, PolicyBasedRouteWarningArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> PolicyBasedRoute: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Output[outputs.PolicyBasedRouteFilter]: ...
    @_builtins.property
    @pulumi.getter(name="interconnectAttachment")
    def interconnect_attachment(
        self,
    ) -> pulumi.Output[Optional[outputs.PolicyBasedRouteInterconnectAttachment]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextHopIlbIp")
    def next_hop_ilb_ip(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="nextHopOtherRoutes")
    def next_hop_other_routes(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(
        self,
    ) -> pulumi.Output[Optional[outputs.PolicyBasedRouteVirtualMachine]]: ...
    @_builtins.property
    @pulumi.getter
    def warnings(self) -> pulumi.Output[Sequence[outputs.PolicyBasedRouteWarning]]: ...
