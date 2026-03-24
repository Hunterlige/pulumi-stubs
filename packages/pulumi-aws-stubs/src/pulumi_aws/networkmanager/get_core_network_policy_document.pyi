

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCoreNetworkPolicyDocumentResult', 'AwaitableGetCoreNetworkPolicyDocumentResult', 'get_core_network_policy_document', 'get_core_network_policy_document_output']
@pulumi.output_type
class GetCoreNetworkPolicyDocumentResult:
    
    def __init__(__self__, attachment_policies=..., attachment_routing_policy_rules=..., core_network_configurations=..., id=..., json=..., network_function_groups=..., routing_policies=..., segment_actions=..., segments=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentPolicies")
    def attachment_policies(self) -> Optional[Sequence[outputs.GetCoreNetworkPolicyDocumentAttachmentPolicyResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attachmentRoutingPolicyRules")
    def attachment_routing_policy_rules(self) -> Optional[Sequence[outputs.GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkConfigurations")
    def core_network_configurations(self) -> Sequence[outputs.GetCoreNetworkPolicyDocumentCoreNetworkConfigurationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def json(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkFunctionGroups")
    def network_function_groups(self) -> Optional[Sequence[outputs.GetCoreNetworkPolicyDocumentNetworkFunctionGroupResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingPolicies")
    def routing_policies(self) -> Optional[Sequence[outputs.GetCoreNetworkPolicyDocumentRoutingPolicyResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="segmentActions")
    def segment_actions(self) -> Optional[Sequence[outputs.GetCoreNetworkPolicyDocumentSegmentActionResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def segments(self) -> Sequence[outputs.GetCoreNetworkPolicyDocumentSegmentResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetCoreNetworkPolicyDocumentResult(GetCoreNetworkPolicyDocumentResult):
    def __await__(self): # -> Generator[Never, Any, GetCoreNetworkPolicyDocumentResult]:
        ...
    


def get_core_network_policy_document(attachment_policies: Optional[Sequence[Union[GetCoreNetworkPolicyDocumentAttachmentPolicyArgs, GetCoreNetworkPolicyDocumentAttachmentPolicyArgsDict]]] = ..., attachment_routing_policy_rules: Optional[Sequence[Union[GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleArgs, GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleArgsDict]]] = ..., core_network_configurations: Optional[Sequence[Union[GetCoreNetworkPolicyDocumentCoreNetworkConfigurationArgs, GetCoreNetworkPolicyDocumentCoreNetworkConfigurationArgsDict]]] = ..., network_function_groups: Optional[Sequence[Union[GetCoreNetworkPolicyDocumentNetworkFunctionGroupArgs, GetCoreNetworkPolicyDocumentNetworkFunctionGroupArgsDict]]] = ..., routing_policies: Optional[Sequence[Union[GetCoreNetworkPolicyDocumentRoutingPolicyArgs, GetCoreNetworkPolicyDocumentRoutingPolicyArgsDict]]] = ..., segment_actions: Optional[Sequence[Union[GetCoreNetworkPolicyDocumentSegmentActionArgs, GetCoreNetworkPolicyDocumentSegmentActionArgsDict]]] = ..., segments: Optional[Sequence[Union[GetCoreNetworkPolicyDocumentSegmentArgs, GetCoreNetworkPolicyDocumentSegmentArgsDict]]] = ..., version: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCoreNetworkPolicyDocumentResult:
    
    ...

def get_core_network_policy_document_output(attachment_policies: Optional[pulumi.Input[Optional[Sequence[Union[GetCoreNetworkPolicyDocumentAttachmentPolicyArgs, GetCoreNetworkPolicyDocumentAttachmentPolicyArgsDict]]]]] = ..., attachment_routing_policy_rules: Optional[pulumi.Input[Optional[Sequence[Union[GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleArgs, GetCoreNetworkPolicyDocumentAttachmentRoutingPolicyRuleArgsDict]]]]] = ..., core_network_configurations: Optional[pulumi.Input[Sequence[Union[GetCoreNetworkPolicyDocumentCoreNetworkConfigurationArgs, GetCoreNetworkPolicyDocumentCoreNetworkConfigurationArgsDict]]]] = ..., network_function_groups: Optional[pulumi.Input[Optional[Sequence[Union[GetCoreNetworkPolicyDocumentNetworkFunctionGroupArgs, GetCoreNetworkPolicyDocumentNetworkFunctionGroupArgsDict]]]]] = ..., routing_policies: Optional[pulumi.Input[Optional[Sequence[Union[GetCoreNetworkPolicyDocumentRoutingPolicyArgs, GetCoreNetworkPolicyDocumentRoutingPolicyArgsDict]]]]] = ..., segment_actions: Optional[pulumi.Input[Optional[Sequence[Union[GetCoreNetworkPolicyDocumentSegmentActionArgs, GetCoreNetworkPolicyDocumentSegmentActionArgsDict]]]]] = ..., segments: Optional[pulumi.Input[Sequence[Union[GetCoreNetworkPolicyDocumentSegmentArgs, GetCoreNetworkPolicyDocumentSegmentArgsDict]]]] = ..., version: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCoreNetworkPolicyDocumentResult]:
    
    ...

