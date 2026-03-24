import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["IdentityPoolRoleAttachmentArgs", "IdentityPoolRoleAttachment"]

@pulumi.input_type
class IdentityPoolRoleAttachmentArgs:
    def __init__(
        __self__,
        *,
        identity_pool_id: pulumi.Input[_builtins.str],
        roles: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_mappings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[IdentityPoolRoleAttachmentRoleMappingArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> pulumi.Input[_builtins.str]: ...
    @identity_pool_id.setter
    def identity_pool_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @roles.setter
    def roles(self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleMappings")
    def role_mappings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[IdentityPoolRoleAttachmentRoleMappingArgs]]]
    ]: ...
    @role_mappings.setter
    def role_mappings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[IdentityPoolRoleAttachmentRoleMappingArgs]]
            ]
        ],
    ): ...

@pulumi.input_type
class _IdentityPoolRoleAttachmentState:
    def __init__(
        __self__,
        *,
        identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_mappings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[IdentityPoolRoleAttachmentRoleMappingArgs]]
            ]
        ] = ...,
        roles: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_pool_id.setter
    def identity_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleMappings")
    def role_mappings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[IdentityPoolRoleAttachmentRoleMappingArgs]]]
    ]: ...
    @role_mappings.setter
    def role_mappings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[IdentityPoolRoleAttachmentRoleMappingArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token(...)
class IdentityPoolRoleAttachment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_mappings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            IdentityPoolRoleAttachmentRoleMappingArgs,
                            IdentityPoolRoleAttachmentRoleMappingArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        roles: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: IdentityPoolRoleAttachmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_mappings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            IdentityPoolRoleAttachmentRoleMappingArgs,
                            IdentityPoolRoleAttachmentRoleMappingArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        roles: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> IdentityPoolRoleAttachment: ...
    @_builtins.property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleMappings")
    def role_mappings(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.IdentityPoolRoleAttachmentRoleMapping]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
