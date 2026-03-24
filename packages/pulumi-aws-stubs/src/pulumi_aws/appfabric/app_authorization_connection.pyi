import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AppAuthorizationConnectionArgs", "AppAuthorizationConnection"]

@pulumi.input_type
class AppAuthorizationConnectionArgs:
    def __init__(
        __self__,
        *,
        app_authorization_arn: pulumi.Input[_builtins.str],
        app_bundle_arn: pulumi.Input[_builtins.str],
        auth_request: Optional[
            pulumi.Input[AppAuthorizationConnectionAuthRequestArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[AppAuthorizationConnectionTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appAuthorizationArn")
    def app_authorization_arn(self) -> pulumi.Input[_builtins.str]: ...
    @app_authorization_arn.setter
    def app_authorization_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appBundleArn")
    def app_bundle_arn(self) -> pulumi.Input[_builtins.str]: ...
    @app_bundle_arn.setter
    def app_bundle_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authRequest")
    def auth_request(
        self,
    ) -> Optional[pulumi.Input[AppAuthorizationConnectionAuthRequestArgs]]: ...
    @auth_request.setter
    def auth_request(
        self, value: Optional[pulumi.Input[AppAuthorizationConnectionAuthRequestArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[AppAuthorizationConnectionTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[AppAuthorizationConnectionTimeoutsArgs]]
    ): ...

@pulumi.input_type
class _AppAuthorizationConnectionState:
    def __init__(
        __self__,
        *,
        app: Optional[pulumi.Input[_builtins.str]] = ...,
        app_authorization_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        app_bundle_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_request: Optional[
            pulumi.Input[AppAuthorizationConnectionAuthRequestArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tenants: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppAuthorizationConnectionTenantArgs]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[AppAuthorizationConnectionTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def app(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app.setter
    def app(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="appAuthorizationArn")
    def app_authorization_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_authorization_arn.setter
    def app_authorization_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="appBundleArn")
    def app_bundle_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_bundle_arn.setter
    def app_bundle_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authRequest")
    def auth_request(
        self,
    ) -> Optional[pulumi.Input[AppAuthorizationConnectionAuthRequestArgs]]: ...
    @auth_request.setter
    def auth_request(
        self, value: Optional[pulumi.Input[AppAuthorizationConnectionAuthRequestArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tenants(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppAuthorizationConnectionTenantArgs]]]
    ]: ...
    @tenants.setter
    def tenants(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppAuthorizationConnectionTenantArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[AppAuthorizationConnectionTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[AppAuthorizationConnectionTimeoutsArgs]]
    ): ...

@pulumi.type_token(...)
class AppAuthorizationConnection(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_authorization_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        app_bundle_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_request: Optional[
            pulumi.Input[
                Union[
                    AppAuthorizationConnectionAuthRequestArgs,
                    AppAuthorizationConnectionAuthRequestArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    AppAuthorizationConnectionTimeoutsArgs,
                    AppAuthorizationConnectionTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AppAuthorizationConnectionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        app: Optional[pulumi.Input[_builtins.str]] = ...,
        app_authorization_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        app_bundle_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_request: Optional[
            pulumi.Input[
                Union[
                    AppAuthorizationConnectionAuthRequestArgs,
                    AppAuthorizationConnectionAuthRequestArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tenants: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AppAuthorizationConnectionTenantArgs,
                            AppAuthorizationConnectionTenantArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    AppAuthorizationConnectionTimeoutsArgs,
                    AppAuthorizationConnectionTimeoutsArgsDict,
                ]
            ]
        ] = ...,
    ) -> AppAuthorizationConnection: ...
    @_builtins.property
    @pulumi.getter
    def app(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="appAuthorizationArn")
    def app_authorization_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="appBundleArn")
    def app_bundle_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authRequest")
    def auth_request(
        self,
    ) -> pulumi.Output[Optional[outputs.AppAuthorizationConnectionAuthRequest]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tenants(
        self,
    ) -> pulumi.Output[Sequence[outputs.AppAuthorizationConnectionTenant]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.AppAuthorizationConnectionTimeouts]]: ...
