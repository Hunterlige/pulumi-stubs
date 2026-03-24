

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DataTransferConfigArgs', 'DataTransferConfig']
@pulumi.input_type
class DataTransferConfigArgs:
    def __init__(__self__, *, data_source_id: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], params: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]], data_refresh_window_days: Optional[pulumi.Input[_builtins.int]] = ..., destination_dataset_id: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., email_preferences: Optional[pulumi.Input[DataTransferConfigEmailPreferencesArgs]] = ..., encryption_configuration: Optional[pulumi.Input[DataTransferConfigEncryptionConfigurationArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., notification_pubsub_topic: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[_builtins.str]] = ..., schedule_options: Optional[pulumi.Input[DataTransferConfigScheduleOptionsArgs]] = ..., sensitive_params: Optional[pulumi.Input[DataTransferConfigSensitiveParamsArgs]] = ..., service_account_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_source_id.setter
    def data_source_id(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def params(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]:
        
        ...
    
    @params.setter
    def params(self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRefreshWindowDays")
    def data_refresh_window_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @data_refresh_window_days.setter
    def data_refresh_window_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationDatasetId")
    def destination_dataset_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_dataset_id.setter
    def destination_dataset_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailPreferences")
    def email_preferences(self) -> Optional[pulumi.Input[DataTransferConfigEmailPreferencesArgs]]:
        
        ...
    
    @email_preferences.setter
    def email_preferences(self, value: Optional[pulumi.Input[DataTransferConfigEmailPreferencesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input[DataTransferConfigEncryptionConfigurationArgs]]:
        
        ...
    
    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input[DataTransferConfigEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationPubsubTopic")
    def notification_pubsub_topic(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notification_pubsub_topic.setter
    def notification_pubsub_topic(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleOptions")
    def schedule_options(self) -> Optional[pulumi.Input[DataTransferConfigScheduleOptionsArgs]]:
        
        ...
    
    @schedule_options.setter
    def schedule_options(self, value: Optional[pulumi.Input[DataTransferConfigScheduleOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitiveParams")
    def sensitive_params(self) -> Optional[pulumi.Input[DataTransferConfigSensitiveParamsArgs]]:
        
        ...
    
    @sensitive_params.setter
    def sensitive_params(self, value: Optional[pulumi.Input[DataTransferConfigSensitiveParamsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountName")
    def service_account_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account_name.setter
    def service_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DataTransferConfigState:
    def __init__(__self__, *, data_refresh_window_days: Optional[pulumi.Input[_builtins.int]] = ..., data_source_id: Optional[pulumi.Input[_builtins.str]] = ..., destination_dataset_id: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., email_preferences: Optional[pulumi.Input[DataTransferConfigEmailPreferencesArgs]] = ..., encryption_configuration: Optional[pulumi.Input[DataTransferConfigEncryptionConfigurationArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_pubsub_topic: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[_builtins.str]] = ..., schedule_options: Optional[pulumi.Input[DataTransferConfigScheduleOptionsArgs]] = ..., sensitive_params: Optional[pulumi.Input[DataTransferConfigSensitiveParamsArgs]] = ..., service_account_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRefreshWindowDays")
    def data_refresh_window_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @data_refresh_window_days.setter
    def data_refresh_window_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_source_id.setter
    def data_source_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationDatasetId")
    def destination_dataset_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_dataset_id.setter
    def destination_dataset_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailPreferences")
    def email_preferences(self) -> Optional[pulumi.Input[DataTransferConfigEmailPreferencesArgs]]:
        
        ...
    
    @email_preferences.setter
    def email_preferences(self, value: Optional[pulumi.Input[DataTransferConfigEmailPreferencesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input[DataTransferConfigEncryptionConfigurationArgs]]:
        
        ...
    
    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input[DataTransferConfigEncryptionConfigurationArgs]]): # -> None:
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
    @pulumi.getter(name="notificationPubsubTopic")
    def notification_pubsub_topic(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notification_pubsub_topic.setter
    def notification_pubsub_topic(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleOptions")
    def schedule_options(self) -> Optional[pulumi.Input[DataTransferConfigScheduleOptionsArgs]]:
        
        ...
    
    @schedule_options.setter
    def schedule_options(self, value: Optional[pulumi.Input[DataTransferConfigScheduleOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitiveParams")
    def sensitive_params(self) -> Optional[pulumi.Input[DataTransferConfigSensitiveParamsArgs]]:
        
        ...
    
    @sensitive_params.setter
    def sensitive_params(self, value: Optional[pulumi.Input[DataTransferConfigSensitiveParamsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountName")
    def service_account_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account_name.setter
    def service_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:bigquery/dataTransferConfig:DataTransferConfig")
class DataTransferConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., data_refresh_window_days: Optional[pulumi.Input[_builtins.int]] = ..., data_source_id: Optional[pulumi.Input[_builtins.str]] = ..., destination_dataset_id: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., email_preferences: Optional[pulumi.Input[Union[DataTransferConfigEmailPreferencesArgs, DataTransferConfigEmailPreferencesArgsDict]]] = ..., encryption_configuration: Optional[pulumi.Input[Union[DataTransferConfigEncryptionConfigurationArgs, DataTransferConfigEncryptionConfigurationArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., notification_pubsub_topic: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[_builtins.str]] = ..., schedule_options: Optional[pulumi.Input[Union[DataTransferConfigScheduleOptionsArgs, DataTransferConfigScheduleOptionsArgsDict]]] = ..., sensitive_params: Optional[pulumi.Input[Union[DataTransferConfigSensitiveParamsArgs, DataTransferConfigSensitiveParamsArgsDict]]] = ..., service_account_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DataTransferConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., data_refresh_window_days: Optional[pulumi.Input[_builtins.int]] = ..., data_source_id: Optional[pulumi.Input[_builtins.str]] = ..., destination_dataset_id: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., email_preferences: Optional[pulumi.Input[Union[DataTransferConfigEmailPreferencesArgs, DataTransferConfigEmailPreferencesArgsDict]]] = ..., encryption_configuration: Optional[pulumi.Input[Union[DataTransferConfigEncryptionConfigurationArgs, DataTransferConfigEncryptionConfigurationArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_pubsub_topic: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., schedule: Optional[pulumi.Input[_builtins.str]] = ..., schedule_options: Optional[pulumi.Input[Union[DataTransferConfigScheduleOptionsArgs, DataTransferConfigScheduleOptionsArgsDict]]] = ..., sensitive_params: Optional[pulumi.Input[Union[DataTransferConfigSensitiveParamsArgs, DataTransferConfigSensitiveParamsArgsDict]]] = ..., service_account_name: Optional[pulumi.Input[_builtins.str]] = ...) -> DataTransferConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRefreshWindowDays")
    def data_refresh_window_days(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationDatasetId")
    def destination_dataset_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailPreferences")
    def email_preferences(self) -> pulumi.Output[Optional[outputs.DataTransferConfigEmailPreferences]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> pulumi.Output[Optional[outputs.DataTransferConfigEncryptionConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationPubsubTopic")
    def notification_pubsub_topic(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleOptions")
    def schedule_options(self) -> pulumi.Output[Optional[outputs.DataTransferConfigScheduleOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitiveParams")
    def sensitive_params(self) -> pulumi.Output[Optional[outputs.DataTransferConfigSensitiveParams]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountName")
    def service_account_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


