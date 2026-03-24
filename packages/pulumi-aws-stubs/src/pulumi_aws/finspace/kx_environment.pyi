import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KxEnvironmentArgs", "KxEnvironment"]

@pulumi.input_type
class KxEnvironmentArgs:
    def __init__(
        __self__,
        *,
        kms_key_id: pulumi.Input[_builtins.str],
        custom_dns_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[KxEnvironmentCustomDnsConfigurationArgs]]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transit_gateway_configuration: Optional[
            pulumi.Input[KxEnvironmentTransitGatewayConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customDnsConfigurations")
    def custom_dns_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[KxEnvironmentCustomDnsConfigurationArgs]]]
    ]: ...
    @custom_dns_configurations.setter
    def custom_dns_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[KxEnvironmentCustomDnsConfigurationArgs]]
            ]
        ],
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
    @pulumi.getter(name="transitGatewayConfiguration")
    def transit_gateway_configuration(
        self,
    ) -> Optional[pulumi.Input[KxEnvironmentTransitGatewayConfigurationArgs]]: ...
    @transit_gateway_configuration.setter
    def transit_gateway_configuration(
        self,
        value: Optional[pulumi.Input[KxEnvironmentTransitGatewayConfigurationArgs]],
    ): ...

@pulumi.input_type
class _KxEnvironmentState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        created_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_dns_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[KxEnvironmentCustomDnsConfigurationArgs]]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        infrastructure_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_modified_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transit_gateway_configuration: Optional[
            pulumi.Input[KxEnvironmentTransitGatewayConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @availability_zones.setter
    def availability_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_timestamp.setter
    def created_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customDnsConfigurations")
    def custom_dns_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[KxEnvironmentCustomDnsConfigurationArgs]]]
    ]: ...
    @custom_dns_configurations.setter
    def custom_dns_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[KxEnvironmentCustomDnsConfigurationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="infrastructureAccountId")
    def infrastructure_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @infrastructure_account_id.setter
    def infrastructure_account_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTimestamp")
    def last_modified_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_modified_timestamp.setter
    def last_modified_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="transitGatewayConfiguration")
    def transit_gateway_configuration(
        self,
    ) -> Optional[pulumi.Input[KxEnvironmentTransitGatewayConfigurationArgs]]: ...
    @transit_gateway_configuration.setter
    def transit_gateway_configuration(
        self,
        value: Optional[pulumi.Input[KxEnvironmentTransitGatewayConfigurationArgs]],
    ): ...

@pulumi.type_token("aws:finspace/kxEnvironment:KxEnvironment")
class KxEnvironment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        custom_dns_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            KxEnvironmentCustomDnsConfigurationArgs,
                            KxEnvironmentCustomDnsConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transit_gateway_configuration: Optional[
            pulumi.Input[
                Union[
                    KxEnvironmentTransitGatewayConfigurationArgs,
                    KxEnvironmentTransitGatewayConfigurationArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: KxEnvironmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        created_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_dns_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            KxEnvironmentCustomDnsConfigurationArgs,
                            KxEnvironmentCustomDnsConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        infrastructure_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_modified_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transit_gateway_configuration: Optional[
            pulumi.Input[
                Union[
                    KxEnvironmentTransitGatewayConfigurationArgs,
                    KxEnvironmentTransitGatewayConfigurationArgsDict,
                ]
            ]
        ] = ...,
    ) -> KxEnvironment: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customDnsConfigurations")
    def custom_dns_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.KxEnvironmentCustomDnsConfiguration]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureAccountId")
    def infrastructure_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTimestamp")
    def last_modified_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayConfiguration")
    def transit_gateway_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.KxEnvironmentTransitGatewayConfiguration]]: ...
