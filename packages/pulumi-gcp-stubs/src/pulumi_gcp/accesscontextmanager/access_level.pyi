import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccessLevelArgs", "AccessLevel"]

@pulumi.input_type
class AccessLevelArgs:
    def __init__(
        __self__,
        *,
        parent: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        basic: Optional[pulumi.Input[AccessLevelBasicArgs]] = ...,
        custom: Optional[pulumi.Input[AccessLevelCustomArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]: ...
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def basic(self) -> Optional[pulumi.Input[AccessLevelBasicArgs]]: ...
    @basic.setter
    def basic(self, value: Optional[pulumi.Input[AccessLevelBasicArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def custom(self) -> Optional[pulumi.Input[AccessLevelCustomArgs]]: ...
    @custom.setter
    def custom(self, value: Optional[pulumi.Input[AccessLevelCustomArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AccessLevelState:
    def __init__(
        __self__,
        *,
        basic: Optional[pulumi.Input[AccessLevelBasicArgs]] = ...,
        custom: Optional[pulumi.Input[AccessLevelCustomArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def basic(self) -> Optional[pulumi.Input[AccessLevelBasicArgs]]: ...
    @basic.setter
    def basic(self, value: Optional[pulumi.Input[AccessLevelBasicArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def custom(self) -> Optional[pulumi.Input[AccessLevelCustomArgs]]: ...
    @custom.setter
    def custom(self, value: Optional[pulumi.Input[AccessLevelCustomArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:accesscontextmanager/accessLevel:AccessLevel")
class AccessLevel(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        basic: Optional[
            pulumi.Input[Union[AccessLevelBasicArgs, AccessLevelBasicArgsDict]]
        ] = ...,
        custom: Optional[
            pulumi.Input[Union[AccessLevelCustomArgs, AccessLevelCustomArgsDict]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AccessLevelArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        basic: Optional[
            pulumi.Input[Union[AccessLevelBasicArgs, AccessLevelBasicArgsDict]]
        ] = ...,
        custom: Optional[
            pulumi.Input[Union[AccessLevelCustomArgs, AccessLevelCustomArgsDict]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AccessLevel: ...
    @_builtins.property
    @pulumi.getter
    def basic(self) -> pulumi.Output[Optional[outputs.AccessLevelBasic]]: ...
    @_builtins.property
    @pulumi.getter
    def custom(self) -> pulumi.Output[Optional[outputs.AccessLevelCustom]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Output[_builtins.str]: ...
