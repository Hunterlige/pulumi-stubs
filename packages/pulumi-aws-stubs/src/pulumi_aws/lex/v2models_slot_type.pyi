

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
__all__ = ['V2modelsSlotTypeArgs', 'V2modelsSlotType']
@pulumi.input_type
class V2modelsSlotTypeArgs:
    def __init__(__self__, *, bot_id: pulumi.Input[_builtins.str], bot_version: pulumi.Input[_builtins.str], locale_id: pulumi.Input[_builtins.str], composite_slot_type_settings: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeCompositeSlotTypeSettingArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., external_source_settings: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeExternalSourceSettingArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent_slot_type_signature: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., slot_type_values: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeSlotTypeValueArgs]]]] = ..., timeouts: Optional[pulumi.Input[V2modelsSlotTypeTimeoutsArgs]] = ..., value_selection_setting: Optional[pulumi.Input[V2modelsSlotTypeValueSelectionSettingArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="botId")
    def bot_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bot_id.setter
    def bot_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bot_version.setter
    def bot_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localeId")
    def locale_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @locale_id.setter
    def locale_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compositeSlotTypeSettings")
    def composite_slot_type_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeCompositeSlotTypeSettingArgs]]]]:
        
        ...
    
    @composite_slot_type_settings.setter
    def composite_slot_type_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeCompositeSlotTypeSettingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalSourceSettings")
    def external_source_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeExternalSourceSettingArgs]]]]:
        
        ...
    
    @external_source_settings.setter
    def external_source_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeExternalSourceSettingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentSlotTypeSignature")
    def parent_slot_type_signature(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent_slot_type_signature.setter
    def parent_slot_type_signature(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotTypeValues")
    def slot_type_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeSlotTypeValueArgs]]]]:
        
        ...
    
    @slot_type_values.setter
    def slot_type_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeSlotTypeValueArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[V2modelsSlotTypeTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[V2modelsSlotTypeTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueSelectionSetting")
    def value_selection_setting(self) -> Optional[pulumi.Input[V2modelsSlotTypeValueSelectionSettingArgs]]:
        
        ...
    
    @value_selection_setting.setter
    def value_selection_setting(self, value: Optional[pulumi.Input[V2modelsSlotTypeValueSelectionSettingArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _V2modelsSlotTypeState:
    def __init__(__self__, *, bot_id: Optional[pulumi.Input[_builtins.str]] = ..., bot_version: Optional[pulumi.Input[_builtins.str]] = ..., composite_slot_type_settings: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeCompositeSlotTypeSettingArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., external_source_settings: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeExternalSourceSettingArgs]]]] = ..., locale_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent_slot_type_signature: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., slot_type_id: Optional[pulumi.Input[_builtins.str]] = ..., slot_type_values: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeSlotTypeValueArgs]]]] = ..., timeouts: Optional[pulumi.Input[V2modelsSlotTypeTimeoutsArgs]] = ..., value_selection_setting: Optional[pulumi.Input[V2modelsSlotTypeValueSelectionSettingArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="botId")
    def bot_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bot_id.setter
    def bot_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bot_version.setter
    def bot_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compositeSlotTypeSettings")
    def composite_slot_type_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeCompositeSlotTypeSettingArgs]]]]:
        
        ...
    
    @composite_slot_type_settings.setter
    def composite_slot_type_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeCompositeSlotTypeSettingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalSourceSettings")
    def external_source_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeExternalSourceSettingArgs]]]]:
        
        ...
    
    @external_source_settings.setter
    def external_source_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeExternalSourceSettingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localeId")
    def locale_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @locale_id.setter
    def locale_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentSlotTypeSignature")
    def parent_slot_type_signature(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent_slot_type_signature.setter
    def parent_slot_type_signature(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotTypeId")
    def slot_type_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @slot_type_id.setter
    def slot_type_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotTypeValues")
    def slot_type_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeSlotTypeValueArgs]]]]:
        
        ...
    
    @slot_type_values.setter
    def slot_type_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2modelsSlotTypeSlotTypeValueArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[V2modelsSlotTypeTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[V2modelsSlotTypeTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueSelectionSetting")
    def value_selection_setting(self) -> Optional[pulumi.Input[V2modelsSlotTypeValueSelectionSettingArgs]]:
        
        ...
    
    @value_selection_setting.setter
    def value_selection_setting(self, value: Optional[pulumi.Input[V2modelsSlotTypeValueSelectionSettingArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:lex/v2modelsSlotType:V2modelsSlotType")
class V2modelsSlotType(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bot_id: Optional[pulumi.Input[_builtins.str]] = ..., bot_version: Optional[pulumi.Input[_builtins.str]] = ..., composite_slot_type_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[V2modelsSlotTypeCompositeSlotTypeSettingArgs, V2modelsSlotTypeCompositeSlotTypeSettingArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., external_source_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[V2modelsSlotTypeExternalSourceSettingArgs, V2modelsSlotTypeExternalSourceSettingArgsDict]]]]] = ..., locale_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent_slot_type_signature: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., slot_type_values: Optional[pulumi.Input[Sequence[pulumi.Input[Union[V2modelsSlotTypeSlotTypeValueArgs, V2modelsSlotTypeSlotTypeValueArgsDict]]]]] = ..., timeouts: Optional[pulumi.Input[Union[V2modelsSlotTypeTimeoutsArgs, V2modelsSlotTypeTimeoutsArgsDict]]] = ..., value_selection_setting: Optional[pulumi.Input[Union[V2modelsSlotTypeValueSelectionSettingArgs, V2modelsSlotTypeValueSelectionSettingArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: V2modelsSlotTypeArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bot_id: Optional[pulumi.Input[_builtins.str]] = ..., bot_version: Optional[pulumi.Input[_builtins.str]] = ..., composite_slot_type_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[V2modelsSlotTypeCompositeSlotTypeSettingArgs, V2modelsSlotTypeCompositeSlotTypeSettingArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., external_source_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[V2modelsSlotTypeExternalSourceSettingArgs, V2modelsSlotTypeExternalSourceSettingArgsDict]]]]] = ..., locale_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent_slot_type_signature: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., slot_type_id: Optional[pulumi.Input[_builtins.str]] = ..., slot_type_values: Optional[pulumi.Input[Sequence[pulumi.Input[Union[V2modelsSlotTypeSlotTypeValueArgs, V2modelsSlotTypeSlotTypeValueArgsDict]]]]] = ..., timeouts: Optional[pulumi.Input[Union[V2modelsSlotTypeTimeoutsArgs, V2modelsSlotTypeTimeoutsArgsDict]]] = ..., value_selection_setting: Optional[pulumi.Input[Union[V2modelsSlotTypeValueSelectionSettingArgs, V2modelsSlotTypeValueSelectionSettingArgsDict]]] = ...) -> V2modelsSlotType:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="botId")
    def bot_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="compositeSlotTypeSettings")
    def composite_slot_type_settings(self) -> pulumi.Output[Optional[Sequence[outputs.V2modelsSlotTypeCompositeSlotTypeSetting]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalSourceSettings")
    def external_source_settings(self) -> pulumi.Output[Optional[Sequence[outputs.V2modelsSlotTypeExternalSourceSetting]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localeId")
    def locale_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentSlotTypeSignature")
    def parent_slot_type_signature(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotTypeId")
    def slot_type_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotTypeValues")
    def slot_type_values(self) -> pulumi.Output[Optional[Sequence[outputs.V2modelsSlotTypeSlotTypeValue]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.V2modelsSlotTypeTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueSelectionSetting")
    def value_selection_setting(self) -> pulumi.Output[Optional[outputs.V2modelsSlotTypeValueSelectionSetting]]:
        
        ...
    


