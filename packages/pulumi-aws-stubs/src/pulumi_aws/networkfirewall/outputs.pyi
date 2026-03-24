

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FirewallAvailabilityZoneMapping', 'FirewallEncryptionConfiguration', 'FirewallFirewallStatus', 'FirewallFirewallStatusSyncState', 'FirewallFirewallStatusSyncStateAttachment', ..., 'FirewallPolicyEncryptionConfiguration', 'FirewallPolicyFirewallPolicy', 'FirewallPolicyFirewallPolicyPolicyVariables', ..., ..., 'FirewallPolicyFirewallPolicyStatefulEngineOptions', ..., ..., ..., 'FirewallPolicyFirewallPolicyStatelessCustomAction', ..., ..., ..., ..., 'FirewallSubnetMapping', 'FirewallTransitGatewayAttachmentAccepterTimeouts', 'LoggingConfigurationLoggingConfiguration', ..., 'RuleGroupEncryptionConfiguration', 'RuleGroupRuleGroup', 'RuleGroupRuleGroupReferenceSets', 'RuleGroupRuleGroupReferenceSetsIpSetReference', ..., 'RuleGroupRuleGroupRuleVariables', 'RuleGroupRuleGroupRuleVariablesIpSet', 'RuleGroupRuleGroupRuleVariablesIpSetIpSet', 'RuleGroupRuleGroupRuleVariablesPortSet', 'RuleGroupRuleGroupRuleVariablesPortSetPortSet', 'RuleGroupRuleGroupRulesSource', 'RuleGroupRuleGroupRulesSourceRulesSourceList', 'RuleGroupRuleGroupRulesSourceStatefulRule', 'RuleGroupRuleGroupRulesSourceStatefulRuleHeader', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'RuleGroupRuleGroupStatefulRuleOptions', 'TlsInspectionConfigurationCertificate', 'TlsInspectionConfigurationCertificateAuthority', 'TlsInspectionConfigurationEncryptionConfiguration', 'TlsInspectionConfigurationTimeouts', ..., ..., ..., ..., ..., ..., ..., ..., ..., 'VpcEndpointAssociationSubnetMapping', 'VpcEndpointAssociationTimeouts', 'VpcEndpointAssociationVpcEndpointAssociationStatus', ..., ..., 'GetFirewallAvailabilityZoneMappingResult', 'GetFirewallEncryptionConfigurationResult', 'GetFirewallFirewallStatusResult', ..., ..., ..., 'GetFirewallFirewallStatusSyncStateResult', 'GetFirewallFirewallStatusSyncStateAttachmentResult', ..., 'GetFirewallPolicyFirewallPolicyResult', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'GetFirewallSubnetMappingResult']
@pulumi.output_type
class FirewallAvailabilityZoneMapping(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, availability_zone_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FirewallEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, key_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FirewallFirewallStatus(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, sync_states: Optional[Sequence[outputs.FirewallFirewallStatusSyncState]] = ..., transit_gateway_attachment_sync_states: Optional[Sequence[outputs.FirewallFirewallStatusTransitGatewayAttachmentSyncState]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncStates")
    def sync_states(self) -> Optional[Sequence[outputs.FirewallFirewallStatusSyncState]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentSyncStates")
    def transit_gateway_attachment_sync_states(self) -> Optional[Sequence[outputs.FirewallFirewallStatusTransitGatewayAttachmentSyncState]]:
        
        ...
    


@pulumi.output_type
class FirewallFirewallStatusSyncState(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attachments: Optional[Sequence[outputs.FirewallFirewallStatusSyncStateAttachment]] = ..., availability_zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attachments(self) -> Optional[Sequence[outputs.FirewallFirewallStatusSyncStateAttachment]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FirewallFirewallStatusSyncStateAttachment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, endpoint_id: Optional[_builtins.str] = ..., subnet_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FirewallFirewallStatusTransitGatewayAttachmentSyncState(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attachment_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FirewallPolicyEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, key_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FirewallPolicyFirewallPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, stateless_default_actions: Sequence[_builtins.str], stateless_fragment_default_actions: Sequence[_builtins.str], policy_variables: Optional[outputs.FirewallPolicyFirewallPolicyPolicyVariables] = ..., stateful_default_actions: Optional[Sequence[_builtins.str]] = ..., stateful_engine_options: Optional[outputs.FirewallPolicyFirewallPolicyStatefulEngineOptions] = ..., stateful_rule_group_references: Optional[Sequence[outputs.FirewallPolicyFirewallPolicyStatefulRuleGroupReference]] = ..., stateless_custom_actions: Optional[Sequence[outputs.FirewallPolicyFirewallPolicyStatelessCustomAction]] = ..., stateless_rule_group_references: Optional[Sequence[outputs.FirewallPolicyFirewallPolicyStatelessRuleGroupReference]] = ..., tls_inspection_configuration_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statelessDefaultActions")
    def stateless_default_actions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statelessFragmentDefaultActions")
    def stateless_fragment_default_actions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyVariables")
    def policy_variables(self) -> Optional[outputs.FirewallPolicyFirewallPolicyPolicyVariables]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulDefaultActions")
    def stateful_default_actions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulEngineOptions")
    def stateful_engine_options(self) -> Optional[outputs.FirewallPolicyFirewallPolicyStatefulEngineOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulRuleGroupReferences")
    def stateful_rule_group_references(self) -> Optional[Sequence[outputs.FirewallPolicyFirewallPolicyStatefulRuleGroupReference]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statelessCustomActions")
    def stateless_custom_actions(self) -> Optional[Sequence[outputs.FirewallPolicyFirewallPolicyStatelessCustomAction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statelessRuleGroupReferences")
    def stateless_rule_group_references(self) -> Optional[Sequence[outputs.FirewallPolicyFirewallPolicyStatelessRuleGroupReference]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsInspectionConfigurationArn")
    def tls_inspection_configuration_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FirewallPolicyFirewallPolicyPolicyVariables(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, rule_variables: Optional[Sequence[outputs.FirewallPolicyFirewallPolicyPolicyVariablesRuleVariable]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleVariables")
    def rule_variables(self) -> Optional[Sequence[outputs.FirewallPolicyFirewallPolicyPolicyVariablesRuleVariable]]:
        ...
    


@pulumi.output_type
class FirewallPolicyFirewallPolicyPolicyVariablesRuleVariable(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_set: outputs.FirewallPolicyFirewallPolicyPolicyVariablesRuleVariableIpSet, key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSet")
    def ip_set(self) -> outputs.FirewallPolicyFirewallPolicyPolicyVariablesRuleVariableIpSet:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FirewallPolicyFirewallPolicyPolicyVariablesRuleVariableIpSet(dict):
    def __init__(__self__, *, definitions: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def definitions(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FirewallPolicyFirewallPolicyStatefulEngineOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, flow_timeouts: Optional[outputs.FirewallPolicyFirewallPolicyStatefulEngineOptionsFlowTimeouts] = ..., rule_order: Optional[_builtins.str] = ..., stream_exception_policy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowTimeouts")
    def flow_timeouts(self) -> Optional[outputs.FirewallPolicyFirewallPolicyStatefulEngineOptionsFlowTimeouts]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleOrder")
    def rule_order(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamExceptionPolicy")
    def stream_exception_policy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FirewallPolicyFirewallPolicyStatefulEngineOptionsFlowTimeouts(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, tcp_idle_timeout_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpIdleTimeoutSeconds")
    def tcp_idle_timeout_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class FirewallPolicyFirewallPolicyStatefulRuleGroupReference(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_arn: _builtins.str, deep_threat_inspection: Optional[_builtins.str] = ..., override: Optional[outputs.FirewallPolicyFirewallPolicyStatefulRuleGroupReferenceOverride] = ..., priority: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deepThreatInspection")
    def deep_threat_inspection(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def override(self) -> Optional[outputs.FirewallPolicyFirewallPolicyStatefulRuleGroupReferenceOverride]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class FirewallPolicyFirewallPolicyStatefulRuleGroupReferenceOverride(dict):
    def __init__(__self__, *, action: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FirewallPolicyFirewallPolicyStatelessCustomAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action_definition: outputs.FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinition, action_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionDefinition")
    def action_definition(self) -> outputs.FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinition:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionName")
    def action_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, publish_metric_action: outputs.FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricAction) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishMetricAction")
    def publish_metric_action(self) -> outputs.FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricAction:
        
        ...
    


@pulumi.output_type
class FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricAction(dict):
    def __init__(__self__, *, dimensions: Sequence[outputs.FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionDimension]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Sequence[outputs.FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionDimension]:
        
        ...
    


@pulumi.output_type
class FirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionDimension(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FirewallPolicyFirewallPolicyStatelessRuleGroupReference(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, priority: _builtins.int, resource_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FirewallSubnetMapping(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subnet_id: _builtins.str, ip_address_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FirewallTransitGatewayAttachmentAccepterTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LoggingConfigurationLoggingConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_destination_configs: Sequence[outputs.LoggingConfigurationLoggingConfigurationLogDestinationConfig]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestinationConfigs")
    def log_destination_configs(self) -> Sequence[outputs.LoggingConfigurationLoggingConfigurationLogDestinationConfig]:
        
        ...
    


@pulumi.output_type
class LoggingConfigurationLoggingConfigurationLogDestinationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_destination: Mapping[str, _builtins.str], log_destination_type: _builtins.str, log_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestination")
    def log_destination(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestinationType")
    def log_destination_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, key_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroup(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, rules_source: outputs.RuleGroupRuleGroupRulesSource, reference_sets: Optional[outputs.RuleGroupRuleGroupReferenceSets] = ..., rule_variables: Optional[outputs.RuleGroupRuleGroupRuleVariables] = ..., stateful_rule_options: Optional[outputs.RuleGroupRuleGroupStatefulRuleOptions] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rulesSource")
    def rules_source(self) -> outputs.RuleGroupRuleGroupRulesSource:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="referenceSets")
    def reference_sets(self) -> Optional[outputs.RuleGroupRuleGroupReferenceSets]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleVariables")
    def rule_variables(self) -> Optional[outputs.RuleGroupRuleGroupRuleVariables]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulRuleOptions")
    def stateful_rule_options(self) -> Optional[outputs.RuleGroupRuleGroupStatefulRuleOptions]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupReferenceSets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_set_references: Optional[Sequence[outputs.RuleGroupRuleGroupReferenceSetsIpSetReference]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSetReferences")
    def ip_set_references(self) -> Optional[Sequence[outputs.RuleGroupRuleGroupReferenceSetsIpSetReference]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupReferenceSetsIpSetReference(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_set_references: Sequence[outputs.RuleGroupRuleGroupReferenceSetsIpSetReferenceIpSetReference], key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSetReferences")
    def ip_set_references(self) -> Sequence[outputs.RuleGroupRuleGroupReferenceSetsIpSetReferenceIpSetReference]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupReferenceSetsIpSetReferenceIpSetReference(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, reference_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="referenceArn")
    def reference_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRuleVariables(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_sets: Optional[Sequence[outputs.RuleGroupRuleGroupRuleVariablesIpSet]] = ..., port_sets: Optional[Sequence[outputs.RuleGroupRuleGroupRuleVariablesPortSet]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSets")
    def ip_sets(self) -> Optional[Sequence[outputs.RuleGroupRuleGroupRuleVariablesIpSet]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portSets")
    def port_sets(self) -> Optional[Sequence[outputs.RuleGroupRuleGroupRuleVariablesPortSet]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRuleVariablesIpSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_set: outputs.RuleGroupRuleGroupRuleVariablesIpSetIpSet, key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSet")
    def ip_set(self) -> outputs.RuleGroupRuleGroupRuleVariablesIpSetIpSet:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRuleVariablesIpSetIpSet(dict):
    def __init__(__self__, *, definitions: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def definitions(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRuleVariablesPortSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, port_set: outputs.RuleGroupRuleGroupRuleVariablesPortSetPortSet) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portSet")
    def port_set(self) -> outputs.RuleGroupRuleGroupRuleVariablesPortSetPortSet:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRuleVariablesPortSetPortSet(dict):
    def __init__(__self__, *, definitions: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def definitions(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, rules_source_list: Optional[outputs.RuleGroupRuleGroupRulesSourceRulesSourceList] = ..., rules_string: Optional[_builtins.str] = ..., stateful_rules: Optional[Sequence[outputs.RuleGroupRuleGroupRulesSourceStatefulRule]] = ..., stateless_rules_and_custom_actions: Optional[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActions] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rulesSourceList")
    def rules_source_list(self) -> Optional[outputs.RuleGroupRuleGroupRulesSourceRulesSourceList]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rulesString")
    def rules_string(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulRules")
    def stateful_rules(self) -> Optional[Sequence[outputs.RuleGroupRuleGroupRulesSourceStatefulRule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statelessRulesAndCustomActions")
    def stateless_rules_and_custom_actions(self) -> Optional[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActions]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceRulesSourceList(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, generated_rules_type: _builtins.str, target_types: Sequence[_builtins.str], targets: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generatedRulesType")
    def generated_rules_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetTypes")
    def target_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def targets(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceStatefulRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action: _builtins.str, header: outputs.RuleGroupRuleGroupRulesSourceStatefulRuleHeader, rule_options: Sequence[outputs.RuleGroupRuleGroupRulesSourceStatefulRuleRuleOption]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> outputs.RuleGroupRuleGroupRulesSourceStatefulRuleHeader:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleOptions")
    def rule_options(self) -> Sequence[outputs.RuleGroupRuleGroupRulesSourceStatefulRuleRuleOption]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceStatefulRuleHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination: _builtins.str, destination_port: _builtins.str, direction: _builtins.str, protocol: _builtins.str, source: _builtins.str, source_port: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePort")
    def source_port(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceStatefulRuleRuleOption(dict):
    def __init__(__self__, *, keyword: _builtins.str, settings: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def keyword(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, stateless_rules: Sequence[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRule], custom_actions: Optional[Sequence[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomAction]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statelessRules")
    def stateless_rules(self) -> Sequence[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customActions")
    def custom_actions(self) -> Optional[Sequence[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomAction]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action_definition: outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinition, action_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionDefinition")
    def action_definition(self) -> outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinition:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionName")
    def action_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, publish_metric_action: outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricAction) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishMetricAction")
    def publish_metric_action(self) -> outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricAction:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricAction(dict):
    def __init__(__self__, *, dimensions: Sequence[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricActionDimension]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Sequence[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricActionDimension]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsCustomActionActionDefinitionPublishMetricActionDimension(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, priority: _builtins.int, rule_definition: outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinition) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleDefinition")
    def rule_definition(self) -> outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinition:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actions: Sequence[_builtins.str], match_attributes: outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributes) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchAttributes")
    def match_attributes(self) -> outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributes:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributes(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination_ports: Optional[Sequence[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationPort]] = ..., destinations: Optional[Sequence[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestination]] = ..., protocols: Optional[Sequence[_builtins.int]] = ..., source_ports: Optional[Sequence[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSourcePort]] = ..., sources: Optional[Sequence[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSource]] = ..., tcp_flags: Optional[Sequence[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesTcpFlag]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPorts")
    def destination_ports(self) -> Optional[Sequence[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationPort]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestination]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePorts")
    def source_ports(self) -> Optional[Sequence[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSourcePort]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Optional[Sequence[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpFlags")
    def tcp_flags(self) -> Optional[Sequence[outputs.RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesTcpFlag]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address_definition: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressDefinition")
    def address_definition(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationPort(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_port: _builtins.int, to_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address_definition: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressDefinition")
    def address_definition(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesSourcePort(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_port: _builtins.int, to_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesTcpFlag(dict):
    def __init__(__self__, *, flags: Sequence[_builtins.str], masks: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def flags(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def masks(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleGroupStatefulRuleOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, rule_order: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleOrder")
    def rule_order(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TlsInspectionConfigurationCertificate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, certificate_arn: _builtins.str, certificate_serial: _builtins.str, status: _builtins.str, status_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateSerial")
    def certificate_serial(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TlsInspectionConfigurationCertificateAuthority(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, certificate_arn: _builtins.str, certificate_serial: _builtins.str, status: _builtins.str, status_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateSerial")
    def certificate_serial(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TlsInspectionConfigurationEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_id: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TlsInspectionConfigurationTimeouts(dict):
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
    


@pulumi.output_type
class TlsInspectionConfigurationTlsInspectionConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, server_certificate_configuration: outputs.TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfiguration) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCertificateConfiguration")
    def server_certificate_configuration(self) -> outputs.TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfiguration:
        
        ...
    


@pulumi.output_type
class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scopes: Sequence[outputs.TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScope], certificate_authority_arn: Optional[_builtins.str] = ..., check_certificate_revocation_status: Optional[outputs.TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationCheckCertificateRevocationStatus] = ..., server_certificates: Optional[Sequence[outputs.TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationServerCertificate]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Sequence[outputs.TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScope]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkCertificateRevocationStatus")
    def check_certificate_revocation_status(self) -> Optional[outputs.TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationCheckCertificateRevocationStatus]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCertificates")
    def server_certificates(self) -> Optional[Sequence[outputs.TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationServerCertificate]]:
        
        ...
    


@pulumi.output_type
class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationCheckCertificateRevocationStatus(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, revoked_status_action: Optional[_builtins.str] = ..., unknown_status_action: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="revokedStatusAction")
    def revoked_status_action(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unknownStatusAction")
    def unknown_status_action(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScope(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destinations: Sequence[outputs.TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestination], protocols: Sequence[_builtins.int], destination_ports: Optional[Sequence[outputs.TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestinationPort]] = ..., source_ports: Optional[Sequence[outputs.TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSourcePort]] = ..., sources: Optional[Sequence[outputs.TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSource]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Sequence[outputs.TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestination]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> Sequence[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPorts")
    def destination_ports(self) -> Optional[Sequence[outputs.TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestinationPort]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePorts")
    def source_ports(self) -> Optional[Sequence[outputs.TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSourcePort]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Optional[Sequence[outputs.TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSource]]:
        
        ...
    


@pulumi.output_type
class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address_definition: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressDefinition")
    def address_definition(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeDestinationPort(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_port: _builtins.int, to_port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address_definition: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressDefinition")
    def address_definition(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationScopeSourcePort(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_port: _builtins.int, to_port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class TlsInspectionConfigurationTlsInspectionConfigurationServerCertificateConfigurationServerCertificate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpcEndpointAssociationSubnetMapping(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subnet_id: _builtins.str, ip_address_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpcEndpointAssociationTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VpcEndpointAssociationVpcEndpointAssociationStatus(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, association_sync_states: Sequence[outputs.VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncState]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationSyncStates")
    def association_sync_states(self) -> Sequence[outputs.VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncState]:
        ...
    


@pulumi.output_type
class VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncState(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attachments: Sequence[outputs.VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncStateAttachment], availability_zone: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attachments(self) -> Sequence[outputs.VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncStateAttachment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VpcEndpointAssociationVpcEndpointAssociationStatusAssociationSyncStateAttachment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, endpoint_id: _builtins.str, status: _builtins.str, status_message: _builtins.str, subnet_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFirewallAvailabilityZoneMappingResult(dict):
    def __init__(__self__, *, availability_zone_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFirewallEncryptionConfigurationResult(dict):
    def __init__(__self__, *, key_id: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFirewallFirewallStatusResult(dict):
    def __init__(__self__, *, capacity_usage_summaries: Sequence[outputs.GetFirewallFirewallStatusCapacityUsageSummaryResult], configuration_sync_state_summary: _builtins.str, status: _builtins.str, sync_states: Sequence[outputs.GetFirewallFirewallStatusSyncStateResult], transit_gateway_attachment_sync_states: Sequence[outputs.GetFirewallFirewallStatusTransitGatewayAttachmentSyncStateResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityUsageSummaries")
    def capacity_usage_summaries(self) -> Sequence[outputs.GetFirewallFirewallStatusCapacityUsageSummaryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationSyncStateSummary")
    def configuration_sync_state_summary(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncStates")
    def sync_states(self) -> Sequence[outputs.GetFirewallFirewallStatusSyncStateResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentSyncStates")
    def transit_gateway_attachment_sync_states(self) -> Sequence[outputs.GetFirewallFirewallStatusTransitGatewayAttachmentSyncStateResult]:
        
        ...
    


@pulumi.output_type
class GetFirewallFirewallStatusCapacityUsageSummaryResult(dict):
    def __init__(__self__, *, cidrs: Sequence[outputs.GetFirewallFirewallStatusCapacityUsageSummaryCidrResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidrs(self) -> Sequence[outputs.GetFirewallFirewallStatusCapacityUsageSummaryCidrResult]:
        
        ...
    


@pulumi.output_type
class GetFirewallFirewallStatusCapacityUsageSummaryCidrResult(dict):
    def __init__(__self__, *, available_cidr_count: _builtins.int, ip_set_references: Sequence[outputs.GetFirewallFirewallStatusCapacityUsageSummaryCidrIpSetReferenceResult], utilized_cidr_count: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableCidrCount")
    def available_cidr_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSetReferences")
    def ip_set_references(self) -> Sequence[outputs.GetFirewallFirewallStatusCapacityUsageSummaryCidrIpSetReferenceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="utilizedCidrCount")
    def utilized_cidr_count(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetFirewallFirewallStatusCapacityUsageSummaryCidrIpSetReferenceResult(dict):
    def __init__(__self__, *, resolved_cidr_count: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resolvedCidrCount")
    def resolved_cidr_count(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetFirewallFirewallStatusSyncStateResult(dict):
    def __init__(__self__, *, attachments: Sequence[outputs.GetFirewallFirewallStatusSyncStateAttachmentResult], availability_zone: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attachments(self) -> Sequence[outputs.GetFirewallFirewallStatusSyncStateAttachmentResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFirewallFirewallStatusSyncStateAttachmentResult(dict):
    def __init__(__self__, *, endpoint_id: _builtins.str, status: _builtins.str, status_message: _builtins.str, subnet_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFirewallFirewallStatusTransitGatewayAttachmentSyncStateResult(dict):
    def __init__(__self__, *, attachment_id: _builtins.str, status_message: _builtins.str, transit_gateway_attachment_status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitGatewayAttachmentStatus")
    def transit_gateway_attachment_status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetFirewallPolicyFirewallPolicyResult(dict):
    def __init__(__self__, *, policy_variables: Sequence[outputs.GetFirewallPolicyFirewallPolicyPolicyVariableResult], stateful_default_actions: Sequence[_builtins.str], stateful_engine_options: Sequence[outputs.GetFirewallPolicyFirewallPolicyStatefulEngineOptionResult], stateful_rule_group_references: Sequence[outputs.GetFirewallPolicyFirewallPolicyStatefulRuleGroupReferenceResult], stateless_custom_actions: Sequence[outputs.GetFirewallPolicyFirewallPolicyStatelessCustomActionResult], stateless_default_actions: Sequence[_builtins.str], stateless_fragment_default_actions: Sequence[_builtins.str], stateless_rule_group_references: Sequence[outputs.GetFirewallPolicyFirewallPolicyStatelessRuleGroupReferenceResult], tls_inspection_configuration_arn: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyVariables")
    def policy_variables(self) -> Sequence[outputs.GetFirewallPolicyFirewallPolicyPolicyVariableResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulDefaultActions")
    def stateful_default_actions(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulEngineOptions")
    def stateful_engine_options(self) -> Sequence[outputs.GetFirewallPolicyFirewallPolicyStatefulEngineOptionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statefulRuleGroupReferences")
    def stateful_rule_group_references(self) -> Sequence[outputs.GetFirewallPolicyFirewallPolicyStatefulRuleGroupReferenceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statelessCustomActions")
    def stateless_custom_actions(self) -> Sequence[outputs.GetFirewallPolicyFirewallPolicyStatelessCustomActionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statelessDefaultActions")
    def stateless_default_actions(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statelessFragmentDefaultActions")
    def stateless_fragment_default_actions(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statelessRuleGroupReferences")
    def stateless_rule_group_references(self) -> Sequence[outputs.GetFirewallPolicyFirewallPolicyStatelessRuleGroupReferenceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsInspectionConfigurationArn")
    def tls_inspection_configuration_arn(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetFirewallPolicyFirewallPolicyPolicyVariableResult(dict):
    def __init__(__self__, *, rule_variables: Sequence[outputs.GetFirewallPolicyFirewallPolicyPolicyVariableRuleVariableResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleVariables")
    def rule_variables(self) -> Sequence[outputs.GetFirewallPolicyFirewallPolicyPolicyVariableRuleVariableResult]:
        ...
    


@pulumi.output_type
class GetFirewallPolicyFirewallPolicyPolicyVariableRuleVariableResult(dict):
    def __init__(__self__, *, ip_sets: Sequence[outputs.GetFirewallPolicyFirewallPolicyPolicyVariableRuleVariableIpSetResult], key: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSets")
    def ip_sets(self) -> Sequence[outputs.GetFirewallPolicyFirewallPolicyPolicyVariableRuleVariableIpSetResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetFirewallPolicyFirewallPolicyPolicyVariableRuleVariableIpSetResult(dict):
    def __init__(__self__, *, definitions: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def definitions(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class GetFirewallPolicyFirewallPolicyStatefulEngineOptionResult(dict):
    def __init__(__self__, *, flow_timeouts: Sequence[outputs.GetFirewallPolicyFirewallPolicyStatefulEngineOptionFlowTimeoutResult], rule_order: _builtins.str, stream_exception_policy: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowTimeouts")
    def flow_timeouts(self) -> Sequence[outputs.GetFirewallPolicyFirewallPolicyStatefulEngineOptionFlowTimeoutResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleOrder")
    def rule_order(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamExceptionPolicy")
    def stream_exception_policy(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetFirewallPolicyFirewallPolicyStatefulEngineOptionFlowTimeoutResult(dict):
    def __init__(__self__, *, tcp_idle_timeout_seconds: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpIdleTimeoutSeconds")
    def tcp_idle_timeout_seconds(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetFirewallPolicyFirewallPolicyStatefulRuleGroupReferenceResult(dict):
    def __init__(__self__, *, deep_threat_inspection: _builtins.str, overrides: Sequence[outputs.GetFirewallPolicyFirewallPolicyStatefulRuleGroupReferenceOverrideResult], priority: _builtins.int, resource_arn: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deepThreatInspection")
    def deep_threat_inspection(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def overrides(self) -> Sequence[outputs.GetFirewallPolicyFirewallPolicyStatefulRuleGroupReferenceOverrideResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetFirewallPolicyFirewallPolicyStatefulRuleGroupReferenceOverrideResult(dict):
    def __init__(__self__, *, action: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetFirewallPolicyFirewallPolicyStatelessCustomActionResult(dict):
    def __init__(__self__, *, action_definitions: Sequence[outputs.GetFirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionResult], action_name: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionDefinitions")
    def action_definitions(self) -> Sequence[outputs.GetFirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionName")
    def action_name(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetFirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionResult(dict):
    def __init__(__self__, *, publish_metric_actions: Sequence[outputs.GetFirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishMetricActions")
    def publish_metric_actions(self) -> Sequence[outputs.GetFirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionResult]:
        ...
    


@pulumi.output_type
class GetFirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionResult(dict):
    def __init__(__self__, *, dimensions: Sequence[outputs.GetFirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionDimensionResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Sequence[outputs.GetFirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionDimensionResult]:
        ...
    


@pulumi.output_type
class GetFirewallPolicyFirewallPolicyStatelessCustomActionActionDefinitionPublishMetricActionDimensionResult(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetFirewallPolicyFirewallPolicyStatelessRuleGroupReferenceResult(dict):
    def __init__(__self__, *, priority: _builtins.int, resource_arn: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetFirewallSubnetMappingResult(dict):
    def __init__(__self__, *, subnet_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str:
        
        ...
    


