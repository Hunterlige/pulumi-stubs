

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VaultNotificationsArgs', 'VaultNotifications']
@pulumi.input_type
class VaultNotificationsArgs:
    def __init__(__self__, *, backup_vault_events: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], backup_vault_name: pulumi.Input[_builtins.str], sns_topic_arn: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultEvents")
    def backup_vault_events(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @backup_vault_events.setter
    def backup_vault_events(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultName")
    def backup_vault_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @backup_vault_name.setter
    def backup_vault_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sns_topic_arn.setter
    def sns_topic_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _VaultNotificationsState:
    def __init__(__self__, *, backup_vault_arn: Optional[pulumi.Input[_builtins.str]] = ..., backup_vault_events: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., backup_vault_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultArn")
    def backup_vault_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_vault_arn.setter
    def backup_vault_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultEvents")
    def backup_vault_events(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @backup_vault_events.setter
    def backup_vault_events(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultName")
    def backup_vault_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_vault_name.setter
    def backup_vault_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sns_topic_arn.setter
    def sns_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:backup/vaultNotifications:VaultNotifications")
class VaultNotifications(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., backup_vault_events: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., backup_vault_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VaultNotificationsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., backup_vault_arn: Optional[pulumi.Input[_builtins.str]] = ..., backup_vault_events: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., backup_vault_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> VaultNotifications:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultArn")
    def backup_vault_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultEvents")
    def backup_vault_events(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultName")
    def backup_vault_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


