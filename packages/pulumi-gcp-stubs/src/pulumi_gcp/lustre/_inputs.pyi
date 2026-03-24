import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "InstanceAccessRulesOptionsArgs",
    "InstanceAccessRulesOptionsArgsDict",
    "InstanceAccessRulesOptionsAccessRuleArgs",
    "InstanceAccessRulesOptionsAccessRuleArgsDict",
]

class InstanceAccessRulesOptionsArgsDict(TypedDict):
    default_squash_mode: pulumi.Input[_builtins.str]
    access_rules: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InstanceAccessRulesOptionsAccessRuleArgsDict]]
        ]
    ]
    default_squash_gid: NotRequired[pulumi.Input[_builtins.int]]
    default_squash_uid: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceAccessRulesOptionsArgs:
    def __init__(
        __self__,
        *,
        default_squash_mode: pulumi.Input[_builtins.str],
        access_rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceAccessRulesOptionsAccessRuleArgs]]
            ]
        ] = ...,
        default_squash_gid: Optional[pulumi.Input[_builtins.int]] = ...,
        default_squash_uid: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultSquashMode")
    def default_squash_mode(self) -> pulumi.Input[_builtins.str]: ...
    @default_squash_mode.setter
    def default_squash_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accessRules")
    def access_rules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceAccessRulesOptionsAccessRuleArgs]]]
    ]: ...
    @access_rules.setter
    def access_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceAccessRulesOptionsAccessRuleArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultSquashGid")
    def default_squash_gid(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_squash_gid.setter
    def default_squash_gid(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultSquashUid")
    def default_squash_uid(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_squash_uid.setter
    def default_squash_uid(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstanceAccessRulesOptionsAccessRuleArgsDict(TypedDict):
    ip_address_ranges: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    name: pulumi.Input[_builtins.str]
    squash_mode: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class InstanceAccessRulesOptionsAccessRuleArgs:
    def __init__(
        __self__,
        *,
        ip_address_ranges: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        name: pulumi.Input[_builtins.str],
        squash_mode: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressRanges")
    def ip_address_ranges(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @ip_address_ranges.setter
    def ip_address_ranges(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="squashMode")
    def squash_mode(self) -> pulumi.Input[_builtins.str]: ...
    @squash_mode.setter
    def squash_mode(self, value: pulumi.Input[_builtins.str]): ...
