import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VirtualMachineImageTemplateArgs", "VirtualMachineImageTemplate"]

@pulumi.input_type
class VirtualMachineImageTemplateArgs:
    def __init__(
        __self__,
        *,
        distribute: pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        ImageTemplateManagedImageDistributorArgs,
                        ImageTemplateSharedImageDistributorArgs,
                        ImageTemplateVhdDistributorArgs,
                    ]
                ]
            ]
        ],
        identity: pulumi.Input[ImageTemplateIdentityArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        source: pulumi.Input[
            Union[
                ImageTemplateManagedImageSourceArgs,
                ImageTemplatePlatformImageSourceArgs,
                ImageTemplateSharedImageVersionSourceArgs,
            ]
        ],
        auto_run: Optional[pulumi.Input[ImageTemplateAutoRunArgs]] = ...,
        build_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        customize: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ImageTemplateFileCustomizerArgs,
                            ImageTemplatePowerShellCustomizerArgs,
                            ImageTemplateRestartCustomizerArgs,
                            ImageTemplateShellCustomizerArgs,
                            ImageTemplateWindowsUpdateCustomizerArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        error_handling: Optional[
            pulumi.Input[ImageTemplatePropertiesErrorHandlingArgs]
        ] = ...,
        image_template_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_resource_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        optimize: Optional[pulumi.Input[ImageTemplatePropertiesOptimizeArgs]] = ...,
        staging_resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        validate: Optional[pulumi.Input[ImageTemplatePropertiesValidateArgs]] = ...,
        vm_profile: Optional[pulumi.Input[ImageTemplateVmProfileArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def distribute(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                Union[
                    ImageTemplateManagedImageDistributorArgs,
                    ImageTemplateSharedImageDistributorArgs,
                    ImageTemplateVhdDistributorArgs,
                ]
            ]
        ]
    ]: ...
    @distribute.setter
    def distribute(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        ImageTemplateManagedImageDistributorArgs,
                        ImageTemplateSharedImageDistributorArgs,
                        ImageTemplateVhdDistributorArgs,
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Input[ImageTemplateIdentityArgs]: ...
    @identity.setter
    def identity(self, value: pulumi.Input[ImageTemplateIdentityArgs]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> pulumi.Input[
        Union[
            ImageTemplateManagedImageSourceArgs,
            ImageTemplatePlatformImageSourceArgs,
            ImageTemplateSharedImageVersionSourceArgs,
        ]
    ]: ...
    @source.setter
    def source(
        self,
        value: pulumi.Input[
            Union[
                ImageTemplateManagedImageSourceArgs,
                ImageTemplatePlatformImageSourceArgs,
                ImageTemplateSharedImageVersionSourceArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoRun")
    def auto_run(self) -> Optional[pulumi.Input[ImageTemplateAutoRunArgs]]: ...
    @auto_run.setter
    def auto_run(self, value: Optional[pulumi.Input[ImageTemplateAutoRunArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="buildTimeoutInMinutes")
    def build_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @build_timeout_in_minutes.setter
    def build_timeout_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def customize(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        ImageTemplateFileCustomizerArgs,
                        ImageTemplatePowerShellCustomizerArgs,
                        ImageTemplateRestartCustomizerArgs,
                        ImageTemplateShellCustomizerArgs,
                        ImageTemplateWindowsUpdateCustomizerArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @customize.setter
    def customize(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ImageTemplateFileCustomizerArgs,
                            ImageTemplatePowerShellCustomizerArgs,
                            ImageTemplateRestartCustomizerArgs,
                            ImageTemplateShellCustomizerArgs,
                            ImageTemplateWindowsUpdateCustomizerArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorHandling")
    def error_handling(
        self,
    ) -> Optional[pulumi.Input[ImageTemplatePropertiesErrorHandlingArgs]]: ...
    @error_handling.setter
    def error_handling(
        self, value: Optional[pulumi.Input[ImageTemplatePropertiesErrorHandlingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageTemplateName")
    def image_template_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_template_name.setter
    def image_template_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedResourceTags")
    def managed_resource_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @managed_resource_tags.setter
    def managed_resource_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def optimize(
        self,
    ) -> Optional[pulumi.Input[ImageTemplatePropertiesOptimizeArgs]]: ...
    @optimize.setter
    def optimize(
        self, value: Optional[pulumi.Input[ImageTemplatePropertiesOptimizeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stagingResourceGroup")
    def staging_resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @staging_resource_group.setter
    def staging_resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def validate(
        self,
    ) -> Optional[pulumi.Input[ImageTemplatePropertiesValidateArgs]]: ...
    @validate.setter
    def validate(
        self, value: Optional[pulumi.Input[ImageTemplatePropertiesValidateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmProfile")
    def vm_profile(self) -> Optional[pulumi.Input[ImageTemplateVmProfileArgs]]: ...
    @vm_profile.setter
    def vm_profile(self, value: Optional[pulumi.Input[ImageTemplateVmProfileArgs]]): ...

@pulumi.type_token(...)
class VirtualMachineImageTemplate(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_run: Optional[
            pulumi.Input[Union[ImageTemplateAutoRunArgs, ImageTemplateAutoRunArgsDict]]
        ] = ...,
        build_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        customize: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            Union[
                                ImageTemplateFileCustomizerArgs,
                                ImageTemplateFileCustomizerArgsDict,
                            ],
                            Union[
                                ImageTemplatePowerShellCustomizerArgs,
                                ImageTemplatePowerShellCustomizerArgsDict,
                            ],
                            Union[
                                ImageTemplateRestartCustomizerArgs,
                                ImageTemplateRestartCustomizerArgsDict,
                            ],
                            Union[
                                ImageTemplateShellCustomizerArgs,
                                ImageTemplateShellCustomizerArgsDict,
                            ],
                            Union[
                                ImageTemplateWindowsUpdateCustomizerArgs,
                                ImageTemplateWindowsUpdateCustomizerArgsDict,
                            ],
                        ]
                    ]
                ]
            ]
        ] = ...,
        distribute: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            Union[
                                ImageTemplateManagedImageDistributorArgs,
                                ImageTemplateManagedImageDistributorArgsDict,
                            ],
                            Union[
                                ImageTemplateSharedImageDistributorArgs,
                                ImageTemplateSharedImageDistributorArgsDict,
                            ],
                            Union[
                                ImageTemplateVhdDistributorArgs,
                                ImageTemplateVhdDistributorArgsDict,
                            ],
                        ]
                    ]
                ]
            ]
        ] = ...,
        error_handling: Optional[
            pulumi.Input[
                Union[
                    ImageTemplatePropertiesErrorHandlingArgs,
                    ImageTemplatePropertiesErrorHandlingArgsDict,
                ]
            ]
        ] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ImageTemplateIdentityArgs, ImageTemplateIdentityArgsDict]
            ]
        ] = ...,
        image_template_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_resource_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        optimize: Optional[
            pulumi.Input[
                Union[
                    ImageTemplatePropertiesOptimizeArgs,
                    ImageTemplatePropertiesOptimizeArgsDict,
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[
            pulumi.Input[
                Union[
                    Union[
                        ImageTemplateManagedImageSourceArgs,
                        ImageTemplateManagedImageSourceArgsDict,
                    ],
                    Union[
                        ImageTemplatePlatformImageSourceArgs,
                        ImageTemplatePlatformImageSourceArgsDict,
                    ],
                    Union[
                        ImageTemplateSharedImageVersionSourceArgs,
                        ImageTemplateSharedImageVersionSourceArgsDict,
                    ],
                ]
            ]
        ] = ...,
        staging_resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        validate: Optional[
            pulumi.Input[
                Union[
                    ImageTemplatePropertiesValidateArgs,
                    ImageTemplatePropertiesValidateArgsDict,
                ]
            ]
        ] = ...,
        vm_profile: Optional[
            pulumi.Input[
                Union[ImageTemplateVmProfileArgs, ImageTemplateVmProfileArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VirtualMachineImageTemplateArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VirtualMachineImageTemplate: ...
    @_builtins.property
    @pulumi.getter(name="autoRun")
    def auto_run(
        self,
    ) -> pulumi.Output[Optional[outputs.ImageTemplateAutoRunResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="buildTimeoutInMinutes")
    def build_timeout_in_minutes(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def customize(self) -> pulumi.Output[Optional[Sequence[Any]]]: ...
    @_builtins.property
    @pulumi.getter
    def distribute(self) -> pulumi.Output[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="errorHandling")
    def error_handling(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ImageTemplatePropertiesResponseErrorHandling]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="exactStagingResourceGroup")
    def exact_staging_resource_group(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[outputs.ImageTemplateIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="lastRunStatus")
    def last_run_status(
        self,
    ) -> pulumi.Output[outputs.ImageTemplateLastRunStatusResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedResourceTags")
    def managed_resource_tags(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def optimize(
        self,
    ) -> pulumi.Output[Optional[outputs.ImageTemplatePropertiesResponseOptimize]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningError")
    def provisioning_error(
        self,
    ) -> pulumi.Output[outputs.ProvisioningErrorResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[Any]: ...
    @_builtins.property
    @pulumi.getter(name="stagingResourceGroup")
    def staging_resource_group(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def validate(
        self,
    ) -> pulumi.Output[Optional[outputs.ImageTemplatePropertiesResponseValidate]]: ...
    @_builtins.property
    @pulumi.getter(name="vmProfile")
    def vm_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ImageTemplateVmProfileResponse]]: ...
