import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AddDataLakeStoreWithAccountParametersArgs",
    "AddDataLakeStoreWithAccountParametersArgsDict",
    "AddStorageAccountWithAccountParametersArgs",
    "AddStorageAccountWithAccountParametersArgsDict",
    "CreateComputePolicyWithAccountParametersArgs",
    "CreateComputePolicyWithAccountParametersArgsDict",
    "CreateFirewallRuleWithAccountParametersArgs",
    "CreateFirewallRuleWithAccountParametersArgsDict",
]

class AddDataLakeStoreWithAccountParametersArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    suffix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AddDataLakeStoreWithAccountParametersArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        suffix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AddStorageAccountWithAccountParametersArgsDict(TypedDict):
    access_key: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    suffix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AddStorageAccountWithAccountParametersArgs:
    def __init__(
        __self__,
        *,
        access_key: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        suffix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> pulumi.Input[_builtins.str]: ...
    @access_key.setter
    def access_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CreateComputePolicyWithAccountParametersArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    object_id: pulumi.Input[_builtins.str]
    object_type: pulumi.Input[Union[_builtins.str, AADObjectType]]
    max_degree_of_parallelism_per_job: NotRequired[pulumi.Input[_builtins.int]]
    min_priority_per_job: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class CreateComputePolicyWithAccountParametersArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        object_id: pulumi.Input[_builtins.str],
        object_type: pulumi.Input[Union[_builtins.str, AADObjectType]],
        max_degree_of_parallelism_per_job: Optional[pulumi.Input[_builtins.int]] = ...,
        min_priority_per_job: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Input[_builtins.str]: ...
    @object_id.setter
    def object_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="objectType")
    def object_type(self) -> pulumi.Input[Union[_builtins.str, AADObjectType]]: ...
    @object_type.setter
    def object_type(self, value: pulumi.Input[Union[_builtins.str, AADObjectType]]): ...
    @_builtins.property
    @pulumi.getter(name="maxDegreeOfParallelismPerJob")
    def max_degree_of_parallelism_per_job(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_degree_of_parallelism_per_job.setter
    def max_degree_of_parallelism_per_job(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="minPriorityPerJob")
    def min_priority_per_job(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_priority_per_job.setter
    def min_priority_per_job(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CreateFirewallRuleWithAccountParametersArgsDict(TypedDict):
    end_ip_address: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    start_ip_address: pulumi.Input[_builtins.str]

@pulumi.input_type
class CreateFirewallRuleWithAccountParametersArgs:
    def __init__(
        __self__,
        *,
        end_ip_address: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        start_ip_address: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> pulumi.Input[_builtins.str]: ...
    @end_ip_address.setter
    def end_ip_address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> pulumi.Input[_builtins.str]: ...
    @start_ip_address.setter
    def start_ip_address(self, value: pulumi.Input[_builtins.str]): ...
