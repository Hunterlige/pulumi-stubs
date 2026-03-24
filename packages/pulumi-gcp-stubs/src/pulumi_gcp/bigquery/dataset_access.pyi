import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DatasetAccessInitArgs", "DatasetAccess"]

@pulumi.input_type
class DatasetAccessInitArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        authorized_dataset: Optional[
            pulumi.Input[DatasetAccessAuthorizedDatasetArgs]
        ] = ...,
        condition: Optional[pulumi.Input[DatasetAccessConditionArgs]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        group_by_email: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_member: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        routine: Optional[pulumi.Input[DatasetAccessRoutineArgs]] = ...,
        special_group: Optional[pulumi.Input[_builtins.str]] = ...,
        user_by_email: Optional[pulumi.Input[_builtins.str]] = ...,
        view: Optional[pulumi.Input[DatasetAccessViewArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authorizedDataset")
    def authorized_dataset(
        self,
    ) -> Optional[pulumi.Input[DatasetAccessAuthorizedDatasetArgs]]: ...
    @authorized_dataset.setter
    def authorized_dataset(
        self, value: Optional[pulumi.Input[DatasetAccessAuthorizedDatasetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[DatasetAccessConditionArgs]]: ...
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[DatasetAccessConditionArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="groupByEmail")
    def group_by_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_by_email.setter
    def group_by_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iamMember")
    def iam_member(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iam_member.setter
    def iam_member(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def routine(self) -> Optional[pulumi.Input[DatasetAccessRoutineArgs]]: ...
    @routine.setter
    def routine(self, value: Optional[pulumi.Input[DatasetAccessRoutineArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="specialGroup")
    def special_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @special_group.setter
    def special_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userByEmail")
    def user_by_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_by_email.setter
    def user_by_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def view(self) -> Optional[pulumi.Input[DatasetAccessViewArgs]]: ...
    @view.setter
    def view(self, value: Optional[pulumi.Input[DatasetAccessViewArgs]]): ...

@pulumi.input_type
class _DatasetAccessState:
    def __init__(
        __self__,
        *,
        api_updated_member: Optional[pulumi.Input[_builtins.bool]] = ...,
        authorized_dataset: Optional[
            pulumi.Input[DatasetAccessAuthorizedDatasetArgs]
        ] = ...,
        condition: Optional[pulumi.Input[DatasetAccessConditionArgs]] = ...,
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        group_by_email: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_member: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        routine: Optional[pulumi.Input[DatasetAccessRoutineArgs]] = ...,
        special_group: Optional[pulumi.Input[_builtins.str]] = ...,
        user_by_email: Optional[pulumi.Input[_builtins.str]] = ...,
        view: Optional[pulumi.Input[DatasetAccessViewArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiUpdatedMember")
    def api_updated_member(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @api_updated_member.setter
    def api_updated_member(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="authorizedDataset")
    def authorized_dataset(
        self,
    ) -> Optional[pulumi.Input[DatasetAccessAuthorizedDatasetArgs]]: ...
    @authorized_dataset.setter
    def authorized_dataset(
        self, value: Optional[pulumi.Input[DatasetAccessAuthorizedDatasetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[DatasetAccessConditionArgs]]: ...
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[DatasetAccessConditionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_id.setter
    def dataset_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="groupByEmail")
    def group_by_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_by_email.setter
    def group_by_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iamMember")
    def iam_member(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iam_member.setter
    def iam_member(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def routine(self) -> Optional[pulumi.Input[DatasetAccessRoutineArgs]]: ...
    @routine.setter
    def routine(self, value: Optional[pulumi.Input[DatasetAccessRoutineArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="specialGroup")
    def special_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @special_group.setter
    def special_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userByEmail")
    def user_by_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_by_email.setter
    def user_by_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def view(self) -> Optional[pulumi.Input[DatasetAccessViewArgs]]: ...
    @view.setter
    def view(self, value: Optional[pulumi.Input[DatasetAccessViewArgs]]): ...

@pulumi.type_token("gcp:bigquery/datasetAccess:DatasetAccess")
class DatasetAccess(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        authorized_dataset: Optional[
            pulumi.Input[
                Union[
                    DatasetAccessAuthorizedDatasetArgs,
                    DatasetAccessAuthorizedDatasetArgsDict,
                ]
            ]
        ] = ...,
        condition: Optional[
            pulumi.Input[
                Union[DatasetAccessConditionArgs, DatasetAccessConditionArgsDict]
            ]
        ] = ...,
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        group_by_email: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_member: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        routine: Optional[
            pulumi.Input[Union[DatasetAccessRoutineArgs, DatasetAccessRoutineArgsDict]]
        ] = ...,
        special_group: Optional[pulumi.Input[_builtins.str]] = ...,
        user_by_email: Optional[pulumi.Input[_builtins.str]] = ...,
        view: Optional[
            pulumi.Input[Union[DatasetAccessViewArgs, DatasetAccessViewArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DatasetAccessInitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_updated_member: Optional[pulumi.Input[_builtins.bool]] = ...,
        authorized_dataset: Optional[
            pulumi.Input[
                Union[
                    DatasetAccessAuthorizedDatasetArgs,
                    DatasetAccessAuthorizedDatasetArgsDict,
                ]
            ]
        ] = ...,
        condition: Optional[
            pulumi.Input[
                Union[DatasetAccessConditionArgs, DatasetAccessConditionArgsDict]
            ]
        ] = ...,
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        group_by_email: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_member: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        routine: Optional[
            pulumi.Input[Union[DatasetAccessRoutineArgs, DatasetAccessRoutineArgsDict]]
        ] = ...,
        special_group: Optional[pulumi.Input[_builtins.str]] = ...,
        user_by_email: Optional[pulumi.Input[_builtins.str]] = ...,
        view: Optional[
            pulumi.Input[Union[DatasetAccessViewArgs, DatasetAccessViewArgsDict]]
        ] = ...,
    ) -> DatasetAccess: ...
    @_builtins.property
    @pulumi.getter(name="apiUpdatedMember")
    def api_updated_member(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="authorizedDataset")
    def authorized_dataset(
        self,
    ) -> pulumi.Output[Optional[outputs.DatasetAccessAuthorizedDataset]]: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Output[Optional[outputs.DatasetAccessCondition]]: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="groupByEmail")
    def group_by_email(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="iamMember")
    def iam_member(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def routine(self) -> pulumi.Output[Optional[outputs.DatasetAccessRoutine]]: ...
    @_builtins.property
    @pulumi.getter(name="specialGroup")
    def special_group(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="userByEmail")
    def user_by_email(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def view(self) -> pulumi.Output[Optional[outputs.DatasetAccessView]]: ...
