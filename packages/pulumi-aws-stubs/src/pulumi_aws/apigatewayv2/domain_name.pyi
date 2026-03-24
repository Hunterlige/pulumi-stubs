import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DomainNameArgs", "DomainName"]

@pulumi.input_type
class DomainNameArgs:
    def __init__(
        __self__,
        *,
        domain_name: pulumi.Input[_builtins.str],
        domain_name_configuration: pulumi.Input[DomainNameDomainNameConfigurationArgs],
        mutual_tls_authentication: Optional[
            pulumi.Input[DomainNameMutualTlsAuthenticationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="domainNameConfiguration")
    def domain_name_configuration(
        self,
    ) -> pulumi.Input[DomainNameDomainNameConfigurationArgs]: ...
    @domain_name_configuration.setter
    def domain_name_configuration(
        self, value: pulumi.Input[DomainNameDomainNameConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mutualTlsAuthentication")
    def mutual_tls_authentication(
        self,
    ) -> Optional[pulumi.Input[DomainNameMutualTlsAuthenticationArgs]]: ...
    @mutual_tls_authentication.setter
    def mutual_tls_authentication(
        self, value: Optional[pulumi.Input[DomainNameMutualTlsAuthenticationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingMode")
    def routing_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_mode.setter
    def routing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _DomainNameState:
    def __init__(
        __self__,
        *,
        api_mapping_selection_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name_configuration: Optional[
            pulumi.Input[DomainNameDomainNameConfigurationArgs]
        ] = ...,
        mutual_tls_authentication: Optional[
            pulumi.Input[DomainNameMutualTlsAuthenticationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiMappingSelectionExpression")
    def api_mapping_selection_expression(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_mapping_selection_expression.setter
    def api_mapping_selection_expression(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainNameConfiguration")
    def domain_name_configuration(
        self,
    ) -> Optional[pulumi.Input[DomainNameDomainNameConfigurationArgs]]: ...
    @domain_name_configuration.setter
    def domain_name_configuration(
        self, value: Optional[pulumi.Input[DomainNameDomainNameConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mutualTlsAuthentication")
    def mutual_tls_authentication(
        self,
    ) -> Optional[pulumi.Input[DomainNameMutualTlsAuthenticationArgs]]: ...
    @mutual_tls_authentication.setter
    def mutual_tls_authentication(
        self, value: Optional[pulumi.Input[DomainNameMutualTlsAuthenticationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingMode")
    def routing_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_mode.setter
    def routing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token("aws:apigatewayv2/domainName:DomainName")
class DomainName(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name_configuration: Optional[
            pulumi.Input[
                Union[
                    DomainNameDomainNameConfigurationArgs,
                    DomainNameDomainNameConfigurationArgsDict,
                ]
            ]
        ] = ...,
        mutual_tls_authentication: Optional[
            pulumi.Input[
                Union[
                    DomainNameMutualTlsAuthenticationArgs,
                    DomainNameMutualTlsAuthenticationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DomainNameArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_mapping_selection_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name_configuration: Optional[
            pulumi.Input[
                Union[
                    DomainNameDomainNameConfigurationArgs,
                    DomainNameDomainNameConfigurationArgsDict,
                ]
            ]
        ] = ...,
        mutual_tls_authentication: Optional[
            pulumi.Input[
                Union[
                    DomainNameMutualTlsAuthenticationArgs,
                    DomainNameMutualTlsAuthenticationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> DomainName: ...
    @_builtins.property
    @pulumi.getter(name="apiMappingSelectionExpression")
    def api_mapping_selection_expression(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainNameConfiguration")
    def domain_name_configuration(
        self,
    ) -> pulumi.Output[outputs.DomainNameDomainNameConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="mutualTlsAuthentication")
    def mutual_tls_authentication(
        self,
    ) -> pulumi.Output[Optional[outputs.DomainNameMutualTlsAuthentication]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingMode")
    def routing_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
