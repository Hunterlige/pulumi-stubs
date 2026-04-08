import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KpiArgs", "Kpi"]

@pulumi.input_type
class KpiArgs:
    def __init__(
        __self__,
        *,
        calculation_window: pulumi.Input[CalculationWindowTypes],
        entity_type: pulumi.Input[EntityTypes],
        entity_type_name: pulumi.Input[_builtins.str],
        expression: pulumi.Input[_builtins.str],
        function: pulumi.Input[KpiFunctions],
        hub_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        aliases: Optional[pulumi.Input[Sequence[pulumi.Input[KpiAliasArgs]]]] = ...,
        calculation_window_field_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        extracts: Optional[pulumi.Input[Sequence[pulumi.Input[KpiExtractArgs]]]] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        group_by: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        kpi_name: Optional[pulumi.Input[_builtins.str]] = ...,
        thres_holds: Optional[pulumi.Input[KpiThresholdsArgs]] = ...,
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="calculationWindow")
    def calculation_window(self) -> pulumi.Input[CalculationWindowTypes]: ...
    @calculation_window.setter
    def calculation_window(self, value: pulumi.Input[CalculationWindowTypes]): ...
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Input[EntityTypes]: ...
    @entity_type.setter
    def entity_type(self, value: pulumi.Input[EntityTypes]): ...
    @_builtins.property
    @pulumi.getter(name="entityTypeName")
    def entity_type_name(self) -> pulumi.Input[_builtins.str]: ...
    @entity_type_name.setter
    def entity_type_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def function(self) -> pulumi.Input[KpiFunctions]: ...
    @function.setter
    def function(self, value: pulumi.Input[KpiFunctions]): ...
    @_builtins.property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> pulumi.Input[_builtins.str]: ...
    @hub_name.setter
    def hub_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def aliases(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[KpiAliasArgs]]]]: ...
    @aliases.setter
    def aliases(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[KpiAliasArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="calculationWindowFieldName")
    def calculation_window_field_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @calculation_window_field_name.setter
    def calculation_window_field_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @description.setter
    def description(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @display_name.setter
    def display_name(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def extracts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[KpiExtractArgs]]]]: ...
    @extracts.setter
    def extracts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[KpiExtractArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="groupBy")
    def group_by(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @group_by.setter
    def group_by(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kpiName")
    def kpi_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kpi_name.setter
    def kpi_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="thresHolds")
    def thres_holds(self) -> Optional[pulumi.Input[KpiThresholdsArgs]]: ...
    @thres_holds.setter
    def thres_holds(self, value: Optional[pulumi.Input[KpiThresholdsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:customerinsights:Kpi")
class Kpi(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        aliases: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[KpiAliasArgs, KpiAliasArgsDict]]]]
        ] = ...,
        calculation_window: Optional[pulumi.Input[CalculationWindowTypes]] = ...,
        calculation_window_field_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        entity_type: Optional[pulumi.Input[EntityTypes]] = ...,
        entity_type_name: Optional[pulumi.Input[_builtins.str]] = ...,
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        extracts: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[KpiExtractArgs, KpiExtractArgsDict]]]
            ]
        ] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        function: Optional[pulumi.Input[KpiFunctions]] = ...,
        group_by: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kpi_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        thres_holds: Optional[
            pulumi.Input[Union[KpiThresholdsArgs, KpiThresholdsArgsDict]]
        ] = ...,
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: KpiArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Kpi: ...
    @_builtins.property
    @pulumi.getter
    def aliases(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.KpiAliasResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="calculationWindow")
    def calculation_window(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="calculationWindowFieldName")
    def calculation_window_field_name(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entityTypeName")
    def entity_type_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def extracts(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.KpiExtractResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def function(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="groupBy")
    def group_by(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="groupByMetadata")
    def group_by_metadata(
        self,
    ) -> pulumi.Output[Sequence[outputs.KpiGroupByMetadataResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="kpiName")
    def kpi_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="participantProfilesMetadata")
    def participant_profiles_metadata(
        self,
    ) -> pulumi.Output[Sequence[outputs.KpiParticipantProfilesMetadataResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="thresHolds")
    def thres_holds(self) -> pulumi.Output[Optional[outputs.KpiThresholdsResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Output[Optional[_builtins.str]]: ...
