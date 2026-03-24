

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InstanceArgs', 'Instance']
@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *, identity_management_type: pulumi.Input[_builtins.str], inbound_calls_enabled: pulumi.Input[_builtins.bool], outbound_calls_enabled: pulumi.Input[_builtins.bool], auto_resolve_best_voices_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., contact_flow_logs_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., contact_lens_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., early_media_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., instance_alias: Optional[pulumi.Input[_builtins.str]] = ..., multi_party_conference_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityManagementType")
    def identity_management_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @identity_management_type.setter
    def identity_management_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundCallsEnabled")
    def inbound_calls_enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @inbound_calls_enabled.setter
    def inbound_calls_enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundCallsEnabled")
    def outbound_calls_enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @outbound_calls_enabled.setter
    def outbound_calls_enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoResolveBestVoicesEnabled")
    def auto_resolve_best_voices_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_resolve_best_voices_enabled.setter
    def auto_resolve_best_voices_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactFlowLogsEnabled")
    def contact_flow_logs_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @contact_flow_logs_enabled.setter
    def contact_flow_logs_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactLensEnabled")
    def contact_lens_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @contact_lens_enabled.setter
    def contact_lens_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="earlyMediaEnabled")
    def early_media_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @early_media_enabled.setter
    def early_media_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceAlias")
    def instance_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_alias.setter
    def instance_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiPartyConferenceEnabled")
    def multi_party_conference_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @multi_party_conference_enabled.setter
    def multi_party_conference_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _InstanceState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_resolve_best_voices_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., contact_flow_logs_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., contact_lens_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., created_time: Optional[pulumi.Input[_builtins.str]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., early_media_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., identity_management_type: Optional[pulumi.Input[_builtins.str]] = ..., inbound_calls_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., instance_alias: Optional[pulumi.Input[_builtins.str]] = ..., multi_party_conference_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., outbound_calls_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_role: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoResolveBestVoicesEnabled")
    def auto_resolve_best_voices_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_resolve_best_voices_enabled.setter
    def auto_resolve_best_voices_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactFlowLogsEnabled")
    def contact_flow_logs_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @contact_flow_logs_enabled.setter
    def contact_flow_logs_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactLensEnabled")
    def contact_lens_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @contact_lens_enabled.setter
    def contact_lens_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="earlyMediaEnabled")
    def early_media_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @early_media_enabled.setter
    def early_media_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityManagementType")
    def identity_management_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity_management_type.setter
    def identity_management_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundCallsEnabled")
    def inbound_calls_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @inbound_calls_enabled.setter
    def inbound_calls_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceAlias")
    def instance_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_alias.setter
    def instance_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiPartyConferenceEnabled")
    def multi_party_conference_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @multi_party_conference_enabled.setter
    def multi_party_conference_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundCallsEnabled")
    def outbound_calls_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @outbound_calls_enabled.setter
    def outbound_calls_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_role.setter
    def service_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:connect/instance:Instance")
class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auto_resolve_best_voices_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., contact_flow_logs_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., contact_lens_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., early_media_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., identity_management_type: Optional[pulumi.Input[_builtins.str]] = ..., inbound_calls_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., instance_alias: Optional[pulumi.Input[_builtins.str]] = ..., multi_party_conference_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., outbound_calls_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InstanceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_resolve_best_voices_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., contact_flow_logs_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., contact_lens_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., created_time: Optional[pulumi.Input[_builtins.str]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., early_media_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., identity_management_type: Optional[pulumi.Input[_builtins.str]] = ..., inbound_calls_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., instance_alias: Optional[pulumi.Input[_builtins.str]] = ..., multi_party_conference_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., outbound_calls_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_role: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Instance:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoResolveBestVoicesEnabled")
    def auto_resolve_best_voices_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactFlowLogsEnabled")
    def contact_flow_logs_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactLensEnabled")
    def contact_lens_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="earlyMediaEnabled")
    def early_media_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityManagementType")
    def identity_management_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundCallsEnabled")
    def inbound_calls_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceAlias")
    def instance_alias(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiPartyConferenceEnabled")
    def multi_party_conference_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundCallsEnabled")
    def outbound_calls_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


