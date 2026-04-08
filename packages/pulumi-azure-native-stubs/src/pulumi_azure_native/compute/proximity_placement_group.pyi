import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProximityPlacementGroupArgs", "ProximityPlacementGroup"]

@pulumi.input_type
class ProximityPlacementGroupArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        colocation_status: Optional[pulumi.Input[InstanceViewStatusArgs]] = ...,
        intent: Optional[
            pulumi.Input[ProximityPlacementGroupPropertiesIntentArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        proximity_placement_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        proximity_placement_group_type: Optional[
            pulumi.Input[Union[_builtins.str, ProximityPlacementGroupType]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="colocationStatus")
    def colocation_status(self) -> Optional[pulumi.Input[InstanceViewStatusArgs]]: ...
    @colocation_status.setter
    def colocation_status(
        self, value: Optional[pulumi.Input[InstanceViewStatusArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def intent(
        self,
    ) -> Optional[pulumi.Input[ProximityPlacementGroupPropertiesIntentArgs]]: ...
    @intent.setter
    def intent(
        self, value: Optional[pulumi.Input[ProximityPlacementGroupPropertiesIntentArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroupName")
    def proximity_placement_group_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @proximity_placement_group_name.setter
    def proximity_placement_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroupType")
    def proximity_placement_group_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProximityPlacementGroupType]]]: ...
    @proximity_placement_group_type.setter
    def proximity_placement_group_type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ProximityPlacementGroupType]]
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
    @_builtins.property
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:compute:ProximityPlacementGroup")
class ProximityPlacementGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        colocation_status: Optional[
            pulumi.Input[Union[InstanceViewStatusArgs, InstanceViewStatusArgsDict]]
        ] = ...,
        intent: Optional[
            pulumi.Input[
                Union[
                    ProximityPlacementGroupPropertiesIntentArgs,
                    ProximityPlacementGroupPropertiesIntentArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        proximity_placement_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        proximity_placement_group_type: Optional[
            pulumi.Input[Union[_builtins.str, ProximityPlacementGroupType]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ProximityPlacementGroupArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ProximityPlacementGroup: ...
    @_builtins.property
    @pulumi.getter(name="availabilitySets")
    def availability_sets(
        self,
    ) -> pulumi.Output[Sequence[outputs.SubResourceWithColocationStatusResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="colocationStatus")
    def colocation_status(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceViewStatusResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def intent(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ProximityPlacementGroupPropertiesIntentResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroupType")
    def proximity_placement_group_type(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
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
    @pulumi.getter(name="virtualMachineScaleSets")
    def virtual_machine_scale_sets(
        self,
    ) -> pulumi.Output[Sequence[outputs.SubResourceWithColocationStatusResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachines")
    def virtual_machines(
        self,
    ) -> pulumi.Output[Sequence[outputs.SubResourceWithColocationStatusResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
