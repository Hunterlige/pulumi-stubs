import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConnectedEnvironmentsDaprComponentArgs",
    "ConnectedEnvironmentsDaprComponent",
]

@pulumi.input_type
class ConnectedEnvironmentsDaprComponentArgs:
    def __init__(
        __self__,
        *,
        connected_environment_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        component_name: Optional[pulumi.Input[_builtins.str]] = ...,
        component_type: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_errors: Optional[pulumi.Input[_builtins.bool]] = ...,
        init_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Sequence[pulumi.Input[DaprMetadataArgs]]]
        ] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        secret_store_component: Optional[pulumi.Input[_builtins.str]] = ...,
        secrets: Optional[pulumi.Input[Sequence[pulumi.Input[SecretArgs]]]] = ...,
        service_component_bind: Optional[
            pulumi.Input[Sequence[pulumi.Input[DaprComponentServiceBindingArgs]]]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectedEnvironmentName")
    def connected_environment_name(self) -> pulumi.Input[_builtins.str]: ...
    @connected_environment_name.setter
    def connected_environment_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="componentName")
    def component_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @component_name.setter
    def component_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="componentType")
    def component_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @component_type.setter
    def component_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreErrors")
    def ignore_errors(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_errors.setter
    def ignore_errors(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="initTimeout")
    def init_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @init_timeout.setter
    def init_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DaprMetadataArgs]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DaprMetadataArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scopes.setter
    def scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretStoreComponent")
    def secret_store_component(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_store_component.setter
    def secret_store_component(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecretArgs]]]]: ...
    @secrets.setter
    def secrets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecretArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceComponentBind")
    def service_component_bind(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DaprComponentServiceBindingArgs]]]
    ]: ...
    @service_component_bind.setter
    def service_component_bind(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DaprComponentServiceBindingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ConnectedEnvironmentsDaprComponent(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        component_name: Optional[pulumi.Input[_builtins.str]] = ...,
        component_type: Optional[pulumi.Input[_builtins.str]] = ...,
        connected_environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_errors: Optional[pulumi.Input[_builtins.bool]] = ...,
        init_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[DaprMetadataArgs, DaprMetadataArgsDict]]]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        secret_store_component: Optional[pulumi.Input[_builtins.str]] = ...,
        secrets: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[SecretArgs, SecretArgsDict]]]]
        ] = ...,
        service_component_bind: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DaprComponentServiceBindingArgs,
                            DaprComponentServiceBindingArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ConnectedEnvironmentsDaprComponentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ConnectedEnvironmentsDaprComponent: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="componentType")
    def component_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentErrors")
    def deployment_errors(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreErrors")
    def ignore_errors(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="initTimeout")
    def init_timeout(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.DaprMetadataResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="secretStoreComponent")
    def secret_store_component(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> pulumi.Output[Optional[Sequence[outputs.SecretResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceComponentBind")
    def service_component_bind(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.DaprComponentServiceBindingResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
