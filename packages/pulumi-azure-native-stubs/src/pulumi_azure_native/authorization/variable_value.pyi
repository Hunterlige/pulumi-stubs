import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VariableValueArgs", "VariableValue"]

@pulumi.input_type
class VariableValueArgs:
    def __init__(
        __self__,
        *,
        values: pulumi.Input[
            Sequence[pulumi.Input[PolicyVariableValueColumnValueArgs]]
        ],
        variable_name: pulumi.Input[_builtins.str],
        variable_value_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[PolicyVariableValueColumnValueArgs]]]: ...
    @values.setter
    def values(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[PolicyVariableValueColumnValueArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="variableName")
    def variable_name(self) -> pulumi.Input[_builtins.str]: ...
    @variable_name.setter
    def variable_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="variableValueName")
    def variable_value_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @variable_value_name.setter
    def variable_value_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:authorization:VariableValue")
class VariableValue(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        values: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PolicyVariableValueColumnValueArgs,
                            PolicyVariableValueColumnValueArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        variable_name: Optional[pulumi.Input[_builtins.str]] = ...,
        variable_value_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VariableValueArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VariableValue: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> pulumi.Output[Sequence[outputs.PolicyVariableValueColumnValueResponse]]: ...
