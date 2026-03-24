

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CxSecuritySettingsArgs', 'CxSecuritySettings']
@pulumi.input_type
class CxSecuritySettingsArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], audio_export_settings: Optional[pulumi.Input[CxSecuritySettingsAudioExportSettingsArgs]] = ..., deidentify_template: Optional[pulumi.Input[_builtins.str]] = ..., insights_export_settings: Optional[pulumi.Input[CxSecuritySettingsInsightsExportSettingsArgs]] = ..., inspect_template: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., purge_data_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., redaction_scope: Optional[pulumi.Input[_builtins.str]] = ..., redaction_strategy: Optional[pulumi.Input[_builtins.str]] = ..., retention_strategy: Optional[pulumi.Input[_builtins.str]] = ..., retention_window_days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioExportSettings")
    def audio_export_settings(self) -> Optional[pulumi.Input[CxSecuritySettingsAudioExportSettingsArgs]]:
        
        ...
    
    @audio_export_settings.setter
    def audio_export_settings(self, value: Optional[pulumi.Input[CxSecuritySettingsAudioExportSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deidentifyTemplate")
    def deidentify_template(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deidentify_template.setter
    def deidentify_template(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="insightsExportSettings")
    def insights_export_settings(self) -> Optional[pulumi.Input[CxSecuritySettingsInsightsExportSettingsArgs]]:
        
        ...
    
    @insights_export_settings.setter
    def insights_export_settings(self, value: Optional[pulumi.Input[CxSecuritySettingsInsightsExportSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectTemplate")
    def inspect_template(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @inspect_template.setter
    def inspect_template(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="purgeDataTypes")
    def purge_data_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @purge_data_types.setter
    def purge_data_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactionScope")
    def redaction_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redaction_scope.setter
    def redaction_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactionStrategy")
    def redaction_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redaction_strategy.setter
    def redaction_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionStrategy")
    def retention_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @retention_strategy.setter
    def retention_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionWindowDays")
    def retention_window_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention_window_days.setter
    def retention_window_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.input_type
class _CxSecuritySettingsState:
    def __init__(__self__, *, audio_export_settings: Optional[pulumi.Input[CxSecuritySettingsAudioExportSettingsArgs]] = ..., deidentify_template: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., insights_export_settings: Optional[pulumi.Input[CxSecuritySettingsInsightsExportSettingsArgs]] = ..., inspect_template: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., purge_data_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., redaction_scope: Optional[pulumi.Input[_builtins.str]] = ..., redaction_strategy: Optional[pulumi.Input[_builtins.str]] = ..., retention_strategy: Optional[pulumi.Input[_builtins.str]] = ..., retention_window_days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioExportSettings")
    def audio_export_settings(self) -> Optional[pulumi.Input[CxSecuritySettingsAudioExportSettingsArgs]]:
        
        ...
    
    @audio_export_settings.setter
    def audio_export_settings(self, value: Optional[pulumi.Input[CxSecuritySettingsAudioExportSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deidentifyTemplate")
    def deidentify_template(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deidentify_template.setter
    def deidentify_template(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="insightsExportSettings")
    def insights_export_settings(self) -> Optional[pulumi.Input[CxSecuritySettingsInsightsExportSettingsArgs]]:
        
        ...
    
    @insights_export_settings.setter
    def insights_export_settings(self, value: Optional[pulumi.Input[CxSecuritySettingsInsightsExportSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectTemplate")
    def inspect_template(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @inspect_template.setter
    def inspect_template(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="purgeDataTypes")
    def purge_data_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @purge_data_types.setter
    def purge_data_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactionScope")
    def redaction_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redaction_scope.setter
    def redaction_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactionStrategy")
    def redaction_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redaction_strategy.setter
    def redaction_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionStrategy")
    def retention_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @retention_strategy.setter
    def retention_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionWindowDays")
    def retention_window_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention_window_days.setter
    def retention_window_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("gcp:diagflow/cxSecuritySettings:CxSecuritySettings")
class CxSecuritySettings(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., audio_export_settings: Optional[pulumi.Input[Union[CxSecuritySettingsAudioExportSettingsArgs, CxSecuritySettingsAudioExportSettingsArgsDict]]] = ..., deidentify_template: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., insights_export_settings: Optional[pulumi.Input[Union[CxSecuritySettingsInsightsExportSettingsArgs, CxSecuritySettingsInsightsExportSettingsArgsDict]]] = ..., inspect_template: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., purge_data_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., redaction_scope: Optional[pulumi.Input[_builtins.str]] = ..., redaction_strategy: Optional[pulumi.Input[_builtins.str]] = ..., retention_strategy: Optional[pulumi.Input[_builtins.str]] = ..., retention_window_days: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CxSecuritySettingsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., audio_export_settings: Optional[pulumi.Input[Union[CxSecuritySettingsAudioExportSettingsArgs, CxSecuritySettingsAudioExportSettingsArgsDict]]] = ..., deidentify_template: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., insights_export_settings: Optional[pulumi.Input[Union[CxSecuritySettingsInsightsExportSettingsArgs, CxSecuritySettingsInsightsExportSettingsArgsDict]]] = ..., inspect_template: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., purge_data_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., redaction_scope: Optional[pulumi.Input[_builtins.str]] = ..., redaction_strategy: Optional[pulumi.Input[_builtins.str]] = ..., retention_strategy: Optional[pulumi.Input[_builtins.str]] = ..., retention_window_days: Optional[pulumi.Input[_builtins.int]] = ...) -> CxSecuritySettings:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioExportSettings")
    def audio_export_settings(self) -> pulumi.Output[Optional[outputs.CxSecuritySettingsAudioExportSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deidentifyTemplate")
    def deidentify_template(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insightsExportSettings")
    def insights_export_settings(self) -> pulumi.Output[Optional[outputs.CxSecuritySettingsInsightsExportSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectTemplate")
    def inspect_template(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="purgeDataTypes")
    def purge_data_types(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactionScope")
    def redaction_scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactionStrategy")
    def redaction_strategy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionStrategy")
    def retention_strategy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionWindowDays")
    def retention_window_days(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    


