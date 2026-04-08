import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ExecutionArgs", "Execution"]

@pulumi.input_type
class ExecutionArgs:
    def __init__(
        __self__,
        *,
        context_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        version_name: pulumi.Input[_builtins.str],
        workflow_name: pulumi.Input[_builtins.str],
        execution_name: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_location: Optional[
            pulumi.Input[AzureResourceManagerCommonTypesExtendedLocationArgs]
        ] = ...,
        properties: Optional[pulumi.Input[ExecutionPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contextName")
    def context_name(self) -> pulumi.Input[_builtins.str]: ...
    @context_name.setter
    def context_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> pulumi.Input[_builtins.str]: ...
    @version_name.setter
    def version_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workflowName")
    def workflow_name(self) -> pulumi.Input[_builtins.str]: ...
    @workflow_name.setter
    def workflow_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="executionName")
    def execution_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_name.setter
    def execution_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> Optional[
        pulumi.Input[AzureResourceManagerCommonTypesExtendedLocationArgs]
    ]: ...
    @extended_location.setter
    def extended_location(
        self,
        value: Optional[
            pulumi.Input[AzureResourceManagerCommonTypesExtendedLocationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[ExecutionPropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[ExecutionPropertiesArgs]]): ...

@pulumi.type_token("azure-native:edge:Execution")
class Execution(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        context_name: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_name: Optional[pulumi.Input[_builtins.str]] = ...,
        extended_location: Optional[
            pulumi.Input[
                Union[
                    AzureResourceManagerCommonTypesExtendedLocationArgs,
                    AzureResourceManagerCommonTypesExtendedLocationArgsDict,
                ]
            ]
        ] = ...,
        properties: Optional[
            pulumi.Input[Union[ExecutionPropertiesArgs, ExecutionPropertiesArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        version_name: Optional[pulumi.Input[_builtins.str]] = ...,
        workflow_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ExecutionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Execution: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AzureResourceManagerCommonTypesExtendedLocationResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.ExecutionPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
