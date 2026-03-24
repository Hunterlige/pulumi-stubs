

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DicomStoreArgs', 'DicomStore']
@pulumi.input_type
class DicomStoreArgs:
    def __init__(__self__, *, dataset: pulumi.Input[_builtins.str], labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[DicomStoreNotificationConfigArgs]] = ..., stream_configs: Optional[pulumi.Input[Sequence[pulumi.Input[DicomStoreStreamConfigArgs]]]] = ...) -> None:
        
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
    def notification_config(self) -> Optional[pulumi.Input[DicomStoreNotificationConfigArgs]]:
        
        ...
    
    @notification_config.setter
    def notification_config(self, value: Optional[pulumi.Input[DicomStoreNotificationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamConfigs")
    def stream_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DicomStoreStreamConfigArgs]]]]:
        
        ...
    
    @stream_configs.setter
    def stream_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DicomStoreStreamConfigArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _DicomStoreState:
    def __init__(__self__, *, dataset: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[DicomStoreNotificationConfigArgs]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., stream_configs: Optional[pulumi.Input[Sequence[pulumi.Input[DicomStoreStreamConfigArgs]]]] = ...) -> None:
        
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
    def notification_config(self) -> Optional[pulumi.Input[DicomStoreNotificationConfigArgs]]:
        
        ...
    
    @notification_config.setter
    def notification_config(self, value: Optional[pulumi.Input[DicomStoreNotificationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamConfigs")
    def stream_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DicomStoreStreamConfigArgs]]]]:
        
        ...
    
    @stream_configs.setter
    def stream_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DicomStoreStreamConfigArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:healthcare/dicomStore:DicomStore")
class DicomStore(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., dataset: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[Union[DicomStoreNotificationConfigArgs, DicomStoreNotificationConfigArgsDict]]] = ..., stream_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DicomStoreStreamConfigArgs, DicomStoreStreamConfigArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DicomStoreArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., dataset: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[Union[DicomStoreNotificationConfigArgs, DicomStoreNotificationConfigArgsDict]]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., stream_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DicomStoreStreamConfigArgs, DicomStoreStreamConfigArgsDict]]]]] = ...) -> DicomStore:
        
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
    def notification_config(self) -> pulumi.Output[Optional[outputs.DicomStoreNotificationConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamConfigs")
    def stream_configs(self) -> pulumi.Output[Optional[Sequence[outputs.DicomStoreStreamConfig]]]:
        
        ...
    


