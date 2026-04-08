import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["HyperVCollectorArgs", "HyperVCollector"]

@pulumi.input_type
class HyperVCollectorArgs:
    def __init__(
        __self__,
        *,
        project_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        e_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        hyper_v_collector_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[CollectorPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[_builtins.str]: ...
    @project_name.setter
    def project_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hyperVCollectorName")
    def hyper_v_collector_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hyper_v_collector_name.setter
    def hyper_v_collector_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[CollectorPropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[CollectorPropertiesArgs]]): ...

@pulumi.type_token("azure-native:migrate:HyperVCollector")
class HyperVCollector(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        e_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        hyper_v_collector_name: Optional[pulumi.Input[_builtins.str]] = ...,
        project_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Union[CollectorPropertiesArgs, CollectorPropertiesArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: HyperVCollectorArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> HyperVCollector: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.CollectorPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
