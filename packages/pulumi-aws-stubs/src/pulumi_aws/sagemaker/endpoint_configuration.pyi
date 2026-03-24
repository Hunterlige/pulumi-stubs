

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EndpointConfigurationArgs', 'EndpointConfiguration']
@pulumi.input_type
class EndpointConfigurationArgs:
    def __init__(__self__, *, production_variants: pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationProductionVariantArgs]]], async_inference_config: Optional[pulumi.Input[EndpointConfigurationAsyncInferenceConfigArgs]] = ..., data_capture_config: Optional[pulumi.Input[EndpointConfigurationDataCaptureConfigArgs]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shadow_production_variants: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationShadowProductionVariantArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productionVariants")
    def production_variants(self) -> pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationProductionVariantArgs]]]:
        
        ...
    
    @production_variants.setter
    def production_variants(self, value: pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationProductionVariantArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="asyncInferenceConfig")
    def async_inference_config(self) -> Optional[pulumi.Input[EndpointConfigurationAsyncInferenceConfigArgs]]:
        
        ...
    
    @async_inference_config.setter
    def async_inference_config(self, value: Optional[pulumi.Input[EndpointConfigurationAsyncInferenceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCaptureConfig")
    def data_capture_config(self) -> Optional[pulumi.Input[EndpointConfigurationDataCaptureConfigArgs]]:
        
        ...
    
    @data_capture_config.setter
    def data_capture_config(self, value: Optional[pulumi.Input[EndpointConfigurationDataCaptureConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shadowProductionVariants")
    def shadow_production_variants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationShadowProductionVariantArgs]]]]:
        
        ...
    
    @shadow_production_variants.setter
    def shadow_production_variants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationShadowProductionVariantArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _EndpointConfigurationState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., async_inference_config: Optional[pulumi.Input[EndpointConfigurationAsyncInferenceConfigArgs]] = ..., data_capture_config: Optional[pulumi.Input[EndpointConfigurationDataCaptureConfigArgs]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., production_variants: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationProductionVariantArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shadow_production_variants: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationShadowProductionVariantArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="asyncInferenceConfig")
    def async_inference_config(self) -> Optional[pulumi.Input[EndpointConfigurationAsyncInferenceConfigArgs]]:
        
        ...
    
    @async_inference_config.setter
    def async_inference_config(self, value: Optional[pulumi.Input[EndpointConfigurationAsyncInferenceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCaptureConfig")
    def data_capture_config(self) -> Optional[pulumi.Input[EndpointConfigurationDataCaptureConfigArgs]]:
        
        ...
    
    @data_capture_config.setter
    def data_capture_config(self, value: Optional[pulumi.Input[EndpointConfigurationDataCaptureConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productionVariants")
    def production_variants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationProductionVariantArgs]]]]:
        
        ...
    
    @production_variants.setter
    def production_variants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationProductionVariantArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shadowProductionVariants")
    def shadow_production_variants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationShadowProductionVariantArgs]]]]:
        
        ...
    
    @shadow_production_variants.setter
    def shadow_production_variants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointConfigurationShadowProductionVariantArgs]]]]): # -> None:
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
    


@pulumi.type_token(...)
class EndpointConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., async_inference_config: Optional[pulumi.Input[Union[EndpointConfigurationAsyncInferenceConfigArgs, EndpointConfigurationAsyncInferenceConfigArgsDict]]] = ..., data_capture_config: Optional[pulumi.Input[Union[EndpointConfigurationDataCaptureConfigArgs, EndpointConfigurationDataCaptureConfigArgsDict]]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., production_variants: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EndpointConfigurationProductionVariantArgs, EndpointConfigurationProductionVariantArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shadow_production_variants: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EndpointConfigurationShadowProductionVariantArgs, EndpointConfigurationShadowProductionVariantArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EndpointConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., async_inference_config: Optional[pulumi.Input[Union[EndpointConfigurationAsyncInferenceConfigArgs, EndpointConfigurationAsyncInferenceConfigArgsDict]]] = ..., data_capture_config: Optional[pulumi.Input[Union[EndpointConfigurationDataCaptureConfigArgs, EndpointConfigurationDataCaptureConfigArgsDict]]] = ..., execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., production_variants: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EndpointConfigurationProductionVariantArgs, EndpointConfigurationProductionVariantArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shadow_production_variants: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EndpointConfigurationShadowProductionVariantArgs, EndpointConfigurationShadowProductionVariantArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> EndpointConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asyncInferenceConfig")
    def async_inference_config(self) -> pulumi.Output[Optional[outputs.EndpointConfigurationAsyncInferenceConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCaptureConfig")
    def data_capture_config(self) -> pulumi.Output[Optional[outputs.EndpointConfigurationDataCaptureConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productionVariants")
    def production_variants(self) -> pulumi.Output[Sequence[outputs.EndpointConfigurationProductionVariant]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shadowProductionVariants")
    def shadow_production_variants(self) -> pulumi.Output[Optional[Sequence[outputs.EndpointConfigurationShadowProductionVariant]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


