import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PolicyDefinitionAtManagementGroupArgs", "PolicyDefinitionAtManagementGroup"]

@pulumi.input_type
class PolicyDefinitionAtManagementGroupArgs:
    def __init__(
        __self__,
        *,
        management_group_id: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[Any] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ParameterDefinitionsValueArgs]]]
        ] = ...,
        policy_definition_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_rule: Optional[Any] = ...,
        policy_type: Optional[pulumi.Input[Union[_builtins.str, PolicyType]]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        versions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @management_group_id.setter
    def management_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]: ...
    @metadata.setter
    def metadata(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[ParameterDefinitionsValueArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ParameterDefinitionsValueArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyDefinitionName")
    def policy_definition_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_definition_name.setter
    def policy_definition_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyRule")
    def policy_rule(self) -> Optional[Any]: ...
    @policy_rule.setter
    def policy_rule(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PolicyType]]]: ...
    @policy_type.setter
    def policy_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @versions.setter
    def versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token(...)
class PolicyDefinitionAtManagementGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        management_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[Any] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            ParameterDefinitionsValueArgs,
                            ParameterDefinitionsValueArgsDict,
                        ]
                    ],
                ]
            ]
        ] = ...,
        policy_definition_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_rule: Optional[Any] = ...,
        policy_type: Optional[pulumi.Input[Union[_builtins.str, PolicyType]]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        versions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PolicyDefinitionAtManagementGroupArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> PolicyDefinitionAtManagementGroup: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> pulumi.Output[
        Optional[Mapping[str, outputs.ParameterDefinitionsValueResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="policyRule")
    def policy_rule(self) -> pulumi.Output[Optional[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def versions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
