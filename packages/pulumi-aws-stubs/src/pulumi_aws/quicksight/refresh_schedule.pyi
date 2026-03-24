import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RefreshScheduleArgs", "RefreshSchedule"]

@pulumi.input_type
class RefreshScheduleArgs:
    def __init__(
        __self__,
        *,
        data_set_id: pulumi.Input[_builtins.str],
        schedule: pulumi.Input[RefreshScheduleScheduleArgs],
        schedule_id: pulumi.Input[_builtins.str],
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> pulumi.Input[_builtins.str]: ...
    @data_set_id.setter
    def data_set_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Input[RefreshScheduleScheduleArgs]: ...
    @schedule.setter
    def schedule(self, value: pulumi.Input[RefreshScheduleScheduleArgs]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleId")
    def schedule_id(self) -> pulumi.Input[_builtins.str]: ...
    @schedule_id.setter
    def schedule_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _RefreshScheduleState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule: Optional[pulumi.Input[RefreshScheduleScheduleArgs]] = ...,
        schedule_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_set_id.setter
    def data_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[RefreshScheduleScheduleArgs]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[RefreshScheduleScheduleArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleId")
    def schedule_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule_id.setter
    def schedule_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:quicksight/refreshSchedule:RefreshSchedule")
class RefreshSchedule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule: Optional[
            pulumi.Input[
                Union[RefreshScheduleScheduleArgs, RefreshScheduleScheduleArgsDict]
            ]
        ] = ...,
        schedule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RefreshScheduleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule: Optional[
            pulumi.Input[
                Union[RefreshScheduleScheduleArgs, RefreshScheduleScheduleArgsDict]
            ]
        ] = ...,
        schedule_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> RefreshSchedule: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[outputs.RefreshScheduleSchedule]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleId")
    def schedule_id(self) -> pulumi.Output[_builtins.str]: ...
