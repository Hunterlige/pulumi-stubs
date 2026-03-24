

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NetworkTapRuleArgs', 'NetworkTapRule']
@pulumi.input_type
class NetworkTapRuleArgs:
    def __init__(__self__, *, configuration_type: pulumi.Input[Union[_builtins.str, ConfigurationType]], resource_group_name: pulumi.Input[_builtins.str], annotation: Optional[pulumi.Input[_builtins.str]] = ..., dynamic_match_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[CommonDynamicMatchConfigurationArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., match_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkTapRuleMatchConfigurationArgs]]]] = ..., network_tap_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., polling_interval_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tap_rules_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> pulumi.Input[Union[_builtins.str, ConfigurationType]]:
        
        ...
    
    @configuration_type.setter
    def configuration_type(self, value: pulumi.Input[Union[_builtins.str, ConfigurationType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @annotation.setter
    def annotation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicMatchConfigurations")
    def dynamic_match_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CommonDynamicMatchConfigurationArgs]]]]:
        
        ...
    
    @dynamic_match_configurations.setter
    def dynamic_match_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CommonDynamicMatchConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchConfigurations")
    def match_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkTapRuleMatchConfigurationArgs]]]]:
        
        ...
    
    @match_configurations.setter
    def match_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkTapRuleMatchConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkTapRuleName")
    def network_tap_rule_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_tap_rule_name.setter
    def network_tap_rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pollingIntervalInSeconds")
    def polling_interval_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @polling_interval_in_seconds.setter
    def polling_interval_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tapRulesUrl")
    def tap_rules_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tap_rules_url.setter
    def tap_rules_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:managednetworkfabric:NetworkTapRule")
class NetworkTapRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., annotation: Optional[pulumi.Input[_builtins.str]] = ..., configuration_type: Optional[pulumi.Input[Union[_builtins.str, ConfigurationType]]] = ..., dynamic_match_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CommonDynamicMatchConfigurationArgs, CommonDynamicMatchConfigurationArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., match_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NetworkTapRuleMatchConfigurationArgs, NetworkTapRuleMatchConfigurationArgsDict]]]]] = ..., network_tap_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., polling_interval_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tap_rules_url: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NetworkTapRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> NetworkTapRule:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicMatchConfigurations")
    def dynamic_match_configurations(self) -> pulumi.Output[Optional[Sequence[outputs.CommonDynamicMatchConfigurationResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSyncedTime")
    def last_synced_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchConfigurations")
    def match_configurations(self) -> pulumi.Output[Optional[Sequence[outputs.NetworkTapRuleMatchConfigurationResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkTapId")
    def network_tap_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pollingIntervalInSeconds")
    def polling_interval_in_seconds(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tapRulesUrl")
    def tap_rules_url(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


