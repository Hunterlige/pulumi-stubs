import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EndpointAuthenticationOptionArgs",
    "EndpointAuthenticationOptionArgsDict",
    "EndpointClientConnectOptionsArgs",
    "EndpointClientConnectOptionsArgsDict",
    "EndpointClientLoginBannerOptionsArgs",
    "EndpointClientLoginBannerOptionsArgsDict",
    "EndpointClientRouteEnforcementOptionsArgs",
    "EndpointClientRouteEnforcementOptionsArgsDict",
    "EndpointConnectionLogOptionsArgs",
    "EndpointConnectionLogOptionsArgsDict",
    "GetEndpointFilterArgs",
    "GetEndpointFilterArgsDict",
]

class EndpointAuthenticationOptionArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    active_directory_id: NotRequired[pulumi.Input[_builtins.str]]
    root_certificate_chain_arn: NotRequired[pulumi.Input[_builtins.str]]
    saml_provider_arn: NotRequired[pulumi.Input[_builtins.str]]
    self_service_saml_provider_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EndpointAuthenticationOptionArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        active_directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        root_certificate_chain_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        saml_provider_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        self_service_saml_provider_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="activeDirectoryId")
    def active_directory_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @active_directory_id.setter
    def active_directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootCertificateChainArn")
    def root_certificate_chain_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_certificate_chain_arn.setter
    def root_certificate_chain_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="samlProviderArn")
    def saml_provider_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @saml_provider_arn.setter
    def saml_provider_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfServiceSamlProviderArn")
    def self_service_saml_provider_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_service_saml_provider_arn.setter
    def self_service_saml_provider_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class EndpointClientConnectOptionsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    lambda_function_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EndpointClientConnectOptionsArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        lambda_function_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionArn")
    def lambda_function_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lambda_function_arn.setter
    def lambda_function_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EndpointClientLoginBannerOptionsArgsDict(TypedDict):
    banner_text: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class EndpointClientLoginBannerOptionsArgs:
    def __init__(
        __self__,
        *,
        banner_text: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bannerText")
    def banner_text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @banner_text.setter
    def banner_text(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class EndpointClientRouteEnforcementOptionsArgsDict(TypedDict):
    enforced: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class EndpointClientRouteEnforcementOptionsArgs:
    def __init__(
        __self__, *, enforced: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enforced(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enforced.setter
    def enforced(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class EndpointConnectionLogOptionsArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    cloudwatch_log_group: NotRequired[pulumi.Input[_builtins.str]]
    cloudwatch_log_stream: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EndpointConnectionLogOptionsArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        cloudwatch_log_group: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatch_log_stream: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroup")
    def cloudwatch_log_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatch_log_group.setter
    def cloudwatch_log_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogStream")
    def cloudwatch_log_stream(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudwatch_log_stream.setter
    def cloudwatch_log_stream(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GetEndpointFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetEndpointFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...
