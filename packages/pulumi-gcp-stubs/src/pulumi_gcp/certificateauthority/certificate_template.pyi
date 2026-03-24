

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CertificateTemplateArgs', 'CertificateTemplate']
@pulumi.input_type
class CertificateTemplateArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., identity_constraints: Optional[pulumi.Input[CertificateTemplateIdentityConstraintsArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., maximum_lifetime: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., passthrough_extensions: Optional[pulumi.Input[CertificateTemplatePassthroughExtensionsArgs]] = ..., predefined_values: Optional[pulumi.Input[CertificateTemplatePredefinedValuesArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityConstraints")
    def identity_constraints(self) -> Optional[pulumi.Input[CertificateTemplateIdentityConstraintsArgs]]:
        
        ...
    
    @identity_constraints.setter
    def identity_constraints(self, value: Optional[pulumi.Input[CertificateTemplateIdentityConstraintsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumLifetime")
    def maximum_lifetime(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @maximum_lifetime.setter
    def maximum_lifetime(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passthroughExtensions")
    def passthrough_extensions(self) -> Optional[pulumi.Input[CertificateTemplatePassthroughExtensionsArgs]]:
        
        ...
    
    @passthrough_extensions.setter
    def passthrough_extensions(self, value: Optional[pulumi.Input[CertificateTemplatePassthroughExtensionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedValues")
    def predefined_values(self) -> Optional[pulumi.Input[CertificateTemplatePredefinedValuesArgs]]:
        
        ...
    
    @predefined_values.setter
    def predefined_values(self, value: Optional[pulumi.Input[CertificateTemplatePredefinedValuesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _CertificateTemplateState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., identity_constraints: Optional[pulumi.Input[CertificateTemplateIdentityConstraintsArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maximum_lifetime: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., passthrough_extensions: Optional[pulumi.Input[CertificateTemplatePassthroughExtensionsArgs]] = ..., predefined_values: Optional[pulumi.Input[CertificateTemplatePredefinedValuesArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityConstraints")
    def identity_constraints(self) -> Optional[pulumi.Input[CertificateTemplateIdentityConstraintsArgs]]:
        
        ...
    
    @identity_constraints.setter
    def identity_constraints(self, value: Optional[pulumi.Input[CertificateTemplateIdentityConstraintsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumLifetime")
    def maximum_lifetime(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @maximum_lifetime.setter
    def maximum_lifetime(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passthroughExtensions")
    def passthrough_extensions(self) -> Optional[pulumi.Input[CertificateTemplatePassthroughExtensionsArgs]]:
        
        ...
    
    @passthrough_extensions.setter
    def passthrough_extensions(self, value: Optional[pulumi.Input[CertificateTemplatePassthroughExtensionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedValues")
    def predefined_values(self) -> Optional[pulumi.Input[CertificateTemplatePredefinedValuesArgs]]:
        
        ...
    
    @predefined_values.setter
    def predefined_values(self, value: Optional[pulumi.Input[CertificateTemplatePredefinedValuesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class CertificateTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., identity_constraints: Optional[pulumi.Input[Union[CertificateTemplateIdentityConstraintsArgs, CertificateTemplateIdentityConstraintsArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maximum_lifetime: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., passthrough_extensions: Optional[pulumi.Input[Union[CertificateTemplatePassthroughExtensionsArgs, CertificateTemplatePassthroughExtensionsArgsDict]]] = ..., predefined_values: Optional[pulumi.Input[Union[CertificateTemplatePredefinedValuesArgs, CertificateTemplatePredefinedValuesArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CertificateTemplateArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., identity_constraints: Optional[pulumi.Input[Union[CertificateTemplateIdentityConstraintsArgs, CertificateTemplateIdentityConstraintsArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maximum_lifetime: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., passthrough_extensions: Optional[pulumi.Input[Union[CertificateTemplatePassthroughExtensionsArgs, CertificateTemplatePassthroughExtensionsArgsDict]]] = ..., predefined_values: Optional[pulumi.Input[Union[CertificateTemplatePredefinedValuesArgs, CertificateTemplatePredefinedValuesArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> CertificateTemplate:
        
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
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityConstraints")
    def identity_constraints(self) -> pulumi.Output[Optional[outputs.CertificateTemplateIdentityConstraints]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumLifetime")
    def maximum_lifetime(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passthroughExtensions")
    def passthrough_extensions(self) -> pulumi.Output[Optional[outputs.CertificateTemplatePassthroughExtensions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predefinedValues")
    def predefined_values(self) -> pulumi.Output[Optional[outputs.CertificateTemplatePredefinedValues]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


