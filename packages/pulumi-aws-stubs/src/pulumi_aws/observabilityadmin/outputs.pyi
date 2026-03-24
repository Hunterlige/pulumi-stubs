

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CentralizationRuleForOrganizationRule', 'CentralizationRuleForOrganizationRuleDestination', ..., ..., ..., ..., 'CentralizationRuleForOrganizationRuleSource', ..., 'CentralizationRuleForOrganizationTimeouts', 'TelemetryPipelineConfiguration', 'TelemetryPipelineTimeouts']
@pulumi.output_type
class CentralizationRuleForOrganizationRule(dict):
    def __init__(__self__, *, destination: outputs.CentralizationRuleForOrganizationRuleDestination, source: outputs.CentralizationRuleForOrganizationRuleSource) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> outputs.CentralizationRuleForOrganizationRuleDestination:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> outputs.CentralizationRuleForOrganizationRuleSource:
        
        ...
    


@pulumi.output_type
class CentralizationRuleForOrganizationRuleDestination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account: _builtins.str, region: _builtins.str, destination_logs_configuration: Optional[outputs.CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationLogsConfiguration")
    def destination_logs_configuration(self) -> Optional[outputs.CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfiguration]:
        
        ...
    


@pulumi.output_type
class CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_configuration: Optional[outputs.CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationBackupConfiguration] = ..., log_group_name_configuration: Optional[outputs.CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogGroupNameConfiguration] = ..., logs_encryption_configuration: Optional[outputs.CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogsEncryptionConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfiguration")
    def backup_configuration(self) -> Optional[outputs.CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationBackupConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupNameConfiguration")
    def log_group_name_configuration(self) -> Optional[outputs.CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogGroupNameConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logsEncryptionConfiguration")
    def logs_encryption_configuration(self) -> Optional[outputs.CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogsEncryptionConfiguration]:
        
        ...
    


@pulumi.output_type
class CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationBackupConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_arn: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogGroupNameConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_group_name_pattern: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupNamePattern")
    def log_group_name_pattern(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CentralizationRuleForOrganizationRuleDestinationDestinationLogsConfigurationLogsEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, encryption_strategy: _builtins.str, encryption_conflict_resolution_strategy: Optional[_builtins.str] = ..., kms_key_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionStrategy")
    def encryption_strategy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConflictResolutionStrategy")
    def encryption_conflict_resolution_strategy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CentralizationRuleForOrganizationRuleSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, regions: Sequence[_builtins.str], scope: _builtins.str, source_logs_configuration: Optional[outputs.CentralizationRuleForOrganizationRuleSourceSourceLogsConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceLogsConfiguration")
    def source_logs_configuration(self) -> Optional[outputs.CentralizationRuleForOrganizationRuleSourceSourceLogsConfiguration]:
        
        ...
    


@pulumi.output_type
class CentralizationRuleForOrganizationRuleSourceSourceLogsConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, encrypted_log_group_strategy: _builtins.str, log_group_selection_criteria: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedLogGroupStrategy")
    def encrypted_log_group_strategy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupSelectionCriteria")
    def log_group_selection_criteria(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CentralizationRuleForOrganizationTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TelemetryPipelineConfiguration(dict):
    def __init__(__self__, *, body: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TelemetryPipelineTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


