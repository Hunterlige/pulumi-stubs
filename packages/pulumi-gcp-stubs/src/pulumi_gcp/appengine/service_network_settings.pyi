import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ServiceNetworkSettingsArgs", "ServiceNetworkSettings"]

@pulumi.input_type
class ServiceNetworkSettingsArgs:
    def __init__(
        __self__,
        *,
        network_settings: pulumi.Input[ServiceNetworkSettingsNetworkSettingsArgs],
        service: pulumi.Input[_builtins.str],
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkSettings")
    def network_settings(
        self,
    ) -> pulumi.Input[ServiceNetworkSettingsNetworkSettingsArgs]: ...
    @network_settings.setter
    def network_settings(
        self, value: pulumi.Input[ServiceNetworkSettingsNetworkSettingsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ServiceNetworkSettingsState:
    def __init__(
        __self__,
        *,
        network_settings: Optional[
            pulumi.Input[ServiceNetworkSettingsNetworkSettingsArgs]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkSettings")
    def network_settings(
        self,
    ) -> Optional[pulumi.Input[ServiceNetworkSettingsNetworkSettingsArgs]]: ...
    @network_settings.setter
    def network_settings(
        self, value: Optional[pulumi.Input[ServiceNetworkSettingsNetworkSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ServiceNetworkSettings(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        network_settings: Optional[
            pulumi.Input[
                Union[
                    ServiceNetworkSettingsNetworkSettingsArgs,
                    ServiceNetworkSettingsNetworkSettingsArgsDict,
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ServiceNetworkSettingsArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        network_settings: Optional[
            pulumi.Input[
                Union[
                    ServiceNetworkSettingsNetworkSettingsArgs,
                    ServiceNetworkSettingsNetworkSettingsArgsDict,
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ServiceNetworkSettings: ...
    @_builtins.property
    @pulumi.getter(name="networkSettings")
    def network_settings(
        self,
    ) -> pulumi.Output[outputs.ServiceNetworkSettingsNetworkSettings]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Output[_builtins.str]: ...
