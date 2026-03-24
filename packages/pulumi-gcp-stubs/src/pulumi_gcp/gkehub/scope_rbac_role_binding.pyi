import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ScopeRbacRoleBindingArgs", "ScopeRbacRoleBinding"]

@pulumi.input_type
class ScopeRbacRoleBindingArgs:
    def __init__(
        __self__,
        *,
        role: pulumi.Input[ScopeRbacRoleBindingRoleArgs],
        scope_id: pulumi.Input[_builtins.str],
        scope_rbac_role_binding_id: pulumi.Input[_builtins.str],
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[ScopeRbacRoleBindingRoleArgs]: ...
    @role.setter
    def role(self, value: pulumi.Input[ScopeRbacRoleBindingRoleArgs]): ...
    @_builtins.property
    @pulumi.getter(name="scopeId")
    def scope_id(self) -> pulumi.Input[_builtins.str]: ...
    @scope_id.setter
    def scope_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scopeRbacRoleBindingId")
    def scope_rbac_role_binding_id(self) -> pulumi.Input[_builtins.str]: ...
    @scope_rbac_role_binding_id.setter
    def scope_rbac_role_binding_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group.setter
    def group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user.setter
    def user(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ScopeRbacRoleBindingState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        role: Optional[pulumi.Input[ScopeRbacRoleBindingRoleArgs]] = ...,
        scope_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scope_rbac_role_binding_id: Optional[pulumi.Input[_builtins.str]] = ...,
        states: Optional[
            pulumi.Input[Sequence[pulumi.Input[ScopeRbacRoleBindingStateArgs]]]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group.setter
    def group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[ScopeRbacRoleBindingRoleArgs]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[ScopeRbacRoleBindingRoleArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="scopeId")
    def scope_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope_id.setter
    def scope_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scopeRbacRoleBindingId")
    def scope_rbac_role_binding_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope_rbac_role_binding_id.setter
    def scope_rbac_role_binding_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def states(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ScopeRbacRoleBindingStateArgs]]]
    ]: ...
    @states.setter
    def states(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ScopeRbacRoleBindingStateArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user.setter
    def user(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ScopeRbacRoleBinding(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[
            pulumi.Input[
                Union[ScopeRbacRoleBindingRoleArgs, ScopeRbacRoleBindingRoleArgsDict]
            ]
        ] = ...,
        scope_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scope_rbac_role_binding_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ScopeRbacRoleBindingArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        role: Optional[
            pulumi.Input[
                Union[ScopeRbacRoleBindingRoleArgs, ScopeRbacRoleBindingRoleArgsDict]
            ]
        ] = ...,
        scope_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scope_rbac_role_binding_id: Optional[pulumi.Input[_builtins.str]] = ...,
        states: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ScopeRbacRoleBindingStateArgs,
                            ScopeRbacRoleBindingStateArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ScopeRbacRoleBinding: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[outputs.ScopeRbacRoleBindingRole]: ...
    @_builtins.property
    @pulumi.getter(name="scopeId")
    def scope_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scopeRbacRoleBindingId")
    def scope_rbac_role_binding_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def states(self) -> pulumi.Output[Sequence[outputs.ScopeRbacRoleBindingState]]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Output[Optional[_builtins.str]]: ...
