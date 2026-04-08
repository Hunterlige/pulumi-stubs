import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EmployeePropertiesArgs", "EmployeePropertiesArgsDict"]

class EmployeePropertiesArgsDict(TypedDict):
    age: NotRequired[pulumi.Input[_builtins.int]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    profile: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EmployeePropertiesArgs:
    def __init__(
        __self__,
        *,
        age: Optional[pulumi.Input[_builtins.int]] = ...,
        city: Optional[pulumi.Input[_builtins.str]] = ...,
        profile: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def age(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @age.setter
    def age(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile.setter
    def profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
