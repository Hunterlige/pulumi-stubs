

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApprovalRuleTemplateAssociationArgs', 'ApprovalRuleTemplateAssociation']
@pulumi.input_type
class ApprovalRuleTemplateAssociationArgs:
    def __init__(__self__, *, approval_rule_template_name: pulumi.Input[_builtins.str], repository_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvalRuleTemplateName")
    def approval_rule_template_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @approval_rule_template_name.setter
    def approval_rule_template_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @repository_name.setter
    def repository_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ApprovalRuleTemplateAssociationState:
    def __init__(__self__, *, approval_rule_template_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., repository_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvalRuleTemplateName")
    def approval_rule_template_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @approval_rule_template_name.setter
    def approval_rule_template_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @repository_name.setter
    def repository_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ApprovalRuleTemplateAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., approval_rule_template_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., repository_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ApprovalRuleTemplateAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., approval_rule_template_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., repository_name: Optional[pulumi.Input[_builtins.str]] = ...) -> ApprovalRuleTemplateAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvalRuleTemplateName")
    def approval_rule_template_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


