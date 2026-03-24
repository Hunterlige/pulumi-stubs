import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CustomActionTypeArgs", "CustomActionType"]

@pulumi.input_type
class CustomActionTypeArgs:
    def __init__(
        __self__,
        *,
        category: pulumi.Input[_builtins.str],
        input_artifact_details: pulumi.Input[CustomActionTypeInputArtifactDetailsArgs],
        output_artifact_details: pulumi.Input[
            CustomActionTypeOutputArtifactDetailsArgs
        ],
        provider_name: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.str],
        configuration_properties: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CustomActionTypeConfigurationPropertyArgs]]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        settings: Optional[pulumi.Input[CustomActionTypeSettingsArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> pulumi.Input[_builtins.str]: ...
    @category.setter
    def category(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="inputArtifactDetails")
    def input_artifact_details(
        self,
    ) -> pulumi.Input[CustomActionTypeInputArtifactDetailsArgs]: ...
    @input_artifact_details.setter
    def input_artifact_details(
        self, value: pulumi.Input[CustomActionTypeInputArtifactDetailsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputArtifactDetails")
    def output_artifact_details(
        self,
    ) -> pulumi.Input[CustomActionTypeOutputArtifactDetailsArgs]: ...
    @output_artifact_details.setter
    def output_artifact_details(
        self, value: pulumi.Input[CustomActionTypeOutputArtifactDetailsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> pulumi.Input[_builtins.str]: ...
    @provider_name.setter
    def provider_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="configurationProperties")
    def configuration_properties(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CustomActionTypeConfigurationPropertyArgs]]]
    ]: ...
    @configuration_properties.setter
    def configuration_properties(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CustomActionTypeConfigurationPropertyArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[CustomActionTypeSettingsArgs]]: ...
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[CustomActionTypeSettingsArgs]]): ...
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
class _CustomActionTypeState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        category: Optional[pulumi.Input[_builtins.str]] = ...,
        configuration_properties: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CustomActionTypeConfigurationPropertyArgs]]
            ]
        ] = ...,
        input_artifact_details: Optional[
            pulumi.Input[CustomActionTypeInputArtifactDetailsArgs]
        ] = ...,
        output_artifact_details: Optional[
            pulumi.Input[CustomActionTypeOutputArtifactDetailsArgs]
        ] = ...,
        owner: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        settings: Optional[pulumi.Input[CustomActionTypeSettingsArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @category.setter
    def category(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="configurationProperties")
    def configuration_properties(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CustomActionTypeConfigurationPropertyArgs]]]
    ]: ...
    @configuration_properties.setter
    def configuration_properties(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[CustomActionTypeConfigurationPropertyArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputArtifactDetails")
    def input_artifact_details(
        self,
    ) -> Optional[pulumi.Input[CustomActionTypeInputArtifactDetailsArgs]]: ...
    @input_artifact_details.setter
    def input_artifact_details(
        self, value: Optional[pulumi.Input[CustomActionTypeInputArtifactDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputArtifactDetails")
    def output_artifact_details(
        self,
    ) -> Optional[pulumi.Input[CustomActionTypeOutputArtifactDetailsArgs]]: ...
    @output_artifact_details.setter
    def output_artifact_details(
        self, value: Optional[pulumi.Input[CustomActionTypeOutputArtifactDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provider_name.setter
    def provider_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[CustomActionTypeSettingsArgs]]: ...
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[CustomActionTypeSettingsArgs]]): ...
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
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:codepipeline/customActionType:CustomActionType")
class CustomActionType(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        category: Optional[pulumi.Input[_builtins.str]] = ...,
        configuration_properties: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CustomActionTypeConfigurationPropertyArgs,
                            CustomActionTypeConfigurationPropertyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        input_artifact_details: Optional[
            pulumi.Input[
                Union[
                    CustomActionTypeInputArtifactDetailsArgs,
                    CustomActionTypeInputArtifactDetailsArgsDict,
                ]
            ]
        ] = ...,
        output_artifact_details: Optional[
            pulumi.Input[
                Union[
                    CustomActionTypeOutputArtifactDetailsArgs,
                    CustomActionTypeOutputArtifactDetailsArgsDict,
                ]
            ]
        ] = ...,
        provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        settings: Optional[
            pulumi.Input[
                Union[CustomActionTypeSettingsArgs, CustomActionTypeSettingsArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CustomActionTypeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        category: Optional[pulumi.Input[_builtins.str]] = ...,
        configuration_properties: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CustomActionTypeConfigurationPropertyArgs,
                            CustomActionTypeConfigurationPropertyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        input_artifact_details: Optional[
            pulumi.Input[
                Union[
                    CustomActionTypeInputArtifactDetailsArgs,
                    CustomActionTypeInputArtifactDetailsArgsDict,
                ]
            ]
        ] = ...,
        output_artifact_details: Optional[
            pulumi.Input[
                Union[
                    CustomActionTypeOutputArtifactDetailsArgs,
                    CustomActionTypeOutputArtifactDetailsArgsDict,
                ]
            ]
        ] = ...,
        owner: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        settings: Optional[
            pulumi.Input[
                Union[CustomActionTypeSettingsArgs, CustomActionTypeSettingsArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> CustomActionType: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="configurationProperties")
    def configuration_properties(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.CustomActionTypeConfigurationProperty]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inputArtifactDetails")
    def input_artifact_details(
        self,
    ) -> pulumi.Output[outputs.CustomActionTypeInputArtifactDetails]: ...
    @_builtins.property
    @pulumi.getter(name="outputArtifactDetails")
    def output_artifact_details(
        self,
    ) -> pulumi.Output[outputs.CustomActionTypeOutputArtifactDetails]: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> pulumi.Output[Optional[outputs.CustomActionTypeSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...
