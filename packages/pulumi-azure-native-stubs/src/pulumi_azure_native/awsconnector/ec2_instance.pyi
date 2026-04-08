import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["Ec2InstanceArgs", "Ec2Instance"]

@pulumi.input_type
class Ec2InstanceArgs:
    def __init__(
        __self__,
        *,
        resource_uri: pulumi.Input[_builtins.str],
        properties: Optional[pulumi.Input[Ec2InstancePropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[_builtins.str]: ...
    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Ec2InstancePropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Ec2InstancePropertiesArgs]]): ...

@pulumi.type_token("azure-native:awsconnector:Ec2Instance")
class Ec2Instance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        properties: Optional[
            pulumi.Input[
                Union[Ec2InstancePropertiesArgs, Ec2InstancePropertiesArgsDict]
            ]
        ] = ...,
        resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Ec2InstanceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Ec2Instance: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.Ec2InstancePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
