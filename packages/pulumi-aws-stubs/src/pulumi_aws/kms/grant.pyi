import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GrantArgs", "Grant"]

@pulumi.input_type
class GrantArgs:
    def __init__(
        __self__,
        *,
        grantee_principal: pulumi.Input[_builtins.str],
        key_id: pulumi.Input[_builtins.str],
        operations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        constraints: Optional[
            pulumi.Input[Sequence[pulumi.Input[GrantConstraintArgs]]]
        ] = ...,
        grant_creation_tokens: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retire_on_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        retiring_principal: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="granteePrincipal")
    def grantee_principal(self) -> pulumi.Input[_builtins.str]: ...
    @grantee_principal.setter
    def grantee_principal(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Input[_builtins.str]: ...
    @key_id.setter
    def key_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operations(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @operations.setter
    def operations(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def constraints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[GrantConstraintArgs]]]]: ...
    @constraints.setter
    def constraints(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GrantConstraintArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="grantCreationTokens")
    def grant_creation_tokens(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @grant_creation_tokens.setter
    def grant_creation_tokens(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retireOnDelete")
    def retire_on_delete(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @retire_on_delete.setter
    def retire_on_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="retiringPrincipal")
    def retiring_principal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @retiring_principal.setter
    def retiring_principal(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _GrantState:
    def __init__(
        __self__,
        *,
        constraints: Optional[
            pulumi.Input[Sequence[pulumi.Input[GrantConstraintArgs]]]
        ] = ...,
        grant_creation_tokens: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        grant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        grant_token: Optional[pulumi.Input[_builtins.str]] = ...,
        grantee_principal: Optional[pulumi.Input[_builtins.str]] = ...,
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        operations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retire_on_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        retiring_principal: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def constraints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[GrantConstraintArgs]]]]: ...
    @constraints.setter
    def constraints(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GrantConstraintArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="grantCreationTokens")
    def grant_creation_tokens(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @grant_creation_tokens.setter
    def grant_creation_tokens(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="grantId")
    def grant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grant_id.setter
    def grant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grantToken")
    def grant_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grant_token.setter
    def grant_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="granteePrincipal")
    def grantee_principal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grantee_principal.setter
    def grantee_principal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def operations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @operations.setter
    def operations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retireOnDelete")
    def retire_on_delete(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @retire_on_delete.setter
    def retire_on_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="retiringPrincipal")
    def retiring_principal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @retiring_principal.setter
    def retiring_principal(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:kms/grant:Grant")
class Grant(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        constraints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[GrantConstraintArgs, GrantConstraintArgsDict]]
                ]
            ]
        ] = ...,
        grant_creation_tokens: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        grantee_principal: Optional[pulumi.Input[_builtins.str]] = ...,
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        operations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retire_on_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        retiring_principal: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GrantArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        constraints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[GrantConstraintArgs, GrantConstraintArgsDict]]
                ]
            ]
        ] = ...,
        grant_creation_tokens: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        grant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        grant_token: Optional[pulumi.Input[_builtins.str]] = ...,
        grantee_principal: Optional[pulumi.Input[_builtins.str]] = ...,
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        operations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retire_on_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        retiring_principal: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Grant: ...
    @_builtins.property
    @pulumi.getter
    def constraints(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.GrantConstraint]]]: ...
    @_builtins.property
    @pulumi.getter(name="grantCreationTokens")
    def grant_creation_tokens(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="grantId")
    def grant_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="grantToken")
    def grant_token(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="granteePrincipal")
    def grantee_principal(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def operations(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retireOnDelete")
    def retire_on_delete(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="retiringPrincipal")
    def retiring_principal(self) -> pulumi.Output[Optional[_builtins.str]]: ...
