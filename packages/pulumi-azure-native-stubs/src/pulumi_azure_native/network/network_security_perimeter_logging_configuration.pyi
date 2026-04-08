import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "NetworkSecurityPerimeterLoggingConfigurationArgs",
    "NetworkSecurityPerimeterLoggingConfiguration",
]

@pulumi.input_type
class NetworkSecurityPerimeterLoggingConfigurationArgs:
    def __init__(
        __self__,
        *,
        network_security_perimeter_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        logging_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[NspLoggingConfigurationPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkSecurityPerimeterName")
    def network_security_perimeter_name(self) -> pulumi.Input[_builtins.str]: ...
    @network_security_perimeter_name.setter
    def network_security_perimeter_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfigurationName")
    def logging_configuration_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logging_configuration_name.setter
    def logging_configuration_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[NspLoggingConfigurationPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[NspLoggingConfigurationPropertiesArgs]]
    ): ...

@pulumi.type_token(...)
class NetworkSecurityPerimeterLoggingConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        logging_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_security_perimeter_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    NspLoggingConfigurationPropertiesArgs,
                    NspLoggingConfigurationPropertiesArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NetworkSecurityPerimeterLoggingConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> NetworkSecurityPerimeterLoggingConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Output[outputs.NspLoggingConfigurationPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
