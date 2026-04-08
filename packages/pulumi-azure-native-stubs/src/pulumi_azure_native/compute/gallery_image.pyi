import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GalleryImageArgs", "GalleryImage"]

@pulumi.input_type
class GalleryImageArgs:
    def __init__(
        __self__,
        *,
        gallery_name: pulumi.Input[_builtins.str],
        identifier: pulumi.Input[GalleryImageIdentifierArgs],
        os_state: pulumi.Input[OperatingSystemStateTypes],
        os_type: pulumi.Input[OperatingSystemTypes],
        resource_group_name: pulumi.Input[_builtins.str],
        allow_update_image: Optional[pulumi.Input[_builtins.bool]] = ...,
        architecture: Optional[pulumi.Input[Union[_builtins.str, Architecture]]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disallowed: Optional[pulumi.Input[DisallowedArgs]] = ...,
        end_of_life_date: Optional[pulumi.Input[_builtins.str]] = ...,
        eula: Optional[pulumi.Input[_builtins.str]] = ...,
        features: Optional[
            pulumi.Input[Sequence[pulumi.Input[GalleryImageFeatureArgs]]]
        ] = ...,
        gallery_image_name: Optional[pulumi.Input[_builtins.str]] = ...,
        hyper_v_generation: Optional[
            pulumi.Input[Union[_builtins.str, HyperVGeneration]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        privacy_statement_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        purchase_plan: Optional[pulumi.Input[ImagePurchasePlanArgs]] = ...,
        recommended: Optional[pulumi.Input[RecommendedMachineConfigurationArgs]] = ...,
        release_note_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="galleryName")
    def gallery_name(self) -> pulumi.Input[_builtins.str]: ...
    @gallery_name.setter
    def gallery_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[GalleryImageIdentifierArgs]: ...
    @identifier.setter
    def identifier(self, value: pulumi.Input[GalleryImageIdentifierArgs]): ...
    @_builtins.property
    @pulumi.getter(name="osState")
    def os_state(self) -> pulumi.Input[OperatingSystemStateTypes]: ...
    @os_state.setter
    def os_state(self, value: pulumi.Input[OperatingSystemStateTypes]): ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Input[OperatingSystemTypes]: ...
    @os_type.setter
    def os_type(self, value: pulumi.Input[OperatingSystemTypes]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowUpdateImage")
    def allow_update_image(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_update_image.setter
    def allow_update_image(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def architecture(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, Architecture]]]: ...
    @architecture.setter
    def architecture(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Architecture]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disallowed(self) -> Optional[pulumi.Input[DisallowedArgs]]: ...
    @disallowed.setter
    def disallowed(self, value: Optional[pulumi.Input[DisallowedArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="endOfLifeDate")
    def end_of_life_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_of_life_date.setter
    def end_of_life_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def eula(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @eula.setter
    def eula(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[GalleryImageFeatureArgs]]]]: ...
    @features.setter
    def features(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[GalleryImageFeatureArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="galleryImageName")
    def gallery_image_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gallery_image_name.setter
    def gallery_image_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, HyperVGeneration]]]: ...
    @hyper_v_generation.setter
    def hyper_v_generation(
        self, value: Optional[pulumi.Input[Union[_builtins.str, HyperVGeneration]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privacyStatementUri")
    def privacy_statement_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @privacy_statement_uri.setter
    def privacy_statement_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="purchasePlan")
    def purchase_plan(self) -> Optional[pulumi.Input[ImagePurchasePlanArgs]]: ...
    @purchase_plan.setter
    def purchase_plan(self, value: Optional[pulumi.Input[ImagePurchasePlanArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def recommended(
        self,
    ) -> Optional[pulumi.Input[RecommendedMachineConfigurationArgs]]: ...
    @recommended.setter
    def recommended(
        self, value: Optional[pulumi.Input[RecommendedMachineConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="releaseNoteUri")
    def release_note_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @release_note_uri.setter
    def release_note_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:compute:GalleryImage")
class GalleryImage(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_update_image: Optional[pulumi.Input[_builtins.bool]] = ...,
        architecture: Optional[pulumi.Input[Union[_builtins.str, Architecture]]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disallowed: Optional[
            pulumi.Input[Union[DisallowedArgs, DisallowedArgsDict]]
        ] = ...,
        end_of_life_date: Optional[pulumi.Input[_builtins.str]] = ...,
        eula: Optional[pulumi.Input[_builtins.str]] = ...,
        features: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[GalleryImageFeatureArgs, GalleryImageFeatureArgsDict]
                    ]
                ]
            ]
        ] = ...,
        gallery_image_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gallery_name: Optional[pulumi.Input[_builtins.str]] = ...,
        hyper_v_generation: Optional[
            pulumi.Input[Union[_builtins.str, HyperVGeneration]]
        ] = ...,
        identifier: Optional[
            pulumi.Input[
                Union[GalleryImageIdentifierArgs, GalleryImageIdentifierArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        os_state: Optional[pulumi.Input[OperatingSystemStateTypes]] = ...,
        os_type: Optional[pulumi.Input[OperatingSystemTypes]] = ...,
        privacy_statement_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        purchase_plan: Optional[
            pulumi.Input[Union[ImagePurchasePlanArgs, ImagePurchasePlanArgsDict]]
        ] = ...,
        recommended: Optional[
            pulumi.Input[
                Union[
                    RecommendedMachineConfigurationArgs,
                    RecommendedMachineConfigurationArgsDict,
                ]
            ]
        ] = ...,
        release_note_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GalleryImageArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> GalleryImage: ...
    @_builtins.property
    @pulumi.getter(name="allowUpdateImage")
    def allow_update_image(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def architecture(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def disallowed(self) -> pulumi.Output[Optional[outputs.DisallowedResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="endOfLifeDate")
    def end_of_life_date(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def eula(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def features(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.GalleryImageFeatureResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[outputs.GalleryImageIdentifierResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osState")
    def os_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privacyStatementUri")
    def privacy_statement_uri(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="purchasePlan")
    def purchase_plan(
        self,
    ) -> pulumi.Output[Optional[outputs.ImagePurchasePlanResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def recommended(
        self,
    ) -> pulumi.Output[Optional[outputs.RecommendedMachineConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="releaseNoteUri")
    def release_note_uri(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
