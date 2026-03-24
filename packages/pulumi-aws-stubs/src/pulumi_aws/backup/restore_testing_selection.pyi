import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RestoreTestingSelectionArgs", "RestoreTestingSelection"]

@pulumi.input_type
class RestoreTestingSelectionArgs:
    def __init__(
        __self__,
        *,
        iam_role_arn: pulumi.Input[_builtins.str],
        protected_resource_type: pulumi.Input[_builtins.str],
        restore_testing_plan_name: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_resource_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        protected_resource_conditions: Optional[
            pulumi.Input[RestoreTestingSelectionProtectedResourceConditionsArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        restore_metadata_overrides: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        validation_window_hours: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @iam_role_arn.setter
    def iam_role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="protectedResourceType")
    def protected_resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @protected_resource_type.setter
    def protected_resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="restoreTestingPlanName")
    def restore_testing_plan_name(self) -> pulumi.Input[_builtins.str]: ...
    @restore_testing_plan_name.setter
    def restore_testing_plan_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedResourceArns")
    def protected_resource_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @protected_resource_arns.setter
    def protected_resource_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectedResourceConditions")
    def protected_resource_conditions(
        self,
    ) -> Optional[
        pulumi.Input[RestoreTestingSelectionProtectedResourceConditionsArgs]
    ]: ...
    @protected_resource_conditions.setter
    def protected_resource_conditions(
        self,
        value: Optional[
            pulumi.Input[RestoreTestingSelectionProtectedResourceConditionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="restoreMetadataOverrides")
    def restore_metadata_overrides(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @restore_metadata_overrides.setter
    def restore_metadata_overrides(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationWindowHours")
    def validation_window_hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @validation_window_hours.setter
    def validation_window_hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.input_type
class _RestoreTestingSelectionState:
    def __init__(
        __self__,
        *,
        iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_resource_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        protected_resource_conditions: Optional[
            pulumi.Input[RestoreTestingSelectionProtectedResourceConditionsArgs]
        ] = ...,
        protected_resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        restore_metadata_overrides: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        restore_testing_plan_name: Optional[pulumi.Input[_builtins.str]] = ...,
        validation_window_hours: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="protectedResourceArns")
    def protected_resource_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @protected_resource_arns.setter
    def protected_resource_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectedResourceConditions")
    def protected_resource_conditions(
        self,
    ) -> Optional[
        pulumi.Input[RestoreTestingSelectionProtectedResourceConditionsArgs]
    ]: ...
    @protected_resource_conditions.setter
    def protected_resource_conditions(
        self,
        value: Optional[
            pulumi.Input[RestoreTestingSelectionProtectedResourceConditionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="protectedResourceType")
    def protected_resource_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protected_resource_type.setter
    def protected_resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="restoreMetadataOverrides")
    def restore_metadata_overrides(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @restore_metadata_overrides.setter
    def restore_metadata_overrides(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="restoreTestingPlanName")
    def restore_testing_plan_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @restore_testing_plan_name.setter
    def restore_testing_plan_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationWindowHours")
    def validation_window_hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @validation_window_hours.setter
    def validation_window_hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token(...)
class RestoreTestingSelection(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_resource_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        protected_resource_conditions: Optional[
            pulumi.Input[
                Union[
                    RestoreTestingSelectionProtectedResourceConditionsArgs,
                    RestoreTestingSelectionProtectedResourceConditionsArgsDict,
                ]
            ]
        ] = ...,
        protected_resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        restore_metadata_overrides: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        restore_testing_plan_name: Optional[pulumi.Input[_builtins.str]] = ...,
        validation_window_hours: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RestoreTestingSelectionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        protected_resource_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        protected_resource_conditions: Optional[
            pulumi.Input[
                Union[
                    RestoreTestingSelectionProtectedResourceConditionsArgs,
                    RestoreTestingSelectionProtectedResourceConditionsArgsDict,
                ]
            ]
        ] = ...,
        protected_resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        restore_metadata_overrides: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        restore_testing_plan_name: Optional[pulumi.Input[_builtins.str]] = ...,
        validation_window_hours: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> RestoreTestingSelection: ...
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="protectedResourceArns")
    def protected_resource_arns(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="protectedResourceConditions")
    def protected_resource_conditions(
        self,
    ) -> pulumi.Output[
        Optional[outputs.RestoreTestingSelectionProtectedResourceConditions]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="protectedResourceType")
    def protected_resource_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="restoreMetadataOverrides")
    def restore_metadata_overrides(
        self,
    ) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="restoreTestingPlanName")
    def restore_testing_plan_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validationWindowHours")
    def validation_window_hours(self) -> pulumi.Output[_builtins.int]: ...
