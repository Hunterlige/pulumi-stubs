

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['Hl7StoreArgs', 'Hl7Store']
@pulumi.input_type
class Hl7StoreArgs:
    def __init__(__self__, *, dataset: pulumi.Input[_builtins.str], labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[Hl7StoreNotificationConfigArgs]] = ..., notification_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Hl7StoreNotificationConfigsArgs]]]] = ..., parser_config: Optional[pulumi.Input[Hl7StoreParserConfigArgs]] = ..., reject_duplicate_message: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dataset.setter
    def dataset(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    @_utilities.deprecated(...)
    def notification_config(self) -> Optional[pulumi.Input[Hl7StoreNotificationConfigArgs]]:
        
        ...
    
    @notification_config.setter
    def notification_config(self, value: Optional[pulumi.Input[Hl7StoreNotificationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfigs")
    def notification_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Hl7StoreNotificationConfigsArgs]]]]:
        
        ...
    
    @notification_configs.setter
    def notification_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Hl7StoreNotificationConfigsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parserConfig")
    def parser_config(self) -> Optional[pulumi.Input[Hl7StoreParserConfigArgs]]:
        
        ...
    
    @parser_config.setter
    def parser_config(self, value: Optional[pulumi.Input[Hl7StoreParserConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rejectDuplicateMessage")
    def reject_duplicate_message(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @reject_duplicate_message.setter
    def reject_duplicate_message(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _Hl7StoreState:
    def __init__(__self__, *, dataset: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[Hl7StoreNotificationConfigArgs]] = ..., notification_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Hl7StoreNotificationConfigsArgs]]]] = ..., parser_config: Optional[pulumi.Input[Hl7StoreParserConfigArgs]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., reject_duplicate_message: Optional[pulumi.Input[_builtins.bool]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dataset.setter
    def dataset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    @_utilities.deprecated(...)
    def notification_config(self) -> Optional[pulumi.Input[Hl7StoreNotificationConfigArgs]]:
        
        ...
    
    @notification_config.setter
    def notification_config(self, value: Optional[pulumi.Input[Hl7StoreNotificationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfigs")
    def notification_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Hl7StoreNotificationConfigsArgs]]]]:
        
        ...
    
    @notification_configs.setter
    def notification_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Hl7StoreNotificationConfigsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parserConfig")
    def parser_config(self) -> Optional[pulumi.Input[Hl7StoreParserConfigArgs]]:
        
        ...
    
    @parser_config.setter
    def parser_config(self, value: Optional[pulumi.Input[Hl7StoreParserConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rejectDuplicateMessage")
    def reject_duplicate_message(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @reject_duplicate_message.setter
    def reject_duplicate_message(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:healthcare/hl7Store:Hl7Store")
class Hl7Store(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., dataset: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[Union[Hl7StoreNotificationConfigArgs, Hl7StoreNotificationConfigArgsDict]]] = ..., notification_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[Hl7StoreNotificationConfigsArgs, Hl7StoreNotificationConfigsArgsDict]]]]] = ..., parser_config: Optional[pulumi.Input[Union[Hl7StoreParserConfigArgs, Hl7StoreParserConfigArgsDict]]] = ..., reject_duplicate_message: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Hl7StoreArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., dataset: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[Union[Hl7StoreNotificationConfigArgs, Hl7StoreNotificationConfigArgsDict]]] = ..., notification_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[Hl7StoreNotificationConfigsArgs, Hl7StoreNotificationConfigsArgsDict]]]]] = ..., parser_config: Optional[pulumi.Input[Union[Hl7StoreParserConfigArgs, Hl7StoreParserConfigArgsDict]]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., reject_duplicate_message: Optional[pulumi.Input[_builtins.bool]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ...) -> Hl7Store:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    @_utilities.deprecated(...)
    def notification_config(self) -> pulumi.Output[Optional[outputs.Hl7StoreNotificationConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfigs")
    def notification_configs(self) -> pulumi.Output[Optional[Sequence[outputs.Hl7StoreNotificationConfigs]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parserConfig")
    def parser_config(self) -> pulumi.Output[outputs.Hl7StoreParserConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rejectDuplicateMessage")
    def reject_duplicate_message(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


