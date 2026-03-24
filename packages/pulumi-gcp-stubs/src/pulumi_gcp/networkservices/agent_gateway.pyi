import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AgentGatewayArgs", "AgentGateway"]

@pulumi.input_type
class AgentGatewayArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        protocols: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        google_managed: Optional[pulumi.Input[AgentGatewayGoogleManagedArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[pulumi.Input[AgentGatewayNetworkConfigArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        registries: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        self_managed: Optional[pulumi.Input[AgentGatewaySelfManagedArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @protocols.setter
    def protocols(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="googleManaged")
    def google_managed(
        self,
    ) -> Optional[pulumi.Input[AgentGatewayGoogleManagedArgs]]: ...
    @google_managed.setter
    def google_managed(
        self, value: Optional[pulumi.Input[AgentGatewayGoogleManagedArgs]]
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
    @pulumi.getter(name="networkConfig")
    def network_config(
        self,
    ) -> Optional[pulumi.Input[AgentGatewayNetworkConfigArgs]]: ...
    @network_config.setter
    def network_config(
        self, value: Optional[pulumi.Input[AgentGatewayNetworkConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def registries(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @registries.setter
    def registries(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selfManaged")
    def self_managed(self) -> Optional[pulumi.Input[AgentGatewaySelfManagedArgs]]: ...
    @self_managed.setter
    def self_managed(
        self, value: Optional[pulumi.Input[AgentGatewaySelfManagedArgs]]
    ): ...

@pulumi.input_type
class _AgentGatewayState:
    def __init__(
        __self__,
        *,
        agent_gateway_cards: Optional[
            pulumi.Input[Sequence[pulumi.Input[AgentGatewayAgentGatewayCardArgs]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        google_managed: Optional[pulumi.Input[AgentGatewayGoogleManagedArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[pulumi.Input[AgentGatewayNetworkConfigArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        registries: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        self_managed: Optional[pulumi.Input[AgentGatewaySelfManagedArgs]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentGatewayCards")
    def agent_gateway_cards(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AgentGatewayAgentGatewayCardArgs]]]
    ]: ...
    @agent_gateway_cards.setter
    def agent_gateway_cards(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AgentGatewayAgentGatewayCardArgs]]]
        ],
    ): ...
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
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="googleManaged")
    def google_managed(
        self,
    ) -> Optional[pulumi.Input[AgentGatewayGoogleManagedArgs]]: ...
    @google_managed.setter
    def google_managed(
        self, value: Optional[pulumi.Input[AgentGatewayGoogleManagedArgs]]
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
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(
        self,
    ) -> Optional[pulumi.Input[AgentGatewayNetworkConfigArgs]]: ...
    @network_config.setter
    def network_config(
        self, value: Optional[pulumi.Input[AgentGatewayNetworkConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocols(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @protocols.setter
    def protocols(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
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
    @pulumi.getter
    def registries(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @registries.setter
    def registries(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selfManaged")
    def self_managed(self) -> Optional[pulumi.Input[AgentGatewaySelfManagedArgs]]: ...
    @self_managed.setter
    def self_managed(
        self, value: Optional[pulumi.Input[AgentGatewaySelfManagedArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:networkservices/agentGateway:AgentGateway")
class AgentGateway(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        google_managed: Optional[
            pulumi.Input[
                Union[AgentGatewayGoogleManagedArgs, AgentGatewayGoogleManagedArgsDict]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[
            pulumi.Input[
                Union[AgentGatewayNetworkConfigArgs, AgentGatewayNetworkConfigArgsDict]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        registries: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        self_managed: Optional[
            pulumi.Input[
                Union[AgentGatewaySelfManagedArgs, AgentGatewaySelfManagedArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AgentGatewayArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        agent_gateway_cards: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AgentGatewayAgentGatewayCardArgs,
                            AgentGatewayAgentGatewayCardArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        google_managed: Optional[
            pulumi.Input[
                Union[AgentGatewayGoogleManagedArgs, AgentGatewayGoogleManagedArgsDict]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_config: Optional[
            pulumi.Input[
                Union[AgentGatewayNetworkConfigArgs, AgentGatewayNetworkConfigArgsDict]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        registries: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        self_managed: Optional[
            pulumi.Input[
                Union[AgentGatewaySelfManagedArgs, AgentGatewaySelfManagedArgsDict]
            ]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AgentGateway: ...
    @_builtins.property
    @pulumi.getter(name="agentGatewayCards")
    def agent_gateway_cards(
        self,
    ) -> pulumi.Output[Sequence[outputs.AgentGatewayAgentGatewayCard]]: ...
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
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="googleManaged")
    def google_managed(
        self,
    ) -> pulumi.Output[Optional[outputs.AgentGatewayGoogleManaged]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(
        self,
    ) -> pulumi.Output[Optional[outputs.AgentGatewayNetworkConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def registries(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="selfManaged")
    def self_managed(
        self,
    ) -> pulumi.Output[Optional[outputs.AgentGatewaySelfManaged]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
