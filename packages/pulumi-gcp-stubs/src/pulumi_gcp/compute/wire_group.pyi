import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WireGroupArgs", "WireGroup"]

@pulumi.input_type
class WireGroupArgs:
    def __init__(
        __self__,
        *,
        cross_site_network: pulumi.Input[_builtins.str],
        admin_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[WireGroupEndpointArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        wire_group_properties: Optional[
            pulumi.Input[WireGroupWireGroupPropertiesArgs]
        ] = ...,
        wire_properties: Optional[pulumi.Input[WireGroupWirePropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossSiteNetwork")
    def cross_site_network(self) -> pulumi.Input[_builtins.str]: ...
    @cross_site_network.setter
    def cross_site_network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="adminEnabled")
    def admin_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @admin_enabled.setter
    def admin_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WireGroupEndpointArgs]]]]: ...
    @endpoints.setter
    def endpoints(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[WireGroupEndpointArgs]]]],
    ): ...
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
    @pulumi.getter(name="wireGroupProperties")
    def wire_group_properties(
        self,
    ) -> Optional[pulumi.Input[WireGroupWireGroupPropertiesArgs]]: ...
    @wire_group_properties.setter
    def wire_group_properties(
        self, value: Optional[pulumi.Input[WireGroupWireGroupPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="wireProperties")
    def wire_properties(
        self,
    ) -> Optional[pulumi.Input[WireGroupWirePropertiesArgs]]: ...
    @wire_properties.setter
    def wire_properties(
        self, value: Optional[pulumi.Input[WireGroupWirePropertiesArgs]]
    ): ...

@pulumi.input_type
class _WireGroupState:
    def __init__(
        __self__,
        *,
        admin_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        cross_site_network: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[WireGroupEndpointArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        topologies: Optional[
            pulumi.Input[Sequence[pulumi.Input[WireGroupTopologyArgs]]]
        ] = ...,
        wire_group_properties: Optional[
            pulumi.Input[WireGroupWireGroupPropertiesArgs]
        ] = ...,
        wire_properties: Optional[pulumi.Input[WireGroupWirePropertiesArgs]] = ...,
        wires: Optional[pulumi.Input[Sequence[pulumi.Input[WireGroupWireArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminEnabled")
    def admin_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @admin_enabled.setter
    def admin_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="crossSiteNetwork")
    def cross_site_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cross_site_network.setter
    def cross_site_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WireGroupEndpointArgs]]]]: ...
    @endpoints.setter
    def endpoints(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[WireGroupEndpointArgs]]]],
    ): ...
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
    @pulumi.getter
    def topologies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WireGroupTopologyArgs]]]]: ...
    @topologies.setter
    def topologies(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[WireGroupTopologyArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="wireGroupProperties")
    def wire_group_properties(
        self,
    ) -> Optional[pulumi.Input[WireGroupWireGroupPropertiesArgs]]: ...
    @wire_group_properties.setter
    def wire_group_properties(
        self, value: Optional[pulumi.Input[WireGroupWireGroupPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="wireProperties")
    def wire_properties(
        self,
    ) -> Optional[pulumi.Input[WireGroupWirePropertiesArgs]]: ...
    @wire_properties.setter
    def wire_properties(
        self, value: Optional[pulumi.Input[WireGroupWirePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def wires(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WireGroupWireArgs]]]]: ...
    @wires.setter
    def wires(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WireGroupWireArgs]]]]
    ): ...

@pulumi.type_token("gcp:compute/wireGroup:WireGroup")
class WireGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        admin_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        cross_site_network: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[WireGroupEndpointArgs, WireGroupEndpointArgsDict]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        wire_group_properties: Optional[
            pulumi.Input[
                Union[
                    WireGroupWireGroupPropertiesArgs,
                    WireGroupWireGroupPropertiesArgsDict,
                ]
            ]
        ] = ...,
        wire_properties: Optional[
            pulumi.Input[
                Union[WireGroupWirePropertiesArgs, WireGroupWirePropertiesArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WireGroupArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        admin_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        cross_site_network: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[WireGroupEndpointArgs, WireGroupEndpointArgsDict]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        topologies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[WireGroupTopologyArgs, WireGroupTopologyArgsDict]
                    ]
                ]
            ]
        ] = ...,
        wire_group_properties: Optional[
            pulumi.Input[
                Union[
                    WireGroupWireGroupPropertiesArgs,
                    WireGroupWireGroupPropertiesArgsDict,
                ]
            ]
        ] = ...,
        wire_properties: Optional[
            pulumi.Input[
                Union[WireGroupWirePropertiesArgs, WireGroupWirePropertiesArgsDict]
            ]
        ] = ...,
        wires: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[WireGroupWireArgs, WireGroupWireArgsDict]]]
            ]
        ] = ...,
    ) -> WireGroup: ...
    @_builtins.property
    @pulumi.getter(name="adminEnabled")
    def admin_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="crossSiteNetwork")
    def cross_site_network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.WireGroupEndpoint]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def topologies(self) -> pulumi.Output[Sequence[outputs.WireGroupTopology]]: ...
    @_builtins.property
    @pulumi.getter(name="wireGroupProperties")
    def wire_group_properties(
        self,
    ) -> pulumi.Output[Optional[outputs.WireGroupWireGroupProperties]]: ...
    @_builtins.property
    @pulumi.getter(name="wireProperties")
    def wire_properties(
        self,
    ) -> pulumi.Output[Optional[outputs.WireGroupWireProperties]]: ...
    @_builtins.property
    @pulumi.getter
    def wires(self) -> pulumi.Output[Sequence[outputs.WireGroupWire]]: ...
