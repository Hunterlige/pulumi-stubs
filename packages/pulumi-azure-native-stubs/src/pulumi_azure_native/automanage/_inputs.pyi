import builtins as _builtins
import sys
import pulumi
from typing import Any, NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConfigurationProfileAssignmentPropertiesArgs",
    "ConfigurationProfileAssignmentPropertiesArgsDict",
    "ConfigurationProfilePropertiesArgs",
    "ConfigurationProfilePropertiesArgsDict",
]

class ConfigurationProfileAssignmentPropertiesArgsDict(TypedDict):
    configuration_profile: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConfigurationProfileAssignmentPropertiesArgs:
    def __init__(
        __self__, *, configuration_profile: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationProfile")
    def configuration_profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configuration_profile.setter
    def configuration_profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConfigurationProfilePropertiesArgsDict(TypedDict):
    configuration: NotRequired[Any]

@pulumi.input_type
class ConfigurationProfilePropertiesArgs:
    def __init__(__self__, *, configuration: Optional[Any] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[Any]: ...
    @configuration.setter
    def configuration(self, value: Optional[Any]): ...
