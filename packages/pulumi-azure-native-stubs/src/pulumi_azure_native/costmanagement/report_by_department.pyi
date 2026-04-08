import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReportByDepartmentArgs", "ReportByDepartment"]

@pulumi.input_type
class ReportByDepartmentArgs:
    def __init__(
        __self__,
        *,
        definition: pulumi.Input[ReportDefinitionArgs],
        delivery_info: pulumi.Input[ReportDeliveryInfoArgs],
        department_id: pulumi.Input[_builtins.str],
        format: Optional[pulumi.Input[Union[_builtins.str, FormatType]]] = ...,
        report_name: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule: Optional[pulumi.Input[ReportScheduleArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def definition(self) -> pulumi.Input[ReportDefinitionArgs]: ...
    @definition.setter
    def definition(self, value: pulumi.Input[ReportDefinitionArgs]): ...
    @_builtins.property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> pulumi.Input[ReportDeliveryInfoArgs]: ...
    @delivery_info.setter
    def delivery_info(self, value: pulumi.Input[ReportDeliveryInfoArgs]): ...
    @_builtins.property
    @pulumi.getter(name="departmentId")
    def department_id(self) -> pulumi.Input[_builtins.str]: ...
    @department_id.setter
    def department_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[Union[_builtins.str, FormatType]]]: ...
    @format.setter
    def format(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FormatType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="reportName")
    def report_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @report_name.setter
    def report_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[ReportScheduleArgs]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[ReportScheduleArgs]]): ...

@pulumi.type_token("azure-native:costmanagement:ReportByDepartment")
class ReportByDepartment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        definition: Optional[
            pulumi.Input[Union[ReportDefinitionArgs, ReportDefinitionArgsDict]]
        ] = ...,
        delivery_info: Optional[
            pulumi.Input[Union[ReportDeliveryInfoArgs, ReportDeliveryInfoArgsDict]]
        ] = ...,
        department_id: Optional[pulumi.Input[_builtins.str]] = ...,
        format: Optional[pulumi.Input[Union[_builtins.str, FormatType]]] = ...,
        report_name: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule: Optional[
            pulumi.Input[Union[ReportScheduleArgs, ReportScheduleArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReportByDepartmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ReportByDepartment: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def definition(self) -> pulumi.Output[outputs.ReportDefinitionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> pulumi.Output[outputs.ReportDeliveryInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional[outputs.ReportScheduleResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
