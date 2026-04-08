import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AssessmentArgs", "Assessment"]

@pulumi.input_type
class AssessmentArgs:
    def __init__(
        __self__,
        *,
        resource_details: pulumi.Input[
            Union[
                AzureResourceDetailsArgs,
                OnPremiseResourceDetailsArgs,
                OnPremiseSqlResourceDetailsArgs,
            ]
        ],
        resource_id: pulumi.Input[_builtins.str],
        status: pulumi.Input[AssessmentStatusArgs],
        additional_data: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        assessment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[SecurityAssessmentMetadataPropertiesArgs]
        ] = ...,
        partners_data: Optional[pulumi.Input[SecurityAssessmentPartnerDataArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceDetails")
    def resource_details(
        self,
    ) -> pulumi.Input[
        Union[
            AzureResourceDetailsArgs,
            OnPremiseResourceDetailsArgs,
            OnPremiseSqlResourceDetailsArgs,
        ]
    ]: ...
    @resource_details.setter
    def resource_details(
        self,
        value: pulumi.Input[
            Union[
                AzureResourceDetailsArgs,
                OnPremiseResourceDetailsArgs,
                OnPremiseSqlResourceDetailsArgs,
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[AssessmentStatusArgs]: ...
    @status.setter
    def status(self, value: pulumi.Input[AssessmentStatusArgs]): ...
    @_builtins.property
    @pulumi.getter(name="additionalData")
    def additional_data(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @additional_data.setter
    def additional_data(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="assessmentName")
    def assessment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @assessment_name.setter
    def assessment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[SecurityAssessmentMetadataPropertiesArgs]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[SecurityAssessmentMetadataPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="partnersData")
    def partners_data(
        self,
    ) -> Optional[pulumi.Input[SecurityAssessmentPartnerDataArgs]]: ...
    @partners_data.setter
    def partners_data(
        self, value: Optional[pulumi.Input[SecurityAssessmentPartnerDataArgs]]
    ): ...

@pulumi.type_token("azure-native:security:Assessment")
class Assessment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_data: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        assessment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[
                Union[
                    SecurityAssessmentMetadataPropertiesArgs,
                    SecurityAssessmentMetadataPropertiesArgsDict,
                ]
            ]
        ] = ...,
        partners_data: Optional[
            pulumi.Input[
                Union[
                    SecurityAssessmentPartnerDataArgs,
                    SecurityAssessmentPartnerDataArgsDict,
                ]
            ]
        ] = ...,
        resource_details: Optional[
            pulumi.Input[
                Union[
                    Union[AzureResourceDetailsArgs, AzureResourceDetailsArgsDict],
                    Union[
                        OnPremiseResourceDetailsArgs, OnPremiseResourceDetailsArgsDict
                    ],
                    Union[
                        OnPremiseSqlResourceDetailsArgs,
                        OnPremiseSqlResourceDetailsArgsDict,
                    ],
                ]
            ]
        ] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[AssessmentStatusArgs, AssessmentStatusArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AssessmentArgs,
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
    @pulumi.getter(name="additionalData")
    def additional_data(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def links(self) -> pulumi.Output[outputs.AssessmentLinksResponse]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> pulumi.Output[
        Optional[outputs.SecurityAssessmentMetadataPropertiesResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partnersData")
    def partners_data(
        self,
    ) -> pulumi.Output[Optional[outputs.SecurityAssessmentPartnerDataResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceDetails")
    def resource_details(self) -> pulumi.Output[Any]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[outputs.AssessmentStatusResponseResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
