import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SecurityProfileV2Args", "SecurityProfileV2"]

@pulumi.input_type
class SecurityProfileV2Args:
    def __init__(
        __self__,
        *,
        org_id: pulumi.Input[_builtins.str],
        profile_assessment_configs: pulumi.Input[
            Sequence[pulumi.Input[SecurityProfileV2ProfileAssessmentConfigArgs]]
        ],
        profile_id: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]: ...
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="profileAssessmentConfigs")
    def profile_assessment_configs(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[SecurityProfileV2ProfileAssessmentConfigArgs]]
    ]: ...
    @profile_assessment_configs.setter
    def profile_assessment_configs(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[SecurityProfileV2ProfileAssessmentConfigArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> pulumi.Input[_builtins.str]: ...
    @profile_id.setter
    def profile_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _SecurityProfileV2State:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_assessment_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[SecurityProfileV2ProfileAssessmentConfigArgs]]
            ]
        ] = ...,
        profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="profileAssessmentConfigs")
    def profile_assessment_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[SecurityProfileV2ProfileAssessmentConfigArgs]]
        ]
    ]: ...
    @profile_assessment_configs.setter
    def profile_assessment_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[SecurityProfileV2ProfileAssessmentConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile_id.setter
    def profile_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:apigee/securityProfileV2:SecurityProfileV2")
class SecurityProfileV2(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_assessment_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            SecurityProfileV2ProfileAssessmentConfigArgs,
                            SecurityProfileV2ProfileAssessmentConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SecurityProfileV2Args,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_assessment_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            SecurityProfileV2ProfileAssessmentConfigArgs,
                            SecurityProfileV2ProfileAssessmentConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SecurityProfileV2: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="profileAssessmentConfigs")
    def profile_assessment_configs(
        self,
    ) -> pulumi.Output[Sequence[outputs.SecurityProfileV2ProfileAssessmentConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
