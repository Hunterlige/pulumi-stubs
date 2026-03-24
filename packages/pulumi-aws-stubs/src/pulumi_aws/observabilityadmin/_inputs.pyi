

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CentralizationRuleForOrganizationRuleArgs', 'CentralizationRuleForOrganizationRuleArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'CentralizationRuleForOrganizationRuleSourceArgs', ..., ..., ..., 'CentralizationRuleForOrganizationTimeoutsArgs', 'CentralizationRuleForOrganizationTimeoutsArgsDict', 'TelemetryPipelineConfigurationArgs', 'TelemetryPipelineConfigurationArgsDict', 'TelemetryPipelineTimeoutsArgs', 'TelemetryPipelineTimeoutsArgsDict']
class CentralizationRuleForOrganizationRuleArgsDict(TypedDict):
    destination: pulumi.Input[CentralizationRuleForOrganizationRuleDestinationArgsDict]
    source: pulumi.Input[CentralizationRuleForOrganizationRuleSourceArgsDict]


@pulumi.input_type
class CentralizationRuleForOrganizationRuleArgs:
    def __init__(__self__, *, destination: pulumi.Input[CentralizationRuleForOrganizationRuleDestinationArgs], source: pulumi.Input[CentralizationRuleForOrganizationRuleSourceArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[CentralizationRuleForOrganizationRuleDestinationArgs]:
        
        ...
    
    @destination.setter
    def destination(self, value: pulumi.Input[CentralizationRuleForOrganizationRuleDestinationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[CentralizationRuleForOrganizationRuleSourceArgs]:
        
        ...
    
    @source.setter
    def source(self, value: pulumi.Input[CentralizationRuleForOrganizationRuleSourceArgs]): # -> None:
        ...
    


class CentralizationRuleForOrganizationRuleDestinationArgsDict(TypedDict):
    account: pulumi.Input[_builtins.str]
    region: pulumi.Input[_builtins.str]
    destination_logs_configuration: NotRequired[pulumi.Input[CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationArgsDict]]


@pulumi.input_type
class CentralizationRuleForOrganizationRuleDestinationArgs:
    def __init__(__self__, *, account: pulumi.Input[_builtins.str], region: pulumi.Input[_builtins.str], destination_logs_configuration: Optional[pulumi.Input[CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def account(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account.setter
    def account(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationLogsConfiguration")
    def destination_logs_configuration(self) -> Optional[pulumi.Input[CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationArgs]]:
        
        ...
    
    @destination_logs_configuration.setter
    def destination_logs_configuration(self, value: Optional[pulumi.Input[CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationArgs]]): # -> None:
        ...
    


class CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationArgsDict(TypedDict):
    backup_configuration: NotRequired[pulumi.Input[CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationBackupConfigurationArgsDict]]
    log_group_name_configuration: NotRequired[pulumi.Input[CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogGroupNameConfigurationArgsDict]]
    logs_encryption_configuration: NotRequired[pulumi.Input[CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogsEncryptionConfigurationArgsDict]]


@pulumi.input_type
class CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationArgs:
    def __init__(__self__, *, backup_configuration: Optional[pulumi.Input[CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationBackupConfigurationArgs]] = ..., log_group_name_configuration: Optional[pulumi.Input[CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogGroupNameConfigurationArgs]] = ..., logs_encryption_configuration: Optional[pulumi.Input[CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogsEncryptionConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfiguration")
    def backup_configuration(self) -> Optional[pulumi.Input[CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationBackupConfigurationArgs]]:
        
        ...
    
    @backup_configuration.setter
    def backup_configuration(self, value: Optional[pulumi.Input[CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationBackupConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupNameConfiguration")
    def log_group_name_configuration(self) -> Optional[pulumi.Input[CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogGroupNameConfigurationArgs]]:
        
        ...
    
    @log_group_name_configuration.setter
    def log_group_name_configuration(self, value: Optional[pulumi.Input[CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogGroupNameConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logsEncryptionConfiguration")
    def logs_encryption_configuration(self) -> Optional[pulumi.Input[CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogsEncryptionConfigurationArgs]]:
        
        ...
    
    @logs_encryption_configuration.setter
    def logs_encryption_configuration(self, value: Optional[pulumi.Input[CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogsEncryptionConfigurationArgs]]): # -> None:
        ...
    


class CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationBackupConfigurationArgsDict(TypedDict):
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationBackupConfigurationArgs:
    def __init__(__self__, *, kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogGroupNameConfigurationArgsDict(TypedDict):
    log_group_name_pattern: pulumi.Input[_builtins.str]


@pulumi.input_type
class CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogGroupNameConfigurationArgs:
    def __init__(__self__, *, log_group_name_pattern: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupNamePattern")
    def log_group_name_pattern(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @log_group_name_pattern.setter
    def log_group_name_pattern(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogsEncryptionConfigurationArgsDict(TypedDict):
    encryption_strategy: pulumi.Input[_builtins.str]
    encryption_conflict_resolution_strategy: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogsEncryptionConfigurationArgs:
    def __init__(__self__, *, encryption_strategy: pulumi.Input[_builtins.str], encryption_conflict_resolution_strategy: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionStrategy")
    def encryption_strategy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @encryption_strategy.setter
    def encryption_strategy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConflictResolutionStrategy")
    def encryption_conflict_resolution_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption_conflict_resolution_strategy.setter
    def encryption_conflict_resolution_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CentralizationRuleForOrganizationRuleSourceArgsDict(TypedDict):
    regions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    scope: pulumi.Input[_builtins.str]
    source_logs_configuration: NotRequired[pulumi.Input[CentralizationRuleForOrganizationRuleSourceSourceLogsConfigurationArgsDict]]


@pulumi.input_type
class CentralizationRuleForOrganizationRuleSourceArgs:
    def __init__(__self__, *, regions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], scope: pulumi.Input[_builtins.str], source_logs_configuration: Optional[pulumi.Input[CentralizationRuleForOrganizationRuleSourceSourceLogsConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @regions.setter
    def regions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceLogsConfiguration")
    def source_logs_configuration(self) -> Optional[pulumi.Input[CentralizationRuleForOrganizationRuleSourceSourceLogsConfigurationArgs]]:
        
        ...
    
    @source_logs_configuration.setter
    def source_logs_configuration(self, value: Optional[pulumi.Input[CentralizationRuleForOrganizationRuleSourceSourceLogsConfigurationArgs]]): # -> None:
        ...
    


class CentralizationRuleForOrganizationRuleSourceSourceLogsConfigurationArgsDict(TypedDict):
    encrypted_log_group_strategy: pulumi.Input[_builtins.str]
    log_group_selection_criteria: pulumi.Input[_builtins.str]


@pulumi.input_type
class CentralizationRuleForOrganizationRuleSourceSourceLogsConfigurationArgs:
    def __init__(__self__, *, encrypted_log_group_strategy: pulumi.Input[_builtins.str], log_group_selection_criteria: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedLogGroupStrategy")
    def encrypted_log_group_strategy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @encrypted_log_group_strategy.setter
    def encrypted_log_group_strategy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupSelectionCriteria")
    def log_group_selection_criteria(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @log_group_selection_criteria.setter
    def log_group_selection_criteria(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CentralizationRuleForOrganizationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CentralizationRuleForOrganizationTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TelemetryPipelineConfigurationArgsDict(TypedDict):
    body: pulumi.Input[_builtins.str]


@pulumi.input_type
class TelemetryPipelineConfigurationArgs:
    def __init__(__self__, *, body: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @body.setter
    def body(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TelemetryPipelineTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TelemetryPipelineTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


