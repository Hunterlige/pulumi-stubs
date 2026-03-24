import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ServiceNetworkResourceAssociationArgs", "ServiceNetworkResourceAssociation"]

@pulumi.input_type
class ServiceNetworkResourceAssociationArgs:
    def __init__(
        __self__,
        *,
        resource_configuration_identifier: pulumi.Input[_builtins.str],
        service_network_identifier: pulumi.Input[_builtins.str],
        private_dns_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[ServiceNetworkResourceAssociationTimeoutsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationIdentifier")
    def resource_configuration_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @resource_configuration_identifier.setter
    def resource_configuration_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceNetworkIdentifier")
    def service_network_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @service_network_identifier.setter
    def service_network_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="privateDnsEnabled")
    def private_dns_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @private_dns_enabled.setter
    def private_dns_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[ServiceNetworkResourceAssociationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self,
        value: Optional[pulumi.Input[ServiceNetworkResourceAssociationTimeoutsArgs]],
    ): ...

@pulumi.input_type
class _ServiceNetworkResourceAssociationState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_entries: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceNetworkResourceAssociationDnsEntryArgs]]
            ]
        ] = ...,
        private_dns_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_configuration_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        service_network_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[ServiceNetworkResourceAssociationTimeoutsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsEntries")
    def dns_entries(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ServiceNetworkResourceAssociationDnsEntryArgs]]
        ]
    ]: ...
    @dns_entries.setter
    def dns_entries(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceNetworkResourceAssociationDnsEntryArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateDnsEnabled")
    def private_dns_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @private_dns_enabled.setter
    def private_dns_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationIdentifier")
    def resource_configuration_identifier(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_configuration_identifier.setter
    def resource_configuration_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceNetworkIdentifier")
    def service_network_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_network_identifier.setter
    def service_network_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[ServiceNetworkResourceAssociationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self,
        value: Optional[pulumi.Input[ServiceNetworkResourceAssociationTimeoutsArgs]],
    ): ...

@pulumi.type_token(...)
class ServiceNetworkResourceAssociation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        private_dns_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_configuration_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        service_network_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    ServiceNetworkResourceAssociationTimeoutsArgs,
                    ServiceNetworkResourceAssociationTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ServiceNetworkResourceAssociationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_entries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ServiceNetworkResourceAssociationDnsEntryArgs,
                            ServiceNetworkResourceAssociationDnsEntryArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        private_dns_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_configuration_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        service_network_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    ServiceNetworkResourceAssociationTimeoutsArgs,
                    ServiceNetworkResourceAssociationTimeoutsArgsDict,
                ]
            ]
        ] = ...,
    ) -> ServiceNetworkResourceAssociation: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsEntries")
    def dns_entries(
        self,
    ) -> pulumi.Output[Sequence[outputs.ServiceNetworkResourceAssociationDnsEntry]]: ...
    @_builtins.property
    @pulumi.getter(name="privateDnsEnabled")
    def private_dns_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationIdentifier")
    def resource_configuration_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceNetworkIdentifier")
    def service_network_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.ServiceNetworkResourceAssociationTimeouts]]: ...
