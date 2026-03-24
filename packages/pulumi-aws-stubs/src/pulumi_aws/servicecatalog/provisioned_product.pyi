import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProvisionedProductArgs", "ProvisionedProduct"]

@pulumi.input_type
class ProvisionedProductArgs:
    def __init__(
        __self__,
        *,
        accept_language: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_errors: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        path_id: Optional[pulumi.Input[_builtins.str]] = ...,
        path_name: Optional[pulumi.Input[_builtins.str]] = ...,
        product_id: Optional[pulumi.Input[_builtins.str]] = ...,
        product_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_artifact_id: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_artifact_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_parameters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ProvisionedProductProvisioningParameterArgs]]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retain_physical_resources: Optional[pulumi.Input[_builtins.bool]] = ...,
        stack_set_provisioning_preferences: Optional[
            pulumi.Input[ProvisionedProductStackSetProvisioningPreferencesArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accept_language.setter
    def accept_language(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreErrors")
    def ignore_errors(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_errors.setter
    def ignore_errors(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationArns")
    def notification_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @notification_arns.setter
    def notification_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pathId")
    def path_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path_id.setter
    def path_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pathName")
    def path_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path_name.setter
    def path_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @product_id.setter
    def product_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @product_name.setter
    def product_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisioningArtifactId")
    def provisioning_artifact_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioning_artifact_id.setter
    def provisioning_artifact_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisioningArtifactName")
    def provisioning_artifact_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioning_artifact_name.setter
    def provisioning_artifact_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisioningParameters")
    def provisioning_parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ProvisionedProductProvisioningParameterArgs]]
        ]
    ]: ...
    @provisioning_parameters.setter
    def provisioning_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ProvisionedProductProvisioningParameterArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retainPhysicalResources")
    def retain_physical_resources(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @retain_physical_resources.setter
    def retain_physical_resources(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stackSetProvisioningPreferences")
    def stack_set_provisioning_preferences(
        self,
    ) -> Optional[
        pulumi.Input[ProvisionedProductStackSetProvisioningPreferencesArgs]
    ]: ...
    @stack_set_provisioning_preferences.setter
    def stack_set_provisioning_preferences(
        self,
        value: Optional[
            pulumi.Input[ProvisionedProductStackSetProvisioningPreferencesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _ProvisionedProductState:
    def __init__(
        __self__,
        *,
        accept_language: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatch_dashboard_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        created_time: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_errors: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_provisioning_record_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_record_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_successful_provisioning_record_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        launch_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        outputs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProvisionedProductOutputArgs]]]
        ] = ...,
        path_id: Optional[pulumi.Input[_builtins.str]] = ...,
        path_name: Optional[pulumi.Input[_builtins.str]] = ...,
        product_id: Optional[pulumi.Input[_builtins.str]] = ...,
        product_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_artifact_id: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_artifact_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_parameters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ProvisionedProductProvisioningParameterArgs]]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retain_physical_resources: Optional[pulumi.Input[_builtins.bool]] = ...,
        stack_set_provisioning_preferences: Optional[
            pulumi.Input[ProvisionedProductStackSetProvisioningPreferencesArgs]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        status_message: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accept_language.setter
    def accept_language(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchDashboardNames")
    def cloudwatch_dashboard_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cloudwatch_dashboard_names.setter
    def cloudwatch_dashboard_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreErrors")
    def ignore_errors(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_errors.setter
    def ignore_errors(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="lastProvisioningRecordId")
    def last_provisioning_record_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_provisioning_record_id.setter
    def last_provisioning_record_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastRecordId")
    def last_record_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_record_id.setter
    def last_record_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulProvisioningRecordId")
    def last_successful_provisioning_record_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_successful_provisioning_record_id.setter
    def last_successful_provisioning_record_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="launchRoleArn")
    def launch_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @launch_role_arn.setter
    def launch_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationArns")
    def notification_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @notification_arns.setter
    def notification_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def outputs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ProvisionedProductOutputArgs]]]
    ]: ...
    @outputs.setter
    def outputs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProvisionedProductOutputArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pathId")
    def path_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path_id.setter
    def path_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pathName")
    def path_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path_name.setter
    def path_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @product_id.setter
    def product_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @product_name.setter
    def product_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisioningArtifactId")
    def provisioning_artifact_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioning_artifact_id.setter
    def provisioning_artifact_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisioningArtifactName")
    def provisioning_artifact_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioning_artifact_name.setter
    def provisioning_artifact_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisioningParameters")
    def provisioning_parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ProvisionedProductProvisioningParameterArgs]]
        ]
    ]: ...
    @provisioning_parameters.setter
    def provisioning_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ProvisionedProductProvisioningParameterArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retainPhysicalResources")
    def retain_physical_resources(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @retain_physical_resources.setter
    def retain_physical_resources(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stackSetProvisioningPreferences")
    def stack_set_provisioning_preferences(
        self,
    ) -> Optional[
        pulumi.Input[ProvisionedProductStackSetProvisioningPreferencesArgs]
    ]: ...
    @stack_set_provisioning_preferences.setter
    def stack_set_provisioning_preferences(
        self,
        value: Optional[
            pulumi.Input[ProvisionedProductStackSetProvisioningPreferencesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status_message.setter
    def status_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ProvisionedProduct(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        accept_language: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_errors: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        path_id: Optional[pulumi.Input[_builtins.str]] = ...,
        path_name: Optional[pulumi.Input[_builtins.str]] = ...,
        product_id: Optional[pulumi.Input[_builtins.str]] = ...,
        product_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_artifact_id: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_artifact_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ProvisionedProductProvisioningParameterArgs,
                            ProvisionedProductProvisioningParameterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retain_physical_resources: Optional[pulumi.Input[_builtins.bool]] = ...,
        stack_set_provisioning_preferences: Optional[
            pulumi.Input[
                Union[
                    ProvisionedProductStackSetProvisioningPreferencesArgs,
                    ProvisionedProductStackSetProvisioningPreferencesArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[ProvisionedProductArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        accept_language: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudwatch_dashboard_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        created_time: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_errors: Optional[pulumi.Input[_builtins.bool]] = ...,
        last_provisioning_record_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_record_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_successful_provisioning_record_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        launch_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        outputs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ProvisionedProductOutputArgs,
                            ProvisionedProductOutputArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        path_id: Optional[pulumi.Input[_builtins.str]] = ...,
        path_name: Optional[pulumi.Input[_builtins.str]] = ...,
        product_id: Optional[pulumi.Input[_builtins.str]] = ...,
        product_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_artifact_id: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_artifact_name: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ProvisionedProductProvisioningParameterArgs,
                            ProvisionedProductProvisioningParameterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retain_physical_resources: Optional[pulumi.Input[_builtins.bool]] = ...,
        stack_set_provisioning_preferences: Optional[
            pulumi.Input[
                Union[
                    ProvisionedProductStackSetProvisioningPreferencesArgs,
                    ProvisionedProductStackSetProvisioningPreferencesArgsDict,
                ]
            ]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        status_message: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ProvisionedProduct: ...
    @_builtins.property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchDashboardNames")
    def cloudwatch_dashboard_names(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreErrors")
    def ignore_errors(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="lastProvisioningRecordId")
    def last_provisioning_record_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastRecordId")
    def last_record_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulProvisioningRecordId")
    def last_successful_provisioning_record_id(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="launchRoleArn")
    def launch_role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationArns")
    def notification_arns(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def outputs(self) -> pulumi.Output[Sequence[outputs.ProvisionedProductOutput]]: ...
    @_builtins.property
    @pulumi.getter(name="pathId")
    def path_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pathName")
    def path_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="productName")
    def product_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningArtifactId")
    def provisioning_artifact_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningArtifactName")
    def provisioning_artifact_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningParameters")
    def provisioning_parameters(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ProvisionedProductProvisioningParameter]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retainPhysicalResources")
    def retain_physical_resources(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="stackSetProvisioningPreferences")
    def stack_set_provisioning_preferences(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ProvisionedProductStackSetProvisioningPreferences]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
