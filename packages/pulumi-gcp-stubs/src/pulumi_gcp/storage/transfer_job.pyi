

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TransferJobArgs', 'TransferJob']
@pulumi.input_type
class TransferJobArgs:
    def __init__(__self__, *, description: pulumi.Input[_builtins.str], event_stream: Optional[pulumi.Input[TransferJobEventStreamArgs]] = ..., logging_config: Optional[pulumi.Input[TransferJobLoggingConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[TransferJobNotificationConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., replication_spec: Optional[pulumi.Input[TransferJobReplicationSpecArgs]] = ..., schedule: Optional[pulumi.Input[TransferJobScheduleArgs]] = ..., service_account: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., transfer_spec: Optional[pulumi.Input[TransferJobTransferSpecArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventStream")
    def event_stream(self) -> Optional[pulumi.Input[TransferJobEventStreamArgs]]:
        
        ...
    
    @event_stream.setter
    def event_stream(self, value: Optional[pulumi.Input[TransferJobEventStreamArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input[TransferJobLoggingConfigArgs]]:
        
        ...
    
    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input[TransferJobLoggingConfigArgs]]): # -> None:
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
    def notification_config(self) -> Optional[pulumi.Input[TransferJobNotificationConfigArgs]]:
        
        ...
    
    @notification_config.setter
    def notification_config(self, value: Optional[pulumi.Input[TransferJobNotificationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationSpec")
    def replication_spec(self) -> Optional[pulumi.Input[TransferJobReplicationSpecArgs]]:
        
        ...
    
    @replication_spec.setter
    def replication_spec(self, value: Optional[pulumi.Input[TransferJobReplicationSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[TransferJobScheduleArgs]]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[TransferJobScheduleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferSpec")
    def transfer_spec(self) -> Optional[pulumi.Input[TransferJobTransferSpecArgs]]:
        
        ...
    
    @transfer_spec.setter
    def transfer_spec(self, value: Optional[pulumi.Input[TransferJobTransferSpecArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _TransferJobState:
    def __init__(__self__, *, creation_time: Optional[pulumi.Input[_builtins.str]] = ..., deletion_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., event_stream: Optional[pulumi.Input[TransferJobEventStreamArgs]] = ..., last_modification_time: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[TransferJobLoggingConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[TransferJobNotificationConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., replication_spec: Optional[pulumi.Input[TransferJobReplicationSpecArgs]] = ..., schedule: Optional[pulumi.Input[TransferJobScheduleArgs]] = ..., service_account: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., transfer_spec: Optional[pulumi.Input[TransferJobTransferSpecArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionTime")
    def deletion_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deletion_time.setter
    def deletion_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventStream")
    def event_stream(self) -> Optional[pulumi.Input[TransferJobEventStreamArgs]]:
        
        ...
    
    @event_stream.setter
    def event_stream(self, value: Optional[pulumi.Input[TransferJobEventStreamArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModificationTime")
    def last_modification_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modification_time.setter
    def last_modification_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input[TransferJobLoggingConfigArgs]]:
        
        ...
    
    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input[TransferJobLoggingConfigArgs]]): # -> None:
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
    def notification_config(self) -> Optional[pulumi.Input[TransferJobNotificationConfigArgs]]:
        
        ...
    
    @notification_config.setter
    def notification_config(self, value: Optional[pulumi.Input[TransferJobNotificationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationSpec")
    def replication_spec(self) -> Optional[pulumi.Input[TransferJobReplicationSpecArgs]]:
        
        ...
    
    @replication_spec.setter
    def replication_spec(self, value: Optional[pulumi.Input[TransferJobReplicationSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[TransferJobScheduleArgs]]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[TransferJobScheduleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferSpec")
    def transfer_spec(self) -> Optional[pulumi.Input[TransferJobTransferSpecArgs]]:
        
        ...
    
    @transfer_spec.setter
    def transfer_spec(self, value: Optional[pulumi.Input[TransferJobTransferSpecArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:storage/transferJob:TransferJob")
class TransferJob(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., event_stream: Optional[pulumi.Input[Union[TransferJobEventStreamArgs, TransferJobEventStreamArgsDict]]] = ..., logging_config: Optional[pulumi.Input[Union[TransferJobLoggingConfigArgs, TransferJobLoggingConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[Union[TransferJobNotificationConfigArgs, TransferJobNotificationConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., replication_spec: Optional[pulumi.Input[Union[TransferJobReplicationSpecArgs, TransferJobReplicationSpecArgsDict]]] = ..., schedule: Optional[pulumi.Input[Union[TransferJobScheduleArgs, TransferJobScheduleArgsDict]]] = ..., service_account: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., transfer_spec: Optional[pulumi.Input[Union[TransferJobTransferSpecArgs, TransferJobTransferSpecArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TransferJobArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., creation_time: Optional[pulumi.Input[_builtins.str]] = ..., deletion_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., event_stream: Optional[pulumi.Input[Union[TransferJobEventStreamArgs, TransferJobEventStreamArgsDict]]] = ..., last_modification_time: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[Union[TransferJobLoggingConfigArgs, TransferJobLoggingConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_config: Optional[pulumi.Input[Union[TransferJobNotificationConfigArgs, TransferJobNotificationConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., replication_spec: Optional[pulumi.Input[Union[TransferJobReplicationSpecArgs, TransferJobReplicationSpecArgsDict]]] = ..., schedule: Optional[pulumi.Input[Union[TransferJobScheduleArgs, TransferJobScheduleArgsDict]]] = ..., service_account: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., transfer_spec: Optional[pulumi.Input[Union[TransferJobTransferSpecArgs, TransferJobTransferSpecArgsDict]]] = ...) -> TransferJob:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionTime")
    def deletion_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventStream")
    def event_stream(self) -> pulumi.Output[Optional[outputs.TransferJobEventStream]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModificationTime")
    def last_modification_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> pulumi.Output[Optional[outputs.TransferJobLoggingConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> pulumi.Output[Optional[outputs.TransferJobNotificationConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationSpec")
    def replication_spec(self) -> pulumi.Output[Optional[outputs.TransferJobReplicationSpec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional[outputs.TransferJobSchedule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferSpec")
    def transfer_spec(self) -> pulumi.Output[Optional[outputs.TransferJobTransferSpec]]:
        
        ...
    


