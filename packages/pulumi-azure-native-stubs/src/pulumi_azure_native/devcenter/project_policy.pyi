import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProjectPolicyArgs", "ProjectPolicy"]

@pulumi.input_type
class ProjectPolicyArgs:
    def __init__(
        __self__,
        *,
        dev_center_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        project_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourcePolicyArgs]]]
        ] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="devCenterName")
    def dev_center_name(self) -> pulumi.Input[_builtins.str]: ...
    @dev_center_name.setter
    def dev_center_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectPolicyName")
    def project_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_policy_name.setter
    def project_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourcePolicyArgs]]]]: ...
    @resource_policies.setter
    def resource_policies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourcePolicyArgs]]]]
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

@pulumi.type_token("azure-native:devcenter:ProjectPolicy")
class ProjectPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        dev_center_name: Optional[pulumi.Input[_builtins.str]] = ...,
        project_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[ResourcePolicyArgs, ResourcePolicyArgsDict]]
                ]
            ]
        ] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ProjectPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ProjectPolicy: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ResourcePolicyResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
