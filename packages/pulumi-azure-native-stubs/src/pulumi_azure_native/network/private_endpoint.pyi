import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PrivateEndpointArgs", "PrivateEndpoint"]

@pulumi.input_type
class PrivateEndpointArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        application_security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationSecurityGroupArgs]]]
        ] = ...,
        custom_dns_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[CustomDnsConfigPropertiesFormatArgs]]]
        ] = ...,
        custom_network_interface_name: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateEndpointIPConfigurationArgs]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        manual_private_link_service_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]
        ] = ...,
        private_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_service_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]
        ] = ...,
        subnet: Optional[pulumi.Input[SubnetArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applicationSecurityGroups")
    def application_security_groups(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationSecurityGroupArgs]]]
    ]: ...
    @application_security_groups.setter
    def application_security_groups(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationSecurityGroupArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customDnsConfigs")
    def custom_dns_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CustomDnsConfigPropertiesFormatArgs]]]
    ]: ...
    @custom_dns_configs.setter
    def custom_dns_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CustomDnsConfigPropertiesFormatArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customNetworkInterfaceName")
    def custom_network_interface_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_network_interface_name.setter
    def custom_network_interface_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input[ExtendedLocationArgs]]: ...
    @extended_location.setter
    def extended_location(
        self, value: Optional[pulumi.Input[ExtendedLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PrivateEndpointIPConfigurationArgs]]]
    ]: ...
    @ip_configurations.setter
    def ip_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateEndpointIPConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="manualPrivateLinkServiceConnections")
    def manual_private_link_service_connections(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]
    ]: ...
    @manual_private_link_service_connections.setter
    def manual_private_link_service_connections(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointName")
    def private_endpoint_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_endpoint_name.setter
    def private_endpoint_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnections")
    def private_link_service_connections(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]
    ]: ...
    @private_link_service_connections.setter
    def private_link_service_connections(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateLinkServiceConnectionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[SubnetArgs]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[SubnetArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:network:PrivateEndpoint")
class PrivateEndpoint(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        application_security_groups: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationSecurityGroupArgs,
                            ApplicationSecurityGroupArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        custom_dns_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CustomDnsConfigPropertiesFormatArgs,
                            CustomDnsConfigPropertiesFormatArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        custom_network_interface_name: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_location: Optional[
            pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PrivateEndpointIPConfigurationArgs,
                            PrivateEndpointIPConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        manual_private_link_service_connections: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PrivateLinkServiceConnectionArgs,
                            PrivateLinkServiceConnectionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        private_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_service_connections: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PrivateLinkServiceConnectionArgs,
                            PrivateLinkServiceConnectionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet: Optional[pulumi.Input[Union[SubnetArgs, SubnetArgsDict]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PrivateEndpointArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> PrivateEndpoint: ...
    @_builtins.property
    @pulumi.getter(name="applicationSecurityGroups")
    def application_security_groups(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationSecurityGroupResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customDnsConfigs")
    def custom_dns_configs(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.CustomDnsConfigPropertiesFormatResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="customNetworkInterfaceName")
    def custom_network_interface_name(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> pulumi.Output[Optional[outputs.ExtendedLocationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.PrivateEndpointIPConfigurationResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="manualPrivateLinkServiceConnections")
    def manual_private_link_service_connections(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.PrivateLinkServiceConnectionResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> pulumi.Output[Sequence[outputs.NetworkInterfaceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnections")
    def private_link_service_connections(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.PrivateLinkServiceConnectionResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> pulumi.Output[Optional[outputs.SubnetResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
