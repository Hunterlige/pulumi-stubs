import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ResourceConfigurationArgs", "ResourceConfiguration"]

@pulumi.input_type
class ResourceConfigurationArgs:
    def __init__(
        __self__,
        *,
        allow_association_to_shareable_service_network: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_verification_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        port_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_configuration_definition: Optional[
            pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionArgs]
        ] = ...,
        resource_configuration_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_gateway_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[ResourceConfigurationTimeoutsArgs]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowAssociationToShareableServiceNetwork")
    def allow_association_to_shareable_service_network(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_association_to_shareable_service_network.setter
    def allow_association_to_shareable_service_network(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_domain_name.setter
    def custom_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainVerificationId")
    def domain_verification_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_verification_id.setter
    def domain_verification_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @port_ranges.setter
    def port_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationDefinition")
    def resource_configuration_definition(
        self,
    ) -> Optional[
        pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionArgs]
    ]: ...
    @resource_configuration_definition.setter
    def resource_configuration_definition(
        self,
        value: Optional[
            pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationGroupId")
    def resource_configuration_group_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_configuration_group_id.setter
    def resource_configuration_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGatewayIdentifier")
    def resource_gateway_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_gateway_identifier.setter
    def resource_gateway_identifier(
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ResourceConfigurationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[ResourceConfigurationTimeoutsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ResourceConfigurationState:
    def __init__(
        __self__,
        *,
        allow_association_to_shareable_service_network: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_verification_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_verification_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_verification_status: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        port_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_configuration_definition: Optional[
            pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionArgs]
        ] = ...,
        resource_configuration_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_gateway_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[ResourceConfigurationTimeoutsArgs]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowAssociationToShareableServiceNetwork")
    def allow_association_to_shareable_service_network(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_association_to_shareable_service_network.setter
    def allow_association_to_shareable_service_network(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_domain_name.setter
    def custom_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainVerificationArn")
    def domain_verification_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_verification_arn.setter
    def domain_verification_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainVerificationId")
    def domain_verification_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_verification_id.setter
    def domain_verification_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainVerificationStatus")
    def domain_verification_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_verification_status.setter
    def domain_verification_status(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @port_ranges.setter
    def port_ranges(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationDefinition")
    def resource_configuration_definition(
        self,
    ) -> Optional[
        pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionArgs]
    ]: ...
    @resource_configuration_definition.setter
    def resource_configuration_definition(
        self,
        value: Optional[
            pulumi.Input[ResourceConfigurationResourceConfigurationDefinitionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationGroupId")
    def resource_configuration_group_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_configuration_group_id.setter
    def resource_configuration_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGatewayIdentifier")
    def resource_gateway_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_gateway_identifier.setter
    def resource_gateway_identifier(
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
    def timeouts(self) -> Optional[pulumi.Input[ResourceConfigurationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[ResourceConfigurationTimeoutsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ResourceConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_association_to_shareable_service_network: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_verification_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        port_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_configuration_definition: Optional[
            pulumi.Input[
                Union[
                    ResourceConfigurationResourceConfigurationDefinitionArgs,
                    ResourceConfigurationResourceConfigurationDefinitionArgsDict,
                ]
            ]
        ] = ...,
        resource_configuration_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_gateway_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    ResourceConfigurationTimeoutsArgs,
                    ResourceConfigurationTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[ResourceConfigurationArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_association_to_shareable_service_network: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_verification_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_verification_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_verification_status: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        port_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_configuration_definition: Optional[
            pulumi.Input[
                Union[
                    ResourceConfigurationResourceConfigurationDefinitionArgs,
                    ResourceConfigurationResourceConfigurationDefinitionArgsDict,
                ]
            ]
        ] = ...,
        resource_configuration_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_gateway_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    ResourceConfigurationTimeoutsArgs,
                    ResourceConfigurationTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ResourceConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="allowAssociationToShareableServiceNetwork")
    def allow_association_to_shareable_service_network(
        self,
    ) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="domainVerificationArn")
    def domain_verification_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainVerificationId")
    def domain_verification_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainVerificationStatus")
    def domain_verification_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationDefinition")
    def resource_configuration_definition(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ResourceConfigurationResourceConfigurationDefinition]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationGroupId")
    def resource_configuration_group_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGatewayIdentifier")
    def resource_gateway_identifier(self) -> pulumi.Output[_builtins.str]: ...
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
    ) -> pulumi.Output[Optional[outputs.ResourceConfigurationTimeouts]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
