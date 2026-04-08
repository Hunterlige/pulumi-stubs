import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApplicationAppversionLifecycleArgs",
    "ApplicationAppversionLifecycleArgsDict",
    "ConfigurationTemplateSettingArgs",
    "ConfigurationTemplateSettingArgsDict",
    "EnvironmentAllSettingArgs",
    "EnvironmentAllSettingArgsDict",
    "EnvironmentSettingArgs",
    "EnvironmentSettingArgsDict",
]

class ApplicationAppversionLifecycleArgsDict(TypedDict):
    service_role: pulumi.Input[_builtins.str]
    delete_source_from_s3: NotRequired[pulumi.Input[_builtins.bool]]
    max_age_in_days: NotRequired[pulumi.Input[_builtins.int]]
    max_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ApplicationAppversionLifecycleArgs:
    def __init__(
        __self__,
        *,
        service_role: pulumi.Input[_builtins.str],
        delete_source_from_s3: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_age_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        max_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> pulumi.Input[_builtins.str]: ...
    @service_role.setter
    def service_role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deleteSourceFromS3")
    def delete_source_from_s3(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @delete_source_from_s3.setter
    def delete_source_from_s3(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxAgeInDays")
    def max_age_in_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_age_in_days.setter
    def max_age_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_count.setter
    def max_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ConfigurationTemplateSettingArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConfigurationTemplateSettingArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnvironmentAllSettingArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EnvironmentAllSettingArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnvironmentSettingArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EnvironmentSettingArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...
