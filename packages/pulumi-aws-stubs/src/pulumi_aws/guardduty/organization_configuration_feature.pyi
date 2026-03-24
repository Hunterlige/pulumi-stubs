import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OrganizationConfigurationFeatureArgs", "OrganizationConfigurationFeature"]

@pulumi.input_type
class OrganizationConfigurationFeatureArgs:
    def __init__(
        __self__,
        *,
        auto_enable: pulumi.Input[_builtins.str],
        detector_id: pulumi.Input[_builtins.str],
        additional_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        OrganizationConfigurationFeatureAdditionalConfigurationArgs
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> pulumi.Input[_builtins.str]: ...
    @auto_enable.setter
    def auto_enable(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Input[_builtins.str]: ...
    @detector_id.setter
    def detector_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalConfigurations")
    def additional_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    OrganizationConfigurationFeatureAdditionalConfigurationArgs
                ]
            ]
        ]
    ]: ...
    @additional_configurations.setter
    def additional_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        OrganizationConfigurationFeatureAdditionalConfigurationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _OrganizationConfigurationFeatureState:
    def __init__(
        __self__,
        *,
        additional_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        OrganizationConfigurationFeatureAdditionalConfigurationArgs
                    ]
                ]
            ]
        ] = ...,
        auto_enable: Optional[pulumi.Input[_builtins.str]] = ...,
        detector_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalConfigurations")
    def additional_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    OrganizationConfigurationFeatureAdditionalConfigurationArgs
                ]
            ]
        ]
    ]: ...
    @additional_configurations.setter
    def additional_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        OrganizationConfigurationFeatureAdditionalConfigurationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_enable.setter
    def auto_enable(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @detector_id.setter
    def detector_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class OrganizationConfigurationFeature(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            OrganizationConfigurationFeatureAdditionalConfigurationArgs,
                            OrganizationConfigurationFeatureAdditionalConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        auto_enable: Optional[pulumi.Input[_builtins.str]] = ...,
        detector_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OrganizationConfigurationFeatureArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            OrganizationConfigurationFeatureAdditionalConfigurationArgs,
                            OrganizationConfigurationFeatureAdditionalConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        auto_enable: Optional[pulumi.Input[_builtins.str]] = ...,
        detector_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> OrganizationConfigurationFeature: ...
    @_builtins.property
    @pulumi.getter(name="additionalConfigurations")
    def additional_configurations(
        self,
    ) -> pulumi.Output[
        Optional[
            Sequence[outputs.OrganizationConfigurationFeatureAdditionalConfiguration]
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
