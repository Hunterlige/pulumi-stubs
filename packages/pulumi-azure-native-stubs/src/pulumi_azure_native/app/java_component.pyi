import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["JavaComponentArgs", "JavaComponent"]

@pulumi.input_type
class JavaComponentArgs:
    def __init__(
        __self__,
        *,
        environment_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    NacosComponentArgs,
                    SpringBootAdminComponentArgs,
                    SpringCloudConfigComponentArgs,
                    SpringCloudEurekaComponentArgs,
                    SpringCloudGatewayComponentArgs,
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Input[_builtins.str]: ...
    @environment_name.setter
    def environment_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                NacosComponentArgs,
                SpringBootAdminComponentArgs,
                SpringCloudConfigComponentArgs,
                SpringCloudEurekaComponentArgs,
                SpringCloudGatewayComponentArgs,
            ]
        ]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    NacosComponentArgs,
                    SpringBootAdminComponentArgs,
                    SpringCloudConfigComponentArgs,
                    SpringCloudEurekaComponentArgs,
                    SpringCloudGatewayComponentArgs,
                ]
            ]
        ],
    ): ...

@pulumi.type_token("azure-native:app:JavaComponent")
class JavaComponent(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    Union[NacosComponentArgs, NacosComponentArgsDict],
                    Union[
                        SpringBootAdminComponentArgs, SpringBootAdminComponentArgsDict
                    ],
                    Union[
                        SpringCloudConfigComponentArgs,
                        SpringCloudConfigComponentArgsDict,
                    ],
                    Union[
                        SpringCloudEurekaComponentArgs,
                        SpringCloudEurekaComponentArgsDict,
                    ],
                    Union[
                        SpringCloudGatewayComponentArgs,
                        SpringCloudGatewayComponentArgsDict,
                    ],
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
        args: JavaComponentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> JavaComponent: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
