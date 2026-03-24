

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FirewallArgs', 'Firewall']
@pulumi.input_type
class FirewallArgs:
    def __init__(__self__, *, network: pulumi.Input[_builtins.str], allows: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallAllowArgs]]]] = ..., denies: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallDenyArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., direction: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., log_config: Optional[pulumi.Input[FirewallLogConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[FirewallParamsArgs]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., source_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_service_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_service_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def allows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirewallAllowArgs]]]]:
        
        ...
    
    @allows.setter
    def allows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallAllowArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def denies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirewallDenyArgs]]]]:
        
        ...
    
    @denies.setter
    def denies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallDenyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationRanges")
    def destination_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @destination_ranges.setter
    def destination_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @direction.setter
    def direction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    @_utilities.deprecated("""Deprecated in favor of log_config""")
    def enable_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_logging.setter
    def enable_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[FirewallLogConfigArgs]]:
        
        ...
    
    @log_config.setter
    def log_config(self, value: Optional[pulumi.Input[FirewallLogConfigArgs]]): # -> None:
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
    def params(self) -> Optional[pulumi.Input[FirewallParamsArgs]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[FirewallParamsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRanges")
    def source_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @source_ranges.setter
    def source_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServiceAccounts")
    def source_service_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @source_service_accounts.setter
    def source_service_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceTags")
    def source_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @source_tags.setter
    def source_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServiceAccounts")
    def target_service_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_service_accounts.setter
    def target_service_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetTags")
    def target_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_tags.setter
    def target_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _FirewallState:
    def __init__(__self__, *, allows: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallAllowArgs]]]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., denies: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallDenyArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., direction: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., log_config: Optional[pulumi.Input[FirewallLogConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[FirewallParamsArgs]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., source_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_service_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_service_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def allows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirewallAllowArgs]]]]:
        
        ...
    
    @allows.setter
    def allows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallAllowArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def denies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FirewallDenyArgs]]]]:
        
        ...
    
    @denies.setter
    def denies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FirewallDenyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationRanges")
    def destination_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @destination_ranges.setter
    def destination_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @direction.setter
    def direction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    @_utilities.deprecated("""Deprecated in favor of log_config""")
    def enable_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_logging.setter
    def enable_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[FirewallLogConfigArgs]]:
        
        ...
    
    @log_config.setter
    def log_config(self, value: Optional[pulumi.Input[FirewallLogConfigArgs]]): # -> None:
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
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[FirewallParamsArgs]]:
        
        ...
    
    @params.setter
    def params(self, value: Optional[pulumi.Input[FirewallParamsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRanges")
    def source_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @source_ranges.setter
    def source_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServiceAccounts")
    def source_service_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @source_service_accounts.setter
    def source_service_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceTags")
    def source_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @source_tags.setter
    def source_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServiceAccounts")
    def target_service_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_service_accounts.setter
    def target_service_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetTags")
    def target_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @target_tags.setter
    def target_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/firewall:Firewall")
class Firewall(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allows: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallAllowArgs, FirewallAllowArgsDict]]]]] = ..., denies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallDenyArgs, FirewallDenyArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., direction: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., log_config: Optional[pulumi.Input[Union[FirewallLogConfigArgs, FirewallLogConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Union[FirewallParamsArgs, FirewallParamsArgsDict]]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., source_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_service_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_service_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FirewallArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., allows: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallAllowArgs, FirewallAllowArgsDict]]]]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., denies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FirewallDenyArgs, FirewallDenyArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., direction: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ..., enable_logging: Optional[pulumi.Input[_builtins.bool]] = ..., log_config: Optional[pulumi.Input[Union[FirewallLogConfigArgs, FirewallLogConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., params: Optional[pulumi.Input[Union[FirewallParamsArgs, FirewallParamsArgsDict]]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., source_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_service_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_service_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., target_tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> Firewall:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def allows(self) -> pulumi.Output[Optional[Sequence[outputs.FirewallAllow]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def denies(self) -> pulumi.Output[Optional[Sequence[outputs.FirewallDeny]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationRanges")
    def destination_ranges(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    @_utilities.deprecated("""Deprecated in favor of log_config""")
    def enable_logging(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> pulumi.Output[Optional[outputs.FirewallLogConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> pulumi.Output[Optional[outputs.FirewallParams]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRanges")
    def source_ranges(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceServiceAccounts")
    def source_service_accounts(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceTags")
    def source_tags(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetServiceAccounts")
    def target_service_accounts(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetTags")
    def target_tags(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    


