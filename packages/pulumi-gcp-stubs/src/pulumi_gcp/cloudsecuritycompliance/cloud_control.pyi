

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CloudControlArgs', 'CloudControl']
@pulumi.input_type
class CloudControlArgs:
    def __init__(__self__, *, cloud_control_id: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], organization: pulumi.Input[_builtins.str], categories: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., finding_category: Optional[pulumi.Input[_builtins.str]] = ..., parameter_specs: Optional[pulumi.Input[Sequence[pulumi.Input[CloudControlParameterSpecArgs]]]] = ..., remediation_steps: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[CloudControlRuleArgs]]]] = ..., severity: Optional[pulumi.Input[_builtins.str]] = ..., supported_cloud_providers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudControlId")
    def cloud_control_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cloud_control_id.setter
    def cloud_control_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @organization.setter
    def organization(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @categories.setter
    def categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="findingCategory")
    def finding_category(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @finding_category.setter
    def finding_category(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterSpecs")
    def parameter_specs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CloudControlParameterSpecArgs]]]]:
        
        ...
    
    @parameter_specs.setter
    def parameter_specs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CloudControlParameterSpecArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remediationSteps")
    def remediation_steps(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @remediation_steps.setter
    def remediation_steps(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CloudControlRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CloudControlRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedCloudProviders")
    def supported_cloud_providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @supported_cloud_providers.setter
    def supported_cloud_providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _CloudControlState:
    def __init__(__self__, *, categories: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cloud_control_id: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., finding_category: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., major_revision_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ..., parameter_specs: Optional[pulumi.Input[Sequence[pulumi.Input[CloudControlParameterSpecArgs]]]] = ..., related_frameworks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., remediation_steps: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[CloudControlRuleArgs]]]] = ..., severity: Optional[pulumi.Input[_builtins.str]] = ..., supported_cloud_providers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., supported_enforcement_modes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., supported_target_resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @categories.setter
    def categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudControlId")
    def cloud_control_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloud_control_id.setter
    def cloud_control_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="findingCategory")
    def finding_category(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @finding_category.setter
    def finding_category(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="majorRevisionId")
    def major_revision_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @major_revision_id.setter
    def major_revision_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def organization(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization.setter
    def organization(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterSpecs")
    def parameter_specs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CloudControlParameterSpecArgs]]]]:
        
        ...
    
    @parameter_specs.setter
    def parameter_specs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CloudControlParameterSpecArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedFrameworks")
    def related_frameworks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @related_frameworks.setter
    def related_frameworks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remediationSteps")
    def remediation_steps(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @remediation_steps.setter
    def remediation_steps(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CloudControlRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CloudControlRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedCloudProviders")
    def supported_cloud_providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @supported_cloud_providers.setter
    def supported_cloud_providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedEnforcementModes")
    def supported_enforcement_modes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @supported_enforcement_modes.setter
    def supported_enforcement_modes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedTargetResourceTypes")
    def supported_target_resource_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @supported_target_resource_types.setter
    def supported_target_resource_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class CloudControl(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., categories: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cloud_control_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., finding_category: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ..., parameter_specs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CloudControlParameterSpecArgs, CloudControlParameterSpecArgsDict]]]]] = ..., remediation_steps: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CloudControlRuleArgs, CloudControlRuleArgsDict]]]]] = ..., severity: Optional[pulumi.Input[_builtins.str]] = ..., supported_cloud_providers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CloudControlArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., categories: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cloud_control_id: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., finding_category: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., major_revision_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., organization: Optional[pulumi.Input[_builtins.str]] = ..., parameter_specs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CloudControlParameterSpecArgs, CloudControlParameterSpecArgsDict]]]]] = ..., related_frameworks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., remediation_steps: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CloudControlRuleArgs, CloudControlRuleArgsDict]]]]] = ..., severity: Optional[pulumi.Input[_builtins.str]] = ..., supported_cloud_providers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., supported_enforcement_modes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., supported_target_resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> CloudControl:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def categories(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudControlId")
    def cloud_control_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="findingCategory")
    def finding_category(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="majorRevisionId")
    def major_revision_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterSpecs")
    def parameter_specs(self) -> pulumi.Output[Optional[Sequence[outputs.CloudControlParameterSpec]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedFrameworks")
    def related_frameworks(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remediationSteps")
    def remediation_steps(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence[outputs.CloudControlRule]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedCloudProviders")
    def supported_cloud_providers(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedEnforcementModes")
    def supported_enforcement_modes(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedTargetResourceTypes")
    def supported_target_resource_types(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    


