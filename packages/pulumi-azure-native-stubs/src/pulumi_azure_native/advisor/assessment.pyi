import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AssessmentArgs", "Assessment"]

@pulumi.input_type
class AssessmentArgs:
    def __init__(
        __self__,
        *,
        assessment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        locale: Optional[pulumi.Input[_builtins.str]] = ...,
        type_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assessmentName")
    def assessment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @assessment_name.setter
    def assessment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def locale(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @locale.setter
    def locale(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeId")
    def type_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_id.setter
    def type_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workloadId")
    def workload_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workload_id.setter
    def workload_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:advisor:Assessment")
class Assessment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        assessment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        locale: Optional[pulumi.Input[_builtins.str]] = ...,
        type_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[AssessmentArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Assessment: ...
    @_builtins.property
    @pulumi.getter(name="assessmentId")
    def assessment_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def locale(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeId")
    def type_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="typeVersion")
    def type_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadId")
    def workload_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="workloadName")
    def workload_name(self) -> pulumi.Output[_builtins.str]: ...
